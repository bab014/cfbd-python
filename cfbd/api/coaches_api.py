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


class CoachesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_coaches(self, **kwargs):  # noqa: E501
        """Coaching records and history  # noqa: E501

        Coaching history  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_coaches(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str first_name: First name filter
        :param str last_name: Last name filter
        :param str team: Team name filter
        :param int year: Year filter
        :param int min_year: Minimum year filter (inclusive)
        :param int max_year: Maximum year filter (inclusive)
        :return: list[Coach]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_coaches_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_coaches_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_coaches_with_http_info(self, **kwargs):  # noqa: E501
        """Coaching records and history  # noqa: E501

        Coaching history  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_coaches_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str first_name: First name filter
        :param str last_name: Last name filter
        :param str team: Team name filter
        :param int year: Year filter
        :param int min_year: Minimum year filter (inclusive)
        :param int max_year: Maximum year filter (inclusive)
        :return: list[Coach]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['first_name', 'last_name', 'team', 'year', 'min_year', 'max_year']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_coaches" % key
                )
            params[key] = val
        del params['kwargs']

        if self.api_client.client_side_validation and ('min_year' in params and params['min_year'] < 1869):  # noqa: E501
            raise ValueError("Invalid value for parameter `min_year` when calling `get_coaches`, must be a value greater than or equal to `1869`")  # noqa: E501
        if self.api_client.client_side_validation and ('max_year' in params and params['max_year'] < 1869):  # noqa: E501
            raise ValueError("Invalid value for parameter `max_year` when calling `get_coaches`, must be a value greater than or equal to `1869`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'first_name' in params:
            query_params.append(('firstName', params['first_name']))  # noqa: E501
        if 'last_name' in params:
            query_params.append(('lastName', params['last_name']))  # noqa: E501
        if 'team' in params:
            query_params.append(('team', params['team']))  # noqa: E501
        if 'year' in params:
            query_params.append(('year', params['year']))  # noqa: E501
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
            '/coaches', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Coach]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
