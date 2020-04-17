import json
import serial
import pynmea2
import time
import datetime
import requests
import os


def read_gps(line):
    # port read returns a byte array
    # any standard text decoding will work
    # more info: https://www.gpsinformation.org/dale/nmea.htm
    l = line.decode('ascii')
    if 'GGA' in l:
        try:

            gps = pynmea2.parse(l, check=False)
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


if __name__ == '__main__':
    port_read_rate = 0.01                   # how often to read from the serial port
    observation_interval = 10               # how often (in s) to take a reading
    report_interval = 60                    # how often (in s) to make an API call
    url = os.environ.get("GPS_URL", "")     # get the cloud environment URL

    # Port specific to hardware configuration and pi variant.
    # baudrate chosen from gps chip manual.
    port = serial.Serial('/dev/serial0', baudrate=9600, timeout=0.5)

    while True:
        try:
            msgBody = []
            for c in range(int(report_interval / observation_interval)):

                observations = []
                for _ in range(int(observation_interval * port_read_rate ** -1)):
                    time.sleep(port_read_rate)
                    try:
                        if port.inWaiting():
                            x = read_gps(port.readline())
                            if x is not None:
                                observations.append(x)
                    except Exception as e:
                        # on IO failure, close and port with wait
                        port.close()
                        time.sleep(1)
                        port.open()

                if observations:
                    out = [float(sum(o)) / len(o) for o in zip(*observations)]
                    msgBody.append({
                        "i": c,
                        "utc": datetime.datetime.utcnow().timestamp(),
                        "obs": {
                            "lat": "{:.5f}".format(out[0]),
                            "long": "{:.5f}".format(out[1]),
                            "alt": "{:.1f}".format(out[2]),
                            "sats": "{:.1f}".format(out[3]),
                        }
                    })

                # reset the stream between observations
                port.close()
                time.sleep(5)
                port.open()

            print(json.dumps({"data": msgBody}))
            requests.post(url, data=json.dumps({"data": msgBody}, default=str))

        except Exception as e:

            if e == KeyboardInterrupt:
                exit(0)

            # we can probably log this somewhere if we have issues
            print("Critical runtime error!", json.dumps(e, default=str))
            pass
