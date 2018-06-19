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
from ..models.send_message_response import SendMessageResponse
from ..models.get_app_user_messages_response import GetAppUserMessagesResponse
from ..models.get_app_user_by_id_response import GetAppUserByIdResponse
from ..models.get_app_users_response import GetAppUsersResponse
from ..exceptions.api_exception import APIException

class AppUsersController(BaseController):

    """A Controller to access Endpoints in the message_media_conversations API."""

    def __init__(self, client=None, call_back=None):
        super(AppUsersController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)

    def create_send_message(self,
                            app_user_id,
                            body):
        """Does a POST request to /beta/conversations/users/{appUserId}/messages.

        Sends a message to the App User with the given ID.
        You can use this endpoint in conjuction with the app users or app user
        by id endpoint where the response from one of the latter endpoints
        would display the user id and this can be used with this endpoint to
        send a message to that user. A successful response from this endpoint
        will have the following structure:
        ```
        {
          "channel": "facebook",
          "text": "Thank you for your query we'll be in touch with an answer
          shortly."
        }
        ```

        Args:
            app_user_id (string): appUserId
            body (BaseMessageDto): TODO: type description here. Example: 

        Returns:
            SendMessageResponse: Response from the API. Message was
                successfully sent.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_send_message called.')
    
            # Prepare query URL
            self.logger.info('Preparing query URL for create_send_message.')
            _query_builder = Configuration.base_uri
            _query_builder += '/beta/conversations/users/{appUserId}/messages'
            _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
                'appUserId': app_user_id
            })
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for create_send_message.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for create_send_message.')
            _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
            BasicAuth.apply(_request)
            _context = self.execute_request(_request, name = 'create_send_message')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_send_message.')
            if _context.response.status_code == 400:
                raise APIException('The posted request is invalid or the account is not provisioned.', _context)
            elif _context.response.status_code == 404:
                raise APIException('The app user does not exist.', _context)
            self.validate_response(_context)
    
            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, SendMessageResponse.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def get_app_user_messages(self,
                              app_user_id):
        """Does a GET request to /beta/conversations/users/{appUserId}/messages.

        Gets the list of messages sent to and received by the App User with
        the given ID. A successful response from this endpoint will have the
        following structure:
        ```
        {
          "messages": {
            "data": [
              {
                "direction": "RECEIVED",
                "text": "Hey, I was just wondering how much shipping would be
                to Australia for one of them awesome t-shirts?",
                "channel": "FACEBOOK",
                "timestamp": "2017-12-12T18:18:40.000Z"
              },
              {
                "direction": "SENT",
                "text": "Thank you for your query we'll be in touch with an
                answer shortly.",
                "channel": "FACEBOOK",
                "timestamp": "2017-12-08T10:12:16.000Z"
              }
            ]
          },
          "metadata" : {
            "user_id": "{id}",
            "account_id": "FunGuys007"
          }
        }
        ```

        Args:
            app_user_id (string): appUserId

        Returns:
            GetAppUserMessagesResponse: Response from the API. Messages
                successfully retrieved.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_app_user_messages called.')
    
            # Prepare query URL
            self.logger.info('Preparing query URL for get_app_user_messages.')
            _query_builder = Configuration.base_uri
            _query_builder += '/beta/conversations/users/{appUserId}/messages'
            _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
                'appUserId': app_user_id
            })
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for get_app_user_messages.')
            _headers = {
                'accept': 'application/json'
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_app_user_messages.')
            _request = self.http_client.get(_query_url, headers=_headers)
            BasicAuth.apply(_request)
            _context = self.execute_request(_request, name = 'get_app_user_messages')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_app_user_messages.')
            if _context.response.status_code == 404:
                raise APIException('The app user does not exist.', _context)
            self.validate_response(_context)
    
            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, GetAppUserMessagesResponse.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def get_app_user_by_id(self,
                           app_user_id):
        """Does a GET request to /beta/conversations/users/{appUserId}.

        Gets the App User with the given ID. A successful response from this
        endpoint will have the following structure:
        ```
        {
          "id": "3898c5e4-73cc-44f9-812f-3698a4c3bb1d",
          "surname": "Sims",
          "given_name": "Ben"
        }
        ```

        Args:
            app_user_id (string): appUserId

        Returns:
            GetAppUserByIdResponse: Response from the API. App user
                successfully retrieved.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_app_user_by_id called.')
    
            # Prepare query URL
            self.logger.info('Preparing query URL for get_app_user_by_id.')
            _query_builder = Configuration.base_uri
            _query_builder += '/beta/conversations/users/{appUserId}'
            _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
                'appUserId': app_user_id
            })
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for get_app_user_by_id.')
            _headers = {
                'accept': 'application/json'
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_app_user_by_id.')
            _request = self.http_client.get(_query_url, headers=_headers)
            BasicAuth.apply(_request)
            _context = self.execute_request(_request, name = 'get_app_user_by_id')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_app_user_by_id.')
            if _context.response.status_code == 404:
                raise APIException('The app user does not exist.', _context)
            self.validate_response(_context)
    
            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, GetAppUserByIdResponse.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def get_app_users(self):
        """Does a GET request to /beta/conversations/users.

        Gets a list of App Users that belong to the configured account. A
        successful response from this endpoint will have the following
        structure:
        ```
        {
          "data": [
            {
              "id": "3898c5e4-73cc-44f9-812f-3698a4c3bb1d",
              "surname": "Sims",
              "given_name": "Ben"
            },
            {
              "id": "331b1da8-10a5-44c7-91df-1dc14cc2f373",
              "surname": "Hood",
              "given_name": "Robert"
            }
          ]
        }
        ```

        Returns:
            GetAppUsersResponse: Response from the API. App users successfully
                retrieved.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_app_users called.')
    
            # Prepare query URL
            self.logger.info('Preparing query URL for get_app_users.')
            _query_builder = Configuration.base_uri
            _query_builder += '/beta/conversations/users'
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for get_app_users.')
            _headers = {
                'accept': 'application/json'
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_app_users.')
            _request = self.http_client.get(_query_url, headers=_headers)
            BasicAuth.apply(_request)
            _context = self.execute_request(_request, name = 'get_app_users')
            self.validate_response(_context)
    
            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, GetAppUsersResponse.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise
