# -*- coding: utf-8 -*-

"""
    message_media_conversations.models.get_app_users_response

    This file was automatically generated for MessageMedia by APIMATIC v2.0 ( https://apimatic.io )
"""


class GetAppUsersResponse(object):

    """Implementation of the 'Get app users response' model.

    TODO: type model description here.

    Attributes:
        data (list of object): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "data":'data'
    }

    def __init__(self,
                 data=None):
        """Constructor for the GetAppUsersResponse class"""

        # Initialize members of the class
        self.data = data


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        data = dictionary.get('data')

        # Return an object of this model
        return cls(data)


