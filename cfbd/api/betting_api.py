# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  It currently has a wide array of data ranging from play by play to player statistics to game scores and more.  # noqa: E501

    OpenAPI spec version: 2.2.1
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from cfbd.api_client import ApiClient


class BettingApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_lines(self, **kwargs):  # noqa: E501
        """Get betting line information  # noqa: E501

        Closing betting lines  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_lines(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int game_id: Game id filter
        :param int year: Year/season filter for games
        :param int week: Week filter
        :param str season_type: Season type filter (regular or postseason)
        :param str team: Team
        :param str home: Home team filter
        :param str away: Away team filter
        :param str conference: Conference abbreviation filter
        :return: list[GameLines]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_lines_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_lines_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_lines_with_http_info(self, **kwargs):  # noqa: E501
        """Get betting line information  # noqa: E501

        Closing betting lines  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_lines_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int game_id: Game id filter
        :param int year: Year/season filter for games
        :param int week: Week filter
        :param str season_type: Season type filter (regular or postseason)
        :param str team: Team
        :param str home: Home team filter
        :param str away: Away team filter
        :param str conference: Conference abbreviation filter
        :return: list[GameLines]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['game_id', 'year', 'week', 'season_type', 'team', 'home', 'away', 'conference']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_lines" % key
                )
            params[key] = val
        del params['kwargs']

        if 'year' in params and params['year'] < 2013:  # noqa: E501
            raise ValueError("Invalid value for parameter `year` when calling `get_lines`, must be a value greater than or equal to `2013`")  # noqa: E501
        if 'week' in params and params['week'] > 16:  # noqa: E501
            raise ValueError("Invalid value for parameter `week` when calling `get_lines`, must be a value less than or equal to `16`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'game_id' in params:
            query_params.append(('gameId', params['game_id']))  # noqa: E501
        if 'year' in params:
            query_params.append(('year', params['year']))  # noqa: E501
        if 'week' in params:
            query_params.append(('week', params['week']))  # noqa: E501
        if 'season_type' in params:
            query_params.append(('seasonType', params['season_type']))  # noqa: E501
        if 'team' in params:
            query_params.append(('team', params['team']))  # noqa: E501
        if 'home' in params:
            query_params.append(('home', params['home']))  # noqa: E501
        if 'away' in params:
            query_params.append(('away', params['away']))  # noqa: E501
        if 'conference' in params:
            query_params.append(('conference', params['conference']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/lines', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GameLines]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
