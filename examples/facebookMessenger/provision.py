from message_media_conversations.message_media_conversations_client import MessageMediaConversationsClient

# Configuration parameters and credentials
basic_auth_user_name = 'basic_auth_user_name' # The username to use with basic authentication
basic_auth_password = 'basic_auth_password' # The password to use with basic authentication

client = MessageMediaConversationsClient(basic_auth_user_name, basic_auth_password)
configuration_controller = client.configuration

body_value = "{    \"name\": \"Rainbow Serpent Festival\",    \"callback_url\": \"https://callback.url.com\"}"
body = json.loads(body_value)

result = configuration_controller.create_configure_account(body)
