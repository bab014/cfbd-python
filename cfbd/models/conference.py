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


class Conference(object):
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
        'short_name': 'str',
        'abbreviation': 'str',
        'classification': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'short_name': 'short_name',
        'abbreviation': 'abbreviation',
        'classification': 'classification'
    }

    def __init__(self, id=None, name=None, short_name=None, abbreviation=None, classification=None, _configuration=None):  # noqa: E501
        """Conference - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._short_name = None
        self._abbreviation = None
        self._classification = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if short_name is not None:
            self.short_name = short_name
        if abbreviation is not None:
            self.abbreviation = abbreviation
        if classification is not None:
            self.classification = classification

    @property
    def id(self):
        """Gets the id of this Conference.  # noqa: E501


        :return: The id of this Conference.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Conference.


        :param id: The id of this Conference.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Conference.  # noqa: E501


        :return: The name of this Conference.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Conference.


        :param name: The name of this Conference.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def short_name(self):
        """Gets the short_name of this Conference.  # noqa: E501


        :return: The short_name of this Conference.  # noqa: E501
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """Sets the short_name of this Conference.


        :param short_name: The short_name of this Conference.  # noqa: E501
        :type: str
        """

        self._short_name = short_name

    @property
    def abbreviation(self):
        """Gets the abbreviation of this Conference.  # noqa: E501


        :return: The abbreviation of this Conference.  # noqa: E501
        :rtype: str
        """
        return self._abbreviation

    @abbreviation.setter
    def abbreviation(self, abbreviation):
        """Sets the abbreviation of this Conference.


        :param abbreviation: The abbreviation of this Conference.  # noqa: E501
        :type: str
        """

        self._abbreviation = abbreviation

    @property
    def classification(self):
        """Gets the classification of this Conference.  # noqa: E501


        :return: The classification of this Conference.  # noqa: E501
        :rtype: str
        """
        return self._classification

    @classification.setter
    def classification(self, classification):
        """Sets the classification of this Conference.


        :param classification: The classification of this Conference.  # noqa: E501
        :type: str
        """

        self._classification = classification

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
        if issubclass(Conference, dict):
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
        if not isinstance(other, Conference):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Conference):
            return True

        return self.to_dict() != other.to_dict()
