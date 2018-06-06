from message_media_conversations.message_media_conversations_client import MessageMediaConversationsClient

# Configuration parameters and credentials
basic_auth_user_name = 'basic_auth_user_name' # The username to use with basic authentication
basic_auth_password = 'basic_auth_password' # The password to use with basic authentication

client = MessageMediaConversationsClient(basic_auth_user_name, basic_auth_password)
provisioning_controller = client.provisioning

request = ProvisionAccountRequest("http://accounts-domain.com/callback", "Rainbow Serpent Festival");
provisioning_controller.create_provision_account_using_post(request)
