from swagger_server.models.added import Added  # noqa: E501
from swagger_server.models.coordinate import Coordinate  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.instructions import Instructions  # noqa: E501
from swagger_server import util


def handle_add_coordinates(coordinates):  # noqa: E501
    """add_coordinates

    Adds the latest coordinate data to quick storage # noqa: E501

    :param coordinates:
    :type coordinates: list | bytes

    :rtype: Added
    """
    if connexion.request.is_json:
        coordinates = [Coordinate.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return handle_add_coordinates(coordinates)


def retrive_instructions():  # noqa: E501
    """retrive_instructions

    gets instructions for the Pi to execute # noqa: E501


    :rtype: Instructions
    """
    return 'do some magic!'
