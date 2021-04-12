# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\").  # noqa: E501

    OpenAPI spec version: 3.2.1
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from cfbd.api_client import ApiClient


class StatsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_advanced_team_game_stats(self, **kwargs):  # noqa: E501
        """Advanced team metrics by game  # noqa: E501

        Advanced team game stats  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_advanced_team_game_stats(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Year filter (required if no team specified)
        :param int week: Week filter
        :param str team: Team filter (required if no year specified)
        :param str opponent: Opponent filter
        :param bool exclude_garbage_time: Filter to remove garbage time plays from calculations
        :param str season_type: Season type filter (regular, postseason, or both)
        :return: list[AdvancedGameStat]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_advanced_team_game_stats_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_advanced_team_game_stats_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_advanced_team_game_stats_with_http_info(self, **kwargs):  # noqa: E501
        """Advanced team metrics by game  # noqa: E501

        Advanced team game stats  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_advanced_team_game_stats_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Year filter (required if no team specified)
        :param int week: Week filter
        :param str team: Team filter (required if no year specified)
        :param str opponent: Opponent filter
        :param bool exclude_garbage_time: Filter to remove garbage time plays from calculations
        :param str season_type: Season type filter (regular, postseason, or both)
        :return: list[AdvancedGameStat]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['year', 'week', 'team', 'opponent', 'exclude_garbage_time', 'season_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_advanced_team_game_stats" % key
                )
            params[key] = val
        del params['kwargs']

        if self.api_client.client_side_validation and ('year' in params and params['year'] < 2001):  # noqa: E501
            raise ValueError("Invalid value for parameter `year` when calling `get_advanced_team_game_stats`, must be a value greater than or equal to `2001`")  # noqa: E501
        if self.api_client.client_side_validation and ('week' in params and params['week'] > 16):  # noqa: E501
            raise ValueError("Invalid value for parameter `week` when calling `get_advanced_team_game_stats`, must be a value less than or equal to `16`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'year' in params:
            query_params.append(('year', params['year']))  # noqa: E501
        if 'week' in params:
            query_params.append(('week', params['week']))  # noqa: E501
        if 'team' in params:
            query_params.append(('team', params['team']))  # noqa: E501
        if 'opponent' in params:
            query_params.append(('opponent', params['opponent']))  # noqa: E501
        if 'exclude_garbage_time' in params:
            query_params.append(('excludeGarbageTime', params['exclude_garbage_time']))  # noqa: E501
        if 'season_type' in params:
            query_params.append(('seasonType', params['season_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/stats/game/advanced', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[AdvancedGameStat]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_advanced_team_season_stats(self, **kwargs):  # noqa: E501
        """Advanced team metrics by season  # noqa: E501

        Advanced team season stats  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_advanced_team_season_stats(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Year filter (required if no team specified)
        :param str team: Team filter (required if no year specified)
        :param bool exclude_garbage_time: Filter to remove garbage time plays from calculations
        :param int start_week: Starting week filter
        :param int end_week: Starting week filter
        :return: list[AdvancedSeasonStat]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_advanced_team_season_stats_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_advanced_team_season_stats_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_advanced_team_season_stats_with_http_info(self, **kwargs):  # noqa: E501
        """Advanced team metrics by season  # noqa: E501

        Advanced team season stats  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_advanced_team_season_stats_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Year filter (required if no team specified)
        :param str team: Team filter (required if no year specified)
        :param bool exclude_garbage_time: Filter to remove garbage time plays from calculations
        :param int start_week: Starting week filter
        :param int end_week: Starting week filter
        :return: list[AdvancedSeasonStat]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['year', 'team', 'exclude_garbage_time', 'start_week', 'end_week']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_advanced_team_season_stats" % key
                )
            params[key] = val
        del params['kwargs']

        if self.api_client.client_side_validation and ('year' in params and params['year'] < 2001):  # noqa: E501
            raise ValueError("Invalid value for parameter `year` when calling `get_advanced_team_season_stats`, must be a value greater than or equal to `2001`")  # noqa: E501
        if self.api_client.client_side_validation and ('start_week' in params and params['start_week'] > 16):  # noqa: E501
            raise ValueError("Invalid value for parameter `start_week` when calling `get_advanced_team_season_stats`, must be a value less than or equal to `16`")  # noqa: E501
        if self.api_client.client_side_validation and ('end_week' in params and params['end_week'] > 16):  # noqa: E501
            raise ValueError("Invalid value for parameter `end_week` when calling `get_advanced_team_season_stats`, must be a value less than or equal to `16`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'year' in params:
            query_params.append(('year', params['year']))  # noqa: E501
        if 'team' in params:
            query_params.append(('team', params['team']))  # noqa: E501
        if 'exclude_garbage_time' in params:
            query_params.append(('excludeGarbageTime', params['exclude_garbage_time']))  # noqa: E501
        if 'start_week' in params:
            query_params.append(('startWeek', params['start_week']))  # noqa: E501
        if 'end_week' in params:
            query_params.append(('endWeek', params['end_week']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/stats/season/advanced', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[AdvancedSeasonStat]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_stat_categories(self, **kwargs):  # noqa: E501
        """Team stat categories  # noqa: E501

        Stat category list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_stat_categories(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_stat_categories_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_stat_categories_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_stat_categories_with_http_info(self, **kwargs):  # noqa: E501
        """Team stat categories  # noqa: E501

        Stat category list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_stat_categories_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_stat_categories" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/stats/categories', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[str]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_team_season_stats(self, **kwargs):  # noqa: E501
        """Team statistics by season  # noqa: E501

        Team season stats  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_team_season_stats(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Year filter (required if no team specified)
        :param str team: Team filter (required if no year specified)
        :param str conference: Conference abbreviation filter
        :param int start_week: Starting week filter
        :param int end_week: Starting week filter
        :return: list[TeamSeasonStat]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_team_season_stats_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_team_season_stats_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_team_season_stats_with_http_info(self, **kwargs):  # noqa: E501
        """Team statistics by season  # noqa: E501

        Team season stats  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_team_season_stats_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Year filter (required if no team specified)
        :param str team: Team filter (required if no year specified)
        :param str conference: Conference abbreviation filter
        :param int start_week: Starting week filter
        :param int end_week: Starting week filter
        :return: list[TeamSeasonStat]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['year', 'team', 'conference', 'start_week', 'end_week']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_team_season_stats" % key
                )
            params[key] = val
        del params['kwargs']

        if self.api_client.client_side_validation and ('year' in params and params['year'] < 2001):  # noqa: E501
            raise ValueError("Invalid value for parameter `year` when calling `get_team_season_stats`, must be a value greater than or equal to `2001`")  # noqa: E501
        if self.api_client.client_side_validation and ('start_week' in params and params['start_week'] > 16):  # noqa: E501
            raise ValueError("Invalid value for parameter `start_week` when calling `get_team_season_stats`, must be a value less than or equal to `16`")  # noqa: E501
        if self.api_client.client_side_validation and ('end_week' in params and params['end_week'] > 16):  # noqa: E501
            raise ValueError("Invalid value for parameter `end_week` when calling `get_team_season_stats`, must be a value less than or equal to `16`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'year' in params:
            query_params.append(('year', params['year']))  # noqa: E501
        if 'team' in params:
            query_params.append(('team', params['team']))  # noqa: E501
        if 'conference' in params:
            query_params.append(('conference', params['conference']))  # noqa: E501
        if 'start_week' in params:
            query_params.append(('startWeek', params['start_week']))  # noqa: E501
        if 'end_week' in params:
            query_params.append(('endWeek', params['end_week']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/stats/season', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[TeamSeasonStat]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
