# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\"). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501

    OpenAPI spec version: 4.1.8
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import cfbd
from cfbd.api.metrics_api import MetricsApi  # noqa: E501
from cfbd.rest import ApiException


class TestMetricsApi(unittest.TestCase):
    """MetricsApi unit test stubs"""

    def setUp(self):
        self.api = cfbd.api.metrics_api.MetricsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_game_ppa(self):
        """Test case for get_game_ppa

        Team Predicated Points Added (PPA/EPA) by game  # noqa: E501
        """
        pass

    def test_get_player_game_ppa(self):
        """Test case for get_player_game_ppa

        Player Predicated Points Added (PPA/EPA) broken down by game  # noqa: E501
        """
        pass

    def test_get_player_season_ppa(self):
        """Test case for get_player_season_ppa

        Player Predicated Points Added (PPA/EPA) broken down by season  # noqa: E501
        """
        pass

    def test_get_predicted_points(self):
        """Test case for get_predicted_points

        Predicted Points (i.e. Expected Points or EP)  # noqa: E501
        """
        pass

    def test_get_pregame_win_probabilities(self):
        """Test case for get_pregame_win_probabilities

        Pregame win probability data  # noqa: E501
        """
        pass

    def test_get_team_ppa(self):
        """Test case for get_team_ppa

        Predicted Points Added (PPA/EPA) data by team  # noqa: E501
        """
        pass

    def test_get_win_probability_data(self):
        """Test case for get_win_probability_data

        Win probability chart data  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
