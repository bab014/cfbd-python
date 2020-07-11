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


class TeamSRSRating(object):
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
        'year': 'int',
        'team': 'str',
        'conference': 'str',
        'division': 'str',
        'rating': 'float'
    }

    attribute_map = {
        'year': 'year',
        'team': 'team',
        'conference': 'conference',
        'division': 'division',
        'rating': 'rating'
    }

    def __init__(self, year=None, team=None, conference=None, division=None, rating=None):  # noqa: E501
        """TeamSRSRating - a model defined in Swagger"""  # noqa: E501

        self._year = None
        self._team = None
        self._conference = None
        self._division = None
        self._rating = None
        self.discriminator = None

        if year is not None:
            self.year = year
        if team is not None:
            self.team = team
        if conference is not None:
            self.conference = conference
        if division is not None:
            self.division = division
        if rating is not None:
            self.rating = rating

    @property
    def year(self):
        """Gets the year of this TeamSRSRating.  # noqa: E501


        :return: The year of this TeamSRSRating.  # noqa: E501
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this TeamSRSRating.


        :param year: The year of this TeamSRSRating.  # noqa: E501
        :type: int
        """

        self._year = year

    @property
    def team(self):
        """Gets the team of this TeamSRSRating.  # noqa: E501


        :return: The team of this TeamSRSRating.  # noqa: E501
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this TeamSRSRating.


        :param team: The team of this TeamSRSRating.  # noqa: E501
        :type: str
        """

        self._team = team

    @property
    def conference(self):
        """Gets the conference of this TeamSRSRating.  # noqa: E501


        :return: The conference of this TeamSRSRating.  # noqa: E501
        :rtype: str
        """
        return self._conference

    @conference.setter
    def conference(self, conference):
        """Sets the conference of this TeamSRSRating.


        :param conference: The conference of this TeamSRSRating.  # noqa: E501
        :type: str
        """

        self._conference = conference

    @property
    def division(self):
        """Gets the division of this TeamSRSRating.  # noqa: E501


        :return: The division of this TeamSRSRating.  # noqa: E501
        :rtype: str
        """
        return self._division

    @division.setter
    def division(self, division):
        """Sets the division of this TeamSRSRating.


        :param division: The division of this TeamSRSRating.  # noqa: E501
        :type: str
        """

        self._division = division

    @property
    def rating(self):
        """Gets the rating of this TeamSRSRating.  # noqa: E501


        :return: The rating of this TeamSRSRating.  # noqa: E501
        :rtype: float
        """
        return self._rating

    @rating.setter
    def rating(self, rating):
        """Sets the rating of this TeamSRSRating.


        :param rating: The rating of this TeamSRSRating.  # noqa: E501
        :type: float
        """

        self._rating = rating

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
        if issubclass(TeamSRSRating, dict):
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
        if not isinstance(other, TeamSRSRating):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
