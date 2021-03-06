# -*- coding: utf-8 -*-

"""
    message_media_conversations.message_media_conversations_client

    This file was automatically generated for MessageMedia by APIMATIC v2.0 ( https://apimatic.io ).
"""
from .decorators import lazy_property
from .configuration import Configuration
from .controllers.app_users_controller import AppUsersController
from .controllers.configuration_controller import ConfigurationController
from .controllers.facebook_controller import FacebookController

class MessageMediaConversationsClient(object):

    config = Configuration

    @lazy_property
    def app_users(self):
        return AppUsersController()

    @lazy_property
    def configuration(self):
        return ConfigurationController()

    @lazy_property
    def facebook(self):
        return FacebookController()


    def __init__(self, 
                 basic_auth_user_name = None,
                 basic_auth_password = None):
        if basic_auth_user_name != None:
            Configuration.basic_auth_user_name = basic_auth_user_name
        if basic_auth_password != None:
            Configuration.basic_auth_password = basic_auth_password


