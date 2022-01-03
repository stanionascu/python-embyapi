# embyapi.CollectionServiceApi

All URIs are relative to *https://home.ourflix.de:32865/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_collections_by_id_items**](CollectionServiceApi.md#delete_collections_by_id_items) | **DELETE** /Collections/{Id}/Items | Removes items from a collection
[**post_collections**](CollectionServiceApi.md#post_collections) | **POST** /Collections | Creates a new collection
[**post_collections_by_id_items**](CollectionServiceApi.md#post_collections_by_id_items) | **POST** /Collections/{Id}/Items | Adds items to a collection

# **delete_collections_by_id_items**
> delete_collections_by_id_items(ids, id)

Removes items from a collection

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
api_instance = embyapi.CollectionServiceApi(embyapi.ApiClient(configuration))
ids = 'ids_example' # str | Item id, comma delimited
id = 'id_example' # str | 

try:
    # Removes items from a collection
    api_instance.delete_collections_by_id_items(ids, id)
except ApiException as e:
    print("Exception when calling CollectionServiceApi->delete_collections_by_id_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**| Item id, comma delimited | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_collections**
> CollectionsCollectionCreationResult post_collections(is_locked=is_locked, name=name, parent_id=parent_id, ids=ids)

Creates a new collection

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
api_instance = embyapi.CollectionServiceApi(embyapi.ApiClient(configuration))
is_locked = true # bool | Whether or not to lock the new collection. (optional)
name = 'name_example' # str | The name of the new collection. (optional)
parent_id = 'parent_id_example' # str | Optional - create the collection within a specific folder (optional)
ids = 'ids_example' # str | Item Ids to add to the collection (optional)

try:
    # Creates a new collection
    api_response = api_instance.post_collections(is_locked=is_locked, name=name, parent_id=parent_id, ids=ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionServiceApi->post_collections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_locked** | **bool**| Whether or not to lock the new collection. | [optional] 
 **name** | **str**| The name of the new collection. | [optional] 
 **parent_id** | **str**| Optional - create the collection within a specific folder | [optional] 
 **ids** | **str**| Item Ids to add to the collection | [optional] 

### Return type

[**CollectionsCollectionCreationResult**](CollectionsCollectionCreationResult.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_collections_by_id_items**
> post_collections_by_id_items(ids, id)

Adds items to a collection

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
api_instance = embyapi.CollectionServiceApi(embyapi.ApiClient(configuration))
ids = 'ids_example' # str | Item id, comma delimited
id = 'id_example' # str | 

try:
    # Adds items to a collection
    api_instance.post_collections_by_id_items(ids, id)
except ApiException as e:
    print("Exception when calling CollectionServiceApi->post_collections_by_id_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**| Item id, comma delimited | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

