# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\"). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501

    OpenAPI spec version: 4.1.11
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from cfbd.api_client import ApiClient


class TeamsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_fbs_teams(self, **kwargs):  # noqa: E501
        """FBS team list  # noqa: E501

        Information on major division teams  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_fbs_teams(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Year filter
        :return: list[Team]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_fbs_teams_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_fbs_teams_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_fbs_teams_with_http_info(self, **kwargs):  # noqa: E501
        """FBS team list  # noqa: E501

        Information on major division teams  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_fbs_teams_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Year filter
        :return: list[Team]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['year']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_fbs_teams" % key
                )
            params[key] = val
        del params['kwargs']

        if self.api_client.client_side_validation and ('year' in params and params['year'] < 1869):  # noqa: E501
            raise ValueError("Invalid value for parameter `year` when calling `get_fbs_teams`, must be a value greater than or equal to `1869`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'year' in params:
            query_params.append(('year', params['year']))  # noqa: E501

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
            '/teams/fbs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Team]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_roster(self, **kwargs):  # noqa: E501
        """Team rosters  # noqa: E501

        Roster data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_roster(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str team: Team name
        :param int year: Season year
        :return: list[Player]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_roster_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_roster_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_roster_with_http_info(self, **kwargs):  # noqa: E501
        """Team rosters  # noqa: E501

        Roster data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_roster_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str team: Team name
        :param int year: Season year
        :return: list[Player]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['team', 'year']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_roster" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'team' in params:
            query_params.append(('team', params['team']))  # noqa: E501
        if 'year' in params:
            query_params.append(('year', params['year']))  # noqa: E501

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
            '/roster', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Player]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_talent(self, **kwargs):  # noqa: E501
        """Team talent composite rankings  # noqa: E501

        Team talent composite  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_talent(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Year filter
        :return: list[TeamTalent]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_talent_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_talent_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_talent_with_http_info(self, **kwargs):  # noqa: E501
        """Team talent composite rankings  # noqa: E501

        Team talent composite  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_talent_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Year filter
        :return: list[TeamTalent]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['year']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_talent" % key
                )
            params[key] = val
        del params['kwargs']

        if self.api_client.client_side_validation and ('year' in params and params['year'] < 2015):  # noqa: E501
            raise ValueError("Invalid value for parameter `year` when calling `get_talent`, must be a value greater than or equal to `2015`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'year' in params:
            query_params.append(('year', params['year']))  # noqa: E501

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
            '/talent', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[TeamTalent]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_team_matchup(self, team1, team2, **kwargs):  # noqa: E501
        """Team matchup history  # noqa: E501

        Matchup history  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_team_matchup(team1, team2, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str team1: First team (required)
        :param str team2: Second team (required)
        :param int min_year: Minimum year
        :param int max_year: Maximum year
        :return: TeamMatchup
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_team_matchup_with_http_info(team1, team2, **kwargs)  # noqa: E501
        else:
            (data) = self.get_team_matchup_with_http_info(team1, team2, **kwargs)  # noqa: E501
            return data

    def get_team_matchup_with_http_info(self, team1, team2, **kwargs):  # noqa: E501
        """Team matchup history  # noqa: E501

        Matchup history  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_team_matchup_with_http_info(team1, team2, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str team1: First team (required)
        :param str team2: Second team (required)
        :param int min_year: Minimum year
        :param int max_year: Maximum year
        :return: TeamMatchup
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['team1', 'team2', 'min_year', 'max_year']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_team_matchup" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'team1' is set
        if self.api_client.client_side_validation and ('team1' not in params or
                                                       params['team1'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `team1` when calling `get_team_matchup`")  # noqa: E501
        # verify the required parameter 'team2' is set
        if self.api_client.client_side_validation and ('team2' not in params or
                                                       params['team2'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `team2` when calling `get_team_matchup`")  # noqa: E501

        if self.api_client.client_side_validation and ('max_year' in params and params['max_year'] < 1869):  # noqa: E501
            raise ValueError("Invalid value for parameter `max_year` when calling `get_team_matchup`, must be a value greater than or equal to `1869`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'team1' in params:
            query_params.append(('team1', params['team1']))  # noqa: E501
        if 'team2' in params:
            query_params.append(('team2', params['team2']))  # noqa: E501
        if 'min_year' in params:
            query_params.append(('minYear', params['min_year']))  # noqa: E501
        if 'max_year' in params:
            query_params.append(('maxYear', params['max_year']))  # noqa: E501

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
            '/teams/matchup', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TeamMatchup',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_teams(self, **kwargs):  # noqa: E501
        """Team information  # noqa: E501

        Get team information  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_teams(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str conference: Conference abbreviation filter
        :return: list[Team]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_teams_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_teams_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_teams_with_http_info(self, **kwargs):  # noqa: E501
        """Team information  # noqa: E501

        Get team information  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_teams_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str conference: Conference abbreviation filter
        :return: list[Team]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conference']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_teams" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
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
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/teams', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Team]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
