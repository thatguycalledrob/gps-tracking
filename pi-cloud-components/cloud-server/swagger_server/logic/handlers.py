from typing import List, Dict

import connexion

from swagger_server.models.added import Added  # noqa: E501
from swagger_server.models.coordinate import Coordinate  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.instructions import Instructions  # noqa: E501
from swagger_server import util


# add
#   if not authorization_check(connexion.request.headers): return UnauthorizedResponse("")
def authorization_check(headers: Dict[str, str]):
    headers.get('X-API-Key', 'definitely-unauthorised!')


def handle_add_coordinates(coordinates: List[Coordinate]) -> Added:  # noqa: E501
    print(coordinates)  # todo - add this to the db
    return Added("done")


def handle_retrive_instructions() -> Instructions:  # noqa: E501
    # todo - infer this from the database
    i = Instructions("do-nothing")
    return i
