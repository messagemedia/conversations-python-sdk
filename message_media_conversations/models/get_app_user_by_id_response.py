# -*- coding: utf-8 -*-

"""
    message_media_conversations.models.get_app_user_by_id_response

    This file was automatically generated for MessageMedia by APIMATIC v2.0 ( https://apimatic.io )
"""


class GetAppUserByIdResponse(object):

    """Implementation of the 'Get app user by id response' model.

    TODO: type model description here.

    Attributes:
        id (string): TODO: type description here.
        surname (string): TODO: type description here.
        given_name (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "surname":'surname',
        "given_name":'given_name'
    }

    def __init__(self,
                 id=None,
                 surname=None,
                 given_name=None):
        """Constructor for the GetAppUserByIdResponse class"""

        # Initialize members of the class
        self.id = id
        self.surname = surname
        self.given_name = given_name


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
        surname = dictionary.get('surname')
        given_name = dictionary.get('given_name')

        # Return an object of this model
        return cls(id,
                   surname,
                   given_name)


