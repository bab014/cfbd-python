# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\"). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501

    OpenAPI spec version: 4.1.11
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import cfbd
from cfbd.api.plays_api import PlaysApi  # noqa: E501
from cfbd.rest import ApiException


class TestPlaysApi(unittest.TestCase):
    """PlaysApi unit test stubs"""

    def setUp(self):
        self.api = cfbd.api.plays_api.PlaysApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_play_stat_types(self):
        """Test case for get_play_stat_types

        Types of player play stats  # noqa: E501
        """
        pass

    def test_get_play_stats(self):
        """Test case for get_play_stats

        Play stats by play  # noqa: E501
        """
        pass

    def test_get_play_types(self):
        """Test case for get_play_types

        Play types  # noqa: E501
        """
        pass

    def test_get_plays(self):
        """Test case for get_plays

        Play by play data  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
