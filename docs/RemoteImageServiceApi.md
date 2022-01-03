# embyapi.RemoteImageServiceApi

All URIs are relative to *https://home.ourflix.de:32865/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_images_remote**](RemoteImageServiceApi.md#get_images_remote) | **GET** /Images/Remote | Gets a remote image
[**get_items_by_id_remoteimages**](RemoteImageServiceApi.md#get_items_by_id_remoteimages) | **GET** /Items/{Id}/RemoteImages | Gets available remote images for an item
[**get_items_by_id_remoteimages_providers**](RemoteImageServiceApi.md#get_items_by_id_remoteimages_providers) | **GET** /Items/{Id}/RemoteImages/Providers | Gets available remote image providers for an item
[**post_items_by_id_remoteimages_download**](RemoteImageServiceApi.md#post_items_by_id_remoteimages_download) | **POST** /Items/{Id}/RemoteImages/Download | Downloads a remote image for an item

# **get_images_remote**
> get_images_remote(image_url)

Gets a remote image

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.RemoteImageServiceApi()
image_url = 'image_url_example' # str | The image url

try:
    # Gets a remote image
    api_instance.get_images_remote(image_url)
except ApiException as e:
    print("Exception when calling RemoteImageServiceApi->get_images_remote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_url** | **str**| The image url | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items_by_id_remoteimages**
> RemoteImageResult get_items_by_id_remoteimages(id, type=type, start_index=start_index, limit=limit, provider_name=provider_name, include_all_languages=include_all_languages)

Gets available remote images for an item

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
api_instance = embyapi.RemoteImageServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Item Id
type = 'type_example' # str | The image type (optional)
start_index = 56 # int | Optional. The record index to start at. All items with a lower index will be dropped from the results. (optional)
limit = 56 # int | Optional. The maximum number of records to return (optional)
provider_name = 'provider_name_example' # str | Optional. The image provider to use (optional)
include_all_languages = true # bool | Optional. (optional)

try:
    # Gets available remote images for an item
    api_response = api_instance.get_items_by_id_remoteimages(id, type=type, start_index=start_index, limit=limit, provider_name=provider_name, include_all_languages=include_all_languages)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemoteImageServiceApi->get_items_by_id_remoteimages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **type** | **str**| The image type | [optional] 
 **start_index** | **int**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return | [optional] 
 **provider_name** | **str**| Optional. The image provider to use | [optional] 
 **include_all_languages** | **bool**| Optional. | [optional] 

### Return type

[**RemoteImageResult**](RemoteImageResult.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items_by_id_remoteimages_providers**
> list[ImageProviderInfo] get_items_by_id_remoteimages_providers(id)

Gets available remote image providers for an item

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
api_instance = embyapi.RemoteImageServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Item Id

try:
    # Gets available remote image providers for an item
    api_response = api_instance.get_items_by_id_remoteimages_providers(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemoteImageServiceApi->get_items_by_id_remoteimages_providers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 

### Return type

[**list[ImageProviderInfo]**](ImageProviderInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_items_by_id_remoteimages_download**
> post_items_by_id_remoteimages_download(id, type, provider_name=provider_name, image_url=image_url)

Downloads a remote image for an item

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
api_instance = embyapi.RemoteImageServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Item Id
type = 'type_example' # str | The image type
provider_name = 'provider_name_example' # str | The image provider (optional)
image_url = 'image_url_example' # str | The image url (optional)

try:
    # Downloads a remote image for an item
    api_instance.post_items_by_id_remoteimages_download(id, type, provider_name=provider_name, image_url=image_url)
except ApiException as e:
    print("Exception when calling RemoteImageServiceApi->post_items_by_id_remoteimages_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **type** | **str**| The image type | 
 **provider_name** | **str**| The image provider | [optional] 
 **image_url** | **str**| The image url | [optional] 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

