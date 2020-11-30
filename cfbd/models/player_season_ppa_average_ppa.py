# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  It currently has a wide array of data ranging from play by play to player statistics to game scores and more.  # noqa: E501

    OpenAPI spec version: 2.3.3
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PlayerSeasonPPAAveragePPA(object):
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
        'all': 'float',
        '_pass': 'float',
        'rush': 'float',
        'first_down': 'float',
        'second_down': 'float',
        'third_down': 'float',
        'standard_downs': 'float',
        'passing_downs': 'float'
    }

    attribute_map = {
        'all': 'all',
        '_pass': 'pass',
        'rush': 'rush',
        'first_down': 'firstDown',
        'second_down': 'secondDown',
        'third_down': 'thirdDown',
        'standard_downs': 'standardDowns',
        'passing_downs': 'passingDowns'
    }

    def __init__(self, all=None, _pass=None, rush=None, first_down=None, second_down=None, third_down=None, standard_downs=None, passing_downs=None):  # noqa: E501
        """PlayerSeasonPPAAveragePPA - a model defined in Swagger"""  # noqa: E501

        self._all = None
        self.__pass = None
        self._rush = None
        self._first_down = None
        self._second_down = None
        self._third_down = None
        self._standard_downs = None
        self._passing_downs = None
        self.discriminator = None

        if all is not None:
            self.all = all
        if _pass is not None:
            self._pass = _pass
        if rush is not None:
            self.rush = rush
        if first_down is not None:
            self.first_down = first_down
        if second_down is not None:
            self.second_down = second_down
        if third_down is not None:
            self.third_down = third_down
        if standard_downs is not None:
            self.standard_downs = standard_downs
        if passing_downs is not None:
            self.passing_downs = passing_downs

    @property
    def all(self):
        """Gets the all of this PlayerSeasonPPAAveragePPA.  # noqa: E501


        :return: The all of this PlayerSeasonPPAAveragePPA.  # noqa: E501
        :rtype: float
        """
        return self._all

    @all.setter
    def all(self, all):
        """Sets the all of this PlayerSeasonPPAAveragePPA.


        :param all: The all of this PlayerSeasonPPAAveragePPA.  # noqa: E501
        :type: float
        """

        self._all = all

    @property
    def _pass(self):
        """Gets the _pass of this PlayerSeasonPPAAveragePPA.  # noqa: E501


        :return: The _pass of this PlayerSeasonPPAAveragePPA.  # noqa: E501
        :rtype: float
        """
        return self.__pass

    @_pass.setter
    def _pass(self, _pass):
        """Sets the _pass of this PlayerSeasonPPAAveragePPA.


        :param _pass: The _pass of this PlayerSeasonPPAAveragePPA.  # noqa: E501
        :type: float
        """

        self.__pass = _pass

    @property
    def rush(self):
        """Gets the rush of this PlayerSeasonPPAAveragePPA.  # noqa: E501


        :return: The rush of this PlayerSeasonPPAAveragePPA.  # noqa: E501
        :rtype: float
        """
        return self._rush

    @rush.setter
    def rush(self, rush):
        """Sets the rush of this PlayerSeasonPPAAveragePPA.


        :param rush: The rush of this PlayerSeasonPPAAveragePPA.  # noqa: E501
        :type: float
        """

        self._rush = rush

    @property
    def first_down(self):
        """Gets the first_down of this PlayerSeasonPPAAveragePPA.  # noqa: E501


        :return: The first_down of this PlayerSeasonPPAAveragePPA.  # noqa: E501
        :rtype: float
        """
        return self._first_down

    @first_down.setter
    def first_down(self, first_down):
        """Sets the first_down of this PlayerSeasonPPAAveragePPA.


        :param first_down: The first_down of this PlayerSeasonPPAAveragePPA.  # noqa: E501
        :type: float
        """

        self._first_down = first_down

    @property
    def second_down(self):
        """Gets the second_down of this PlayerSeasonPPAAveragePPA.  # noqa: E501


        :return: The second_down of this PlayerSeasonPPAAveragePPA.  # noqa: E501
        :rtype: float
        """
        return self._second_down

    @second_down.setter
    def second_down(self, second_down):
        """Sets the second_down of this PlayerSeasonPPAAveragePPA.


        :param second_down: The second_down of this PlayerSeasonPPAAveragePPA.  # noqa: E501
        :type: float
        """

        self._second_down = second_down

    @property
    def third_down(self):
        """Gets the third_down of this PlayerSeasonPPAAveragePPA.  # noqa: E501


        :return: The third_down of this PlayerSeasonPPAAveragePPA.  # noqa: E501
        :rtype: float
        """
        return self._third_down

    @third_down.setter
    def third_down(self, third_down):
        """Sets the third_down of this PlayerSeasonPPAAveragePPA.


        :param third_down: The third_down of this PlayerSeasonPPAAveragePPA.  # noqa: E501
        :type: float
        """

        self._third_down = third_down

    @property
    def standard_downs(self):
        """Gets the standard_downs of this PlayerSeasonPPAAveragePPA.  # noqa: E501


        :return: The standard_downs of this PlayerSeasonPPAAveragePPA.  # noqa: E501
        :rtype: float
        """
        return self._standard_downs

    @standard_downs.setter
    def standard_downs(self, standard_downs):
        """Sets the standard_downs of this PlayerSeasonPPAAveragePPA.


        :param standard_downs: The standard_downs of this PlayerSeasonPPAAveragePPA.  # noqa: E501
        :type: float
        """

        self._standard_downs = standard_downs

    @property
    def passing_downs(self):
        """Gets the passing_downs of this PlayerSeasonPPAAveragePPA.  # noqa: E501


        :return: The passing_downs of this PlayerSeasonPPAAveragePPA.  # noqa: E501
        :rtype: float
        """
        return self._passing_downs

    @passing_downs.setter
    def passing_downs(self, passing_downs):
        """Sets the passing_downs of this PlayerSeasonPPAAveragePPA.


        :param passing_downs: The passing_downs of this PlayerSeasonPPAAveragePPA.  # noqa: E501
        :type: float
        """

        self._passing_downs = passing_downs

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
        if issubclass(PlayerSeasonPPAAveragePPA, dict):
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
        if not isinstance(other, PlayerSeasonPPAAveragePPA):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
