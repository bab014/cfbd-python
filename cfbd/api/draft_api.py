# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\"). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501

    OpenAPI spec version: 4.0.0
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from cfbd.api_client import ApiClient


class DraftApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_draft_picks(self, **kwargs):  # noqa: E501
        """List of NFL Draft picks  # noqa: E501

        List of NFL Draft picks  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_draft_picks(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Year filter
        :param str nfl_team: NFL team filter
        :param str college: Player college filter
        :param str conference: College confrence abbreviation filter
        :param str position: NFL position filter
        :return: list[DraftPick]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_draft_picks_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_draft_picks_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_draft_picks_with_http_info(self, **kwargs):  # noqa: E501
        """List of NFL Draft picks  # noqa: E501

        List of NFL Draft picks  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_draft_picks_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Year filter
        :param str nfl_team: NFL team filter
        :param str college: Player college filter
        :param str conference: College confrence abbreviation filter
        :param str position: NFL position filter
        :return: list[DraftPick]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['year', 'nfl_team', 'college', 'conference', 'position']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_draft_picks" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'year' in params:
            query_params.append(('year', params['year']))  # noqa: E501
        if 'nfl_team' in params:
            query_params.append(('nflTeam', params['nfl_team']))  # noqa: E501
        if 'college' in params:
            query_params.append(('college', params['college']))  # noqa: E501
        if 'conference' in params:
            query_params.append(('conference', params['conference']))  # noqa: E501
        if 'position' in params:
            query_params.append(('position', params['position']))  # noqa: E501

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
            '/draft/picks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[DraftPick]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_nfl_positions(self, **kwargs):  # noqa: E501
        """List of NFL positions  # noqa: E501

        List of NFL positions  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_nfl_positions(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[DraftPosition]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_nfl_positions_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_nfl_positions_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_nfl_positions_with_http_info(self, **kwargs):  # noqa: E501
        """List of NFL positions  # noqa: E501

        List of NFL positions  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_nfl_positions_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[DraftPosition]
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
                    " to method get_nfl_positions" % key
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
            '/draft/positions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[DraftPosition]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_nfl_teams(self, **kwargs):  # noqa: E501
        """List of NFL teams  # noqa: E501

        List of NFL teams  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_nfl_teams(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[DraftTeam]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_nfl_teams_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_nfl_teams_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_nfl_teams_with_http_info(self, **kwargs):  # noqa: E501
        """List of NFL teams  # noqa: E501

        List of NFL teams  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_nfl_teams_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[DraftTeam]
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
                    " to method get_nfl_teams" % key
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
            '/draft/teams', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[DraftTeam]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
