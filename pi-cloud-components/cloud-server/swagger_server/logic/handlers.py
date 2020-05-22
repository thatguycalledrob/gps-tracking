import json
from os.path import dirname, join, abspath
from typing import List, Dict, Tuple

from swagger_client import UnauthorizedResponse
from swagger_server.models.added import Added  # noqa: E501
from swagger_server.models.coordinate import Coordinate  # noqa: E501
from swagger_server.models.instructions import Instructions  # noqa: E501
from swagger_server.logic.stackdriver_logger import slogger


# todo: change mustache config to include the below auto-magically!
# add the following into the controllers.
#    if not authorization_check(connexion.request.headers): return AuthError()
def authorization_check(headers: Dict[str, str]) -> bool:
    h = headers.get('X-API-Key', 'no-api-key-is-definitely-unauthorised!')
    with open(join(abspath(dirname(__file__)), 'secret.json'), mode='r', encoding='utf-8') as f:
        try:
            # json.load is getting weird errors with this file!
            # doing the load manually.
            # May be due to windows file endings todo: check
            j = json.loads(f.read().strip())
            secret = j.get('secret')
        except Exception as e:
            slogger.warn(f"secret file read exception: {e}")
            # deny access by default.
            return False

    slogger.info("secret = ", secret)
    slogger.info("header = ", h)

    return h.strip() == secret.strip()


def AuthError() -> Tuple[UnauthorizedResponse, int]:
    return UnauthorizedResponse("missing or invalid API key"), 401


def handle_add_coordinates(coordinates: List[Coordinate]) -> Tuple[Added, int]:  # noqa: E501
    print(coordinates)  # todo - add this to the db
    return Added("done"), 201


def handle_retrive_instructions() -> Tuple[Instructions, int]:  # noqa: E501
    # todo - infer this from the database
    i = Instructions("do-nothing")
    return i, 200
