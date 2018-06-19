# -*- coding: utf-8 -*-

"""
    message_media_conversations.models.facebook_page_dto

    This file was automatically generated for MessageMedia by APIMATIC v2.0 ( https://apimatic.io )
"""


class FacebookPageDto(object):

    """Implementation of the 'FacebookPageDto' model.

    TODO: type model description here.

    Attributes:
        id (string): TODO: type description here.
        name (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "name":'name'
    }

    def __init__(self,
                 id=None,
                 name=None):
        """Constructor for the FacebookPageDto class"""

        # Initialize members of the class
        self.id = id
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
        id = dictionary.get('id')
        name = dictionary.get('name')

        # Return an object of this model
        return cls(id,
                   name)


