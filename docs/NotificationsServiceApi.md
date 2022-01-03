# embyapi.NotificationsServiceApi

All URIs are relative to *https://home.ourflix.de:32865/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_notifications_by_userid**](NotificationsServiceApi.md#get_notifications_by_userid) | **GET** /Notifications/{UserId} | Gets notifications
[**get_notifications_by_userid_summary**](NotificationsServiceApi.md#get_notifications_by_userid_summary) | **GET** /Notifications/{UserId}/Summary | Gets a notification summary for a user
[**get_notifications_services**](NotificationsServiceApi.md#get_notifications_services) | **GET** /Notifications/Services | Gets notification types
[**get_notifications_types**](NotificationsServiceApi.md#get_notifications_types) | **GET** /Notifications/Types | Gets notification types
[**post_notifications_admin**](NotificationsServiceApi.md#post_notifications_admin) | **POST** /Notifications/Admin | Sends a notification to all admin users
[**post_notifications_by_userid_read**](NotificationsServiceApi.md#post_notifications_by_userid_read) | **POST** /Notifications/{UserId}/Read | Marks notifications as read
[**post_notifications_by_userid_unread**](NotificationsServiceApi.md#post_notifications_by_userid_unread) | **POST** /Notifications/{UserId}/Unread | Marks notifications as unread

# **get_notifications_by_userid**
> EmbyNotificationsApiNotificationResult get_notifications_by_userid(user_id, is_read=is_read, start_index=start_index, limit=limit)

Gets notifications

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
api_instance = embyapi.NotificationsServiceApi(embyapi.ApiClient(configuration))
user_id = 'user_id_example' # str | User Id
is_read = true # bool | An optional filter by IsRead (optional)
start_index = 56 # int | Optional. The record index to start at. All items with a lower index will be dropped from the results. (optional)
limit = 56 # int | Optional. The maximum number of records to return (optional)

try:
    # Gets notifications
    api_response = api_instance.get_notifications_by_userid(user_id, is_read=is_read, start_index=start_index, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsServiceApi->get_notifications_by_userid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | 
 **is_read** | **bool**| An optional filter by IsRead | [optional] 
 **start_index** | **int**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return | [optional] 

### Return type

[**EmbyNotificationsApiNotificationResult**](EmbyNotificationsApiNotificationResult.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notifications_by_userid_summary**
> EmbyNotificationsApiNotificationsSummary get_notifications_by_userid_summary(user_id)

Gets a notification summary for a user

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
api_instance = embyapi.NotificationsServiceApi(embyapi.ApiClient(configuration))
user_id = 'user_id_example' # str | User Id

try:
    # Gets a notification summary for a user
    api_response = api_instance.get_notifications_by_userid_summary(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsServiceApi->get_notifications_by_userid_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | 

### Return type

[**EmbyNotificationsApiNotificationsSummary**](EmbyNotificationsApiNotificationsSummary.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notifications_services**
> list[NameIdPair] get_notifications_services()

Gets notification types

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
api_instance = embyapi.NotificationsServiceApi(embyapi.ApiClient(configuration))

try:
    # Gets notification types
    api_response = api_instance.get_notifications_services()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsServiceApi->get_notifications_services: %s\n" % e)
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

# **get_notifications_types**
> list[NotificationsNotificationTypeInfo] get_notifications_types()

Gets notification types

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
api_instance = embyapi.NotificationsServiceApi(embyapi.ApiClient(configuration))

try:
    # Gets notification types
    api_response = api_instance.get_notifications_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsServiceApi->get_notifications_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[NotificationsNotificationTypeInfo]**](NotificationsNotificationTypeInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_notifications_admin**
> post_notifications_admin(name, description, image_url=image_url, url=url, level=level)

Sends a notification to all admin users

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
api_instance = embyapi.NotificationsServiceApi(embyapi.ApiClient(configuration))
name = 'name_example' # str | The notification's name
description = 'description_example' # str | The notification's description
image_url = 'image_url_example' # str | The notification's image url (optional)
url = 'url_example' # str | The notification's info url (optional)
level = 'level_example' # str | The notification level (optional)

try:
    # Sends a notification to all admin users
    api_instance.post_notifications_admin(name, description, image_url=image_url, url=url, level=level)
except ApiException as e:
    print("Exception when calling NotificationsServiceApi->post_notifications_admin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The notification&#x27;s name | 
 **description** | **str**| The notification&#x27;s description | 
 **image_url** | **str**| The notification&#x27;s image url | [optional] 
 **url** | **str**| The notification&#x27;s info url | [optional] 
 **level** | **str**| The notification level | [optional] 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_notifications_by_userid_read**
> post_notifications_by_userid_read(user_id, ids)

Marks notifications as read

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
api_instance = embyapi.NotificationsServiceApi(embyapi.ApiClient(configuration))
user_id = 'user_id_example' # str | User Id
ids = 'ids_example' # str | A list of notification ids, comma delimited

try:
    # Marks notifications as read
    api_instance.post_notifications_by_userid_read(user_id, ids)
except ApiException as e:
    print("Exception when calling NotificationsServiceApi->post_notifications_by_userid_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | 
 **ids** | **str**| A list of notification ids, comma delimited | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_notifications_by_userid_unread**
> post_notifications_by_userid_unread(user_id, ids)

Marks notifications as unread

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
api_instance = embyapi.NotificationsServiceApi(embyapi.ApiClient(configuration))
user_id = 'user_id_example' # str | User Id
ids = 'ids_example' # str | A list of notification ids, comma delimited

try:
    # Marks notifications as unread
    api_instance.post_notifications_by_userid_unread(user_id, ids)
except ApiException as e:
    print("Exception when calling NotificationsServiceApi->post_notifications_by_userid_unread: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | 
 **ids** | **str**| A list of notification ids, comma delimited | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

