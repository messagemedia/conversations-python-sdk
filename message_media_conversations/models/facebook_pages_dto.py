# -*- coding: utf-8 -*-


import message_media_conversations.models.facebook_page_dto

class FacebookPagesDto(object):

    """Implementation of the 'FacebookPagesDto' model.

    TODO: type model description here.

    Attributes:
        pages (list of FacebookPageDto): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "pages":'pages'
    }

    def __init__(self,
                 pages=None):
        """Constructor for the FacebookPagesDto class"""

        # Initialize members of the class
        self.pages = pages


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
        pages = None
        if dictionary.get('pages') != None:
            pages = list()
            for structure in dictionary.get('pages'):
                pages.append(message_media_conversations.models.facebook_page_dto.FacebookPageDto.from_dictionary(structure))

        # Return an object of this model
        return cls(pages)
