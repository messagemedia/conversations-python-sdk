# -*- coding: utf-8 -*-


import base64
from ...configuration import Configuration

class BasicAuth:

    @staticmethod
    def apply(http_request):
        """ Add basic authentication to the request.

        Args:
            http_request (HttpRequest): The HttpRequest object to which
                authentication will be added.

        """
        username = Configuration.basic_auth_user_name
        password = Configuration.basic_auth_password
        joined = "{}:{}".format(username, password)
        encoded = base64.b64encode(str.encode(joined)).decode('iso-8859-1')
        header_value = "Basic {}".format(encoded)
        http_request.headers["Authorization"] = header_value
