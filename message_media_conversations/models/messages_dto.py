# -*- coding: utf-8 -*-

"""
    message_media_conversations.models.messages_dto

    This file was automatically generated for MessageMedia by APIMATIC v2.0 ( https://apimatic.io )
"""
import message_media_conversations.models.message_dto

class MessagesDto(object):

    """Implementation of the 'MessagesDto' model.

    TODO: type model description here.

    Attributes:
        messages (list of MessageDto): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "messages":'messages'
    }

    def __init__(self,
                 messages=None):
        """Constructor for the MessagesDto class"""

        # Initialize members of the class
        self.messages = messages


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
        messages = None
        if dictionary.get('messages') != None:
            messages = list()
            for structure in dictionary.get('messages'):
                messages.append(message_media_conversations.models.message_dto.MessageDto.from_dictionary(structure))

        # Return an object of this model
        return cls(messages)


