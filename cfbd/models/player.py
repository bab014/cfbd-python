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
        'height': 'int',
        'weight': 'int',
        'jersey': 'int',
        'year': 'int',
        'position': 'str',
        'city': 'str',
        'state': 'str',
        'country': 'str'
    }

    attribute_map = {
        'id': 'id',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'height': 'height',
        'weight': 'weight',
        'jersey': 'jersey',
        'year': 'year',
        'position': 'position',
        'city': 'city',
        'state': 'state',
        'country': 'country'
    }

    def __init__(self, id=None, first_name=None, last_name=None, height=None, weight=None, jersey=None, year=None, position=None, city=None, state=None, country=None):  # noqa: E501
        """Player - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._first_name = None
        self._last_name = None
        self._height = None
        self._weight = None
        self._jersey = None
        self._year = None
        self._position = None
        self._city = None
        self._state = None
        self._country = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
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
        if city is not None:
            self.city = city
        if state is not None:
            self.state = state
        if country is not None:
            self.country = country

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
    def city(self):
        """Gets the city of this Player.  # noqa: E501


        :return: The city of this Player.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Player.


        :param city: The city of this Player.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def state(self):
        """Gets the state of this Player.  # noqa: E501


        :return: The state of this Player.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Player.


        :param state: The state of this Player.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def country(self):
        """Gets the country of this Player.  # noqa: E501


        :return: The country of this Player.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Player.


        :param country: The country of this Player.  # noqa: E501
        :type: str
        """

        self._country = country

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

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
