# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  It currently has a wide array of data ranging from play by play to player statistics to game scores and more.  # noqa: E501

    OpenAPI spec version: 2.2.10
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class BoxScoreTeamsExplosiveness(object):
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
        'team': 'str',
        'overall': 'BoxScoreTeamsOverall'
    }

    attribute_map = {
        'team': 'team',
        'overall': 'overall'
    }

    def __init__(self, team=None, overall=None):  # noqa: E501
        """BoxScoreTeamsExplosiveness - a model defined in Swagger"""  # noqa: E501

        self._team = None
        self._overall = None
        self.discriminator = None

        if team is not None:
            self.team = team
        if overall is not None:
            self.overall = overall

    @property
    def team(self):
        """Gets the team of this BoxScoreTeamsExplosiveness.  # noqa: E501


        :return: The team of this BoxScoreTeamsExplosiveness.  # noqa: E501
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this BoxScoreTeamsExplosiveness.


        :param team: The team of this BoxScoreTeamsExplosiveness.  # noqa: E501
        :type: str
        """

        self._team = team

    @property
    def overall(self):
        """Gets the overall of this BoxScoreTeamsExplosiveness.  # noqa: E501


        :return: The overall of this BoxScoreTeamsExplosiveness.  # noqa: E501
        :rtype: BoxScoreTeamsOverall
        """
        return self._overall

    @overall.setter
    def overall(self, overall):
        """Sets the overall of this BoxScoreTeamsExplosiveness.


        :param overall: The overall of this BoxScoreTeamsExplosiveness.  # noqa: E501
        :type: BoxScoreTeamsOverall
        """

        self._overall = overall

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
        if issubclass(BoxScoreTeamsExplosiveness, dict):
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
        if not isinstance(other, BoxScoreTeamsExplosiveness):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
