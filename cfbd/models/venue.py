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


class Venue(object):
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
        'name': 'str',
        'capacity': 'int',
        'grass': 'bool',
        'city': 'str',
        'state': 'str',
        'zip': 'str',
        'country_code': 'str',
        'location': 'object',
        'elevation': 'float',
        'year': 'int',
        'dome': 'bool',
        'timezone': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'capacity': 'capacity',
        'grass': 'grass',
        'city': 'city',
        'state': 'state',
        'zip': 'zip',
        'country_code': 'country_code',
        'location': 'location',
        'elevation': 'elevation',
        'year': 'year',
        'dome': 'dome',
        'timezone': 'timezone'
    }

    def __init__(self, id=None, name=None, capacity=None, grass=None, city=None, state=None, zip=None, country_code=None, location=None, elevation=None, year=None, dome=None, timezone=None, _configuration=None):  # noqa: E501
        """Venue - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._capacity = None
        self._grass = None
        self._city = None
        self._state = None
        self._zip = None
        self._country_code = None
        self._location = None
        self._elevation = None
        self._year = None
        self._dome = None
        self._timezone = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if capacity is not None:
            self.capacity = capacity
        if grass is not None:
            self.grass = grass
        if city is not None:
            self.city = city
        if state is not None:
            self.state = state
        if zip is not None:
            self.zip = zip
        if country_code is not None:
            self.country_code = country_code
        if location is not None:
            self.location = location
        if elevation is not None:
            self.elevation = elevation
        if year is not None:
            self.year = year
        if dome is not None:
            self.dome = dome
        if timezone is not None:
            self.timezone = timezone

    @property
    def id(self):
        """Gets the id of this Venue.  # noqa: E501


        :return: The id of this Venue.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Venue.


        :param id: The id of this Venue.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Venue.  # noqa: E501


        :return: The name of this Venue.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Venue.


        :param name: The name of this Venue.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def capacity(self):
        """Gets the capacity of this Venue.  # noqa: E501


        :return: The capacity of this Venue.  # noqa: E501
        :rtype: int
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this Venue.


        :param capacity: The capacity of this Venue.  # noqa: E501
        :type: int
        """

        self._capacity = capacity

    @property
    def grass(self):
        """Gets the grass of this Venue.  # noqa: E501


        :return: The grass of this Venue.  # noqa: E501
        :rtype: bool
        """
        return self._grass

    @grass.setter
    def grass(self, grass):
        """Sets the grass of this Venue.


        :param grass: The grass of this Venue.  # noqa: E501
        :type: bool
        """

        self._grass = grass

    @property
    def city(self):
        """Gets the city of this Venue.  # noqa: E501


        :return: The city of this Venue.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Venue.


        :param city: The city of this Venue.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def state(self):
        """Gets the state of this Venue.  # noqa: E501


        :return: The state of this Venue.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Venue.


        :param state: The state of this Venue.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def zip(self):
        """Gets the zip of this Venue.  # noqa: E501


        :return: The zip of this Venue.  # noqa: E501
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """Sets the zip of this Venue.


        :param zip: The zip of this Venue.  # noqa: E501
        :type: str
        """

        self._zip = zip

    @property
    def country_code(self):
        """Gets the country_code of this Venue.  # noqa: E501


        :return: The country_code of this Venue.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this Venue.


        :param country_code: The country_code of this Venue.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def location(self):
        """Gets the location of this Venue.  # noqa: E501


        :return: The location of this Venue.  # noqa: E501
        :rtype: object
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this Venue.


        :param location: The location of this Venue.  # noqa: E501
        :type: object
        """

        self._location = location

    @property
    def elevation(self):
        """Gets the elevation of this Venue.  # noqa: E501


        :return: The elevation of this Venue.  # noqa: E501
        :rtype: float
        """
        return self._elevation

    @elevation.setter
    def elevation(self, elevation):
        """Sets the elevation of this Venue.


        :param elevation: The elevation of this Venue.  # noqa: E501
        :type: float
        """

        self._elevation = elevation

    @property
    def year(self):
        """Gets the year of this Venue.  # noqa: E501


        :return: The year of this Venue.  # noqa: E501
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this Venue.


        :param year: The year of this Venue.  # noqa: E501
        :type: int
        """

        self._year = year

    @property
    def dome(self):
        """Gets the dome of this Venue.  # noqa: E501


        :return: The dome of this Venue.  # noqa: E501
        :rtype: bool
        """
        return self._dome

    @dome.setter
    def dome(self, dome):
        """Sets the dome of this Venue.


        :param dome: The dome of this Venue.  # noqa: E501
        :type: bool
        """

        self._dome = dome

    @property
    def timezone(self):
        """Gets the timezone of this Venue.  # noqa: E501


        :return: The timezone of this Venue.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this Venue.


        :param timezone: The timezone of this Venue.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

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
        if issubclass(Venue, dict):
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
        if not isinstance(other, Venue):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Venue):
            return True

        return self.to_dict() != other.to_dict()
