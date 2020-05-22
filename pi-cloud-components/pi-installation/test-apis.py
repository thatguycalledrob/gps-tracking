from __future__ import print_function

import json
import sys

import swagger_client
from swagger_client.configuration import Configuration
from swagger_client.rest import ApiException
from pprint import pprint

from os.path import dirname, join, abspath

if __name__ == '__main__':

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
    c = Configuration()
    c.host = url
    c.api_key = {'X-API-Key': 'secret'}
    api_instance = swagger_client.DefaultApi(
        swagger_client.ApiClient(c)
    )

    # Declare some coordinates - just dummy ones for now
    coord1 = swagger_client.Coordinate(
        time=1590142853, sats=5, lat=51.641845, long=-1.563285, alt=100, order=1
    )
    coord2 = swagger_client.Coordinate(
        time=1590145853, sats=10, lat=51.652324, long=-1.559012, alt=50, order=2
    )
    coordinates = [coord1, coord2]

    print("Setup complete...")

    try:
        api_response = api_instance.add_coordinates(coordinates)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->add_coordinates: %s\n" % e)

    try:
        api_response = api_instance.retrive_instructions()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->retrive_instructions: %s\n" % e)
