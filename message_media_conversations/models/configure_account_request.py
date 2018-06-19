# -*- coding: utf-8 -*-

"""
    message_media_conversations.models.configure_account_request

    This file was automatically generated for MessageMedia by APIMATIC v2.0 ( https://apimatic.io )
"""


class ConfigureAccountRequest(object):

    """Implementation of the 'Configure account request' model.

    TODO: type model description here.

    Attributes:
        name (string): TODO: type description here.
        callback_url (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "callback_url":'callback_url'
    }

    def __init__(self,
                 name=None,
                 callback_url=None):
        """Constructor for the ConfigureAccountRequest class"""

        # Initialize members of the class
        self.name = name
        self.callback_url = callback_url


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
        name = dictionary.get('name')
        callback_url = dictionary.get('callback_url')

        # Return an object of this model
        return cls(name,
                   callback_url)


