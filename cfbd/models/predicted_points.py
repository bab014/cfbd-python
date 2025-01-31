# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\"). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501

    OpenAPI spec version: 4.1.11
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from cfbd.configuration import Configuration


class PredictedPoints(object):
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
        'yard_line': 'int',
        'predicted_points': 'float'
    }

    attribute_map = {
        'yard_line': 'yardLine',
        'predicted_points': 'predictedPoints'
    }

    def __init__(self, yard_line=None, predicted_points=None, _configuration=None):  # noqa: E501
        """PredictedPoints - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._yard_line = None
        self._predicted_points = None
        self.discriminator = None

        if yard_line is not None:
            self.yard_line = yard_line
        if predicted_points is not None:
            self.predicted_points = predicted_points

    @property
    def yard_line(self):
        """Gets the yard_line of this PredictedPoints.  # noqa: E501


        :return: The yard_line of this PredictedPoints.  # noqa: E501
        :rtype: int
        """
        return self._yard_line

    @yard_line.setter
    def yard_line(self, yard_line):
        """Sets the yard_line of this PredictedPoints.


        :param yard_line: The yard_line of this PredictedPoints.  # noqa: E501
        :type: int
        """

        self._yard_line = yard_line

    @property
    def predicted_points(self):
        """Gets the predicted_points of this PredictedPoints.  # noqa: E501


        :return: The predicted_points of this PredictedPoints.  # noqa: E501
        :rtype: float
        """
        return self._predicted_points

    @predicted_points.setter
    def predicted_points(self, predicted_points):
        """Sets the predicted_points of this PredictedPoints.


        :param predicted_points: The predicted_points of this PredictedPoints.  # noqa: E501
        :type: float
        """

        self._predicted_points = predicted_points

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
        if issubclass(PredictedPoints, dict):
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
        if not isinstance(other, PredictedPoints):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PredictedPoints):
            return True

        return self.to_dict() != other.to_dict()
