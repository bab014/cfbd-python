# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\").  # noqa: E501

    OpenAPI spec version: 3.2.0
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import cfbd
from cfbd.models.team_record import TeamRecord  # noqa: E501
from cfbd.rest import ApiException


class TestTeamRecord(unittest.TestCase):
    """TeamRecord unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTeamRecord(self):
        """Test TeamRecord"""
        # FIXME: construct object with mandatory attributes with example values
        # model = cfbd.models.team_record.TeamRecord()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
