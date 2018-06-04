# -*- coding: utf-8 -*-

"""
    message_media_conversations.models.provision_account_request

    This file was automatically generated for MessageMedia by APIMATIC v2.0 ( https://apimatic.io )
"""


class ProvisionAccountRequest(object):

    """Implementation of the 'ProvisionAccountRequest' model.

    TODO: type model description here.

    Attributes:
        callback_url (string): TODO: type description here.
        name (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "callback_url":'callbackUrl',
        "name":'name'
    }

    def __init__(self,
                 callback_url=None,
                 name=None):
        """Constructor for the ProvisionAccountRequest class"""

        # Initialize members of the class
        self.callback_url = callback_url
        self.name = name


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
        callback_url = dictionary.get('callbackUrl')
        name = dictionary.get('name')

        # Return an object of this model
        return cls(callback_url,
                   name)


