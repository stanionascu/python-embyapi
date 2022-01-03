# embyapi.VideosServiceApi

All URIs are relative to *https://home.ourflix.de:32865/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_videos_by_id_alternatesources**](VideosServiceApi.md#delete_videos_by_id_alternatesources) | **DELETE** /Videos/{Id}/AlternateSources | Removes alternate video sources.
[**get_videos_by_id_additionalparts**](VideosServiceApi.md#get_videos_by_id_additionalparts) | **GET** /Videos/{Id}/AdditionalParts | Gets additional parts for a video.
[**post_videos_mergeversions**](VideosServiceApi.md#post_videos_mergeversions) | **POST** /Videos/MergeVersions | Merges videos into a single record

# **delete_videos_by_id_alternatesources**
> delete_videos_by_id_alternatesources(id)

Removes alternate video sources.

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
api_instance = embyapi.VideosServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Item Id

try:
    # Removes alternate video sources.
    api_instance.delete_videos_by_id_alternatesources(id)
except ApiException as e:
    print("Exception when calling VideosServiceApi->delete_videos_by_id_alternatesources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_videos_by_id_additionalparts**
> QueryResultBaseItemDto get_videos_by_id_additionalparts(id, user_id=user_id)

Gets additional parts for a video.

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
api_instance = embyapi.VideosServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Item Id
user_id = 'user_id_example' # str | Optional. Filter by user id, and attach user data (optional)

try:
    # Gets additional parts for a video.
    api_response = api_instance.get_videos_by_id_additionalparts(id, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosServiceApi->get_videos_by_id_additionalparts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **user_id** | **str**| Optional. Filter by user id, and attach user data | [optional] 

### Return type

[**QueryResultBaseItemDto**](QueryResultBaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_videos_mergeversions**
> post_videos_mergeversions(ids=ids)

Merges videos into a single record

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
api_instance = embyapi.VideosServiceApi(embyapi.ApiClient(configuration))
ids = 'ids_example' # str | Item id list. This allows multiple, comma delimited. (optional)

try:
    # Merges videos into a single record
    api_instance.post_videos_mergeversions(ids=ids)
except ApiException as e:
    print("Exception when calling VideosServiceApi->post_videos_mergeversions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**| Item id list. This allows multiple, comma delimited. | [optional] 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

