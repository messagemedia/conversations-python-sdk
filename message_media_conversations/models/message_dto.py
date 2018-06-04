# -*- coding: utf-8 -*-

"""
    message_media_conversations.models.message_dto

    This file was automatically generated for MessageMedia by APIMATIC v2.0 ( https://apimatic.io )
"""
from message_media_conversations.api_helper import APIHelper

class MessageDto(object):

    """Implementation of the 'MessageDto' model.

    TODO: type model description here.

    Attributes:
        channel (string): TODO: type description here.
        id (string): TODO: type description here.
        text (string): TODO: type description here.
        timestamp (datetime): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "channel":'channel',
        "id":'id',
        "text":'text',
        "timestamp":'timestamp'
    }

    def __init__(self,
                 channel=None,
                 id=None,
                 text=None,
                 timestamp=None):
        """Constructor for the MessageDto class"""

        # Initialize members of the class
        self.channel = channel
        self.id = id
        self.text = text
        self.timestamp = APIHelper.RFC3339DateTime(timestamp) if timestamp else None


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
        channel = dictionary.get('channel')
        id = dictionary.get('id')
        text = dictionary.get('text')
        timestamp = APIHelper.RFC3339DateTime.from_value(dictionary.get("timestamp")).datetime if dictionary.get("timestamp") else None

        # Return an object of this model
        return cls(channel,
                   id,
                   text,
                   timestamp)


