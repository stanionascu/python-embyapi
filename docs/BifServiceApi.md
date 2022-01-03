# embyapi.BifServiceApi

All URIs are relative to *https://home.ourflix.de:32865/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_items_by_id_thumbnailset**](BifServiceApi.md#get_items_by_id_thumbnailset) | **GET** /Items/{Id}/ThumbnailSet | 
[**get_videos_by_id_index_bif**](BifServiceApi.md#get_videos_by_id_index_bif) | **GET** /Videos/{Id}/index.bif | 

# **get_items_by_id_thumbnailset**
> RokuMetadataApiThumbnailSetInfo get_items_by_id_thumbnailset(width, id)



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
api_instance = embyapi.BifServiceApi(embyapi.ApiClient(configuration))
width = 56 # int | 
id = 'id_example' # str | Item Id

try:
    api_response = api_instance.get_items_by_id_thumbnailset(width, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BifServiceApi->get_items_by_id_thumbnailset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **width** | **int**|  | 
 **id** | **str**| Item Id | 

### Return type

[**RokuMetadataApiThumbnailSetInfo**](RokuMetadataApiThumbnailSetInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_videos_by_id_index_bif**
> get_videos_by_id_index_bif(width, id)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.BifServiceApi()
width = 56 # int | 
id = 'id_example' # str | Item Id

try:
    api_instance.get_videos_by_id_index_bif(width, id)
except ApiException as e:
    print("Exception when calling BifServiceApi->get_videos_by_id_index_bif: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **width** | **int**|  | 
 **id** | **str**| Item Id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

