# -*- coding: utf-8 -*-

"""
    message_media_conversations.models.send_message_response

    This file was automatically generated for MessageMedia by APIMATIC v2.0 ( https://apimatic.io )
"""


class SendMessageResponse(object):

    """Implementation of the 'Send message response' model.

    TODO: type model description here.

    Attributes:
        channel (string): TODO: type description here.
        text (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "channel":'channel',
        "text":'text'
    }

    def __init__(self,
                 channel=None,
                 text=None):
        """Constructor for the SendMessageResponse class"""

        # Initialize members of the class
        self.channel = channel
        self.text = text


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
        text = dictionary.get('text')

        # Return an object of this model
        return cls(channel,
                   text)


