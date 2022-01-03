# embyapi.SessionsServiceApi

All URIs are relative to *https://home.ourflix.de:32865/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_auth_keys_by_key**](SessionsServiceApi.md#delete_auth_keys_by_key) | **DELETE** /Auth/Keys/{Key} | 
[**delete_sessions_by_id_users_by_userid**](SessionsServiceApi.md#delete_sessions_by_id_users_by_userid) | **DELETE** /Sessions/{Id}/Users/{UserId} | Removes an additional user from a session
[**get_auth_keys**](SessionsServiceApi.md#get_auth_keys) | **GET** /Auth/Keys | 
[**get_auth_providers**](SessionsServiceApi.md#get_auth_providers) | **GET** /Auth/Providers | 
[**get_sessions**](SessionsServiceApi.md#get_sessions) | **GET** /Sessions | Gets a list of sessions
[**post_auth_keys**](SessionsServiceApi.md#post_auth_keys) | **POST** /Auth/Keys | 
[**post_sessions_by_id_command**](SessionsServiceApi.md#post_sessions_by_id_command) | **POST** /Sessions/{Id}/Command | Issues a system command to a client
[**post_sessions_by_id_command_by_command**](SessionsServiceApi.md#post_sessions_by_id_command_by_command) | **POST** /Sessions/{Id}/Command/{Command} | Issues a system command to a client
[**post_sessions_by_id_message**](SessionsServiceApi.md#post_sessions_by_id_message) | **POST** /Sessions/{Id}/Message | Issues a command to a client to display a message to the user
[**post_sessions_by_id_playing**](SessionsServiceApi.md#post_sessions_by_id_playing) | **POST** /Sessions/{Id}/Playing | Instructs a session to play an item
[**post_sessions_by_id_playing_by_command**](SessionsServiceApi.md#post_sessions_by_id_playing_by_command) | **POST** /Sessions/{Id}/Playing/{Command} | Issues a playstate command to a client
[**post_sessions_by_id_system_by_command**](SessionsServiceApi.md#post_sessions_by_id_system_by_command) | **POST** /Sessions/{Id}/System/{Command} | Issues a system command to a client
[**post_sessions_by_id_users_by_userid**](SessionsServiceApi.md#post_sessions_by_id_users_by_userid) | **POST** /Sessions/{Id}/Users/{UserId} | Adds an additional user to a session
[**post_sessions_by_id_viewing**](SessionsServiceApi.md#post_sessions_by_id_viewing) | **POST** /Sessions/{Id}/Viewing | Instructs a session to browse to an item or view
[**post_sessions_capabilities**](SessionsServiceApi.md#post_sessions_capabilities) | **POST** /Sessions/Capabilities | Updates capabilities for a device
[**post_sessions_capabilities_full**](SessionsServiceApi.md#post_sessions_capabilities_full) | **POST** /Sessions/Capabilities/Full | Updates capabilities for a device
[**post_sessions_logout**](SessionsServiceApi.md#post_sessions_logout) | **POST** /Sessions/Logout | Reports that a session has ended

# **delete_auth_keys_by_key**
> delete_auth_keys_by_key(key)



Requires authentication as administrator

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikeyauth
configuration = embyapi.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = embyapi.SessionsServiceApi(embyapi.ApiClient(configuration))
key = 'key_example' # str | Auth Key

try:
    api_instance.delete_auth_keys_by_key(key)
except ApiException as e:
    print("Exception when calling SessionsServiceApi->delete_auth_keys_by_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Auth Key | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sessions_by_id_users_by_userid**
> delete_sessions_by_id_users_by_userid(id, user_id)

Removes an additional user from a session

Requires authentication as user

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikeyauth
configuration = embyapi.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = embyapi.SessionsServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Session Id
user_id = 'user_id_example' # str | UserId Id

try:
    # Removes an additional user from a session
    api_instance.delete_sessions_by_id_users_by_userid(id, user_id)
except ApiException as e:
    print("Exception when calling SessionsServiceApi->delete_sessions_by_id_users_by_userid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Session Id | 
 **user_id** | **str**| UserId Id | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auth_keys**
> get_auth_keys()



Requires authentication as administrator

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikeyauth
configuration = embyapi.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = embyapi.SessionsServiceApi(embyapi.ApiClient(configuration))

try:
    api_instance.get_auth_keys()
except ApiException as e:
    print("Exception when calling SessionsServiceApi->get_auth_keys: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auth_providers**
> list[NameIdPair] get_auth_providers()



Requires authentication as administrator

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikeyauth
configuration = embyapi.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = embyapi.SessionsServiceApi(embyapi.ApiClient(configuration))

try:
    api_response = api_instance.get_auth_providers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionsServiceApi->get_auth_providers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[NameIdPair]**](NameIdPair.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sessions**
> list[SessionSessionInfo] get_sessions(controllable_by_user_id=controllable_by_user_id, device_id=device_id)

Gets a list of sessions

Requires authentication as user

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikeyauth
configuration = embyapi.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = embyapi.SessionsServiceApi(embyapi.ApiClient(configuration))
controllable_by_user_id = 'controllable_by_user_id_example' # str | Optional. Filter by sessions that a given user is allowed to remote control. (optional)
device_id = 'device_id_example' # str | Optional. Filter by device id. (optional)

try:
    # Gets a list of sessions
    api_response = api_instance.get_sessions(controllable_by_user_id=controllable_by_user_id, device_id=device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionsServiceApi->get_sessions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **controllable_by_user_id** | **str**| Optional. Filter by sessions that a given user is allowed to remote control. | [optional] 
 **device_id** | **str**| Optional. Filter by device id. | [optional] 

### Return type

[**list[SessionSessionInfo]**](SessionSessionInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_auth_keys**
> post_auth_keys(app)



Requires authentication as administrator

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikeyauth
configuration = embyapi.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = embyapi.SessionsServiceApi(embyapi.ApiClient(configuration))
app = 'app_example' # str | App

try:
    api_instance.post_auth_keys(app)
except ApiException as e:
    print("Exception when calling SessionsServiceApi->post_auth_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app** | **str**| App | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sessions_by_id_command**
> post_sessions_by_id_command(body, id)

Issues a system command to a client

Requires authentication as user

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikeyauth
configuration = embyapi.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = embyapi.SessionsServiceApi(embyapi.ApiClient(configuration))
body = embyapi.GeneralCommand() # GeneralCommand | GeneralCommand: 
id = 'id_example' # str | Session Id

try:
    # Issues a system command to a client
    api_instance.post_sessions_by_id_command(body, id)
except ApiException as e:
    print("Exception when calling SessionsServiceApi->post_sessions_by_id_command: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GeneralCommand**](GeneralCommand.md)| GeneralCommand:  | 
 **id** | **str**| Session Id | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sessions_by_id_command_by_command**
> post_sessions_by_id_command_by_command(id, command)

Issues a system command to a client

Requires authentication as user

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikeyauth
configuration = embyapi.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = embyapi.SessionsServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Session Id
command = 'command_example' # str | The command to send.

try:
    # Issues a system command to a client
    api_instance.post_sessions_by_id_command_by_command(id, command)
except ApiException as e:
    print("Exception when calling SessionsServiceApi->post_sessions_by_id_command_by_command: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Session Id | 
 **command** | **str**| The command to send. | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sessions_by_id_message**
> post_sessions_by_id_message(id, text, header, timeout_ms=timeout_ms)

Issues a command to a client to display a message to the user

Requires authentication as user

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikeyauth
configuration = embyapi.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = embyapi.SessionsServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Session Id
text = 'text_example' # str | The message text.
header = 'header_example' # str | The message header.
timeout_ms = 789 # int | The message timeout. If omitted the user will have to confirm viewing the message. (optional)

try:
    # Issues a command to a client to display a message to the user
    api_instance.post_sessions_by_id_message(id, text, header, timeout_ms=timeout_ms)
except ApiException as e:
    print("Exception when calling SessionsServiceApi->post_sessions_by_id_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Session Id | 
 **text** | **str**| The message text. | 
 **header** | **str**| The message header. | 
 **timeout_ms** | **int**| The message timeout. If omitted the user will have to confirm viewing the message. | [optional] 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sessions_by_id_playing**
> post_sessions_by_id_playing(body, item_ids, play_command, id, start_position_ticks=start_position_ticks)

Instructs a session to play an item

Requires authentication as user

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikeyauth
configuration = embyapi.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = embyapi.SessionsServiceApi(embyapi.ApiClient(configuration))
body = embyapi.PlayRequest() # PlayRequest | PlayRequest: 
item_ids = [56] # list[int] | The ids of the items to play, comma delimited
play_command = 'play_command_example' # str | The type of play command to issue (PlayNow, PlayNext, PlayLast). Clients who have not yet implemented play next and play last may play now.
id = 'id_example' # str | Session Id
start_position_ticks = 789 # int | The starting position of the first item. (optional)

try:
    # Instructs a session to play an item
    api_instance.post_sessions_by_id_playing(body, item_ids, play_command, id, start_position_ticks=start_position_ticks)
except ApiException as e:
    print("Exception when calling SessionsServiceApi->post_sessions_by_id_playing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PlayRequest**](PlayRequest.md)| PlayRequest:  | 
 **item_ids** | [**list[int]**](int.md)| The ids of the items to play, comma delimited | 
 **play_command** | **str**| The type of play command to issue (PlayNow, PlayNext, PlayLast). Clients who have not yet implemented play next and play last may play now. | 
 **id** | **str**| Session Id | 
 **start_position_ticks** | **int**| The starting position of the first item. | [optional] 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sessions_by_id_playing_by_command**
> post_sessions_by_id_playing_by_command(body, id, command)

Issues a playstate command to a client

Requires authentication as user

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikeyauth
configuration = embyapi.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = embyapi.SessionsServiceApi(embyapi.ApiClient(configuration))
body = embyapi.PlaystateRequest() # PlaystateRequest | PlaystateRequest: 
id = 'id_example' # str | Session Id
command = 'command_example' # str | 

try:
    # Issues a playstate command to a client
    api_instance.post_sessions_by_id_playing_by_command(body, id, command)
except ApiException as e:
    print("Exception when calling SessionsServiceApi->post_sessions_by_id_playing_by_command: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PlaystateRequest**](PlaystateRequest.md)| PlaystateRequest:  | 
 **id** | **str**| Session Id | 
 **command** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sessions_by_id_system_by_command**
> post_sessions_by_id_system_by_command(id, command)

Issues a system command to a client

Requires authentication as user

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikeyauth
configuration = embyapi.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = embyapi.SessionsServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Session Id
command = 'command_example' # str | The command to send.

try:
    # Issues a system command to a client
    api_instance.post_sessions_by_id_system_by_command(id, command)
except ApiException as e:
    print("Exception when calling SessionsServiceApi->post_sessions_by_id_system_by_command: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Session Id | 
 **command** | **str**| The command to send. | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sessions_by_id_users_by_userid**
> post_sessions_by_id_users_by_userid(id, user_id)

Adds an additional user to a session

Requires authentication as user

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikeyauth
configuration = embyapi.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = embyapi.SessionsServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Session Id
user_id = 'user_id_example' # str | UserId Id

try:
    # Adds an additional user to a session
    api_instance.post_sessions_by_id_users_by_userid(id, user_id)
except ApiException as e:
    print("Exception when calling SessionsServiceApi->post_sessions_by_id_users_by_userid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Session Id | 
 **user_id** | **str**| UserId Id | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sessions_by_id_viewing**
> post_sessions_by_id_viewing(id, item_type, item_id, item_name)

Instructs a session to browse to an item or view

Requires authentication as user

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikeyauth
configuration = embyapi.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = embyapi.SessionsServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Session Id
item_type = 'item_type_example' # str | The type of item to browse to.
item_id = 'item_id_example' # str | The Id of the item.
item_name = 'item_name_example' # str | The name of the item.

try:
    # Instructs a session to browse to an item or view
    api_instance.post_sessions_by_id_viewing(id, item_type, item_id, item_name)
except ApiException as e:
    print("Exception when calling SessionsServiceApi->post_sessions_by_id_viewing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Session Id | 
 **item_type** | **str**| The type of item to browse to. | 
 **item_id** | **str**| The Id of the item. | 
 **item_name** | **str**| The name of the item. | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sessions_capabilities**
> post_sessions_capabilities(id, playable_media_types=playable_media_types, supported_commands=supported_commands, supports_media_control=supports_media_control, supports_sync=supports_sync, supports_persistent_identifier=supports_persistent_identifier)

Updates capabilities for a device

Requires authentication as user

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikeyauth
configuration = embyapi.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = embyapi.SessionsServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Session Id
playable_media_types = 'playable_media_types_example' # str | A list of playable media types, comma delimited. Audio, Video, Book, Game, Photo. (optional)
supported_commands = 'supported_commands_example' # str | A list of supported remote control commands, comma delimited (optional)
supports_media_control = true # bool | Determines whether media can be played remotely. (optional)
supports_sync = true # bool | Determines whether sync is supported. (optional)
supports_persistent_identifier = true # bool | Determines whether the device supports a unique identifier. (optional)

try:
    # Updates capabilities for a device
    api_instance.post_sessions_capabilities(id, playable_media_types=playable_media_types, supported_commands=supported_commands, supports_media_control=supports_media_control, supports_sync=supports_sync, supports_persistent_identifier=supports_persistent_identifier)
except ApiException as e:
    print("Exception when calling SessionsServiceApi->post_sessions_capabilities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Session Id | 
 **playable_media_types** | **str**| A list of playable media types, comma delimited. Audio, Video, Book, Game, Photo. | [optional] 
 **supported_commands** | **str**| A list of supported remote control commands, comma delimited | [optional] 
 **supports_media_control** | **bool**| Determines whether media can be played remotely. | [optional] 
 **supports_sync** | **bool**| Determines whether sync is supported. | [optional] 
 **supports_persistent_identifier** | **bool**| Determines whether the device supports a unique identifier. | [optional] 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sessions_capabilities_full**
> post_sessions_capabilities_full(body, id)

Updates capabilities for a device

Requires authentication as user

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikeyauth
configuration = embyapi.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = embyapi.SessionsServiceApi(embyapi.ApiClient(configuration))
body = embyapi.ClientCapabilities() # ClientCapabilities | ClientCapabilities: 
id = 'id_example' # str | Session Id

try:
    # Updates capabilities for a device
    api_instance.post_sessions_capabilities_full(body, id)
except ApiException as e:
    print("Exception when calling SessionsServiceApi->post_sessions_capabilities_full: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClientCapabilities**](ClientCapabilities.md)| ClientCapabilities:  | 
 **id** | **str**| Session Id | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sessions_logout**
> post_sessions_logout()

Reports that a session has ended

Requires authentication as user

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikeyauth
configuration = embyapi.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = embyapi.SessionsServiceApi(embyapi.ApiClient(configuration))

try:
    # Reports that a session has ended
    api_instance.post_sessions_logout()
except ApiException as e:
    print("Exception when calling SessionsServiceApi->post_sessions_logout: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

