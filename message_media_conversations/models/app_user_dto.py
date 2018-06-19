# -*- coding: utf-8 -*-

"""
    message_media_conversations.models.app_user_dto

    This file was automatically generated for MessageMedia by APIMATIC v2.0 ( https://apimatic.io )
"""


class AppUserDto(object):

    """Implementation of the 'AppUserDto' model.

    TODO: type model description here.

    Attributes:
        given_name (string): TODO: type description here.
        id (string): TODO: type description here.
        surname (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "given_name":'givenName',
        "id":'id',
        "surname":'surname'
    }

    def __init__(self,
                 given_name=None,
                 id=None,
                 surname=None):
        """Constructor for the AppUserDto class"""

        # Initialize members of the class
        self.given_name = given_name
        self.id = id
        self.surname = surname


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
        given_name = dictionary.get('givenName')
        id = dictionary.get('id')
        surname = dictionary.get('surname')

        # Return an object of this model
        return cls(given_name,
                   id,
                   surname)


