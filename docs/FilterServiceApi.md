# embyapi.FilterServiceApi

All URIs are relative to *https://home.ourflix.de:32865/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_items_filters**](FilterServiceApi.md#get_items_filters) | **GET** /Items/Filters | Gets branding configuration
[**get_items_filters2**](FilterServiceApi.md#get_items_filters2) | **GET** /Items/Filters2 | Gets branding configuration

# **get_items_filters**
> QueryFiltersLegacy get_items_filters(user_id=user_id, parent_id=parent_id, include_item_types=include_item_types, media_types=media_types)

Gets branding configuration

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
api_instance = embyapi.FilterServiceApi(embyapi.ApiClient(configuration))
user_id = 'user_id_example' # str | User Id (optional)
parent_id = 'parent_id_example' # str | Specify this to localize the search to a specific item or folder. Omit to use the root (optional)
include_item_types = 'include_item_types_example' # str | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. (optional)
media_types = 'media_types_example' # str | Optional filter by MediaType. Allows multiple, comma delimited. (optional)

try:
    # Gets branding configuration
    api_response = api_instance.get_items_filters(user_id=user_id, parent_id=parent_id, include_item_types=include_item_types, media_types=media_types)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilterServiceApi->get_items_filters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | [optional] 
 **parent_id** | **str**| Specify this to localize the search to a specific item or folder. Omit to use the root | [optional] 
 **include_item_types** | **str**| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. | [optional] 
 **media_types** | **str**| Optional filter by MediaType. Allows multiple, comma delimited. | [optional] 

### Return type

[**QueryFiltersLegacy**](QueryFiltersLegacy.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items_filters2**
> QueryFilters get_items_filters2(user_id=user_id, parent_id=parent_id, include_item_types=include_item_types, media_types=media_types)

Gets branding configuration

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
api_instance = embyapi.FilterServiceApi(embyapi.ApiClient(configuration))
user_id = 'user_id_example' # str | User Id (optional)
parent_id = 'parent_id_example' # str | Specify this to localize the search to a specific item or folder. Omit to use the root (optional)
include_item_types = 'include_item_types_example' # str | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. (optional)
media_types = 'media_types_example' # str | Optional filter by MediaType. Allows multiple, comma delimited. (optional)

try:
    # Gets branding configuration
    api_response = api_instance.get_items_filters2(user_id=user_id, parent_id=parent_id, include_item_types=include_item_types, media_types=media_types)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilterServiceApi->get_items_filters2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | [optional] 
 **parent_id** | **str**| Specify this to localize the search to a specific item or folder. Omit to use the root | [optional] 
 **include_item_types** | **str**| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. | [optional] 
 **media_types** | **str**| Optional filter by MediaType. Allows multiple, comma delimited. | [optional] 

### Return type

[**QueryFilters**](QueryFilters.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

