# Getting started

Conversations Api Documentation

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

* [ProvisioningController](#provisioning_controller)
* [AppUsersController](#app_users_controller)
* [FacebookController](#facebook_controller)

## <a name="provisioning_controller"></a>![Class: ](https://apidocs.io/img/class.png ".ProvisioningController") ProvisioningController

### Get controller instance

An instance of the ``` ProvisioningController ``` class can be accessed from the API Client.

```python
 provisioning_controller = client.provisioning
```

### <a name="create_provision_account_using_post"></a>![Method: ](https://apidocs.io/img/method.png ".ProvisioningController.create_provision_account_using_post") create_provision_account_using_post

> Provisions an account to use the Conversations API.

```python
def create_provision_account_using_post(self,
                                            request)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| request |  ``` Required ```  | request |



#### Example Usage

```python
request = ProvisionAccountRequest()

provisioning_controller.create_provision_account_using_post(request)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |




[Back to List of Controllers](#list_of_controllers)

## <a name="app_users_controller"></a>![Class: ](https://apidocs.io/img/class.png ".AppUsersController") AppUsersController

### Get controller instance

An instance of the ``` AppUsersController ``` class can be accessed from the API Client.

```python
 app_users_controller = client.app_users
```

### <a name="create_send_message_using_post"></a>![Method: ](https://apidocs.io/img/method.png ".AppUsersController.create_send_message_using_post") create_send_message_using_post

> Sends a message to the App User with the given ID.

```python
def create_send_message_using_post(self,
                                       app_user_id,
                                       message)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| appUserId |  ``` Required ```  | appUserId |
| message |  ``` Required ```  | message |



#### Example Usage

```python
app_user_id = 'appUserId'
message = BaseMessageDto()

app_users_controller.create_send_message_using_post(app_user_id, message)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |




### <a name="get_app_user_messages_using_get"></a>![Method: ](https://apidocs.io/img/method.png ".AppUsersController.get_app_user_messages_using_get") get_app_user_messages_using_get

> Gets the list of messages for the App User with the given ID.

```python
def get_app_user_messages_using_get(self,
                                        app_user_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| appUserId |  ``` Required ```  | appUserId |



#### Example Usage

```python
app_user_id = 'appUserId'

result = app_users_controller.get_app_user_messages_using_get(app_user_id)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |




### <a name="get_app_user_using_get"></a>![Method: ](https://apidocs.io/img/method.png ".AppUsersController.get_app_user_using_get") get_app_user_using_get

> Gets the App User with the given ID.

```python
def get_app_user_using_get(self,
                               app_user_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| appUserId |  ``` Required ```  | appUserId |



#### Example Usage

```python
app_user_id = 'appUserId'

result = app_users_controller.get_app_user_using_get(app_user_id)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |




### <a name="get_app_users_using_get"></a>![Method: ](https://apidocs.io/img/method.png ".AppUsersController.get_app_users_using_get") get_app_users_using_get

> Gets a list of App Users that belong to the provisioned account.

```python
def get_app_users_using_get(self)
```

#### Example Usage

```python

result = app_users_controller.get_app_users_using_get()

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |




[Back to List of Controllers](#list_of_controllers)

## <a name="facebook_controller"></a>![Class: ](https://apidocs.io/img/class.png ".FacebookController") FacebookController

### Get controller instance

An instance of the ``` FacebookController ``` class can be accessed from the API Client.

```python
 facebook_controller = client.facebook
```

### <a name="create_integrate_facebook_page_using_post"></a>![Method: ](https://apidocs.io/img/method.png ".FacebookController.create_integrate_facebook_page_using_post") create_integrate_facebook_page_using_post

> Integrates the Facebook page with the given ID with the provisioned account.

```python
def create_integrate_facebook_page_using_post(self,
                                                  facebook_page_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| facebookPageId |  ``` Required ```  | facebookPageId |



#### Example Usage

```python
facebook_page_id = 'facebookPageId'

facebook_controller.create_integrate_facebook_page_using_post(facebook_page_id)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |




### <a name="get_facebook_pages_using_get"></a>![Method: ](https://apidocs.io/img/method.png ".FacebookController.get_facebook_pages_using_get") get_facebook_pages_using_get

> Gets a list of Facebook pages belonging to the provisioned and Facebook authorised account.

```python
def get_facebook_pages_using_get(self)
```

#### Example Usage

```python

result = facebook_controller.get_facebook_pages_using_get()

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |




### <a name="get_facebook_authorisation_url_using_get"></a>![Method: ](https://apidocs.io/img/method.png ".FacebookController.get_facebook_authorisation_url_using_get") get_facebook_authorisation_url_using_get

> Once an account has been provisioned, endpoint can be called to get the Facebook authorisation URL.

```python
def get_facebook_authorisation_url_using_get(self)
```

#### Example Usage

```python

result = facebook_controller.get_facebook_authorisation_url_using_get()

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |




[Back to List of Controllers](#list_of_controllers)



