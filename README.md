# Getting started

The Conversations API allows users to communicate by sending and receiving messages via Over-The-Top (OTT) messaging services. OTT application is an app or service that provides a product over the Internet and bypasses traditional distribution. Here's an in-depth explanation of what the term means.This feature is disabled by default. To enable it, you don't need to make any changes to your application, just an account configuration change by MessageMedia's support team support@messagemedia.com.For our initial release, we're releasing Facebook Messenger which allows you to send messages as a Facebook page owner and receive messages from other Facebook users.

## How to Build


You must have Python ```2 >=2.7.9``` or Python ```3 >=3.4``` installed on your system to install and run this SDK. This SDK package depends on other Python packages like nose, jsonpickle etc. 
These dependencies are defined in the ```requirements.txt``` file that comes with the SDK.
To resolve these dependencies, you can use the PIP Dependency manager. Install it by following steps at [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/).

Python and PIP executables should be defined in your PATH. Open command prompt and type ```pip --version```.
This should display the version of the PIP Dependency Manager installed if your installation was successful and the paths are properly defined.

* Using command line, navigate to the directory containing the generated files (including ```requirements.txt```) for the SDK.
* Run the command ```pip install -r requirements.txt```. This should install all the required dependencies.

![Building SDK - Step 1](https://apidocs.io/illustration/python?step=installDependencies&workspaceFolder=MessageMediaConversations-Python)


## How to Use

The following section explains how to use the MessageMediaConversations SDK package in a new project.

### 1. Open Project in an IDE

Open up a Python IDE like PyCharm. The basic workflow presented here is also applicable if you prefer using a different editor or IDE.

![Open project in PyCharm - Step 1](https://apidocs.io/illustration/python?step=pyCharm)

Click on ```Open``` in PyCharm to browse to your generated SDK directory and then click ```OK```.

![Open project in PyCharm - Step 2](https://apidocs.io/illustration/python?step=openProject0&workspaceFolder=MessageMediaConversations-Python)     

The project files will be displayed in the side bar as follows:

![Open project in PyCharm - Step 3](https://apidocs.io/illustration/python?step=openProject1&workspaceFolder=MessageMediaConversations-Python&projectName=message_media_conversations)     

### 2. Add a new Test Project

Create a new directory by right clicking on the solution name as shown below:

![Add a new project in PyCharm - Step 1](https://apidocs.io/illustration/python?step=createDirectory&workspaceFolder=MessageMediaConversations-Python&projectName=message_media_conversations)

Name the directory as "test"

![Add a new project in PyCharm - Step 2](https://apidocs.io/illustration/python?step=nameDirectory)
   
Add a python file to this project with the name "testsdk"

![Add a new project in PyCharm - Step 3](https://apidocs.io/illustration/python?step=createFile&workspaceFolder=MessageMediaConversations-Python&projectName=message_media_conversations)

Name it "testsdk"

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?step=nameFile)

In your python file you will be required to import the generated python library using the following code lines

```Python
from message_media_conversations.message_media_conversations_client import MessageMediaConversationsClient
```

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?step=projectFiles&workspaceFolder=MessageMediaConversations-Python&libraryName=message_media_conversations.message_media_conversations_client&projectName=message_media_conversations&className=MessageMediaConversationsClient)

After this you can write code to instantiate an API client object, get a controller object and  make API calls. Sample code is given in the subsequent sections.

### 3. Run the Test Project

To run the file within your test project, right click on your Python file inside your Test project and click on ```Run```

![Run Test Project - Step 1](https://apidocs.io/illustration/python?step=runProject&workspaceFolder=MessageMediaConversations-Python&libraryName=message_media_conversations.message_media_conversations_client&projectName=message_media_conversations&className=MessageMediaConversationsClient)


## How to Test

You can test the generated SDK and the server with automatically generated test
cases. unittest is used as the testing framework and nose is used as the test
runner. You can run the tests as follows:

  1. From terminal/cmd navigate to the root directory of the SDK.
  2. Invoke ```pip install -r test-requirements.txt```
  3. Invoke ```nosetests```

## Initialization

### Authentication
In order to setup authentication and initialization of the API client, you need the following information.

| Parameter | Description |
|-----------|-------------|
| basic_auth_user_name | The username to use with basic authentication |
| basic_auth_password | The password to use with basic authentication |



API client can be initialized as following.

```python
# Configuration parameters and credentials
basic_auth_user_name = 'basic_auth_user_name' # The username to use with basic authentication
basic_auth_password = 'basic_auth_password' # The password to use with basic authentication

client = MessageMediaConversationsClient(basic_auth_user_name, basic_auth_password)
```



# Class Reference

## <a name="list_of_controllers"></a>List of Controllers

* [AppUsersController](#app_users_controller)
* [ConfigurationController](#configuration_controller)
* [FacebookController](#facebook_controller)

## <a name="app_users_controller"></a>![Class: ](https://apidocs.io/img/class.png ".AppUsersController") AppUsersController

### Get controller instance

An instance of the ``` AppUsersController ``` class can be accessed from the API Client.

```python
 app_users_controller = client.app_users
```

### <a name="create_send_message"></a>![Method: ](https://apidocs.io/img/method.png ".AppUsersController.create_send_message") create_send_message

> Sends a message to the App User with the given ID.
> You can use this endpoint in conjuction with the app users or app user by id endpoint where the response from one of the latter endpoints would display the user id and this can be used with this endpoint to send a message to that user. A successful response from this endpoint will have the following structure:
> ```
> {
>   "channel": "facebook",
>   "text": "Thank you for your query we'll be in touch with an answer shortly."
> }
> ```

```python
def create_send_message(self,
                            app_user_id,
                            body)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| appUserId |  ``` Required ```  | appUserId |
| body |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
app_user_id = 'appUserId'
body = BaseMessageDto()

result = app_users_controller.create_send_message(app_user_id, body)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | The posted request is invalid or the account is not provisioned. |
| 404 | The app user does not exist. |




### <a name="get_app_user_messages"></a>![Method: ](https://apidocs.io/img/method.png ".AppUsersController.get_app_user_messages") get_app_user_messages

> Gets the list of messages sent to and received by the App User with the given ID. A successful response from this endpoint will have the following structure:
> ```
> {
>   "messages": {
>     "data": [
>       {
>         "direction": "RECEIVED",
>         "text": "Hey, I was just wondering how much shipping would be to Australia for one of them awesome t-shirts?",
>         "channel": "FACEBOOK",
>         "timestamp": "2017-12-12T18:18:40.000Z"
>       },
>       {
>         "direction": "SENT",
>         "text": "Thank you for your query we'll be in touch with an answer shortly.",
>         "channel": "FACEBOOK",
>         "timestamp": "2017-12-08T10:12:16.000Z"
>       }
>     ]
>   },
>   "metadata" : {
>     "user_id": "{id}",
>     "account_id": "FunGuys007"
>   }
> }
> ```

```python
def get_app_user_messages(self,
                              app_user_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| appUserId |  ``` Required ```  | appUserId |



#### Example Usage

```python
app_user_id = 'appUserId'

result = app_users_controller.get_app_user_messages(app_user_id)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 404 | The app user does not exist. |




### <a name="get_app_user_by_id"></a>![Method: ](https://apidocs.io/img/method.png ".AppUsersController.get_app_user_by_id") get_app_user_by_id

> Gets the App User with the given ID. A successful response from this endpoint will have the following structure:
> ```
> {
>   "id": "3898c5e4-73cc-44f9-812f-3698a4c3bb1d",
>   "surname": "Sims",
>   "given_name": "Ben"
> }
> ```

```python
def get_app_user_by_id(self,
                           app_user_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| appUserId |  ``` Required ```  | appUserId |



#### Example Usage

```python
app_user_id = 'appUserId'

result = app_users_controller.get_app_user_by_id(app_user_id)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 404 | The app user does not exist. |




### <a name="get_app_users"></a>![Method: ](https://apidocs.io/img/method.png ".AppUsersController.get_app_users") get_app_users

> Gets a list of App Users that belong to the configured account. A successful response from this endpoint will have the following structure:
> ```
> {
>   "data": [
>     {
>       "id": "3898c5e4-73cc-44f9-812f-3698a4c3bb1d",
>       "surname": "Sims",
>       "given_name": "Ben"
>     },
>     {
>       "id": "331b1da8-10a5-44c7-91df-1dc14cc2f373",
>       "surname": "Hood",
>       "given_name": "Robert"
>     }
>   ]
> }
> ```

```python
def get_app_users(self)
```

#### Example Usage

```python

result = app_users_controller.get_app_users()

```


[Back to List of Controllers](#list_of_controllers)

## <a name="configuration_controller"></a>![Class: ](https://apidocs.io/img/class.png ".ConfigurationController") ConfigurationController

### Get controller instance

An instance of the ``` ConfigurationController ``` class can be accessed from the API Client.

```python
 configuration_controller = client.configuration
```

### <a name="create_configure_account"></a>![Method: ](https://apidocs.io/img/method.png ".ConfigurationController.create_configure_account") create_configure_account

> Configures your existing MessageMedia account to use the Conversations API by giving it a human readable name (for reference later on), and also by specifying a callback URL which is where any Inbound Messages and/or Notifications will be pushed to. The request would have the following structure:
> ```
> {
>   "name": "Rainbow Serpent Festival",
>   "callback_url": "http://accounts-domain.com/callback"
> }
> ```
> * `name` is a required property and is a customer friendly name to identify your provisioned account
> * `callback_url` is an optional property is the callback URL to forward inbound messages to.
> *Note: We are currently NOT using our Webhooks functionality for this while it's in beta, when we make this production ready we will look at switching to having these webhooks managed via the Webhooks Management API*

```python
def create_configure_account(self,
                                 body)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| body |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
body_value = "{    \"name\": \"Rainbow Serpent Festival\",    \"callback_url\": \"https://callback.url.com\"}"
body = json.loads(body_value)

result = configuration_controller.create_configure_account(body)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Not a valid request body. |
| 409 | The account has already been provisioned. |




[Back to List of Controllers](#list_of_controllers)

## <a name="facebook_controller"></a>![Class: ](https://apidocs.io/img/class.png ".FacebookController") FacebookController

### Get controller instance

An instance of the ``` FacebookController ``` class can be accessed from the API Client.

```python
 facebook_controller = client.facebook
```

### <a name="create_integrate_facebook_page"></a>![Method: ](https://apidocs.io/img/method.png ".FacebookController.create_integrate_facebook_page") create_integrate_facebook_page

> Integrates the Facebook page with the given ID with the configured account.

```python
def create_integrate_facebook_page(self,
                                       facebook_page_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| facebookPageId |  ``` Required ```  | facebookPageId |



#### Example Usage

```python
facebook_page_id = 'facebookPageId'

result = facebook_controller.create_integrate_facebook_page(facebook_page_id)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | The account is not provisioned or the Facebook user isn't authenticated or the facebookPageId is invalid. |




### <a name="get_facebook_pages"></a>![Method: ](https://apidocs.io/img/method.png ".FacebookController.get_facebook_pages") get_facebook_pages

> Gets a list of Facebook pages belonging to the provisioned and Facebook authorised account. A successful response from this endpoint will have the following structure:
> ```
> {
>   "data": [
>     {
>       "id": "1573307926039629",
>       "name": "Rainbow Serpent Festival"
>     },
>     {
>       "id": "373479609790958",
>       "name": "Fans of Doing Live Demos"
>     }
>   ]
> }
> ```

```python
def get_facebook_pages(self)
```

#### Example Usage

```python

result = facebook_controller.get_facebook_pages()

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | The account is not provisioned or the Facebook user isn't authenticated. |




### <a name="get_facebook_authorisation_url"></a>![Method: ](https://apidocs.io/img/method.png ".FacebookController.get_facebook_authorisation_url") get_facebook_authorisation_url

> Before you can start integrating Facebook pages on your Facebook account, MessageMedia's messaging platform needs access to that page via what Facebook call a page access token. To get the page access token you first need to provide MessageMedia limited access to your Facebook account.
> Calling this endpoint will get the Facebook authorisation URL which you are required to go through before you can call the integration endpoints. A successful response from this endpoint will have the following structure:
> ```
> {
>   "authorisation_url": "https://www.facebook.com/v2.12/dialog/oauth?client_id={facebookAppId}&amp;redirect_uri={apiUrl}/beta/integration/authenticated&amp;state={provisionedAccountUUID}&amp;response_type=token&amp;scope=email,manage_pages,pages_messaging"
> }
> ```
> *Note: Granting MessageMedia access will only see allow us to see your basic details and the list of pages you have*

```python
def get_facebook_authorisation_url(self)
```

#### Example Usage

```python

result = facebook_controller.get_facebook_authorisation_url()

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | The account is not provisioned |




[Back to List of Controllers](#list_of_controllers)



