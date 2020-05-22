from __future__ import print_function
import swagger_client
from swagger_client.configuration import Configuration
from swagger_client.rest import ApiException
from pprint import pprint

if __name__ == '__main__':
    # configure API endpoints
    c = Configuration()
    c.host = "https://van-tracker-lcn55j3ska-ew.a.run.app/pi/v1"
    api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(c))

    # Declare some coordinates
    coord1 = swagger_client.Coordinate(
        time=1590142853, sats=5, lat=51.641845, long=-1.563285, alt=100,  order=1
    )
    coord2 = swagger_client.Coordinate(
        time=1590145853, sats=10, lat=51.652324, long=-1.559012, alt=50,  order=2
    )
    coordinates = [coord1, coord2]

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
