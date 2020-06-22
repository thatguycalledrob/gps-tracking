#! /usr/bin/python3
from typing import List
from os.path import dirname, join, abspath
from swagger_client import Coordinate, DefaultApi, ApiClient
from swagger_client.configuration import Configuration

import datetime
import json
import pynmea2
import multiprocessing
import serial
import sys
import time


def read_gps(line):
    # port read returns a byte array
    # any standard text decoding will work
    # more info: https://www.gpsinformation.org/dale/nmea.htm
    ln = line.decode('ascii')
    if 'GGA' in ln:
        try:

            gps = pynmea2.parse(ln, check=False)
            calc = [
                float(gps.latitude),
                float(gps.longitude),
                float(gps.altitude),
                float(gps.num_sats)
            ]

            if 0.0 not in calc:
                return calc

        except Exception:
            # decoding, casting and parsing are not critical.
            # good old embedded system error handling. ignore the lot.
            pass
    return None


def setup_client() -> DefaultApi:
    # read the secret.json file right off
    with open(join(abspath(dirname(__file__)), 'secret.json'), mode='r', encoding='utf-8') as f:
        try:
            # json.load is getting weird errors with this file!
            # doing the load manually.
            j = json.loads(f.read().strip())
            secret: str = j.get('secret')
            url: str = j.get('url')
        except Exception as e:
            print(f"secret file read exception: {e}", file=sys.stderr)
            print("warning: missing or invalid secret.json file!", file=sys.stderr)
            exit(1)

    # configure API client.
    cl = Configuration()
    cl.host = url
    cl.api_key = {'X-API-Key': secret}

    return DefaultApi(ApiClient(cl))


def main() -> None:
    # reporting
    PORT_READ_RATE = 0.01  # how often to read from the serial port
    OBSERVATION_INTERVAL = 10  # how often (in s) to take a reading
    REPORT_INTERVAL = 60  # how often (in s) to make an API call

    api_client = setup_client()

    # Port specific to hardware configuration and pi variant.
    # baudrate chosen from gps chip manual.
    port = serial.Serial('/dev/serial0', baudrate=9600, timeout=0.5)

    try:
        # Initialise message body
        msgBody: List[Coordinate] = []

        for c in range(int(REPORT_INTERVAL / OBSERVATION_INTERVAL)):

            observations = []
            for _ in range(int(OBSERVATION_INTERVAL * PORT_READ_RATE ** -1)):
                time.sleep(PORT_READ_RATE)
                try:
                    if port.inWaiting():
                        x = read_gps(port.readline())
                        if x is not None:
                            observations.append(x)
                except Exception:
                    # on IO failure, close and port with wait
                    port.close()
                    time.sleep(1)
                    port.open()

            if observations:
                out = [float(sum(o)) / len(o) for o in zip(*observations)]

                # Use the API struct to define the Coordinates
                msgBody.append(
                    Coordinate(
                        time=int(datetime.datetime.utcnow().timestamp()),
                        lat=float("{:.5f}".format(out[0])),
                        long=float("{:.5f}".format(out[1])),
                        alt=float("{:.1f}".format(out[2])),
                        sats=float("{:.1f}".format(out[3])),
                        order=float(c)
                    )
                )

            # reset the IO stream between observations
            # this reduces frequency of locks and drops
            port.close()
            time.sleep(5)
            port.open()

        api_client.add_coordinates(msgBody)

    except Exception as e:

        # ah... the issue with wrapping everything in a try catch!
        if e == KeyboardInterrupt:
            sys.exit(0)

        # we can probably log this somewhere if we have issues
        print("Critical runtime error!", json.dumps(e, default=str))
        pass


if __name__ == '__main__':
    # 1 min 30s timeout
    # This main thread will be spawned on a cron schedule of 2 minuites
    # it will read data for approx 60s, and then transit via a HTTP API.
    # This leaves 30s for spinup and shutdown, plus 30s between the cron
    # taks for the py interpreter to clean itself up.
    TIMEOUT = 90

    p = multiprocessing.Process(target=main, name="read")
    p.start()

    # obey a 90s timeout on the processing thread
    p.join(TIMEOUT)
    if p.is_alive():
        try:
            p.terminate()
            p.join()
        except Exception:
            pass

    sys.exit(0)
