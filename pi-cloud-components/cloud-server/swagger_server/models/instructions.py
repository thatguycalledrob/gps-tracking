# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Instructions(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, instruction: str = None):  # noqa: E501
        """Instructions - a model defined in Swagger

        :param instruction: The instruction of this Instructions.  # noqa: E501
        :type instruction: str
        """
        self.swagger_types = {
            'instruction': str
        }

        self.attribute_map = {
            'instruction': 'instruction'
        }

        self._instruction = instruction

    @classmethod
    def from_dict(cls, dikt) -> 'Instructions':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The instructions of this Instructions.  # noqa: E501
        :rtype: Instructions
        """
        return util.deserialize_model(dikt, cls)

    @property
    def instruction(self) -> str:
        """Gets the instruction of this Instructions.


        :return: The instruction of this Instructions.
        :rtype: str
        """
        return self._instruction

    @instruction.setter
    def instruction(self, instruction: str):
        """Sets the instruction of this Instructions.


        :param instruction: The instruction of this Instructions.
        :type instruction: str
        """
        allowed_values = ["restart", "startVnc"]  # noqa: E501
        if instruction not in allowed_values:
            raise ValueError(
                "Invalid value for `instruction` ({0}), must be one of {1}"
                    .format(instruction, allowed_values)
            )

        self._instruction = instruction
