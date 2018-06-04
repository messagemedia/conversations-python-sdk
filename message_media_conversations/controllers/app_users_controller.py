# -*- coding: utf-8 -*-

"""
    message_media_conversations.controllers.app_users_controller

    This file was automatically generated for MessageMedia by APIMATIC v2.0 ( https://apimatic.io ).
"""

import logging
from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.basic_auth import BasicAuth
from ..models.messages_dto import MessagesDto
from ..models.app_user_dto import AppUserDto
from ..models.app_users_dto import AppUsersDto
from ..exceptions.api_exception import APIException

class AppUsersController(BaseController):

    """A Controller to access Endpoints in the message_media_conversations API."""

    def __init__(self, client=None, call_back=None):
        super(AppUsersController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)

    def create_send_message_using_post(self,
                                       app_user_id,
                                       message):
        """Does a POST request to /v1/conversations/users/{appUserId}/messages.

        Sends a message to the App User with the given ID.

        Args:
            app_user_id (string): appUserId
            message (BaseMessageDto): message

        Returns:
            void: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_send_message_using_post called.')
    
            # Prepare query URL
            self.logger.info('Preparing query URL for create_send_message_using_post.')
            _query_builder = Configuration.base_uri
            _query_builder += '/v1/conversations/users/{appUserId}/messages'
            _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
                'appUserId': app_user_id
            })
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for create_send_message_using_post.')
            _headers = {
                'content-type': 'application/json; charset=utf-8'
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for create_send_message_using_post.')
            _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(message))
            BasicAuth.apply(_request)
            _context = self.execute_request(_request, name = 'create_send_message_using_post')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_send_message_using_post.')
            if _context.response.status_code == 401:
                raise APIException('Unauthorized', _context)
            elif _context.response.status_code == 403:
                raise APIException('Forbidden', _context)
            elif _context.response.status_code == 404:
                raise APIException('Not Found', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def get_app_user_messages_using_get(self,
                                        app_user_id):
        """Does a GET request to /v1/conversations/users/{appUserId}/messages.

        Gets the list of messages for the App User with the given ID.

        Args:
            app_user_id (string): appUserId

        Returns:
            MessagesDto: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_app_user_messages_using_get called.')
    
            # Prepare query URL
            self.logger.info('Preparing query URL for get_app_user_messages_using_get.')
            _query_builder = Configuration.base_uri
            _query_builder += '/v1/conversations/users/{appUserId}/messages'
            _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
                'appUserId': app_user_id
            })
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for get_app_user_messages_using_get.')
            _headers = {
                'accept': 'application/json'
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_app_user_messages_using_get.')
            _request = self.http_client.get(_query_url, headers=_headers)
            BasicAuth.apply(_request)
            _context = self.execute_request(_request, name = 'get_app_user_messages_using_get')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_app_user_messages_using_get.')
            if _context.response.status_code == 401:
                raise APIException('Unauthorized', _context)
            elif _context.response.status_code == 403:
                raise APIException('Forbidden', _context)
            elif _context.response.status_code == 404:
                raise APIException('Not Found', _context)
            self.validate_response(_context)
    
            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, MessagesDto.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def get_app_user_using_get(self,
                               app_user_id):
        """Does a GET request to /v1/conversations/users/{appUserId}.

        Gets the App User with the given ID.

        Args:
            app_user_id (string): appUserId

        Returns:
            AppUserDto: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_app_user_using_get called.')
    
            # Prepare query URL
            self.logger.info('Preparing query URL for get_app_user_using_get.')
            _query_builder = Configuration.base_uri
            _query_builder += '/v1/conversations/users/{appUserId}'
            _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
                'appUserId': app_user_id
            })
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for get_app_user_using_get.')
            _headers = {
                'accept': 'application/json'
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_app_user_using_get.')
            _request = self.http_client.get(_query_url, headers=_headers)
            BasicAuth.apply(_request)
            _context = self.execute_request(_request, name = 'get_app_user_using_get')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_app_user_using_get.')
            if _context.response.status_code == 401:
                raise APIException('Unauthorized', _context)
            elif _context.response.status_code == 403:
                raise APIException('Forbidden', _context)
            elif _context.response.status_code == 404:
                raise APIException('Not Found', _context)
            self.validate_response(_context)
    
            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, AppUserDto.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def get_app_users_using_get(self):
        """Does a GET request to /v1/conversations/users.

        Gets a list of App Users that belong to the provisioned account.

        Returns:
            AppUsersDto: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_app_users_using_get called.')
    
            # Prepare query URL
            self.logger.info('Preparing query URL for get_app_users_using_get.')
            _query_builder = Configuration.base_uri
            _query_builder += '/v1/conversations/users'
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for get_app_users_using_get.')
            _headers = {
                'accept': 'application/json'
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_app_users_using_get.')
            _request = self.http_client.get(_query_url, headers=_headers)
            BasicAuth.apply(_request)
            _context = self.execute_request(_request, name = 'get_app_users_using_get')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_app_users_using_get.')
            if _context.response.status_code == 401:
                raise APIException('Unauthorized', _context)
            elif _context.response.status_code == 403:
                raise APIException('Forbidden', _context)
            elif _context.response.status_code == 404:
                raise APIException('Not Found', _context)
            self.validate_response(_context)
    
            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, AppUsersDto.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise
