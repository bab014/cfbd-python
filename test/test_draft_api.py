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
from cfbd.api.draft_api import DraftApi  # noqa: E501
from cfbd.rest import ApiException


class TestDraftApi(unittest.TestCase):
    """DraftApi unit test stubs"""

    def setUp(self):
        self.api = cfbd.api.draft_api.DraftApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_draft_picks(self):
        """Test case for get_draft_picks

        List of NFL Draft picks  # noqa: E501
        """
        pass

    def test_get_nfl_positions(self):
        """Test case for get_nfl_positions

        List of NFL positions  # noqa: E501
        """
        pass

    def test_get_nfl_teams(self):
        """Test case for get_nfl_teams

        List of NFL teams  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
