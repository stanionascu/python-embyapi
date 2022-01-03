# embyapi.UniversalAudioServiceApi

All URIs are relative to *https://home.ourflix.de:32865/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_audio_by_id_by_container**](UniversalAudioServiceApi.md#get_audio_by_id_by_container) | **GET** /Audio/{Id}/universal.{Container} | Gets an audio stream
[**get_audio_by_id_universal**](UniversalAudioServiceApi.md#get_audio_by_id_universal) | **GET** /Audio/{Id}/universal | Gets an audio stream
[**head_audio_by_id_by_container**](UniversalAudioServiceApi.md#head_audio_by_id_by_container) | **HEAD** /Audio/{Id}/universal.{Container} | Gets an audio stream
[**head_audio_by_id_universal**](UniversalAudioServiceApi.md#head_audio_by_id_universal) | **HEAD** /Audio/{Id}/universal | Gets an audio stream

# **get_audio_by_id_by_container**
> get_audio_by_id_by_container(id, container, device_id=device_id, start_time_ticks=start_time_ticks)

Gets an audio stream

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
api_instance = embyapi.UniversalAudioServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Item Id
container = 'container_example' # str | 
device_id = 'device_id_example' # str | The device id of the client requesting. Used to stop encoding processes when needed. (optional)
start_time_ticks = 789 # int | Optional. Specify a starting offset, in ticks. 1 tick = 10000 ms (optional)

try:
    # Gets an audio stream
    api_instance.get_audio_by_id_by_container(id, container, device_id=device_id, start_time_ticks=start_time_ticks)
except ApiException as e:
    print("Exception when calling UniversalAudioServiceApi->get_audio_by_id_by_container: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **container** | **str**|  | 
 **device_id** | **str**| The device id of the client requesting. Used to stop encoding processes when needed. | [optional] 
 **start_time_ticks** | **int**| Optional. Specify a starting offset, in ticks. 1 tick &#x3D; 10000 ms | [optional] 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audio_by_id_universal**
> get_audio_by_id_universal(id, device_id=device_id, start_time_ticks=start_time_ticks)

Gets an audio stream

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
api_instance = embyapi.UniversalAudioServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Item Id
device_id = 'device_id_example' # str | The device id of the client requesting. Used to stop encoding processes when needed. (optional)
start_time_ticks = 789 # int | Optional. Specify a starting offset, in ticks. 1 tick = 10000 ms (optional)

try:
    # Gets an audio stream
    api_instance.get_audio_by_id_universal(id, device_id=device_id, start_time_ticks=start_time_ticks)
except ApiException as e:
    print("Exception when calling UniversalAudioServiceApi->get_audio_by_id_universal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **device_id** | **str**| The device id of the client requesting. Used to stop encoding processes when needed. | [optional] 
 **start_time_ticks** | **int**| Optional. Specify a starting offset, in ticks. 1 tick &#x3D; 10000 ms | [optional] 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_audio_by_id_by_container**
> head_audio_by_id_by_container(id, container, device_id=device_id, start_time_ticks=start_time_ticks)

Gets an audio stream

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
api_instance = embyapi.UniversalAudioServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Item Id
container = 'container_example' # str | 
device_id = 'device_id_example' # str | The device id of the client requesting. Used to stop encoding processes when needed. (optional)
start_time_ticks = 789 # int | Optional. Specify a starting offset, in ticks. 1 tick = 10000 ms (optional)

try:
    # Gets an audio stream
    api_instance.head_audio_by_id_by_container(id, container, device_id=device_id, start_time_ticks=start_time_ticks)
except ApiException as e:
    print("Exception when calling UniversalAudioServiceApi->head_audio_by_id_by_container: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **container** | **str**|  | 
 **device_id** | **str**| The device id of the client requesting. Used to stop encoding processes when needed. | [optional] 
 **start_time_ticks** | **int**| Optional. Specify a starting offset, in ticks. 1 tick &#x3D; 10000 ms | [optional] 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_audio_by_id_universal**
> head_audio_by_id_universal(id, device_id=device_id, start_time_ticks=start_time_ticks)

Gets an audio stream

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
api_instance = embyapi.UniversalAudioServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Item Id
device_id = 'device_id_example' # str | The device id of the client requesting. Used to stop encoding processes when needed. (optional)
start_time_ticks = 789 # int | Optional. Specify a starting offset, in ticks. 1 tick = 10000 ms (optional)

try:
    # Gets an audio stream
    api_instance.head_audio_by_id_universal(id, device_id=device_id, start_time_ticks=start_time_ticks)
except ApiException as e:
    print("Exception when calling UniversalAudioServiceApi->head_audio_by_id_universal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **device_id** | **str**| The device id of the client requesting. Used to stop encoding processes when needed. | [optional] 
 **start_time_ticks** | **int**| Optional. Specify a starting offset, in ticks. 1 tick &#x3D; 10000 ms | [optional] 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

