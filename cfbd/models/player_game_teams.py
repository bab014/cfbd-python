# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  It currently has a wide array of data ranging from play by play to player statistics to game scores and more.  # noqa: E501

    OpenAPI spec version: 2.2.1
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PlayerGameTeams(object):
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
        'school': 'PlayerGameSchool',
        'home_away': 'bool',
        'points': 'int',
        'categories': 'list[PlayerGameCategories]'
    }

    attribute_map = {
        'school': 'school',
        'home_away': 'homeAway',
        'points': 'points',
        'categories': 'categories'
    }

    def __init__(self, school=None, home_away=None, points=None, categories=None):  # noqa: E501
        """PlayerGameTeams - a model defined in Swagger"""  # noqa: E501

        self._school = None
        self._home_away = None
        self._points = None
        self._categories = None
        self.discriminator = None

        if school is not None:
            self.school = school
        if home_away is not None:
            self.home_away = home_away
        if points is not None:
            self.points = points
        if categories is not None:
            self.categories = categories

    @property
    def school(self):
        """Gets the school of this PlayerGameTeams.  # noqa: E501


        :return: The school of this PlayerGameTeams.  # noqa: E501
        :rtype: PlayerGameSchool
        """
        return self._school

    @school.setter
    def school(self, school):
        """Sets the school of this PlayerGameTeams.


        :param school: The school of this PlayerGameTeams.  # noqa: E501
        :type: PlayerGameSchool
        """

        self._school = school

    @property
    def home_away(self):
        """Gets the home_away of this PlayerGameTeams.  # noqa: E501


        :return: The home_away of this PlayerGameTeams.  # noqa: E501
        :rtype: bool
        """
        return self._home_away

    @home_away.setter
    def home_away(self, home_away):
        """Sets the home_away of this PlayerGameTeams.


        :param home_away: The home_away of this PlayerGameTeams.  # noqa: E501
        :type: bool
        """

        self._home_away = home_away

    @property
    def points(self):
        """Gets the points of this PlayerGameTeams.  # noqa: E501


        :return: The points of this PlayerGameTeams.  # noqa: E501
        :rtype: int
        """
        return self._points

    @points.setter
    def points(self, points):
        """Sets the points of this PlayerGameTeams.


        :param points: The points of this PlayerGameTeams.  # noqa: E501
        :type: int
        """

        self._points = points

    @property
    def categories(self):
        """Gets the categories of this PlayerGameTeams.  # noqa: E501


        :return: The categories of this PlayerGameTeams.  # noqa: E501
        :rtype: list[PlayerGameCategories]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this PlayerGameTeams.


        :param categories: The categories of this PlayerGameTeams.  # noqa: E501
        :type: list[PlayerGameCategories]
        """

        self._categories = categories

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
        if issubclass(PlayerGameTeams, dict):
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
        if not isinstance(other, PlayerGameTeams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
