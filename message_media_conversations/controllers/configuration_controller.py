# -*- coding: utf-8 -*-

"""
    message_media_conversations.controllers.configuration_controller

    This file was automatically generated for MessageMedia by APIMATIC v2.0 ( https://apimatic.io ).
"""

import logging
from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.basic_auth import BasicAuth
from ..models.configure_account_response import ConfigureAccountResponse
from ..exceptions.api_exception import APIException

class ConfigurationController(BaseController):

    """A Controller to access Endpoints in the message_media_conversations API."""

    def __init__(self, client=None, call_back=None):
        super(ConfigurationController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)

    def create_configure_account(self,
                                 body):
        """Does a POST request to /beta/conversations/provision.

        Configures your existing MessageMedia account to use the Conversations
        API by giving it a human readable name (for reference later on), and
        also by specifying a callback URL which is where any Inbound Messages
        and/or Notifications will be pushed to. The request would have the
        following structure:
        ```
        {
          "name": "Rainbow Serpent Festival",
          "callback_url": "http://accounts-domain.com/callback"
        }
        ```
        * `name` is a required property and is a customer friendly name to
        identify your provisioned account
        * `callback_url` is an optional property is the callback URL to
        forward inbound messages to.
        *Note: We are currently NOT using our Webhooks functionality for this
        while it's in beta, when we make this production ready we will look at
        switching to having these webhooks managed via the Webhooks Management
        API*

        Args:
            body (ConfigureAccountRequest): TODO: type description here.
                Example: 

        Returns:
            ConfigureAccountResponse: Response from the API. Provisioned
                account has been created.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_configure_account called.')
    
            # Prepare query URL
            self.logger.info('Preparing query URL for create_configure_account.')
            _query_builder = Configuration.base_uri
            _query_builder += '/beta/conversations/provision'
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for create_configure_account.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for create_configure_account.')
            _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
            BasicAuth.apply(_request)
            _context = self.execute_request(_request, name = 'create_configure_account')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_configure_account.')
            if _context.response.status_code == 400:
                raise APIException('Not a valid request body.', _context)
            elif _context.response.status_code == 409:
                raise APIException('The account has already been provisioned.', _context)
            self.validate_response(_context)
    
            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, ConfigureAccountResponse.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise
