# -*- coding: utf-8 -*-

"""
    message_media_conversations.models.base_message_dto

    This file was automatically generated for MessageMedia by APIMATIC v2.0 ( https://apimatic.io )
"""


class BaseMessageDto(object):

    """Implementation of the 'BaseMessageDto' model.

    TODO: type model description here.

    Attributes:
        text (string): TODO: type description here.
        channel (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "text":'text',
        "channel":'channel'
    }

    def __init__(self,
                 text=None,
                 channel=None):
        """Constructor for the BaseMessageDto class"""

        # Initialize members of the class
        self.text = text
        self.channel = channel


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
        text = dictionary.get('text')
        channel = dictionary.get('channel')

        # Return an object of this model
        return cls(text,
                   channel)


