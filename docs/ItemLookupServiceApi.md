# embyapi.ItemLookupServiceApi

All URIs are relative to *https://home.ourflix.de:32865/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_items_by_id_externalidinfos**](ItemLookupServiceApi.md#get_items_by_id_externalidinfos) | **GET** /Items/{Id}/ExternalIdInfos | Gets external id infos for an item
[**get_items_remotesearch_image**](ItemLookupServiceApi.md#get_items_remotesearch_image) | **GET** /Items/RemoteSearch/Image | Gets a remote image
[**post_items_remotesearch_apply_by_id**](ItemLookupServiceApi.md#post_items_remotesearch_apply_by_id) | **POST** /Items/RemoteSearch/Apply/{Id} | Applies search criteria to an item and refreshes metadata
[**post_items_remotesearch_book**](ItemLookupServiceApi.md#post_items_remotesearch_book) | **POST** /Items/RemoteSearch/Book | 
[**post_items_remotesearch_boxset**](ItemLookupServiceApi.md#post_items_remotesearch_boxset) | **POST** /Items/RemoteSearch/BoxSet | 
[**post_items_remotesearch_game**](ItemLookupServiceApi.md#post_items_remotesearch_game) | **POST** /Items/RemoteSearch/Game | 
[**post_items_remotesearch_movie**](ItemLookupServiceApi.md#post_items_remotesearch_movie) | **POST** /Items/RemoteSearch/Movie | 
[**post_items_remotesearch_musicalbum**](ItemLookupServiceApi.md#post_items_remotesearch_musicalbum) | **POST** /Items/RemoteSearch/MusicAlbum | 
[**post_items_remotesearch_musicartist**](ItemLookupServiceApi.md#post_items_remotesearch_musicartist) | **POST** /Items/RemoteSearch/MusicArtist | 
[**post_items_remotesearch_musicvideo**](ItemLookupServiceApi.md#post_items_remotesearch_musicvideo) | **POST** /Items/RemoteSearch/MusicVideo | 
[**post_items_remotesearch_person**](ItemLookupServiceApi.md#post_items_remotesearch_person) | **POST** /Items/RemoteSearch/Person | 
[**post_items_remotesearch_series**](ItemLookupServiceApi.md#post_items_remotesearch_series) | **POST** /Items/RemoteSearch/Series | 
[**post_items_remotesearch_trailer**](ItemLookupServiceApi.md#post_items_remotesearch_trailer) | **POST** /Items/RemoteSearch/Trailer | 

# **get_items_by_id_externalidinfos**
> list[ExternalIdInfo] get_items_by_id_externalidinfos(id)

Gets external id infos for an item

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
api_instance = embyapi.ItemLookupServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Item Id

try:
    # Gets external id infos for an item
    api_response = api_instance.get_items_by_id_externalidinfos(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemLookupServiceApi->get_items_by_id_externalidinfos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 

### Return type

[**list[ExternalIdInfo]**](ExternalIdInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items_remotesearch_image**
> get_items_remotesearch_image(image_url, provider_name)

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
api_instance = embyapi.ItemLookupServiceApi()
image_url = 'image_url_example' # str | The image url
provider_name = 'provider_name_example' # str | 

try:
    # Gets a remote image
    api_instance.get_items_remotesearch_image(image_url, provider_name)
except ApiException as e:
    print("Exception when calling ItemLookupServiceApi->get_items_remotesearch_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_url** | **str**| The image url | 
 **provider_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_items_remotesearch_apply_by_id**
> post_items_remotesearch_apply_by_id(body, id, replace_all_images=replace_all_images)

Applies search criteria to an item and refreshes metadata

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
api_instance = embyapi.ItemLookupServiceApi(embyapi.ApiClient(configuration))
body = embyapi.RemoteSearchResult() # RemoteSearchResult | RemoteSearchResult: 
id = 'id_example' # str | The item id
replace_all_images = true # bool | Whether or not to replace all images (optional)

try:
    # Applies search criteria to an item and refreshes metadata
    api_instance.post_items_remotesearch_apply_by_id(body, id, replace_all_images=replace_all_images)
except ApiException as e:
    print("Exception when calling ItemLookupServiceApi->post_items_remotesearch_apply_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RemoteSearchResult**](RemoteSearchResult.md)| RemoteSearchResult:  | 
 **id** | **str**| The item id | 
 **replace_all_images** | **bool**| Whether or not to replace all images | [optional] 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_items_remotesearch_book**
> list[RemoteSearchResult] post_items_remotesearch_book(body)



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
api_instance = embyapi.ItemLookupServiceApi(embyapi.ApiClient(configuration))
body = embyapi.ProvidersRemoteSearchQueryProvidersBookInfo() # ProvidersRemoteSearchQueryProvidersBookInfo | RemoteSearchQuery`1: 

try:
    api_response = api_instance.post_items_remotesearch_book(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemLookupServiceApi->post_items_remotesearch_book: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProvidersRemoteSearchQueryProvidersBookInfo**](ProvidersRemoteSearchQueryProvidersBookInfo.md)| RemoteSearchQuery&#x60;1:  | 

### Return type

[**list[RemoteSearchResult]**](RemoteSearchResult.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_items_remotesearch_boxset**
> list[RemoteSearchResult] post_items_remotesearch_boxset(body)



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
api_instance = embyapi.ItemLookupServiceApi(embyapi.ApiClient(configuration))
body = embyapi.ProvidersRemoteSearchQueryProvidersBoxSetInfo() # ProvidersRemoteSearchQueryProvidersBoxSetInfo | RemoteSearchQuery`1: 

try:
    api_response = api_instance.post_items_remotesearch_boxset(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemLookupServiceApi->post_items_remotesearch_boxset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProvidersRemoteSearchQueryProvidersBoxSetInfo**](ProvidersRemoteSearchQueryProvidersBoxSetInfo.md)| RemoteSearchQuery&#x60;1:  | 

### Return type

[**list[RemoteSearchResult]**](RemoteSearchResult.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_items_remotesearch_game**
> list[RemoteSearchResult] post_items_remotesearch_game(body)



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
api_instance = embyapi.ItemLookupServiceApi(embyapi.ApiClient(configuration))
body = embyapi.ProvidersRemoteSearchQueryProvidersGameInfo() # ProvidersRemoteSearchQueryProvidersGameInfo | RemoteSearchQuery`1: 

try:
    api_response = api_instance.post_items_remotesearch_game(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemLookupServiceApi->post_items_remotesearch_game: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProvidersRemoteSearchQueryProvidersGameInfo**](ProvidersRemoteSearchQueryProvidersGameInfo.md)| RemoteSearchQuery&#x60;1:  | 

### Return type

[**list[RemoteSearchResult]**](RemoteSearchResult.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_items_remotesearch_movie**
> list[RemoteSearchResult] post_items_remotesearch_movie(body)



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
api_instance = embyapi.ItemLookupServiceApi(embyapi.ApiClient(configuration))
body = embyapi.ProvidersRemoteSearchQueryProvidersMovieInfo() # ProvidersRemoteSearchQueryProvidersMovieInfo | RemoteSearchQuery`1: 

try:
    api_response = api_instance.post_items_remotesearch_movie(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemLookupServiceApi->post_items_remotesearch_movie: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProvidersRemoteSearchQueryProvidersMovieInfo**](ProvidersRemoteSearchQueryProvidersMovieInfo.md)| RemoteSearchQuery&#x60;1:  | 

### Return type

[**list[RemoteSearchResult]**](RemoteSearchResult.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_items_remotesearch_musicalbum**
> list[RemoteSearchResult] post_items_remotesearch_musicalbum(body)



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
api_instance = embyapi.ItemLookupServiceApi(embyapi.ApiClient(configuration))
body = embyapi.ProvidersRemoteSearchQueryProvidersAlbumInfo() # ProvidersRemoteSearchQueryProvidersAlbumInfo | RemoteSearchQuery`1: 

try:
    api_response = api_instance.post_items_remotesearch_musicalbum(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemLookupServiceApi->post_items_remotesearch_musicalbum: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProvidersRemoteSearchQueryProvidersAlbumInfo**](ProvidersRemoteSearchQueryProvidersAlbumInfo.md)| RemoteSearchQuery&#x60;1:  | 

### Return type

[**list[RemoteSearchResult]**](RemoteSearchResult.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_items_remotesearch_musicartist**
> list[RemoteSearchResult] post_items_remotesearch_musicartist(body)



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
api_instance = embyapi.ItemLookupServiceApi(embyapi.ApiClient(configuration))
body = embyapi.ProvidersRemoteSearchQueryProvidersArtistInfo() # ProvidersRemoteSearchQueryProvidersArtistInfo | RemoteSearchQuery`1: 

try:
    api_response = api_instance.post_items_remotesearch_musicartist(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemLookupServiceApi->post_items_remotesearch_musicartist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProvidersRemoteSearchQueryProvidersArtistInfo**](ProvidersRemoteSearchQueryProvidersArtistInfo.md)| RemoteSearchQuery&#x60;1:  | 

### Return type

[**list[RemoteSearchResult]**](RemoteSearchResult.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_items_remotesearch_musicvideo**
> list[RemoteSearchResult] post_items_remotesearch_musicvideo(body)



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
api_instance = embyapi.ItemLookupServiceApi(embyapi.ApiClient(configuration))
body = embyapi.ProvidersRemoteSearchQueryProvidersMusicVideoInfo() # ProvidersRemoteSearchQueryProvidersMusicVideoInfo | RemoteSearchQuery`1: 

try:
    api_response = api_instance.post_items_remotesearch_musicvideo(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemLookupServiceApi->post_items_remotesearch_musicvideo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProvidersRemoteSearchQueryProvidersMusicVideoInfo**](ProvidersRemoteSearchQueryProvidersMusicVideoInfo.md)| RemoteSearchQuery&#x60;1:  | 

### Return type

[**list[RemoteSearchResult]**](RemoteSearchResult.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_items_remotesearch_person**
> list[RemoteSearchResult] post_items_remotesearch_person(body)



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
api_instance = embyapi.ItemLookupServiceApi(embyapi.ApiClient(configuration))
body = embyapi.ProvidersRemoteSearchQueryProvidersPersonLookupInfo() # ProvidersRemoteSearchQueryProvidersPersonLookupInfo | RemoteSearchQuery`1: 

try:
    api_response = api_instance.post_items_remotesearch_person(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemLookupServiceApi->post_items_remotesearch_person: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProvidersRemoteSearchQueryProvidersPersonLookupInfo**](ProvidersRemoteSearchQueryProvidersPersonLookupInfo.md)| RemoteSearchQuery&#x60;1:  | 

### Return type

[**list[RemoteSearchResult]**](RemoteSearchResult.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_items_remotesearch_series**
> list[RemoteSearchResult] post_items_remotesearch_series(body)



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
api_instance = embyapi.ItemLookupServiceApi(embyapi.ApiClient(configuration))
body = embyapi.ProvidersRemoteSearchQueryProvidersSeriesInfo() # ProvidersRemoteSearchQueryProvidersSeriesInfo | RemoteSearchQuery`1: 

try:
    api_response = api_instance.post_items_remotesearch_series(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemLookupServiceApi->post_items_remotesearch_series: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProvidersRemoteSearchQueryProvidersSeriesInfo**](ProvidersRemoteSearchQueryProvidersSeriesInfo.md)| RemoteSearchQuery&#x60;1:  | 

### Return type

[**list[RemoteSearchResult]**](RemoteSearchResult.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_items_remotesearch_trailer**
> list[RemoteSearchResult] post_items_remotesearch_trailer(body)



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
api_instance = embyapi.ItemLookupServiceApi(embyapi.ApiClient(configuration))
body = embyapi.ProvidersRemoteSearchQueryProvidersTrailerInfo() # ProvidersRemoteSearchQueryProvidersTrailerInfo | RemoteSearchQuery`1: 

try:
    api_response = api_instance.post_items_remotesearch_trailer(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemLookupServiceApi->post_items_remotesearch_trailer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProvidersRemoteSearchQueryProvidersTrailerInfo**](ProvidersRemoteSearchQueryProvidersTrailerInfo.md)| RemoteSearchQuery&#x60;1:  | 

### Return type

[**list[RemoteSearchResult]**](RemoteSearchResult.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

