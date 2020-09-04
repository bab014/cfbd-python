# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  It currently has a wide array of data ranging from play by play to player statistics to game scores and more.  # noqa: E501

    OpenAPI spec version: 2.2.11
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class BoxScore(object):
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
        'teams': 'BoxScoreTeams',
        'players': 'BoxScorePlayers'
    }

    attribute_map = {
        'teams': 'teams',
        'players': 'players'
    }

    def __init__(self, teams=None, players=None):  # noqa: E501
        """BoxScore - a model defined in Swagger"""  # noqa: E501

        self._teams = None
        self._players = None
        self.discriminator = None

        if teams is not None:
            self.teams = teams
        if players is not None:
            self.players = players

    @property
    def teams(self):
        """Gets the teams of this BoxScore.  # noqa: E501


        :return: The teams of this BoxScore.  # noqa: E501
        :rtype: BoxScoreTeams
        """
        return self._teams

    @teams.setter
    def teams(self, teams):
        """Sets the teams of this BoxScore.


        :param teams: The teams of this BoxScore.  # noqa: E501
        :type: BoxScoreTeams
        """

        self._teams = teams

    @property
    def players(self):
        """Gets the players of this BoxScore.  # noqa: E501


        :return: The players of this BoxScore.  # noqa: E501
        :rtype: BoxScorePlayers
        """
        return self._players

    @players.setter
    def players(self, players):
        """Sets the players of this BoxScore.


        :param players: The players of this BoxScore.  # noqa: E501
        :type: BoxScorePlayers
        """

        self._players = players

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
        if issubclass(BoxScore, dict):
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
        if not isinstance(other, BoxScore):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
