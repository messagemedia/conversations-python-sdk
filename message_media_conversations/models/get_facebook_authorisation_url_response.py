# -*- coding: utf-8 -*-

"""
    message_media_conversations.models.get_facebook_authorisation_url_response

    This file was automatically generated for MessageMedia by APIMATIC v2.0 ( https://apimatic.io )
"""


class GetFacebookAuthorisationURLResponse(object):

    """Implementation of the 'Get Facebook authorisation URL response' model.

    TODO: type model description here.

    Attributes:
        authorisation_url (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "authorisation_url":'authorisation_url'
    }

    def __init__(self,
                 authorisation_url=None):
        """Constructor for the GetFacebookAuthorisationURLResponse class"""

        # Initialize members of the class
        self.authorisation_url = authorisation_url


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
        authorisation_url = dictionary.get('authorisation_url')

        # Return an object of this model
        return cls(authorisation_url)


