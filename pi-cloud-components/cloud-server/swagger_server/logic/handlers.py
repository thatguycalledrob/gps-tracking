from typing import List, Dict

import connexion

from swagger_server.models.added import Added  # noqa: E501
from swagger_server.models.coordinate import Coordinate  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.instructions import Instructions  # noqa: E501
from swagger_server import util
from swagger_server.logic.stackdriver_logger import slogger


# todo: change mustache config to include the below auto-magically!
# add the following into the controllers.
#   if not authorization_check(connexion.request.headers): return UnauthorizedResponse("missing or invalid API key")
def authorization_check(headers: Dict[str, str]) -> bool:
    h = headers.get('X-API-Key', 'no-api-key-is-definitely-unauthorised!')
    slogger.info("h = ", h)
    return True


def handle_add_coordinates(coordinates: List[Coordinate]) -> Added:  # noqa: E501
    print(coordinates)  # todo - add this to the db
    return Added("done")


def handle_retrive_instructions() -> Instructions:  # noqa: E501
    # todo - infer this from the database
    i = Instructions("do-nothing")
    return i
