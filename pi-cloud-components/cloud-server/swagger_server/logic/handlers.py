import hashlib
import json
from os.path import dirname, join, abspath
from typing import List, Dict, Tuple

from swagger_server.logic.firestore import add_coordinate, add_coordinates
from swagger_server.models import UnauthorizedResponse
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

            # we use a hash here, not that anyone will try hacking us,
            # but you can exploit string comparison time to easily break
            # plaintext comparison. A hash mitigates this issue
            secret = hashlib.sha1(j.get('secret').strip().encode()).hexdigest()
        except Exception as e:
            slogger.warn(f"secret file read exception: {e}")
            # deny access by default.
            return False
    return hashlib.sha1(h.strip().encode()).hexdigest() == secret.strip()


def AuthError() -> Tuple[UnauthorizedResponse, int]:
    return UnauthorizedResponse("missing or invalid API key"), 401


def handle_add_coordinates(coordinates: List[Coordinate]) -> Tuple[Added, int]:  # noqa: E501
    add_coordinates(coordinates)
    return Added("done"), 201


def handle_retrive_instructions() -> Tuple[Instructions, int]:  # noqa: E501
    # todo - infer this from the database
    i = Instructions("do-nothing")
    return i, 200
