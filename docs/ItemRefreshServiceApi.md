# embyapi.ItemRefreshServiceApi

All URIs are relative to *https://home.ourflix.de:32865/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_items_by_id_refresh**](ItemRefreshServiceApi.md#post_items_by_id_refresh) | **POST** /Items/{Id}/Refresh | Refreshes metadata for an item

# **post_items_by_id_refresh**
> post_items_by_id_refresh(id, recursive=recursive, metadata_refresh_mode=metadata_refresh_mode, image_refresh_mode=image_refresh_mode, replace_all_metadata=replace_all_metadata, replace_all_images=replace_all_images)

Refreshes metadata for an item

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
api_instance = embyapi.ItemRefreshServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Item Id
recursive = true # bool | Indicates if the refresh should occur recursively. (optional)
metadata_refresh_mode = 'metadata_refresh_mode_example' # str | Specifies the metadata refresh mode (optional)
image_refresh_mode = 'image_refresh_mode_example' # str | Specifies the image refresh mode (optional)
replace_all_metadata = true # bool | Determines if metadata should be replaced. Only applicable if mode is FullRefresh (optional)
replace_all_images = true # bool | Determines if images should be replaced. Only applicable if mode is FullRefresh (optional)

try:
    # Refreshes metadata for an item
    api_instance.post_items_by_id_refresh(id, recursive=recursive, metadata_refresh_mode=metadata_refresh_mode, image_refresh_mode=image_refresh_mode, replace_all_metadata=replace_all_metadata, replace_all_images=replace_all_images)
except ApiException as e:
    print("Exception when calling ItemRefreshServiceApi->post_items_by_id_refresh: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **recursive** | **bool**| Indicates if the refresh should occur recursively. | [optional] 
 **metadata_refresh_mode** | **str**| Specifies the metadata refresh mode | [optional] 
 **image_refresh_mode** | **str**| Specifies the image refresh mode | [optional] 
 **replace_all_metadata** | **bool**| Determines if metadata should be replaced. Only applicable if mode is FullRefresh | [optional] 
 **replace_all_images** | **bool**| Determines if images should be replaced. Only applicable if mode is FullRefresh | [optional] 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

