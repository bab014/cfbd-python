# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  It currently has a wide array of data ranging from play by play to player statistics to game scores and more.  # noqa: E501

    OpenAPI spec version: 2.2.10
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AdvancedGameStatOffenseRushingPlays(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'ppa': 'float',
        'total_ppa': 'float',
        'success_rate': 'float',
        'explosiveness': 'float'
    }

    attribute_map = {
        'ppa': 'ppa',
        'total_ppa': 'totalPPA',
        'success_rate': 'successRate',
        'explosiveness': 'explosiveness'
    }

    def __init__(self, ppa=None, total_ppa=None, success_rate=None, explosiveness=None):  # noqa: E501
        """AdvancedGameStatOffenseRushingPlays - a model defined in Swagger"""  # noqa: E501

        self._ppa = None
        self._total_ppa = None
        self._success_rate = None
        self._explosiveness = None
        self.discriminator = None

        if ppa is not None:
            self.ppa = ppa
        if total_ppa is not None:
            self.total_ppa = total_ppa
        if success_rate is not None:
            self.success_rate = success_rate
        if explosiveness is not None:
            self.explosiveness = explosiveness

    @property
    def ppa(self):
        """Gets the ppa of this AdvancedGameStatOffenseRushingPlays.  # noqa: E501


        :return: The ppa of this AdvancedGameStatOffenseRushingPlays.  # noqa: E501
        :rtype: float
        """
        return self._ppa

    @ppa.setter
    def ppa(self, ppa):
        """Sets the ppa of this AdvancedGameStatOffenseRushingPlays.


        :param ppa: The ppa of this AdvancedGameStatOffenseRushingPlays.  # noqa: E501
        :type: float
        """

        self._ppa = ppa

    @property
    def total_ppa(self):
        """Gets the total_ppa of this AdvancedGameStatOffenseRushingPlays.  # noqa: E501


        :return: The total_ppa of this AdvancedGameStatOffenseRushingPlays.  # noqa: E501
        :rtype: float
        """
        return self._total_ppa

    @total_ppa.setter
    def total_ppa(self, total_ppa):
        """Sets the total_ppa of this AdvancedGameStatOffenseRushingPlays.


        :param total_ppa: The total_ppa of this AdvancedGameStatOffenseRushingPlays.  # noqa: E501
        :type: float
        """

        self._total_ppa = total_ppa

    @property
    def success_rate(self):
        """Gets the success_rate of this AdvancedGameStatOffenseRushingPlays.  # noqa: E501


        :return: The success_rate of this AdvancedGameStatOffenseRushingPlays.  # noqa: E501
        :rtype: float
        """
        return self._success_rate

    @success_rate.setter
    def success_rate(self, success_rate):
        """Sets the success_rate of this AdvancedGameStatOffenseRushingPlays.


        :param success_rate: The success_rate of this AdvancedGameStatOffenseRushingPlays.  # noqa: E501
        :type: float
        """

        self._success_rate = success_rate

    @property
    def explosiveness(self):
        """Gets the explosiveness of this AdvancedGameStatOffenseRushingPlays.  # noqa: E501


        :return: The explosiveness of this AdvancedGameStatOffenseRushingPlays.  # noqa: E501
        :rtype: float
        """
        return self._explosiveness

    @explosiveness.setter
    def explosiveness(self, explosiveness):
        """Sets the explosiveness of this AdvancedGameStatOffenseRushingPlays.


        :param explosiveness: The explosiveness of this AdvancedGameStatOffenseRushingPlays.  # noqa: E501
        :type: float
        """

        self._explosiveness = explosiveness

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AdvancedGameStatOffenseRushingPlays, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AdvancedGameStatOffenseRushingPlays):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
