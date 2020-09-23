# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  It currently has a wide array of data ranging from play by play to player statistics to game scores and more.  # noqa: E501

    OpenAPI spec version: 2.2.14
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PositionGroupRecruitingRating(object):
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
        'conference': 'str',
        'positiion_group': 'str',
        'average_rating': 'float',
        'total_rating': 'float',
        'commits': 'float',
        'average_stars': 'float'
    }

    attribute_map = {
        'team': 'team',
        'conference': 'conference',
        'positiion_group': 'positiionGroup',
        'average_rating': 'averageRating',
        'total_rating': 'totalRating',
        'commits': 'commits',
        'average_stars': 'averageStars'
    }

    def __init__(self, team=None, conference=None, positiion_group=None, average_rating=None, total_rating=None, commits=None, average_stars=None):  # noqa: E501
        """PositionGroupRecruitingRating - a model defined in Swagger"""  # noqa: E501

        self._team = None
        self._conference = None
        self._positiion_group = None
        self._average_rating = None
        self._total_rating = None
        self._commits = None
        self._average_stars = None
        self.discriminator = None

        if team is not None:
            self.team = team
        if conference is not None:
            self.conference = conference
        if positiion_group is not None:
            self.positiion_group = positiion_group
        if average_rating is not None:
            self.average_rating = average_rating
        if total_rating is not None:
            self.total_rating = total_rating
        if commits is not None:
            self.commits = commits
        if average_stars is not None:
            self.average_stars = average_stars

    @property
    def team(self):
        """Gets the team of this PositionGroupRecruitingRating.  # noqa: E501


        :return: The team of this PositionGroupRecruitingRating.  # noqa: E501
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this PositionGroupRecruitingRating.


        :param team: The team of this PositionGroupRecruitingRating.  # noqa: E501
        :type: str
        """

        self._team = team

    @property
    def conference(self):
        """Gets the conference of this PositionGroupRecruitingRating.  # noqa: E501


        :return: The conference of this PositionGroupRecruitingRating.  # noqa: E501
        :rtype: str
        """
        return self._conference

    @conference.setter
    def conference(self, conference):
        """Sets the conference of this PositionGroupRecruitingRating.


        :param conference: The conference of this PositionGroupRecruitingRating.  # noqa: E501
        :type: str
        """

        self._conference = conference

    @property
    def positiion_group(self):
        """Gets the positiion_group of this PositionGroupRecruitingRating.  # noqa: E501


        :return: The positiion_group of this PositionGroupRecruitingRating.  # noqa: E501
        :rtype: str
        """
        return self._positiion_group

    @positiion_group.setter
    def positiion_group(self, positiion_group):
        """Sets the positiion_group of this PositionGroupRecruitingRating.


        :param positiion_group: The positiion_group of this PositionGroupRecruitingRating.  # noqa: E501
        :type: str
        """

        self._positiion_group = positiion_group

    @property
    def average_rating(self):
        """Gets the average_rating of this PositionGroupRecruitingRating.  # noqa: E501


        :return: The average_rating of this PositionGroupRecruitingRating.  # noqa: E501
        :rtype: float
        """
        return self._average_rating

    @average_rating.setter
    def average_rating(self, average_rating):
        """Sets the average_rating of this PositionGroupRecruitingRating.


        :param average_rating: The average_rating of this PositionGroupRecruitingRating.  # noqa: E501
        :type: float
        """

        self._average_rating = average_rating

    @property
    def total_rating(self):
        """Gets the total_rating of this PositionGroupRecruitingRating.  # noqa: E501


        :return: The total_rating of this PositionGroupRecruitingRating.  # noqa: E501
        :rtype: float
        """
        return self._total_rating

    @total_rating.setter
    def total_rating(self, total_rating):
        """Sets the total_rating of this PositionGroupRecruitingRating.


        :param total_rating: The total_rating of this PositionGroupRecruitingRating.  # noqa: E501
        :type: float
        """

        self._total_rating = total_rating

    @property
    def commits(self):
        """Gets the commits of this PositionGroupRecruitingRating.  # noqa: E501


        :return: The commits of this PositionGroupRecruitingRating.  # noqa: E501
        :rtype: float
        """
        return self._commits

    @commits.setter
    def commits(self, commits):
        """Sets the commits of this PositionGroupRecruitingRating.


        :param commits: The commits of this PositionGroupRecruitingRating.  # noqa: E501
        :type: float
        """

        self._commits = commits

    @property
    def average_stars(self):
        """Gets the average_stars of this PositionGroupRecruitingRating.  # noqa: E501


        :return: The average_stars of this PositionGroupRecruitingRating.  # noqa: E501
        :rtype: float
        """
        return self._average_stars

    @average_stars.setter
    def average_stars(self, average_stars):
        """Sets the average_stars of this PositionGroupRecruitingRating.


        :param average_stars: The average_stars of this PositionGroupRecruitingRating.  # noqa: E501
        :type: float
        """

        self._average_stars = average_stars

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
        if issubclass(PositionGroupRecruitingRating, dict):
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
        if not isinstance(other, PositionGroupRecruitingRating):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
