# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  It currently has a wide array of data ranging from play by play to player statistics to game scores and more.  # noqa: E501

    OpenAPI spec version: 2.2.12
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AdvancedSeasonStatOffenseFieldPosition(object):
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
        'average_start': 'float',
        'average_predicted_points': 'float'
    }

    attribute_map = {
        'average_start': 'averageStart',
        'average_predicted_points': 'averagePredictedPoints'
    }

    def __init__(self, average_start=None, average_predicted_points=None):  # noqa: E501
        """AdvancedSeasonStatOffenseFieldPosition - a model defined in Swagger"""  # noqa: E501

        self._average_start = None
        self._average_predicted_points = None
        self.discriminator = None

        if average_start is not None:
            self.average_start = average_start
        if average_predicted_points is not None:
            self.average_predicted_points = average_predicted_points

    @property
    def average_start(self):
        """Gets the average_start of this AdvancedSeasonStatOffenseFieldPosition.  # noqa: E501


        :return: The average_start of this AdvancedSeasonStatOffenseFieldPosition.  # noqa: E501
        :rtype: float
        """
        return self._average_start

    @average_start.setter
    def average_start(self, average_start):
        """Sets the average_start of this AdvancedSeasonStatOffenseFieldPosition.


        :param average_start: The average_start of this AdvancedSeasonStatOffenseFieldPosition.  # noqa: E501
        :type: float
        """

        self._average_start = average_start

    @property
    def average_predicted_points(self):
        """Gets the average_predicted_points of this AdvancedSeasonStatOffenseFieldPosition.  # noqa: E501


        :return: The average_predicted_points of this AdvancedSeasonStatOffenseFieldPosition.  # noqa: E501
        :rtype: float
        """
        return self._average_predicted_points

    @average_predicted_points.setter
    def average_predicted_points(self, average_predicted_points):
        """Sets the average_predicted_points of this AdvancedSeasonStatOffenseFieldPosition.


        :param average_predicted_points: The average_predicted_points of this AdvancedSeasonStatOffenseFieldPosition.  # noqa: E501
        :type: float
        """

        self._average_predicted_points = average_predicted_points

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
        if issubclass(AdvancedSeasonStatOffenseFieldPosition, dict):
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
        if not isinstance(other, AdvancedSeasonStatOffenseFieldPosition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
