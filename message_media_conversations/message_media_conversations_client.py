# -*- coding: utf-8 -*-

from .decorators import lazy_property
from .configuration import Configuration
from .controllers.provisioning_controller import ProvisioningController
from .controllers.app_users_controller import AppUsersController
from .controllers.facebook_controller import FacebookController

class MessageMediaConversationsClient(object):

    config = Configuration

    @lazy_property
    def provisioning(self):
        return ProvisioningController()

    @lazy_property
    def app_users(self):
        return AppUsersController()

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
