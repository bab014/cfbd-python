# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  It currently has a wide array of data ranging from play by play to player statistics to game scores and more.  # noqa: E501

    OpenAPI spec version: 2.2.2
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class BoxScorePlayersUsage(object):
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
        'player': 'str',
        'team': 'str',
        'position': 'str',
        'total': 'float',
        'quarter1': 'float',
        'quarter2': 'float',
        'quarter3': 'float',
        'quarter4': 'float',
        'rushing': 'float',
        'passing': 'float'
    }

    attribute_map = {
        'player': 'player',
        'team': 'team',
        'position': 'position',
        'total': 'total',
        'quarter1': 'quarter1',
        'quarter2': 'quarter2',
        'quarter3': 'quarter3',
        'quarter4': 'quarter4',
        'rushing': 'rushing',
        'passing': 'passing'
    }

    def __init__(self, player=None, team=None, position=None, total=None, quarter1=None, quarter2=None, quarter3=None, quarter4=None, rushing=None, passing=None):  # noqa: E501
        """BoxScorePlayersUsage - a model defined in Swagger"""  # noqa: E501

        self._player = None
        self._team = None
        self._position = None
        self._total = None
        self._quarter1 = None
        self._quarter2 = None
        self._quarter3 = None
        self._quarter4 = None
        self._rushing = None
        self._passing = None
        self.discriminator = None

        if player is not None:
            self.player = player
        if team is not None:
            self.team = team
        if position is not None:
            self.position = position
        if total is not None:
            self.total = total
        if quarter1 is not None:
            self.quarter1 = quarter1
        if quarter2 is not None:
            self.quarter2 = quarter2
        if quarter3 is not None:
            self.quarter3 = quarter3
        if quarter4 is not None:
            self.quarter4 = quarter4
        if rushing is not None:
            self.rushing = rushing
        if passing is not None:
            self.passing = passing

    @property
    def player(self):
        """Gets the player of this BoxScorePlayersUsage.  # noqa: E501


        :return: The player of this BoxScorePlayersUsage.  # noqa: E501
        :rtype: str
        """
        return self._player

    @player.setter
    def player(self, player):
        """Sets the player of this BoxScorePlayersUsage.


        :param player: The player of this BoxScorePlayersUsage.  # noqa: E501
        :type: str
        """

        self._player = player

    @property
    def team(self):
        """Gets the team of this BoxScorePlayersUsage.  # noqa: E501


        :return: The team of this BoxScorePlayersUsage.  # noqa: E501
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this BoxScorePlayersUsage.


        :param team: The team of this BoxScorePlayersUsage.  # noqa: E501
        :type: str
        """

        self._team = team

    @property
    def position(self):
        """Gets the position of this BoxScorePlayersUsage.  # noqa: E501


        :return: The position of this BoxScorePlayersUsage.  # noqa: E501
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this BoxScorePlayersUsage.


        :param position: The position of this BoxScorePlayersUsage.  # noqa: E501
        :type: str
        """

        self._position = position

    @property
    def total(self):
        """Gets the total of this BoxScorePlayersUsage.  # noqa: E501


        :return: The total of this BoxScorePlayersUsage.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this BoxScorePlayersUsage.


        :param total: The total of this BoxScorePlayersUsage.  # noqa: E501
        :type: float
        """

        self._total = total

    @property
    def quarter1(self):
        """Gets the quarter1 of this BoxScorePlayersUsage.  # noqa: E501


        :return: The quarter1 of this BoxScorePlayersUsage.  # noqa: E501
        :rtype: float
        """
        return self._quarter1

    @quarter1.setter
    def quarter1(self, quarter1):
        """Sets the quarter1 of this BoxScorePlayersUsage.


        :param quarter1: The quarter1 of this BoxScorePlayersUsage.  # noqa: E501
        :type: float
        """

        self._quarter1 = quarter1

    @property
    def quarter2(self):
        """Gets the quarter2 of this BoxScorePlayersUsage.  # noqa: E501


        :return: The quarter2 of this BoxScorePlayersUsage.  # noqa: E501
        :rtype: float
        """
        return self._quarter2

    @quarter2.setter
    def quarter2(self, quarter2):
        """Sets the quarter2 of this BoxScorePlayersUsage.


        :param quarter2: The quarter2 of this BoxScorePlayersUsage.  # noqa: E501
        :type: float
        """

        self._quarter2 = quarter2

    @property
    def quarter3(self):
        """Gets the quarter3 of this BoxScorePlayersUsage.  # noqa: E501


        :return: The quarter3 of this BoxScorePlayersUsage.  # noqa: E501
        :rtype: float
        """
        return self._quarter3

    @quarter3.setter
    def quarter3(self, quarter3):
        """Sets the quarter3 of this BoxScorePlayersUsage.


        :param quarter3: The quarter3 of this BoxScorePlayersUsage.  # noqa: E501
        :type: float
        """

        self._quarter3 = quarter3

    @property
    def quarter4(self):
        """Gets the quarter4 of this BoxScorePlayersUsage.  # noqa: E501


        :return: The quarter4 of this BoxScorePlayersUsage.  # noqa: E501
        :rtype: float
        """
        return self._quarter4

    @quarter4.setter
    def quarter4(self, quarter4):
        """Sets the quarter4 of this BoxScorePlayersUsage.


        :param quarter4: The quarter4 of this BoxScorePlayersUsage.  # noqa: E501
        :type: float
        """

        self._quarter4 = quarter4

    @property
    def rushing(self):
        """Gets the rushing of this BoxScorePlayersUsage.  # noqa: E501


        :return: The rushing of this BoxScorePlayersUsage.  # noqa: E501
        :rtype: float
        """
        return self._rushing

    @rushing.setter
    def rushing(self, rushing):
        """Sets the rushing of this BoxScorePlayersUsage.


        :param rushing: The rushing of this BoxScorePlayersUsage.  # noqa: E501
        :type: float
        """

        self._rushing = rushing

    @property
    def passing(self):
        """Gets the passing of this BoxScorePlayersUsage.  # noqa: E501


        :return: The passing of this BoxScorePlayersUsage.  # noqa: E501
        :rtype: float
        """
        return self._passing

    @passing.setter
    def passing(self, passing):
        """Sets the passing of this BoxScorePlayersUsage.


        :param passing: The passing of this BoxScorePlayersUsage.  # noqa: E501
        :type: float
        """

        self._passing = passing

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
        if issubclass(BoxScorePlayersUsage, dict):
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
        if not isinstance(other, BoxScorePlayersUsage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
