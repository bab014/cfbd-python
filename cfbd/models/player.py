# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\"). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501

    OpenAPI spec version: 4.1.7
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from cfbd.configuration import Configuration


class Player(object):
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
        'first_name': 'str',
        'last_name': 'str',
        'team': 'str',
        'height': 'int',
        'weight': 'int',
        'jersey': 'int',
        'year': 'int',
        'position': 'str',
        'home_city': 'str',
        'home_state': 'str',
        'home_country': 'str',
        'home_latitude': 'float',
        'home_longitude': 'float',
        'home_county_fips': 'str',
        'recruit_ids': 'list[int]'
    }

    attribute_map = {
        'id': 'id',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'team': 'team',
        'height': 'height',
        'weight': 'weight',
        'jersey': 'jersey',
        'year': 'year',
        'position': 'position',
        'home_city': 'home_city',
        'home_state': 'home_state',
        'home_country': 'home_country',
        'home_latitude': 'home_latitude',
        'home_longitude': 'home_longitude',
        'home_county_fips': 'home_county_fips',
        'recruit_ids': 'recruit_ids'
    }

    def __init__(self, id=None, first_name=None, last_name=None, team=None, height=None, weight=None, jersey=None, year=None, position=None, home_city=None, home_state=None, home_country=None, home_latitude=None, home_longitude=None, home_county_fips=None, recruit_ids=None, _configuration=None):  # noqa: E501
        """Player - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._first_name = None
        self._last_name = None
        self._team = None
        self._height = None
        self._weight = None
        self._jersey = None
        self._year = None
        self._position = None
        self._home_city = None
        self._home_state = None
        self._home_country = None
        self._home_latitude = None
        self._home_longitude = None
        self._home_county_fips = None
        self._recruit_ids = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if team is not None:
            self.team = team
        if height is not None:
            self.height = height
        if weight is not None:
            self.weight = weight
        if jersey is not None:
            self.jersey = jersey
        if year is not None:
            self.year = year
        if position is not None:
            self.position = position
        if home_city is not None:
            self.home_city = home_city
        if home_state is not None:
            self.home_state = home_state
        if home_country is not None:
            self.home_country = home_country
        if home_latitude is not None:
            self.home_latitude = home_latitude
        if home_longitude is not None:
            self.home_longitude = home_longitude
        if home_county_fips is not None:
            self.home_county_fips = home_county_fips
        if recruit_ids is not None:
            self.recruit_ids = recruit_ids

    @property
    def id(self):
        """Gets the id of this Player.  # noqa: E501


        :return: The id of this Player.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Player.


        :param id: The id of this Player.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def first_name(self):
        """Gets the first_name of this Player.  # noqa: E501


        :return: The first_name of this Player.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this Player.


        :param first_name: The first_name of this Player.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this Player.  # noqa: E501


        :return: The last_name of this Player.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this Player.


        :param last_name: The last_name of this Player.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def team(self):
        """Gets the team of this Player.  # noqa: E501


        :return: The team of this Player.  # noqa: E501
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this Player.


        :param team: The team of this Player.  # noqa: E501
        :type: str
        """

        self._team = team

    @property
    def height(self):
        """Gets the height of this Player.  # noqa: E501


        :return: The height of this Player.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this Player.


        :param height: The height of this Player.  # noqa: E501
        :type: int
        """

        self._height = height

    @property
    def weight(self):
        """Gets the weight of this Player.  # noqa: E501


        :return: The weight of this Player.  # noqa: E501
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this Player.


        :param weight: The weight of this Player.  # noqa: E501
        :type: int
        """

        self._weight = weight

    @property
    def jersey(self):
        """Gets the jersey of this Player.  # noqa: E501


        :return: The jersey of this Player.  # noqa: E501
        :rtype: int
        """
        return self._jersey

    @jersey.setter
    def jersey(self, jersey):
        """Sets the jersey of this Player.


        :param jersey: The jersey of this Player.  # noqa: E501
        :type: int
        """

        self._jersey = jersey

    @property
    def year(self):
        """Gets the year of this Player.  # noqa: E501


        :return: The year of this Player.  # noqa: E501
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this Player.


        :param year: The year of this Player.  # noqa: E501
        :type: int
        """

        self._year = year

    @property
    def position(self):
        """Gets the position of this Player.  # noqa: E501


        :return: The position of this Player.  # noqa: E501
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this Player.


        :param position: The position of this Player.  # noqa: E501
        :type: str
        """

        self._position = position

    @property
    def home_city(self):
        """Gets the home_city of this Player.  # noqa: E501


        :return: The home_city of this Player.  # noqa: E501
        :rtype: str
        """
        return self._home_city

    @home_city.setter
    def home_city(self, home_city):
        """Sets the home_city of this Player.


        :param home_city: The home_city of this Player.  # noqa: E501
        :type: str
        """

        self._home_city = home_city

    @property
    def home_state(self):
        """Gets the home_state of this Player.  # noqa: E501


        :return: The home_state of this Player.  # noqa: E501
        :rtype: str
        """
        return self._home_state

    @home_state.setter
    def home_state(self, home_state):
        """Sets the home_state of this Player.


        :param home_state: The home_state of this Player.  # noqa: E501
        :type: str
        """

        self._home_state = home_state

    @property
    def home_country(self):
        """Gets the home_country of this Player.  # noqa: E501


        :return: The home_country of this Player.  # noqa: E501
        :rtype: str
        """
        return self._home_country

    @home_country.setter
    def home_country(self, home_country):
        """Sets the home_country of this Player.


        :param home_country: The home_country of this Player.  # noqa: E501
        :type: str
        """

        self._home_country = home_country

    @property
    def home_latitude(self):
        """Gets the home_latitude of this Player.  # noqa: E501


        :return: The home_latitude of this Player.  # noqa: E501
        :rtype: float
        """
        return self._home_latitude

    @home_latitude.setter
    def home_latitude(self, home_latitude):
        """Sets the home_latitude of this Player.


        :param home_latitude: The home_latitude of this Player.  # noqa: E501
        :type: float
        """

        self._home_latitude = home_latitude

    @property
    def home_longitude(self):
        """Gets the home_longitude of this Player.  # noqa: E501


        :return: The home_longitude of this Player.  # noqa: E501
        :rtype: float
        """
        return self._home_longitude

    @home_longitude.setter
    def home_longitude(self, home_longitude):
        """Sets the home_longitude of this Player.


        :param home_longitude: The home_longitude of this Player.  # noqa: E501
        :type: float
        """

        self._home_longitude = home_longitude

    @property
    def home_county_fips(self):
        """Gets the home_county_fips of this Player.  # noqa: E501


        :return: The home_county_fips of this Player.  # noqa: E501
        :rtype: str
        """
        return self._home_county_fips

    @home_county_fips.setter
    def home_county_fips(self, home_county_fips):
        """Sets the home_county_fips of this Player.


        :param home_county_fips: The home_county_fips of this Player.  # noqa: E501
        :type: str
        """

        self._home_county_fips = home_county_fips

    @property
    def recruit_ids(self):
        """Gets the recruit_ids of this Player.  # noqa: E501


        :return: The recruit_ids of this Player.  # noqa: E501
        :rtype: list[int]
        """
        return self._recruit_ids

    @recruit_ids.setter
    def recruit_ids(self, recruit_ids):
        """Sets the recruit_ids of this Player.


        :param recruit_ids: The recruit_ids of this Player.  # noqa: E501
        :type: list[int]
        """

        self._recruit_ids = recruit_ids

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
        if issubclass(Player, dict):
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
        if not isinstance(other, Player):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Player):
            return True

        return self.to_dict() != other.to_dict()
