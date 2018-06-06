# -*- coding: utf-8 -*-

import logging
from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.basic_auth import BasicAuth
from ..exceptions.api_exception import APIException

class ProvisioningController(BaseController):

    """A Controller to access Endpoints in the message_media_conversations API."""

    def __init__(self, client=None, call_back=None):
        super(ProvisioningController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)

    def create_provision_account_using_post(self,
                                            request):
        """Does a POST request to /v1/conversations/provision.

        Provisions an account to use the Conversations API.

        Args:
            request (ProvisionAccountRequest): request

        Returns:
            void: Response from the API. Created

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_provision_account_using_post called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for create_provision_account_using_post.')
            _query_builder = Configuration.base_uri
            _query_builder += '/v1/conversations/provision'
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_provision_account_using_post.')
            _headers = {
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for create_provision_account_using_post.')
            _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(request))
            BasicAuth.apply(_request)
            _context = self.execute_request(_request, name = 'create_provision_account_using_post')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_provision_account_using_post.')
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
