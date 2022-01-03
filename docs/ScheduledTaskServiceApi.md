# embyapi.ScheduledTaskServiceApi

All URIs are relative to *https://home.ourflix.de:32865/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_scheduledtasks_running_by_id**](ScheduledTaskServiceApi.md#delete_scheduledtasks_running_by_id) | **DELETE** /ScheduledTasks/Running/{Id} | Stops a scheduled task
[**get_scheduledtasks**](ScheduledTaskServiceApi.md#get_scheduledtasks) | **GET** /ScheduledTasks | Gets scheduled tasks
[**get_scheduledtasks_by_id**](ScheduledTaskServiceApi.md#get_scheduledtasks_by_id) | **GET** /ScheduledTasks/{Id} | Gets a scheduled task, by Id
[**post_scheduledtasks_by_id_triggers**](ScheduledTaskServiceApi.md#post_scheduledtasks_by_id_triggers) | **POST** /ScheduledTasks/{Id}/Triggers | Updates the triggers for a scheduled task
[**post_scheduledtasks_running_by_id**](ScheduledTaskServiceApi.md#post_scheduledtasks_running_by_id) | **POST** /ScheduledTasks/Running/{Id} | Starts a scheduled task

# **delete_scheduledtasks_running_by_id**
> delete_scheduledtasks_running_by_id(id)

Stops a scheduled task

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
api_instance = embyapi.ScheduledTaskServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Stops a scheduled task
    api_instance.delete_scheduledtasks_running_by_id(id)
except ApiException as e:
    print("Exception when calling ScheduledTaskServiceApi->delete_scheduledtasks_running_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scheduledtasks**
> list[TasksTaskInfo] get_scheduledtasks(is_hidden=is_hidden, is_enabled=is_enabled)

Gets scheduled tasks

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
api_instance = embyapi.ScheduledTaskServiceApi(embyapi.ApiClient(configuration))
is_hidden = true # bool | Optional filter tasks that are hidden, or not. (optional)
is_enabled = true # bool | Optional filter tasks that are enabled, or not. (optional)

try:
    # Gets scheduled tasks
    api_response = api_instance.get_scheduledtasks(is_hidden=is_hidden, is_enabled=is_enabled)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledTaskServiceApi->get_scheduledtasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_hidden** | **bool**| Optional filter tasks that are hidden, or not. | [optional] 
 **is_enabled** | **bool**| Optional filter tasks that are enabled, or not. | [optional] 

### Return type

[**list[TasksTaskInfo]**](TasksTaskInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scheduledtasks_by_id**
> TasksTaskInfo get_scheduledtasks_by_id(id)

Gets a scheduled task, by Id

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
api_instance = embyapi.ScheduledTaskServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Gets a scheduled task, by Id
    api_response = api_instance.get_scheduledtasks_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledTaskServiceApi->get_scheduledtasks_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**TasksTaskInfo**](TasksTaskInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_scheduledtasks_by_id_triggers**
> post_scheduledtasks_by_id_triggers(body, id)

Updates the triggers for a scheduled task

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
api_instance = embyapi.ScheduledTaskServiceApi(embyapi.ApiClient(configuration))
body = [embyapi.TasksTaskTriggerInfo()] # list[TasksTaskTriggerInfo] | List`1: 
id = 'id_example' # str | 

try:
    # Updates the triggers for a scheduled task
    api_instance.post_scheduledtasks_by_id_triggers(body, id)
except ApiException as e:
    print("Exception when calling ScheduledTaskServiceApi->post_scheduledtasks_by_id_triggers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[TasksTaskTriggerInfo]**](TasksTaskTriggerInfo.md)| List&#x60;1:  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_scheduledtasks_running_by_id**
> post_scheduledtasks_running_by_id(id)

Starts a scheduled task

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
api_instance = embyapi.ScheduledTaskServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Starts a scheduled task
    api_instance.post_scheduledtasks_running_by_id(id)
except ApiException as e:
    print("Exception when calling ScheduledTaskServiceApi->post_scheduledtasks_running_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

