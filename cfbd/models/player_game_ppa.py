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


class PlayerGamePPA(object):
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
        'season': 'int',
        'week': 'int',
        'name': 'str',
        'position': 'str',
        'team': 'str',
        'opponent': 'str',
        'average_ppa': 'object'
    }

    attribute_map = {
        'season': 'season',
        'week': 'week',
        'name': 'name',
        'position': 'position',
        'team': 'team',
        'opponent': 'opponent',
        'average_ppa': 'averagePPA'
    }

    def __init__(self, season=None, week=None, name=None, position=None, team=None, opponent=None, average_ppa=None, _configuration=None):  # noqa: E501
        """PlayerGamePPA - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._season = None
        self._week = None
        self._name = None
        self._position = None
        self._team = None
        self._opponent = None
        self._average_ppa = None
        self.discriminator = None

        if season is not None:
            self.season = season
        if week is not None:
            self.week = week
        if name is not None:
            self.name = name
        if position is not None:
            self.position = position
        if team is not None:
            self.team = team
        if opponent is not None:
            self.opponent = opponent
        if average_ppa is not None:
            self.average_ppa = average_ppa

    @property
    def season(self):
        """Gets the season of this PlayerGamePPA.  # noqa: E501


        :return: The season of this PlayerGamePPA.  # noqa: E501
        :rtype: int
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this PlayerGamePPA.


        :param season: The season of this PlayerGamePPA.  # noqa: E501
        :type: int
        """

        self._season = season

    @property
    def week(self):
        """Gets the week of this PlayerGamePPA.  # noqa: E501


        :return: The week of this PlayerGamePPA.  # noqa: E501
        :rtype: int
        """
        return self._week

    @week.setter
    def week(self, week):
        """Sets the week of this PlayerGamePPA.


        :param week: The week of this PlayerGamePPA.  # noqa: E501
        :type: int
        """

        self._week = week

    @property
    def name(self):
        """Gets the name of this PlayerGamePPA.  # noqa: E501


        :return: The name of this PlayerGamePPA.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PlayerGamePPA.


        :param name: The name of this PlayerGamePPA.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def position(self):
        """Gets the position of this PlayerGamePPA.  # noqa: E501


        :return: The position of this PlayerGamePPA.  # noqa: E501
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this PlayerGamePPA.


        :param position: The position of this PlayerGamePPA.  # noqa: E501
        :type: str
        """

        self._position = position

    @property
    def team(self):
        """Gets the team of this PlayerGamePPA.  # noqa: E501


        :return: The team of this PlayerGamePPA.  # noqa: E501
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this PlayerGamePPA.


        :param team: The team of this PlayerGamePPA.  # noqa: E501
        :type: str
        """

        self._team = team

    @property
    def opponent(self):
        """Gets the opponent of this PlayerGamePPA.  # noqa: E501


        :return: The opponent of this PlayerGamePPA.  # noqa: E501
        :rtype: str
        """
        return self._opponent

    @opponent.setter
    def opponent(self, opponent):
        """Sets the opponent of this PlayerGamePPA.


        :param opponent: The opponent of this PlayerGamePPA.  # noqa: E501
        :type: str
        """

        self._opponent = opponent

    @property
    def average_ppa(self):
        """Gets the average_ppa of this PlayerGamePPA.  # noqa: E501


        :return: The average_ppa of this PlayerGamePPA.  # noqa: E501
        :rtype: object
        """
        return self._average_ppa

    @average_ppa.setter
    def average_ppa(self, average_ppa):
        """Sets the average_ppa of this PlayerGamePPA.


        :param average_ppa: The average_ppa of this PlayerGamePPA.  # noqa: E501
        :type: object
        """

        self._average_ppa = average_ppa

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
        if issubclass(PlayerGamePPA, dict):
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
        if not isinstance(other, PlayerGamePPA):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PlayerGamePPA):
            return True

        return self.to_dict() != other.to_dict()
