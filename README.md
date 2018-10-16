# MessageMedia Conversations Python SDK
[![Travis Build Status](https://api.travis-ci.org/messagemedia/conversations-python-sdk.svg?branch=master)](https://travis-ci.org/messagemedia/conversations-python-sdk)
[![PyPI](https://badge.fury.io/py/messagemedia-conversations-sdk.svg)](https://pypi.python.org/pypi/messagemedia-conversations-sdk)

⚠️ **Please note the API documented is in beta and is subject to breaking changes in the short term.** ⚠️

The MessageMedia Conversations API allows users to communicate by sending and receiving messages via OTT messaging services. This feature is disabled by default. To enable it, you don't need to make any changes to your application, just an account configuration change by MessageMedia's support team (support@messagemedia.com).

## ⭐️ Install via PIP
Run the following command to install the SDK via pip:
`pip install messagemedia-conversations-sdk`

## 🎬 Get Started
It's easy to get started. Simply enter the API Key and secret you obtained from the [MessageMedia Developers Portal](https://developers.messagemedia.com) into the code snippet below.

### 🚀 Provision an account
```python
from message_media_conversations.message_media_conversations_client import MessageMediaConversationsClient

# Configuration parameters and credentials
basic_auth_user_name = 'basic_auth_user_name' # The username to use with basic authentication
basic_auth_password = 'basic_auth_password' # The password to use with basic authentication

client = MessageMediaConversationsClient(basic_auth_user_name, basic_auth_password)
configuration_controller = client.configuration

body_value = "{    \"name\": \"Rainbow Serpent Festival\",    \"callback_url\": \"https://callback.url.com\"}"
body = json.loads(body_value)

result = configuration_controller.create_configure_account(body)

```

### 🔐 Facebook Authorization
```python
from message_media_conversations.message_media_conversations_client import MessageMediaConversationsClient

# Configuration parameters and credentials
basic_auth_user_name = 'basic_auth_user_name' # The username to use with basic authentication
basic_auth_password = 'basic_auth_password' # The password to use with basic authentication

facebook_controller = client.facebook
result = facebook_controller.get_facebook_authorisation_url()

```

### ⬇️ Get Facebook pages
```python
from message_media_conversations.message_media_conversations_client import MessageMediaConversationsClient

# Configuration parameters and credentials
basic_auth_user_name = 'basic_auth_user_name' # The username to use with basic authentication
basic_auth_password = 'basic_auth_password' # The password to use with basic authentication

facebook_controller = client.facebook
result = facebook_controller.get_facebook_pages()

```

### ♻️ Integrate Facebook page
You can get the facebookPageId by looking at the response of the Get Facebook pages example.
```python
from message_media_conversations.message_media_conversations_client import MessageMediaConversationsClient

# Configuration parameters and credentials
basic_auth_user_name = 'basic_auth_user_name' # The username to use with basic authentication
basic_auth_password = 'basic_auth_password' # The password to use with basic authentication

facebook_controller = client.facebook
facebook_page_id = 'facebookPageId'
facebook_controller.create_integrate_facebook_page(facebook_page_id)

```

### 👤 Get users
```python
from message_media_conversations.message_media_conversations_client import MessageMediaConversationsClient

# Configuration parameters and credentials
basic_auth_user_name = 'basic_auth_user_name' # The username to use with basic authentication
basic_auth_password = 'basic_auth_password' # The password to use with basic authentication

app_users_controller = client.app_users
result = app_users_controller.get_app_users()

```

### 👤 Get user by id
```python
from message_media_conversations.message_media_conversations_client import MessageMediaConversationsClient

# Configuration parameters and credentials
basic_auth_user_name = 'basic_auth_user_name' # The username to use with basic authentication
basic_auth_password = 'basic_auth_password' # The password to use with basic authentication

app_users_controller = client.app_users
app_user_id = 'appUserId'

result = app_users_controller.get_app_user_by_id(app_user_id)

```

### 💬 Get user messages
You can get the appUserId from the response of the Get users example.
```python
from message_media_conversations.message_media_conversations_client import MessageMediaConversationsClient

# Configuration parameters and credentials
basic_auth_user_name = 'basic_auth_user_name' # The username to use with basic authentication
basic_auth_password = 'basic_auth_password' # The password to use with basic authentication

app_users_controller = client.app_users
app_user_id = 'appUserId'
result = app_users_controller.get_app_user_messages(app_user_id)

```

### ✉️ Send message to user
You can get the appUserId from the response of the Get users example.
```python
from message_media_conversations.message_media_conversations_client import MessageMediaConversationsClient

# Configuration parameters and credentials
basic_auth_user_name = 'basic_auth_user_name' # The username to use with basic authentication
basic_auth_password = 'basic_auth_password' # The password to use with basic authentication

app_users_controller = client.app_users
app_user_id = 'appUserId'
message = BaseMessageDto({"key":"value"})
result = app_users_controller.create_send_message(app_user_id, body)

```

## 📕 Documentation
Check out the [full API documentation](DOCUMENTATION.md) for more detailed information.

## 😕 Need help?
Please contact developer support at developers@messagemedia.com or check out the developer portal at [developers.messagemedia.com](https://developers.messagemedia.com/)

## 📃 License
Apache License. See the [LICENSE](LICENSE) file.
