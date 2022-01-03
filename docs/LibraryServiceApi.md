# embyapi.LibraryServiceApi

All URIs are relative to *https://home.ourflix.de:32865/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_items**](LibraryServiceApi.md#delete_items) | **DELETE** /Items | Deletes an item from the library and file system
[**delete_items_by_id**](LibraryServiceApi.md#delete_items_by_id) | **DELETE** /Items/{Id} | Deletes an item from the library and file system
[**get_albums_by_id_similar**](LibraryServiceApi.md#get_albums_by_id_similar) | **GET** /Albums/{Id}/Similar | Finds albums similar to a given album.
[**get_artists_by_id_similar**](LibraryServiceApi.md#get_artists_by_id_similar) | **GET** /Artists/{Id}/Similar | Finds albums similar to a given album.
[**get_games_by_id_similar**](LibraryServiceApi.md#get_games_by_id_similar) | **GET** /Games/{Id}/Similar | Finds games similar to a given game.
[**get_items_by_id_ancestors**](LibraryServiceApi.md#get_items_by_id_ancestors) | **GET** /Items/{Id}/Ancestors | Gets all parents of an item
[**get_items_by_id_criticreviews**](LibraryServiceApi.md#get_items_by_id_criticreviews) | **GET** /Items/{Id}/CriticReviews | Gets critic reviews for an item
[**get_items_by_id_deleteinfo**](LibraryServiceApi.md#get_items_by_id_deleteinfo) | **GET** /Items/{Id}/DeleteInfo | Gets delete info for an item
[**get_items_by_id_download**](LibraryServiceApi.md#get_items_by_id_download) | **GET** /Items/{Id}/Download | Downloads item media
[**get_items_by_id_file**](LibraryServiceApi.md#get_items_by_id_file) | **GET** /Items/{Id}/File | Gets the original file of an item
[**get_items_by_id_similar**](LibraryServiceApi.md#get_items_by_id_similar) | **GET** /Items/{Id}/Similar | Gets similar items
[**get_items_by_id_thememedia**](LibraryServiceApi.md#get_items_by_id_thememedia) | **GET** /Items/{Id}/ThemeMedia | Gets theme videos and songs for an item
[**get_items_by_id_themesongs**](LibraryServiceApi.md#get_items_by_id_themesongs) | **GET** /Items/{Id}/ThemeSongs | Gets theme songs for an item
[**get_items_by_id_themevideos**](LibraryServiceApi.md#get_items_by_id_themevideos) | **GET** /Items/{Id}/ThemeVideos | Gets theme videos for an item
[**get_items_counts**](LibraryServiceApi.md#get_items_counts) | **GET** /Items/Counts | 
[**get_libraries_availableoptions**](LibraryServiceApi.md#get_libraries_availableoptions) | **GET** /Libraries/AvailableOptions | 
[**get_library_mediafolders**](LibraryServiceApi.md#get_library_mediafolders) | **GET** /Library/MediaFolders | Gets all user media folders.
[**get_library_physicalpaths**](LibraryServiceApi.md#get_library_physicalpaths) | **GET** /Library/PhysicalPaths | Gets a list of physical paths from virtual folders
[**get_library_selectablemediafolders**](LibraryServiceApi.md#get_library_selectablemediafolders) | **GET** /Library/SelectableMediaFolders | Gets all user media folders.
[**get_movies_by_id_similar**](LibraryServiceApi.md#get_movies_by_id_similar) | **GET** /Movies/{Id}/Similar | Finds movies and trailers similar to a given movie.
[**get_shows_by_id_similar**](LibraryServiceApi.md#get_shows_by_id_similar) | **GET** /Shows/{Id}/Similar | Finds tv shows similar to a given one.
[**get_trailers_by_id_similar**](LibraryServiceApi.md#get_trailers_by_id_similar) | **GET** /Trailers/{Id}/Similar | Finds movies and trailers similar to a given trailer.
[**post_library_media_updated**](LibraryServiceApi.md#post_library_media_updated) | **POST** /Library/Media/Updated | Reports that new movies have been added by an external source
[**post_library_movies_added**](LibraryServiceApi.md#post_library_movies_added) | **POST** /Library/Movies/Added | Deprecated. Use /Library/Media/Updated
[**post_library_movies_updated**](LibraryServiceApi.md#post_library_movies_updated) | **POST** /Library/Movies/Updated | Deprecated. Use /Library/Media/Updated
[**post_library_refresh**](LibraryServiceApi.md#post_library_refresh) | **POST** /Library/Refresh | Starts a library scan
[**post_library_series_added**](LibraryServiceApi.md#post_library_series_added) | **POST** /Library/Series/Added | Deprecated. Use /Library/Media/Updated
[**post_library_series_updated**](LibraryServiceApi.md#post_library_series_updated) | **POST** /Library/Series/Updated | Deprecated. Use /Library/Media/Updated

# **delete_items**
> delete_items(ids)

Deletes an item from the library and file system

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
api_instance = embyapi.LibraryServiceApi(embyapi.ApiClient(configuration))
ids = 'ids_example' # str | Ids

try:
    # Deletes an item from the library and file system
    api_instance.delete_items(ids)
except ApiException as e:
    print("Exception when calling LibraryServiceApi->delete_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**| Ids | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_items_by_id**
> delete_items_by_id(id)

Deletes an item from the library and file system

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
api_instance = embyapi.LibraryServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Item Id

try:
    # Deletes an item from the library and file system
    api_instance.delete_items_by_id(id)
except ApiException as e:
    print("Exception when calling LibraryServiceApi->delete_items_by_id: %s\n" % e)
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

# **get_albums_by_id_similar**
> QueryResultBaseItemDto get_albums_by_id_similar(id, include_item_types=include_item_types, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, user_id=user_id, limit=limit, fields=fields)

Finds albums similar to a given album.

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
api_instance = embyapi.LibraryServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Item Id
include_item_types = 'include_item_types_example' # str | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. (optional)
enable_images = true # bool | Optional, include image information in output (optional)
enable_user_data = true # bool | Optional, include user data (optional)
image_type_limit = 56 # int | Optional, the max number of images to return, per image type (optional)
enable_image_types = 'enable_image_types_example' # str | Optional. The image types to include in the output. (optional)
user_id = 'user_id_example' # str | Optional. Filter by user id, and attach user data (optional)
limit = 56 # int | Optional. The maximum number of records to return (optional)
fields = 'fields_example' # str | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls (optional)

try:
    # Finds albums similar to a given album.
    api_response = api_instance.get_albums_by_id_similar(id, include_item_types=include_item_types, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, user_id=user_id, limit=limit, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryServiceApi->get_albums_by_id_similar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **include_item_types** | **str**| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. | [optional] 
 **enable_images** | **bool**| Optional, include image information in output | [optional] 
 **enable_user_data** | **bool**| Optional, include user data | [optional] 
 **image_type_limit** | **int**| Optional, the max number of images to return, per image type | [optional] 
 **enable_image_types** | **str**| Optional. The image types to include in the output. | [optional] 
 **user_id** | **str**| Optional. Filter by user id, and attach user data | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return | [optional] 
 **fields** | **str**| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls | [optional] 

### Return type

[**QueryResultBaseItemDto**](QueryResultBaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artists_by_id_similar**
> QueryResultBaseItemDto get_artists_by_id_similar(id, include_item_types=include_item_types, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, user_id=user_id, limit=limit, fields=fields)

Finds albums similar to a given album.

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
api_instance = embyapi.LibraryServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Item Id
include_item_types = 'include_item_types_example' # str | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. (optional)
enable_images = true # bool | Optional, include image information in output (optional)
enable_user_data = true # bool | Optional, include user data (optional)
image_type_limit = 56 # int | Optional, the max number of images to return, per image type (optional)
enable_image_types = 'enable_image_types_example' # str | Optional. The image types to include in the output. (optional)
user_id = 'user_id_example' # str | Optional. Filter by user id, and attach user data (optional)
limit = 56 # int | Optional. The maximum number of records to return (optional)
fields = 'fields_example' # str | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls (optional)

try:
    # Finds albums similar to a given album.
    api_response = api_instance.get_artists_by_id_similar(id, include_item_types=include_item_types, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, user_id=user_id, limit=limit, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryServiceApi->get_artists_by_id_similar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **include_item_types** | **str**| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. | [optional] 
 **enable_images** | **bool**| Optional, include image information in output | [optional] 
 **enable_user_data** | **bool**| Optional, include user data | [optional] 
 **image_type_limit** | **int**| Optional, the max number of images to return, per image type | [optional] 
 **enable_image_types** | **str**| Optional. The image types to include in the output. | [optional] 
 **user_id** | **str**| Optional. Filter by user id, and attach user data | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return | [optional] 
 **fields** | **str**| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls | [optional] 

### Return type

[**QueryResultBaseItemDto**](QueryResultBaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_games_by_id_similar**
> QueryResultBaseItemDto get_games_by_id_similar(id, include_item_types=include_item_types, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, user_id=user_id, limit=limit, fields=fields)

Finds games similar to a given game.

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
api_instance = embyapi.LibraryServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Item Id
include_item_types = 'include_item_types_example' # str | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. (optional)
enable_images = true # bool | Optional, include image information in output (optional)
enable_user_data = true # bool | Optional, include user data (optional)
image_type_limit = 56 # int | Optional, the max number of images to return, per image type (optional)
enable_image_types = 'enable_image_types_example' # str | Optional. The image types to include in the output. (optional)
user_id = 'user_id_example' # str | Optional. Filter by user id, and attach user data (optional)
limit = 56 # int | Optional. The maximum number of records to return (optional)
fields = 'fields_example' # str | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls (optional)

try:
    # Finds games similar to a given game.
    api_response = api_instance.get_games_by_id_similar(id, include_item_types=include_item_types, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, user_id=user_id, limit=limit, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryServiceApi->get_games_by_id_similar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **include_item_types** | **str**| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. | [optional] 
 **enable_images** | **bool**| Optional, include image information in output | [optional] 
 **enable_user_data** | **bool**| Optional, include user data | [optional] 
 **image_type_limit** | **int**| Optional, the max number of images to return, per image type | [optional] 
 **enable_image_types** | **str**| Optional. The image types to include in the output. | [optional] 
 **user_id** | **str**| Optional. Filter by user id, and attach user data | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return | [optional] 
 **fields** | **str**| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls | [optional] 

### Return type

[**QueryResultBaseItemDto**](QueryResultBaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items_by_id_ancestors**
> list[BaseItemDto] get_items_by_id_ancestors(id, user_id=user_id)

Gets all parents of an item

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
api_instance = embyapi.LibraryServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Item Id
user_id = 'user_id_example' # str | Optional. Filter by user id, and attach user data (optional)

try:
    # Gets all parents of an item
    api_response = api_instance.get_items_by_id_ancestors(id, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryServiceApi->get_items_by_id_ancestors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **user_id** | **str**| Optional. Filter by user id, and attach user data | [optional] 

### Return type

[**list[BaseItemDto]**](BaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items_by_id_criticreviews**
> QueryResultBaseItemDto get_items_by_id_criticreviews(id, start_index=start_index, limit=limit)

Gets critic reviews for an item

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
api_instance = embyapi.LibraryServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Item Id
start_index = 56 # int | Optional. The record index to start at. All items with a lower index will be dropped from the results. (optional)
limit = 56 # int | Optional. The maximum number of records to return (optional)

try:
    # Gets critic reviews for an item
    api_response = api_instance.get_items_by_id_criticreviews(id, start_index=start_index, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryServiceApi->get_items_by_id_criticreviews: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **start_index** | **int**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return | [optional] 

### Return type

[**QueryResultBaseItemDto**](QueryResultBaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items_by_id_deleteinfo**
> LibraryDeleteInfo get_items_by_id_deleteinfo(id)

Gets delete info for an item

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
api_instance = embyapi.LibraryServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Item Id

try:
    # Gets delete info for an item
    api_response = api_instance.get_items_by_id_deleteinfo(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryServiceApi->get_items_by_id_deleteinfo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 

### Return type

[**LibraryDeleteInfo**](LibraryDeleteInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items_by_id_download**
> get_items_by_id_download(id)

Downloads item media

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
api_instance = embyapi.LibraryServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Item Id

try:
    # Downloads item media
    api_instance.get_items_by_id_download(id)
except ApiException as e:
    print("Exception when calling LibraryServiceApi->get_items_by_id_download: %s\n" % e)
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

# **get_items_by_id_file**
> get_items_by_id_file(id)

Gets the original file of an item

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
api_instance = embyapi.LibraryServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Item Id

try:
    # Gets the original file of an item
    api_instance.get_items_by_id_file(id)
except ApiException as e:
    print("Exception when calling LibraryServiceApi->get_items_by_id_file: %s\n" % e)
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

# **get_items_by_id_similar**
> QueryResultBaseItemDto get_items_by_id_similar(id, include_item_types=include_item_types, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, user_id=user_id, limit=limit, fields=fields)

Gets similar items

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
api_instance = embyapi.LibraryServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Item Id
include_item_types = 'include_item_types_example' # str | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. (optional)
enable_images = true # bool | Optional, include image information in output (optional)
enable_user_data = true # bool | Optional, include user data (optional)
image_type_limit = 56 # int | Optional, the max number of images to return, per image type (optional)
enable_image_types = 'enable_image_types_example' # str | Optional. The image types to include in the output. (optional)
user_id = 'user_id_example' # str | Optional. Filter by user id, and attach user data (optional)
limit = 56 # int | Optional. The maximum number of records to return (optional)
fields = 'fields_example' # str | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls (optional)

try:
    # Gets similar items
    api_response = api_instance.get_items_by_id_similar(id, include_item_types=include_item_types, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, user_id=user_id, limit=limit, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryServiceApi->get_items_by_id_similar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **include_item_types** | **str**| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. | [optional] 
 **enable_images** | **bool**| Optional, include image information in output | [optional] 
 **enable_user_data** | **bool**| Optional, include user data | [optional] 
 **image_type_limit** | **int**| Optional, the max number of images to return, per image type | [optional] 
 **enable_image_types** | **str**| Optional. The image types to include in the output. | [optional] 
 **user_id** | **str**| Optional. Filter by user id, and attach user data | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return | [optional] 
 **fields** | **str**| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls | [optional] 

### Return type

[**QueryResultBaseItemDto**](QueryResultBaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items_by_id_thememedia**
> AllThemeMediaResult get_items_by_id_thememedia(id, user_id=user_id, inherit_from_parent=inherit_from_parent)

Gets theme videos and songs for an item

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
api_instance = embyapi.LibraryServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Item Id
user_id = 'user_id_example' # str | Optional. Filter by user id, and attach user data (optional)
inherit_from_parent = true # bool | Determines whether or not parent items should be searched for theme media. (optional)

try:
    # Gets theme videos and songs for an item
    api_response = api_instance.get_items_by_id_thememedia(id, user_id=user_id, inherit_from_parent=inherit_from_parent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryServiceApi->get_items_by_id_thememedia: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **user_id** | **str**| Optional. Filter by user id, and attach user data | [optional] 
 **inherit_from_parent** | **bool**| Determines whether or not parent items should be searched for theme media. | [optional] 

### Return type

[**AllThemeMediaResult**](AllThemeMediaResult.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items_by_id_themesongs**
> ThemeMediaResult get_items_by_id_themesongs(id, user_id=user_id, inherit_from_parent=inherit_from_parent)

Gets theme songs for an item

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
api_instance = embyapi.LibraryServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Item Id
user_id = 'user_id_example' # str | Optional. Filter by user id, and attach user data (optional)
inherit_from_parent = true # bool | Determines whether or not parent items should be searched for theme media. (optional)

try:
    # Gets theme songs for an item
    api_response = api_instance.get_items_by_id_themesongs(id, user_id=user_id, inherit_from_parent=inherit_from_parent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryServiceApi->get_items_by_id_themesongs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **user_id** | **str**| Optional. Filter by user id, and attach user data | [optional] 
 **inherit_from_parent** | **bool**| Determines whether or not parent items should be searched for theme media. | [optional] 

### Return type

[**ThemeMediaResult**](ThemeMediaResult.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items_by_id_themevideos**
> ThemeMediaResult get_items_by_id_themevideos(id, user_id=user_id, inherit_from_parent=inherit_from_parent)

Gets theme videos for an item

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
api_instance = embyapi.LibraryServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Item Id
user_id = 'user_id_example' # str | Optional. Filter by user id, and attach user data (optional)
inherit_from_parent = true # bool | Determines whether or not parent items should be searched for theme media. (optional)

try:
    # Gets theme videos for an item
    api_response = api_instance.get_items_by_id_themevideos(id, user_id=user_id, inherit_from_parent=inherit_from_parent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryServiceApi->get_items_by_id_themevideos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **user_id** | **str**| Optional. Filter by user id, and attach user data | [optional] 
 **inherit_from_parent** | **bool**| Determines whether or not parent items should be searched for theme media. | [optional] 

### Return type

[**ThemeMediaResult**](ThemeMediaResult.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items_counts**
> ItemCounts get_items_counts(user_id=user_id, is_favorite=is_favorite)



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
api_instance = embyapi.LibraryServiceApi(embyapi.ApiClient(configuration))
user_id = 'user_id_example' # str | Optional. Get counts from a specific user's library. (optional)
is_favorite = true # bool | Optional. Get counts of favorite items (optional)

try:
    api_response = api_instance.get_items_counts(user_id=user_id, is_favorite=is_favorite)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryServiceApi->get_items_counts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Optional. Get counts from a specific user&#x27;s library. | [optional] 
 **is_favorite** | **bool**| Optional. Get counts of favorite items | [optional] 

### Return type

[**ItemCounts**](ItemCounts.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_libraries_availableoptions**
> LibraryLibraryOptionsResult get_libraries_availableoptions()



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
api_instance = embyapi.LibraryServiceApi(embyapi.ApiClient(configuration))

try:
    api_response = api_instance.get_libraries_availableoptions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryServiceApi->get_libraries_availableoptions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LibraryLibraryOptionsResult**](LibraryLibraryOptionsResult.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_library_mediafolders**
> QueryResultBaseItemDto get_library_mediafolders(is_hidden=is_hidden)

Gets all user media folders.

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
api_instance = embyapi.LibraryServiceApi(embyapi.ApiClient(configuration))
is_hidden = true # bool | Optional. Filter by folders that are marked hidden, or not. (optional)

try:
    # Gets all user media folders.
    api_response = api_instance.get_library_mediafolders(is_hidden=is_hidden)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryServiceApi->get_library_mediafolders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_hidden** | **bool**| Optional. Filter by folders that are marked hidden, or not. | [optional] 

### Return type

[**QueryResultBaseItemDto**](QueryResultBaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_library_physicalpaths**
> list[str] get_library_physicalpaths()

Gets a list of physical paths from virtual folders

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
api_instance = embyapi.LibraryServiceApi(embyapi.ApiClient(configuration))

try:
    # Gets a list of physical paths from virtual folders
    api_response = api_instance.get_library_physicalpaths()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryServiceApi->get_library_physicalpaths: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_library_selectablemediafolders**
> list[LibraryMediaFolder] get_library_selectablemediafolders()

Gets all user media folders.

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
api_instance = embyapi.LibraryServiceApi(embyapi.ApiClient(configuration))

try:
    # Gets all user media folders.
    api_response = api_instance.get_library_selectablemediafolders()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryServiceApi->get_library_selectablemediafolders: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[LibraryMediaFolder]**](LibraryMediaFolder.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_movies_by_id_similar**
> QueryResultBaseItemDto get_movies_by_id_similar(id, include_item_types=include_item_types, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, user_id=user_id, limit=limit, fields=fields)

Finds movies and trailers similar to a given movie.

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
api_instance = embyapi.LibraryServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Item Id
include_item_types = 'include_item_types_example' # str | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. (optional)
enable_images = true # bool | Optional, include image information in output (optional)
enable_user_data = true # bool | Optional, include user data (optional)
image_type_limit = 56 # int | Optional, the max number of images to return, per image type (optional)
enable_image_types = 'enable_image_types_example' # str | Optional. The image types to include in the output. (optional)
user_id = 'user_id_example' # str | Optional. Filter by user id, and attach user data (optional)
limit = 56 # int | Optional. The maximum number of records to return (optional)
fields = 'fields_example' # str | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls (optional)

try:
    # Finds movies and trailers similar to a given movie.
    api_response = api_instance.get_movies_by_id_similar(id, include_item_types=include_item_types, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, user_id=user_id, limit=limit, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryServiceApi->get_movies_by_id_similar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **include_item_types** | **str**| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. | [optional] 
 **enable_images** | **bool**| Optional, include image information in output | [optional] 
 **enable_user_data** | **bool**| Optional, include user data | [optional] 
 **image_type_limit** | **int**| Optional, the max number of images to return, per image type | [optional] 
 **enable_image_types** | **str**| Optional. The image types to include in the output. | [optional] 
 **user_id** | **str**| Optional. Filter by user id, and attach user data | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return | [optional] 
 **fields** | **str**| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls | [optional] 

### Return type

[**QueryResultBaseItemDto**](QueryResultBaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shows_by_id_similar**
> QueryResultBaseItemDto get_shows_by_id_similar(id, include_item_types=include_item_types, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, user_id=user_id, limit=limit, fields=fields)

Finds tv shows similar to a given one.

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
api_instance = embyapi.LibraryServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Item Id
include_item_types = 'include_item_types_example' # str | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. (optional)
enable_images = true # bool | Optional, include image information in output (optional)
enable_user_data = true # bool | Optional, include user data (optional)
image_type_limit = 56 # int | Optional, the max number of images to return, per image type (optional)
enable_image_types = 'enable_image_types_example' # str | Optional. The image types to include in the output. (optional)
user_id = 'user_id_example' # str | Optional. Filter by user id, and attach user data (optional)
limit = 56 # int | Optional. The maximum number of records to return (optional)
fields = 'fields_example' # str | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls (optional)

try:
    # Finds tv shows similar to a given one.
    api_response = api_instance.get_shows_by_id_similar(id, include_item_types=include_item_types, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, user_id=user_id, limit=limit, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryServiceApi->get_shows_by_id_similar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **include_item_types** | **str**| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. | [optional] 
 **enable_images** | **bool**| Optional, include image information in output | [optional] 
 **enable_user_data** | **bool**| Optional, include user data | [optional] 
 **image_type_limit** | **int**| Optional, the max number of images to return, per image type | [optional] 
 **enable_image_types** | **str**| Optional. The image types to include in the output. | [optional] 
 **user_id** | **str**| Optional. Filter by user id, and attach user data | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return | [optional] 
 **fields** | **str**| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls | [optional] 

### Return type

[**QueryResultBaseItemDto**](QueryResultBaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trailers_by_id_similar**
> QueryResultBaseItemDto get_trailers_by_id_similar(id, include_item_types=include_item_types, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, user_id=user_id, limit=limit, fields=fields)

Finds movies and trailers similar to a given trailer.

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
api_instance = embyapi.LibraryServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Item Id
include_item_types = 'include_item_types_example' # str | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. (optional)
enable_images = true # bool | Optional, include image information in output (optional)
enable_user_data = true # bool | Optional, include user data (optional)
image_type_limit = 56 # int | Optional, the max number of images to return, per image type (optional)
enable_image_types = 'enable_image_types_example' # str | Optional. The image types to include in the output. (optional)
user_id = 'user_id_example' # str | Optional. Filter by user id, and attach user data (optional)
limit = 56 # int | Optional. The maximum number of records to return (optional)
fields = 'fields_example' # str | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls (optional)

try:
    # Finds movies and trailers similar to a given trailer.
    api_response = api_instance.get_trailers_by_id_similar(id, include_item_types=include_item_types, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, user_id=user_id, limit=limit, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryServiceApi->get_trailers_by_id_similar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **include_item_types** | **str**| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. | [optional] 
 **enable_images** | **bool**| Optional, include image information in output | [optional] 
 **enable_user_data** | **bool**| Optional, include user data | [optional] 
 **image_type_limit** | **int**| Optional, the max number of images to return, per image type | [optional] 
 **enable_image_types** | **str**| Optional. The image types to include in the output. | [optional] 
 **user_id** | **str**| Optional. Filter by user id, and attach user data | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return | [optional] 
 **fields** | **str**| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls | [optional] 

### Return type

[**QueryResultBaseItemDto**](QueryResultBaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_library_media_updated**
> post_library_media_updated(body)

Reports that new movies have been added by an external source

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
api_instance = embyapi.LibraryServiceApi(embyapi.ApiClient(configuration))
body = embyapi.LibraryPostUpdatedMedia() # LibraryPostUpdatedMedia | PostUpdatedMedia

try:
    # Reports that new movies have been added by an external source
    api_instance.post_library_media_updated(body)
except ApiException as e:
    print("Exception when calling LibraryServiceApi->post_library_media_updated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LibraryPostUpdatedMedia**](LibraryPostUpdatedMedia.md)| PostUpdatedMedia | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_library_movies_added**
> post_library_movies_added()

Deprecated. Use /Library/Media/Updated

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
api_instance = embyapi.LibraryServiceApi(embyapi.ApiClient(configuration))

try:
    # Deprecated. Use /Library/Media/Updated
    api_instance.post_library_movies_added()
except ApiException as e:
    print("Exception when calling LibraryServiceApi->post_library_movies_added: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_library_movies_updated**
> post_library_movies_updated()

Deprecated. Use /Library/Media/Updated

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
api_instance = embyapi.LibraryServiceApi(embyapi.ApiClient(configuration))

try:
    # Deprecated. Use /Library/Media/Updated
    api_instance.post_library_movies_updated()
except ApiException as e:
    print("Exception when calling LibraryServiceApi->post_library_movies_updated: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_library_refresh**
> post_library_refresh()

Starts a library scan

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
api_instance = embyapi.LibraryServiceApi(embyapi.ApiClient(configuration))

try:
    # Starts a library scan
    api_instance.post_library_refresh()
except ApiException as e:
    print("Exception when calling LibraryServiceApi->post_library_refresh: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_library_series_added**
> post_library_series_added()

Deprecated. Use /Library/Media/Updated

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
api_instance = embyapi.LibraryServiceApi(embyapi.ApiClient(configuration))

try:
    # Deprecated. Use /Library/Media/Updated
    api_instance.post_library_series_added()
except ApiException as e:
    print("Exception when calling LibraryServiceApi->post_library_series_added: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_library_series_updated**
> post_library_series_updated()

Deprecated. Use /Library/Media/Updated

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
api_instance = embyapi.LibraryServiceApi(embyapi.ApiClient(configuration))

try:
    # Deprecated. Use /Library/Media/Updated
    api_instance.post_library_series_updated()
except ApiException as e:
    print("Exception when calling LibraryServiceApi->post_library_series_updated: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

