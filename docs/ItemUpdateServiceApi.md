# embyapi.ItemUpdateServiceApi

All URIs are relative to *https://home.ourflix.de:32865/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_items_by_itemid_metadataeditor**](ItemUpdateServiceApi.md#get_items_by_itemid_metadataeditor) | **GET** /Items/{ItemId}/MetadataEditor | Gets metadata editor info for an item
[**post_items_by_itemid**](ItemUpdateServiceApi.md#post_items_by_itemid) | **POST** /Items/{ItemId} | Updates an item

# **get_items_by_itemid_metadataeditor**
> MetadataEditorInfo get_items_by_itemid_metadataeditor(item_id)

Gets metadata editor info for an item

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
api_instance = embyapi.ItemUpdateServiceApi(embyapi.ApiClient(configuration))
item_id = 'item_id_example' # str | The id of the item

try:
    # Gets metadata editor info for an item
    api_response = api_instance.get_items_by_itemid_metadataeditor(item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemUpdateServiceApi->get_items_by_itemid_metadataeditor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The id of the item | 

### Return type

[**MetadataEditorInfo**](MetadataEditorInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_items_by_itemid**
> post_items_by_itemid(body, item_id)

Updates an item

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
api_instance = embyapi.ItemUpdateServiceApi(embyapi.ApiClient(configuration))
body = embyapi.BaseItemDto() # BaseItemDto | BaseItemDto: 
item_id = 'item_id_example' # str | The id of the item

try:
    # Updates an item
    api_instance.post_items_by_itemid(body, item_id)
except ApiException as e:
    print("Exception when calling ItemUpdateServiceApi->post_items_by_itemid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BaseItemDto**](BaseItemDto.md)| BaseItemDto:  | 
 **item_id** | **str**| The id of the item | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

