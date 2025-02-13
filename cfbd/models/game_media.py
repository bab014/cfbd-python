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


class GameMedia(object):
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
        'id': 'int',
        'season': 'int',
        'week': 'int',
        'season_type': 'str',
        'start_time': 'str',
        'is_start_time_tbd': 'bool',
        'home_team': 'str',
        'home_conference': 'str',
        'away_team': 'str',
        'away_conference': 'str',
        'media_type': 'str',
        'outlet': 'str'
    }

    attribute_map = {
        'id': 'id',
        'season': 'season',
        'week': 'week',
        'season_type': 'seasonType',
        'start_time': 'startTime',
        'is_start_time_tbd': 'isStartTimeTBD',
        'home_team': 'homeTeam',
        'home_conference': 'homeConference',
        'away_team': 'awayTeam',
        'away_conference': 'awayConference',
        'media_type': 'mediaType',
        'outlet': 'outlet'
    }

    def __init__(self, id=None, season=None, week=None, season_type=None, start_time=None, is_start_time_tbd=None, home_team=None, home_conference=None, away_team=None, away_conference=None, media_type=None, outlet=None, _configuration=None):  # noqa: E501
        """GameMedia - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._season = None
        self._week = None
        self._season_type = None
        self._start_time = None
        self._is_start_time_tbd = None
        self._home_team = None
        self._home_conference = None
        self._away_team = None
        self._away_conference = None
        self._media_type = None
        self._outlet = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if season is not None:
            self.season = season
        if week is not None:
            self.week = week
        if season_type is not None:
            self.season_type = season_type
        if start_time is not None:
            self.start_time = start_time
        if is_start_time_tbd is not None:
            self.is_start_time_tbd = is_start_time_tbd
        if home_team is not None:
            self.home_team = home_team
        if home_conference is not None:
            self.home_conference = home_conference
        if away_team is not None:
            self.away_team = away_team
        if away_conference is not None:
            self.away_conference = away_conference
        if media_type is not None:
            self.media_type = media_type
        if outlet is not None:
            self.outlet = outlet

    @property
    def id(self):
        """Gets the id of this GameMedia.  # noqa: E501


        :return: The id of this GameMedia.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GameMedia.


        :param id: The id of this GameMedia.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def season(self):
        """Gets the season of this GameMedia.  # noqa: E501


        :return: The season of this GameMedia.  # noqa: E501
        :rtype: int
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this GameMedia.


        :param season: The season of this GameMedia.  # noqa: E501
        :type: int
        """

        self._season = season

    @property
    def week(self):
        """Gets the week of this GameMedia.  # noqa: E501


        :return: The week of this GameMedia.  # noqa: E501
        :rtype: int
        """
        return self._week

    @week.setter
    def week(self, week):
        """Sets the week of this GameMedia.


        :param week: The week of this GameMedia.  # noqa: E501
        :type: int
        """

        self._week = week

    @property
    def season_type(self):
        """Gets the season_type of this GameMedia.  # noqa: E501


        :return: The season_type of this GameMedia.  # noqa: E501
        :rtype: str
        """
        return self._season_type

    @season_type.setter
    def season_type(self, season_type):
        """Sets the season_type of this GameMedia.


        :param season_type: The season_type of this GameMedia.  # noqa: E501
        :type: str
        """

        self._season_type = season_type

    @property
    def start_time(self):
        """Gets the start_time of this GameMedia.  # noqa: E501


        :return: The start_time of this GameMedia.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this GameMedia.


        :param start_time: The start_time of this GameMedia.  # noqa: E501
        :type: str
        """

        self._start_time = start_time

    @property
    def is_start_time_tbd(self):
        """Gets the is_start_time_tbd of this GameMedia.  # noqa: E501


        :return: The is_start_time_tbd of this GameMedia.  # noqa: E501
        :rtype: bool
        """
        return self._is_start_time_tbd

    @is_start_time_tbd.setter
    def is_start_time_tbd(self, is_start_time_tbd):
        """Sets the is_start_time_tbd of this GameMedia.


        :param is_start_time_tbd: The is_start_time_tbd of this GameMedia.  # noqa: E501
        :type: bool
        """

        self._is_start_time_tbd = is_start_time_tbd

    @property
    def home_team(self):
        """Gets the home_team of this GameMedia.  # noqa: E501


        :return: The home_team of this GameMedia.  # noqa: E501
        :rtype: str
        """
        return self._home_team

    @home_team.setter
    def home_team(self, home_team):
        """Sets the home_team of this GameMedia.


        :param home_team: The home_team of this GameMedia.  # noqa: E501
        :type: str
        """

        self._home_team = home_team

    @property
    def home_conference(self):
        """Gets the home_conference of this GameMedia.  # noqa: E501


        :return: The home_conference of this GameMedia.  # noqa: E501
        :rtype: str
        """
        return self._home_conference

    @home_conference.setter
    def home_conference(self, home_conference):
        """Sets the home_conference of this GameMedia.


        :param home_conference: The home_conference of this GameMedia.  # noqa: E501
        :type: str
        """

        self._home_conference = home_conference

    @property
    def away_team(self):
        """Gets the away_team of this GameMedia.  # noqa: E501


        :return: The away_team of this GameMedia.  # noqa: E501
        :rtype: str
        """
        return self._away_team

    @away_team.setter
    def away_team(self, away_team):
        """Sets the away_team of this GameMedia.


        :param away_team: The away_team of this GameMedia.  # noqa: E501
        :type: str
        """

        self._away_team = away_team

    @property
    def away_conference(self):
        """Gets the away_conference of this GameMedia.  # noqa: E501


        :return: The away_conference of this GameMedia.  # noqa: E501
        :rtype: str
        """
        return self._away_conference

    @away_conference.setter
    def away_conference(self, away_conference):
        """Sets the away_conference of this GameMedia.


        :param away_conference: The away_conference of this GameMedia.  # noqa: E501
        :type: str
        """

        self._away_conference = away_conference

    @property
    def media_type(self):
        """Gets the media_type of this GameMedia.  # noqa: E501


        :return: The media_type of this GameMedia.  # noqa: E501
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """Sets the media_type of this GameMedia.


        :param media_type: The media_type of this GameMedia.  # noqa: E501
        :type: str
        """

        self._media_type = media_type

    @property
    def outlet(self):
        """Gets the outlet of this GameMedia.  # noqa: E501


        :return: The outlet of this GameMedia.  # noqa: E501
        :rtype: str
        """
        return self._outlet

    @outlet.setter
    def outlet(self, outlet):
        """Sets the outlet of this GameMedia.


        :param outlet: The outlet of this GameMedia.  # noqa: E501
        :type: str
        """

        self._outlet = outlet

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
        if issubclass(GameMedia, dict):
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
        if not isinstance(other, GameMedia):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GameMedia):
            return True

        return self.to_dict() != other.to_dict()
