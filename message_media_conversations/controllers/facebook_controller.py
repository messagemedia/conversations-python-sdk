# -*- coding: utf-8 -*-

import logging
from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.basic_auth import BasicAuth
from ..models.facebook_pages_dto import FacebookPagesDto
from ..models.facebook_authorisation_response import FacebookAuthorisationResponse
from ..exceptions.api_exception import APIException

class FacebookController(BaseController):

    """A Controller to access Endpoints in the message_media_conversations API."""

    def __init__(self, client=None, call_back=None):
        super(FacebookController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)

    def create_integrate_facebook_page_using_post(self,
                                                  facebook_page_id):
        """Does a POST request to /v1/conversations/facebook/pages/{facebookPageId}/integrate.

        Integrates the Facebook page with the given ID with the provisioned
        account.

        Args:
            facebook_page_id (string): facebookPageId

        Returns:
            void: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_integrate_facebook_page_using_post called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for create_integrate_facebook_page_using_post.')
            _query_builder = Configuration.base_uri
            _query_builder += '/v1/conversations/facebook/pages/{facebookPageId}/integrate'
            _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, {
                'facebookPageId': facebook_page_id
            })
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info('Preparing and executing request for create_integrate_facebook_page_using_post.')
            _request = self.http_client.post(_query_url)
            BasicAuth.apply(_request)
            _context = self.execute_request(_request, name = 'create_integrate_facebook_page_using_post')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_integrate_facebook_page_using_post.')
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

    def get_facebook_pages_using_get(self):
        """Does a GET request to /v1/conversations/facebook/pages.

        Gets a list of Facebook pages belonging to the provisioned and
        Facebook authorised account.

        Returns:
            FacebookPagesDto: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_facebook_pages_using_get called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_facebook_pages_using_get.')
            _query_builder = Configuration.base_uri
            _query_builder += '/v1/conversations/facebook/pages'
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_facebook_pages_using_get.')
            _headers = {
                'accept': 'application/json'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_facebook_pages_using_get.')
            _request = self.http_client.get(_query_url, headers=_headers)
            BasicAuth.apply(_request)
            _context = self.execute_request(_request, name = 'get_facebook_pages_using_get')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_facebook_pages_using_get.')
            if _context.response.status_code == 401:
                raise APIException('Unauthorized', _context)
            elif _context.response.status_code == 403:
                raise APIException('Forbidden', _context)
            elif _context.response.status_code == 404:
                raise APIException('Not Found', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, FacebookPagesDto.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def get_facebook_authorisation_url_using_get(self):
        """Does a GET request to /v1/conversations/facebook/authorise.

        Once an account has been provisioned, endpoint can be called to get
        the Facebook authorisation URL.

        Returns:
            FacebookAuthorisationResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_facebook_authorisation_url_using_get called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_facebook_authorisation_url_using_get.')
            _query_builder = Configuration.base_uri
            _query_builder += '/v1/conversations/facebook/authorise'
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_facebook_authorisation_url_using_get.')
            _headers = {
                'accept': 'application/json'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_facebook_authorisation_url_using_get.')
            _request = self.http_client.get(_query_url, headers=_headers)
            BasicAuth.apply(_request)
            _context = self.execute_request(_request, name = 'get_facebook_authorisation_url_using_get')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_facebook_authorisation_url_using_get.')
            if _context.response.status_code == 401:
                raise APIException('Unauthorized', _context)
            elif _context.response.status_code == 403:
                raise APIException('Forbidden', _context)
            elif _context.response.status_code == 404:
                raise APIException('Not Found', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, FacebookAuthorisationResponse.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise
