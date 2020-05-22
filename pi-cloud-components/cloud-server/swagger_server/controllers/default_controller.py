import connexion
import six

from swagger_server.models.unauthorized_response import UnauthorizedResponse
from swagger_server.logic.handlers import authorization_check, handle_add_coordinates, handle_retrive_instructions, \
    AuthError
from swagger_server.models.added import Added  # noqa: E501
from swagger_server.models.coordinate import Coordinate  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.instructions import Instructions  # noqa: E501
from swagger_server import util


def add_coordinates(coordinates):  # noqa: E501
    """add_coordinates

    Adds the latest coordinate data to quick storage # noqa: E501

    :param coordinates: 
    :type coordinates: list | bytes

    :rtype: Added
    """
    if not authorization_check(connexion.request.headers): return AuthError()
    if connexion.request.is_json:
        coordinates = [Coordinate.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return handle_add_coordinates(coordinates)


def retrive_instructions():  # noqa: E501
    """retrive_instructions

    gets instructions for the Pi to execute # noqa: E501


    :rtype: Instructions
    """
    if not authorization_check(connexion.request.headers): return AuthError()
    return handle_retrive_instructions()
