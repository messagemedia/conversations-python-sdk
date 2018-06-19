# -*- coding: utf-8 -*-

"""
    message_media_conversations.controllers.facebook_controller

    This file was automatically generated for MessageMedia by APIMATIC v2.0 ( https://apimatic.io ).
"""

import logging
from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.basic_auth import BasicAuth
from ..models.get_facebook_pages_response import GetFacebookPagesResponse
from ..models.get_facebook_authorisation_url_response import GetFacebookAuthorisationURLResponse
from ..exceptions.api_exception import APIException

class FacebookController(BaseController):

    """A Controller to access Endpoints in the message_media_conversations API."""

    def __init__(self, client=None, call_back=None):
        super(FacebookController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)

    def create_integrate_facebook_page(self,
                                       facebook_page_id):
        """Does a POST request to /beta/conversations/facebook/pages/{facebookPageId}/integrate.

        Integrates the Facebook page with the given ID with the configured
        account.

        Args:
            facebook_page_id (string): facebookPageId

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_integrate_facebook_page called.')
    
            # Prepare query URL
            self.logger.info('Preparing query URL for create_integrate_facebook_page.')
            _query_builder = Configuration.base_uri
            _query_builder += '/beta/conversations/facebook/pages/{facebookPageId}/integrate'
            _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
                'facebookPageId': facebook_page_id
            })
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for create_integrate_facebook_page.')
            _request = self.http_client.post(_query_url)
            BasicAuth.apply(_request)
            _context = self.execute_request(_request, name = 'create_integrate_facebook_page')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_integrate_facebook_page.')
            if _context.response.status_code == 400:
                raise APIException('The account is not provisioned or the Facebook user isn\'t authenticated or the facebookPageId is invalid.', _context)
            self.validate_response(_context)
    
            # Return appropriate type
            return _context.response.raw_body

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def get_facebook_pages(self):
        """Does a GET request to /beta/conversations/facebook/pages.

        Gets a list of Facebook pages belonging to the provisioned and
        Facebook authorised account. A successful response from this endpoint
        will have the following structure:
        ```
        {
          "data": [
            {
              "id": "1573307926039629",
              "name": "Rainbow Serpent Festival"
            },
            {
              "id": "373479609790958",
              "name": "Fans of Doing Live Demos"
            }
          ]
        }
        ```

        Returns:
            GetFacebookPagesResponse: Response from the API. Facebook pages
                successfully retrieved.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_facebook_pages called.')
    
            # Prepare query URL
            self.logger.info('Preparing query URL for get_facebook_pages.')
            _query_builder = Configuration.base_uri
            _query_builder += '/beta/conversations/facebook/pages'
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for get_facebook_pages.')
            _headers = {
                'accept': 'application/json'
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_facebook_pages.')
            _request = self.http_client.get(_query_url, headers=_headers)
            BasicAuth.apply(_request)
            _context = self.execute_request(_request, name = 'get_facebook_pages')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_facebook_pages.')
            if _context.response.status_code == 400:
                raise APIException('The account is not provisioned or the Facebook user isn\'t authenticated.', _context)
            self.validate_response(_context)
    
            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, GetFacebookPagesResponse.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def get_facebook_authorisation_url(self):
        """Does a GET request to /beta/conversations/facebook/authorise.

        Before you can start integrating Facebook pages on your Facebook
        account, MessageMedia's messaging platform needs access to that page
        via what Facebook call a page access token. To get the page access
        token you first need to provide MessageMedia limited access to your
        Facebook account.
        Calling this endpoint will get the Facebook authorisation URL which
        you are required to go through before you can call the integration
        endpoints. A successful response from this endpoint will have the
        following structure:
        ```
        {
          "authorisation_url":
          "https://www.facebook.com/v2.12/dialog/oauth?client_id={facebookAppId
          }&amp;redirect_uri={apiUrl}/beta/integration/authenticated&amp;state=
          {provisionedAccountUUID}&amp;response_type=token&amp;scope=email,mana
          ge_pages,pages_messaging"
        }
        ```
        *Note: Granting MessageMedia access will only see allow us to see your
        basic details and the list of pages you have*

        Returns:
            GetFacebookAuthorisationURLResponse: Response from the API. URL
                successfully returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_facebook_authorisation_url called.')
    
            # Prepare query URL
            self.logger.info('Preparing query URL for get_facebook_authorisation_url.')
            _query_builder = Configuration.base_uri
            _query_builder += '/beta/conversations/facebook/authorise'
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for get_facebook_authorisation_url.')
            _headers = {
                'accept': 'application/json'
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_facebook_authorisation_url.')
            _request = self.http_client.get(_query_url, headers=_headers)
            BasicAuth.apply(_request)
            _context = self.execute_request(_request, name = 'get_facebook_authorisation_url')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_facebook_authorisation_url.')
            if _context.response.status_code == 400:
                raise APIException('The account is not provisioned', _context)
            self.validate_response(_context)
    
            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, GetFacebookAuthorisationURLResponse.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise
