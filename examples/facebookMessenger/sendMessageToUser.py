from message_media_conversations.message_media_conversations_client import MessageMediaConversationsClient

# Configuration parameters and credentials
basic_auth_user_name = 'basic_auth_user_name' # The username to use with basic authentication
basic_auth_password = 'basic_auth_password' # The password to use with basic authentication

app_users_controller = client.app_users
app_user_id = 'appUserId'
message = BaseMessageDto({"key":"value"})
app_users_controller.create_send_message_using_post(app_user_id, message)
