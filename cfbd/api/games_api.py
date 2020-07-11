# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  It currently has a wide array of data ranging from play by play to player statistics to game scores and more.  # noqa: E501

    OpenAPI spec version: 2.2.0
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from cfbd.api_client import ApiClient


class GamesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_advanced_box_score(self, game_id, **kwargs):  # noqa: E501
        """Get advanced box score  # noqa: E501

        Advanced box score  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_advanced_box_score(game_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int game_id: Game id parameters (required)
        :return: list[BoxScore]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_advanced_box_score_with_http_info(game_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_advanced_box_score_with_http_info(game_id, **kwargs)  # noqa: E501
            return data

    def get_advanced_box_score_with_http_info(self, game_id, **kwargs):  # noqa: E501
        """Get advanced box score  # noqa: E501

        Advanced box score  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_advanced_box_score_with_http_info(game_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int game_id: Game id parameters (required)
        :return: list[BoxScore]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['game_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_advanced_box_score" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'game_id' is set
        if ('game_id' not in params or
                params['game_id'] is None):
            raise ValueError("Missing the required parameter `game_id` when calling `get_advanced_box_score`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'game_id' in params:
            query_params.append(('gameId', params['game_id']))  # noqa: E501

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
            '/game/box/advanced', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[BoxScore]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_game_media(self, year, **kwargs):  # noqa: E501
        """Get game media information (TV, radio, etc)  # noqa: E501

        Game media information (TV, radio, etc)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_game_media(year, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Year filter (required)
        :param int week: Week filter
        :param str season_type: Season type filter (regular, postseason, or both)
        :param str team: Team filter
        :param str conference: Conference filter
        :param str media_type: Media type filter (tv, radio, web, ppv, or mobile)
        :return: list[GameMedia]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_game_media_with_http_info(year, **kwargs)  # noqa: E501
        else:
            (data) = self.get_game_media_with_http_info(year, **kwargs)  # noqa: E501
            return data

    def get_game_media_with_http_info(self, year, **kwargs):  # noqa: E501
        """Get game media information (TV, radio, etc)  # noqa: E501

        Game media information (TV, radio, etc)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_game_media_with_http_info(year, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Year filter (required)
        :param int week: Week filter
        :param str season_type: Season type filter (regular, postseason, or both)
        :param str team: Team filter
        :param str conference: Conference filter
        :param str media_type: Media type filter (tv, radio, web, ppv, or mobile)
        :return: list[GameMedia]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['year', 'week', 'season_type', 'team', 'conference', 'media_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_game_media" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'year' is set
        if ('year' not in params or
                params['year'] is None):
            raise ValueError("Missing the required parameter `year` when calling `get_game_media`")  # noqa: E501

        if 'year' in params and params['year'] < 2001:  # noqa: E501
            raise ValueError("Invalid value for parameter `year` when calling `get_game_media`, must be a value greater than or equal to `2001`")  # noqa: E501
        if 'week' in params and params['week'] > 16:  # noqa: E501
            raise ValueError("Invalid value for parameter `week` when calling `get_game_media`, must be a value less than or equal to `16`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'year' in params:
            query_params.append(('year', params['year']))  # noqa: E501
        if 'week' in params:
            query_params.append(('week', params['week']))  # noqa: E501
        if 'season_type' in params:
            query_params.append(('seasonType', params['season_type']))  # noqa: E501
        if 'team' in params:
            query_params.append(('team', params['team']))  # noqa: E501
        if 'conference' in params:
            query_params.append(('conference', params['conference']))  # noqa: E501
        if 'media_type' in params:
            query_params.append(('mediaType', params['media_type']))  # noqa: E501

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
            '/games/media', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GameMedia]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_games(self, year, **kwargs):  # noqa: E501
        """Get game information  # noqa: E501

        Game results  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_games(year, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Year/season filter for games (required)
        :param int week: Week filter
        :param str season_type: Season type filter (regular or postseason)
        :param str team: Team
        :param str home: Home team filter
        :param str away: Away team filter
        :param str conference: Conference abbreviation filter
        :param int id: id filter for querying a single game
        :return: list[Game]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_games_with_http_info(year, **kwargs)  # noqa: E501
        else:
            (data) = self.get_games_with_http_info(year, **kwargs)  # noqa: E501
            return data

    def get_games_with_http_info(self, year, **kwargs):  # noqa: E501
        """Get game information  # noqa: E501

        Game results  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_games_with_http_info(year, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Year/season filter for games (required)
        :param int week: Week filter
        :param str season_type: Season type filter (regular or postseason)
        :param str team: Team
        :param str home: Home team filter
        :param str away: Away team filter
        :param str conference: Conference abbreviation filter
        :param int id: id filter for querying a single game
        :return: list[Game]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['year', 'week', 'season_type', 'team', 'home', 'away', 'conference', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_games" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'year' is set
        if ('year' not in params or
                params['year'] is None):
            raise ValueError("Missing the required parameter `year` when calling `get_games`")  # noqa: E501

        if 'year' in params and params['year'] < 1869:  # noqa: E501
            raise ValueError("Invalid value for parameter `year` when calling `get_games`, must be a value greater than or equal to `1869`")  # noqa: E501
        if 'week' in params and params['week'] > 16:  # noqa: E501
            raise ValueError("Invalid value for parameter `week` when calling `get_games`, must be a value less than or equal to `16`")  # noqa: E501
        if 'week' in params and params['week'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `week` when calling `get_games`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
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
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501

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
            '/games', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Game]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_player_game_stats(self, year, **kwargs):  # noqa: E501
        """Get player statistics by game  # noqa: E501

        Player game stats  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_player_game_stats(year, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Year/season filter for games (required)
        :param int week: Week filter
        :param str season_type: Season type filter (regular or postseason)
        :param str team: Team filter
        :param str conference: Conference abbreviation filter
        :param str category: Category filter (e.g defensive)
        :param int game_id: Game id filter
        :return: list[PlayerGame]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_player_game_stats_with_http_info(year, **kwargs)  # noqa: E501
        else:
            (data) = self.get_player_game_stats_with_http_info(year, **kwargs)  # noqa: E501
            return data

    def get_player_game_stats_with_http_info(self, year, **kwargs):  # noqa: E501
        """Get player statistics by game  # noqa: E501

        Player game stats  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_player_game_stats_with_http_info(year, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Year/season filter for games (required)
        :param int week: Week filter
        :param str season_type: Season type filter (regular or postseason)
        :param str team: Team filter
        :param str conference: Conference abbreviation filter
        :param str category: Category filter (e.g defensive)
        :param int game_id: Game id filter
        :return: list[PlayerGame]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['year', 'week', 'season_type', 'team', 'conference', 'category', 'game_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_player_game_stats" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'year' is set
        if ('year' not in params or
                params['year'] is None):
            raise ValueError("Missing the required parameter `year` when calling `get_player_game_stats`")  # noqa: E501

        if 'week' in params and params['week'] > 16:  # noqa: E501
            raise ValueError("Invalid value for parameter `week` when calling `get_player_game_stats`, must be a value less than or equal to `16`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'year' in params:
            query_params.append(('year', params['year']))  # noqa: E501
        if 'week' in params:
            query_params.append(('week', params['week']))  # noqa: E501
        if 'season_type' in params:
            query_params.append(('seasonType', params['season_type']))  # noqa: E501
        if 'team' in params:
            query_params.append(('team', params['team']))  # noqa: E501
        if 'conference' in params:
            query_params.append(('conference', params['conference']))  # noqa: E501
        if 'category' in params:
            query_params.append(('category', params['category']))  # noqa: E501
        if 'game_id' in params:
            query_params.append(('gameId', params['game_id']))  # noqa: E501

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
            '/games/players', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[PlayerGame]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_team_game_stats(self, year, **kwargs):  # noqa: E501
        """Get team statistics by game  # noqa: E501

        Team game stats  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_team_game_stats(year, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Year/season filter for games (required)
        :param int week: Week filter
        :param str season_type: Season type filter (regular or postseason)
        :param str team: Team filter
        :param str conference: Conference abbreviation filter
        :param int game_id: Game id filter
        :return: list[TeamGame]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_team_game_stats_with_http_info(year, **kwargs)  # noqa: E501
        else:
            (data) = self.get_team_game_stats_with_http_info(year, **kwargs)  # noqa: E501
            return data

    def get_team_game_stats_with_http_info(self, year, **kwargs):  # noqa: E501
        """Get team statistics by game  # noqa: E501

        Team game stats  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_team_game_stats_with_http_info(year, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Year/season filter for games (required)
        :param int week: Week filter
        :param str season_type: Season type filter (regular or postseason)
        :param str team: Team filter
        :param str conference: Conference abbreviation filter
        :param int game_id: Game id filter
        :return: list[TeamGame]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['year', 'week', 'season_type', 'team', 'conference', 'game_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_team_game_stats" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'year' is set
        if ('year' not in params or
                params['year'] is None):
            raise ValueError("Missing the required parameter `year` when calling `get_team_game_stats`")  # noqa: E501

        if 'year' in params and params['year'] < 2001:  # noqa: E501
            raise ValueError("Invalid value for parameter `year` when calling `get_team_game_stats`, must be a value greater than or equal to `2001`")  # noqa: E501
        if 'week' in params and params['week'] > 16:  # noqa: E501
            raise ValueError("Invalid value for parameter `week` when calling `get_team_game_stats`, must be a value less than or equal to `16`")  # noqa: E501
        if 'week' in params and params['week'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `week` when calling `get_team_game_stats`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'year' in params:
            query_params.append(('year', params['year']))  # noqa: E501
        if 'week' in params:
            query_params.append(('week', params['week']))  # noqa: E501
        if 'season_type' in params:
            query_params.append(('seasonType', params['season_type']))  # noqa: E501
        if 'team' in params:
            query_params.append(('team', params['team']))  # noqa: E501
        if 'conference' in params:
            query_params.append(('conference', params['conference']))  # noqa: E501
        if 'game_id' in params:
            query_params.append(('gameId', params['game_id']))  # noqa: E501

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
            '/games/teams', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[TeamGame]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_team_records(self, **kwargs):  # noqa: E501
        """Get records by year  # noqa: E501

        Team records by year  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_team_records(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Year filter
        :param str team: Team filter
        :param str conference: Conference filter
        :return: list[TeamRecord]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_team_records_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_team_records_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_team_records_with_http_info(self, **kwargs):  # noqa: E501
        """Get records by year  # noqa: E501

        Team records by year  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_team_records_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Year filter
        :param str team: Team filter
        :param str conference: Conference filter
        :return: list[TeamRecord]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['year', 'team', 'conference']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_team_records" % key
                )
            params[key] = val
        del params['kwargs']

        if 'year' in params and params['year'] < 1869:  # noqa: E501
            raise ValueError("Invalid value for parameter `year` when calling `get_team_records`, must be a value greater than or equal to `1869`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'year' in params:
            query_params.append(('year', params['year']))  # noqa: E501
        if 'team' in params:
            query_params.append(('team', params['team']))  # noqa: E501
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
            '/records', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[TeamRecord]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
