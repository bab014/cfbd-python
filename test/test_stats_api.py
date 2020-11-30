# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  It currently has a wide array of data ranging from play by play to player statistics to game scores and more.  # noqa: E501

    OpenAPI spec version: 2.3.2
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import cfbd
from cfbd.api.stats_api import StatsApi  # noqa: E501
from cfbd.rest import ApiException


class TestStatsApi(unittest.TestCase):
    """StatsApi unit test stubs"""

    def setUp(self):
        self.api = cfbd.api.stats_api.StatsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_advanced_team_game_stats(self):
        """Test case for get_advanced_team_game_stats

        Advanced team metrics by game  # noqa: E501
        """
        pass

    def test_get_advanced_team_season_stats(self):
        """Test case for get_advanced_team_season_stats

        Advanced team metrics by season  # noqa: E501
        """
        pass

    def test_get_stat_categories(self):
        """Test case for get_stat_categories

        Team stat categories  # noqa: E501
        """
        pass

    def test_get_team_season_stats(self):
        """Test case for get_team_season_stats

        Team statistics by season  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
