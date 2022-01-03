# embyapi.ImageByNameServiceApi

All URIs are relative to *https://home.ourflix.de:32865/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_images_general**](ImageByNameServiceApi.md#get_images_general) | **GET** /Images/General | Gets all general images by name
[**get_images_general_by_name_by_type**](ImageByNameServiceApi.md#get_images_general_by_name_by_type) | **GET** /Images/General/{Name}/{Type} | Gets a general image by name
[**get_images_mediainfo**](ImageByNameServiceApi.md#get_images_mediainfo) | **GET** /Images/MediaInfo | Gets all media info image by name
[**get_images_mediainfo_by_theme_by_name**](ImageByNameServiceApi.md#get_images_mediainfo_by_theme_by_name) | **GET** /Images/MediaInfo/{Theme}/{Name} | Gets a media info image by name
[**get_images_ratings**](ImageByNameServiceApi.md#get_images_ratings) | **GET** /Images/Ratings | Gets all rating images by name
[**get_images_ratings_by_theme_by_name**](ImageByNameServiceApi.md#get_images_ratings_by_theme_by_name) | **GET** /Images/Ratings/{Theme}/{Name} | Gets a rating image by name

# **get_images_general**
> list[ImageByNameInfo] get_images_general()

Gets all general images by name

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
api_instance = embyapi.ImageByNameServiceApi(embyapi.ApiClient(configuration))

try:
    # Gets all general images by name
    api_response = api_instance.get_images_general()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageByNameServiceApi->get_images_general: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ImageByNameInfo]**](ImageByNameInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_images_general_by_name_by_type**
> get_images_general_by_name_by_type(name, type)

Gets a general image by name

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.ImageByNameServiceApi()
name = 'name_example' # str | The name of the image
type = 'type_example' # str | Image Type (primary, backdrop, logo, etc).

try:
    # Gets a general image by name
    api_instance.get_images_general_by_name_by_type(name, type)
except ApiException as e:
    print("Exception when calling ImageByNameServiceApi->get_images_general_by_name_by_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the image | 
 **type** | **str**| Image Type (primary, backdrop, logo, etc). | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_images_mediainfo**
> list[ImageByNameInfo] get_images_mediainfo()

Gets all media info image by name

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
api_instance = embyapi.ImageByNameServiceApi(embyapi.ApiClient(configuration))

try:
    # Gets all media info image by name
    api_response = api_instance.get_images_mediainfo()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageByNameServiceApi->get_images_mediainfo: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ImageByNameInfo]**](ImageByNameInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_images_mediainfo_by_theme_by_name**
> get_images_mediainfo_by_theme_by_name(name, theme)

Gets a media info image by name

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.ImageByNameServiceApi()
name = 'name_example' # str | The name of the image
theme = 'theme_example' # str | The theme to get the image from

try:
    # Gets a media info image by name
    api_instance.get_images_mediainfo_by_theme_by_name(name, theme)
except ApiException as e:
    print("Exception when calling ImageByNameServiceApi->get_images_mediainfo_by_theme_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the image | 
 **theme** | **str**| The theme to get the image from | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_images_ratings**
> list[ImageByNameInfo] get_images_ratings()

Gets all rating images by name

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
api_instance = embyapi.ImageByNameServiceApi(embyapi.ApiClient(configuration))

try:
    # Gets all rating images by name
    api_response = api_instance.get_images_ratings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageByNameServiceApi->get_images_ratings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ImageByNameInfo]**](ImageByNameInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_images_ratings_by_theme_by_name**
> get_images_ratings_by_theme_by_name(name, theme)

Gets a rating image by name

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.ImageByNameServiceApi()
name = 'name_example' # str | The name of the image
theme = 'theme_example' # str | The theme to get the image from

try:
    # Gets a rating image by name
    api_instance.get_images_ratings_by_theme_by_name(name, theme)
except ApiException as e:
    print("Exception when calling ImageByNameServiceApi->get_images_ratings_by_theme_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the image | 
 **theme** | **str**| The theme to get the image from | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

