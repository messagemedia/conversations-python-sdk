# -*- coding: utf-8 -*-

"""
    message_media_conversations.models.app_users_dto

    This file was automatically generated for MessageMedia by APIMATIC v2.0 ( https://apimatic.io )
"""
import message_media_conversations.models.app_user_dto

class AppUsersDto(object):

    """Implementation of the 'AppUsersDto' model.

    TODO: type model description here.

    Attributes:
        users (list of AppUserDto): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "users":'users'
    }

    def __init__(self,
                 users=None):
        """Constructor for the AppUsersDto class"""

        # Initialize members of the class
        self.users = users


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
        users = None
        if dictionary.get('users') != None:
            users = list()
            for structure in dictionary.get('users'):
                users.append(message_media_conversations.models.app_user_dto.AppUserDto.from_dictionary(structure))

        # Return an object of this model
        return cls(users)


