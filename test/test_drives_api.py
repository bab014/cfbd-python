# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\"). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501

    OpenAPI spec version: 4.1.3
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import cfbd
from cfbd.api.drives_api import DrivesApi  # noqa: E501
from cfbd.rest import ApiException


class TestDrivesApi(unittest.TestCase):
    """DrivesApi unit test stubs"""

    def setUp(self):
        self.api = cfbd.api.drives_api.DrivesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_drives(self):
        """Test case for get_drives

        Drive data and results  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
