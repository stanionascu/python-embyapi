# embyapi.PlaylistServiceApi

All URIs are relative to *https://home.ourflix.de:32865/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_playlists_by_id_items**](PlaylistServiceApi.md#delete_playlists_by_id_items) | **DELETE** /Playlists/{Id}/Items | Removes items from a playlist
[**get_playlists_by_id_items**](PlaylistServiceApi.md#get_playlists_by_id_items) | **GET** /Playlists/{Id}/Items | Gets the original items of a playlist
[**post_playlists**](PlaylistServiceApi.md#post_playlists) | **POST** /Playlists | Creates a new playlist
[**post_playlists_by_id_items**](PlaylistServiceApi.md#post_playlists_by_id_items) | **POST** /Playlists/{Id}/Items | Adds items to a playlist
[**post_playlists_by_id_items_by_itemid_move_by_newindex**](PlaylistServiceApi.md#post_playlists_by_id_items_by_itemid_move_by_newindex) | **POST** /Playlists/{Id}/Items/{ItemId}/Move/{NewIndex} | Moves a playlist item

# **delete_playlists_by_id_items**
> delete_playlists_by_id_items(id, entry_ids)

Removes items from a playlist

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
api_instance = embyapi.PlaylistServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | 
entry_ids = 'entry_ids_example' # str | 

try:
    # Removes items from a playlist
    api_instance.delete_playlists_by_id_items(id, entry_ids)
except ApiException as e:
    print("Exception when calling PlaylistServiceApi->delete_playlists_by_id_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **entry_ids** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_playlists_by_id_items**
> QueryResultBaseItemDto get_playlists_by_id_items(id, user_id=user_id, start_index=start_index, limit=limit, fields=fields, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types)

Gets the original items of a playlist

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
api_instance = embyapi.PlaylistServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | 
user_id = 'user_id_example' # str | User Id (optional)
start_index = 56 # int | Optional. The record index to start at. All items with a lower index will be dropped from the results. (optional)
limit = 56 # int | Optional. The maximum number of records to return (optional)
fields = 'fields_example' # str | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines (optional)
enable_images = true # bool | Optional, include image information in output (optional)
enable_user_data = true # bool | Optional, include user data (optional)
image_type_limit = 56 # int | Optional, the max number of images to return, per image type (optional)
enable_image_types = 'enable_image_types_example' # str | Optional. The image types to include in the output. (optional)

try:
    # Gets the original items of a playlist
    api_response = api_instance.get_playlists_by_id_items(id, user_id=user_id, start_index=start_index, limit=limit, fields=fields, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlaylistServiceApi->get_playlists_by_id_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **user_id** | **str**| User Id | [optional] 
 **start_index** | **int**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return | [optional] 
 **fields** | **str**| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines | [optional] 
 **enable_images** | **bool**| Optional, include image information in output | [optional] 
 **enable_user_data** | **bool**| Optional, include user data | [optional] 
 **image_type_limit** | **int**| Optional, the max number of images to return, per image type | [optional] 
 **enable_image_types** | **str**| Optional. The image types to include in the output. | [optional] 

### Return type

[**QueryResultBaseItemDto**](QueryResultBaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_playlists**
> PlaylistsPlaylistCreationResult post_playlists(name=name, ids=ids, media_type=media_type)

Creates a new playlist

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
api_instance = embyapi.PlaylistServiceApi(embyapi.ApiClient(configuration))
name = 'name_example' # str | The name of the new playlist. (optional)
ids = 'ids_example' # str | Item Ids to add to the playlist (optional)
media_type = 'media_type_example' # str | The playlist media type (optional)

try:
    # Creates a new playlist
    api_response = api_instance.post_playlists(name=name, ids=ids, media_type=media_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlaylistServiceApi->post_playlists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the new playlist. | [optional] 
 **ids** | **str**| Item Ids to add to the playlist | [optional] 
 **media_type** | **str**| The playlist media type | [optional] 

### Return type

[**PlaylistsPlaylistCreationResult**](PlaylistsPlaylistCreationResult.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_playlists_by_id_items**
> post_playlists_by_id_items(ids, id, user_id=user_id)

Adds items to a playlist

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
api_instance = embyapi.PlaylistServiceApi(embyapi.ApiClient(configuration))
ids = 'ids_example' # str | Item id, comma delimited
id = 'id_example' # str | 
user_id = 'user_id_example' # str | User Id (optional)

try:
    # Adds items to a playlist
    api_instance.post_playlists_by_id_items(ids, id, user_id=user_id)
except ApiException as e:
    print("Exception when calling PlaylistServiceApi->post_playlists_by_id_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**| Item id, comma delimited | 
 **id** | **str**|  | 
 **user_id** | **str**| User Id | [optional] 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_playlists_by_id_items_by_itemid_move_by_newindex**
> post_playlists_by_id_items_by_itemid_move_by_newindex(item_id, id, new_index)

Moves a playlist item

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
api_instance = embyapi.PlaylistServiceApi(embyapi.ApiClient(configuration))
item_id = 789 # int | ItemId
id = 'id_example' # str | 
new_index = 56 # int | NewIndex

try:
    # Moves a playlist item
    api_instance.post_playlists_by_id_items_by_itemid_move_by_newindex(item_id, id, new_index)
except ApiException as e:
    print("Exception when calling PlaylistServiceApi->post_playlists_by_id_items_by_itemid_move_by_newindex: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**| ItemId | 
 **id** | **str**|  | 
 **new_index** | **int**| NewIndex | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

