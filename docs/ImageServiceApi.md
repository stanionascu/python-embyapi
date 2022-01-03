# embyapi.ImageServiceApi

All URIs are relative to *https://home.ourflix.de:32865/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_items_by_id_images_by_type**](ImageServiceApi.md#delete_items_by_id_images_by_type) | **DELETE** /Items/{Id}/Images/{Type} | 
[**delete_items_by_id_images_by_type_by_index**](ImageServiceApi.md#delete_items_by_id_images_by_type_by_index) | **DELETE** /Items/{Id}/Images/{Type}/{Index} | 
[**delete_users_by_id_images_by_type**](ImageServiceApi.md#delete_users_by_id_images_by_type) | **DELETE** /Users/{Id}/Images/{Type} | 
[**delete_users_by_id_images_by_type_by_index**](ImageServiceApi.md#delete_users_by_id_images_by_type_by_index) | **DELETE** /Users/{Id}/Images/{Type}/{Index} | 
[**get_artists_by_name_images_by_type**](ImageServiceApi.md#get_artists_by_name_images_by_type) | **GET** /Artists/{Name}/Images/{Type} | 
[**get_artists_by_name_images_by_type_by_index**](ImageServiceApi.md#get_artists_by_name_images_by_type_by_index) | **GET** /Artists/{Name}/Images/{Type}/{Index} | 
[**get_gamegenres_by_name_images_by_type**](ImageServiceApi.md#get_gamegenres_by_name_images_by_type) | **GET** /GameGenres/{Name}/Images/{Type} | 
[**get_gamegenres_by_name_images_by_type_by_index**](ImageServiceApi.md#get_gamegenres_by_name_images_by_type_by_index) | **GET** /GameGenres/{Name}/Images/{Type}/{Index} | 
[**get_genres_by_name_images_by_type**](ImageServiceApi.md#get_genres_by_name_images_by_type) | **GET** /Genres/{Name}/Images/{Type} | 
[**get_genres_by_name_images_by_type_by_index**](ImageServiceApi.md#get_genres_by_name_images_by_type_by_index) | **GET** /Genres/{Name}/Images/{Type}/{Index} | 
[**get_items_by_id_images**](ImageServiceApi.md#get_items_by_id_images) | **GET** /Items/{Id}/Images | Gets information about an item&#x27;s images
[**get_items_by_id_images_by_type**](ImageServiceApi.md#get_items_by_id_images_by_type) | **GET** /Items/{Id}/Images/{Type} | 
[**get_items_by_id_images_by_type_by_index**](ImageServiceApi.md#get_items_by_id_images_by_type_by_index) | **GET** /Items/{Id}/Images/{Type}/{Index} | 
[**get_items_by_id_images_by_type_by_index_by_tag_by_format_by_maxwidth_by_maxheight_by_percentplayed_by_unplayedcount**](ImageServiceApi.md#get_items_by_id_images_by_type_by_index_by_tag_by_format_by_maxwidth_by_maxheight_by_percentplayed_by_unplayedcount) | **GET** /Items/{Id}/Images/{Type}/{Index}/{Tag}/{Format}/{MaxWidth}/{MaxHeight}/{PercentPlayed}/{UnplayedCount} | 
[**get_musicgenres_by_name_images_by_type**](ImageServiceApi.md#get_musicgenres_by_name_images_by_type) | **GET** /MusicGenres/{Name}/Images/{Type} | 
[**get_musicgenres_by_name_images_by_type_by_index**](ImageServiceApi.md#get_musicgenres_by_name_images_by_type_by_index) | **GET** /MusicGenres/{Name}/Images/{Type}/{Index} | 
[**get_persons_by_name_images_by_type**](ImageServiceApi.md#get_persons_by_name_images_by_type) | **GET** /Persons/{Name}/Images/{Type} | 
[**get_persons_by_name_images_by_type_by_index**](ImageServiceApi.md#get_persons_by_name_images_by_type_by_index) | **GET** /Persons/{Name}/Images/{Type}/{Index} | 
[**get_studios_by_name_images_by_type**](ImageServiceApi.md#get_studios_by_name_images_by_type) | **GET** /Studios/{Name}/Images/{Type} | 
[**get_studios_by_name_images_by_type_by_index**](ImageServiceApi.md#get_studios_by_name_images_by_type_by_index) | **GET** /Studios/{Name}/Images/{Type}/{Index} | 
[**get_users_by_id_images_by_type**](ImageServiceApi.md#get_users_by_id_images_by_type) | **GET** /Users/{Id}/Images/{Type} | 
[**get_users_by_id_images_by_type_by_index**](ImageServiceApi.md#get_users_by_id_images_by_type_by_index) | **GET** /Users/{Id}/Images/{Type}/{Index} | 
[**head_artists_by_name_images_by_type**](ImageServiceApi.md#head_artists_by_name_images_by_type) | **HEAD** /Artists/{Name}/Images/{Type} | 
[**head_artists_by_name_images_by_type_by_index**](ImageServiceApi.md#head_artists_by_name_images_by_type_by_index) | **HEAD** /Artists/{Name}/Images/{Type}/{Index} | 
[**head_gamegenres_by_name_images_by_type**](ImageServiceApi.md#head_gamegenres_by_name_images_by_type) | **HEAD** /GameGenres/{Name}/Images/{Type} | 
[**head_gamegenres_by_name_images_by_type_by_index**](ImageServiceApi.md#head_gamegenres_by_name_images_by_type_by_index) | **HEAD** /GameGenres/{Name}/Images/{Type}/{Index} | 
[**head_genres_by_name_images_by_type**](ImageServiceApi.md#head_genres_by_name_images_by_type) | **HEAD** /Genres/{Name}/Images/{Type} | 
[**head_genres_by_name_images_by_type_by_index**](ImageServiceApi.md#head_genres_by_name_images_by_type_by_index) | **HEAD** /Genres/{Name}/Images/{Type}/{Index} | 
[**head_items_by_id_images_by_type**](ImageServiceApi.md#head_items_by_id_images_by_type) | **HEAD** /Items/{Id}/Images/{Type} | 
[**head_items_by_id_images_by_type_by_index**](ImageServiceApi.md#head_items_by_id_images_by_type_by_index) | **HEAD** /Items/{Id}/Images/{Type}/{Index} | 
[**head_items_by_id_images_by_type_by_index_by_tag_by_format_by_maxwidth_by_maxheight_by_percentplayed_by_unplayedcount**](ImageServiceApi.md#head_items_by_id_images_by_type_by_index_by_tag_by_format_by_maxwidth_by_maxheight_by_percentplayed_by_unplayedcount) | **HEAD** /Items/{Id}/Images/{Type}/{Index}/{Tag}/{Format}/{MaxWidth}/{MaxHeight}/{PercentPlayed}/{UnplayedCount} | 
[**head_musicgenres_by_name_images_by_type**](ImageServiceApi.md#head_musicgenres_by_name_images_by_type) | **HEAD** /MusicGenres/{Name}/Images/{Type} | 
[**head_musicgenres_by_name_images_by_type_by_index**](ImageServiceApi.md#head_musicgenres_by_name_images_by_type_by_index) | **HEAD** /MusicGenres/{Name}/Images/{Type}/{Index} | 
[**head_persons_by_name_images_by_type**](ImageServiceApi.md#head_persons_by_name_images_by_type) | **HEAD** /Persons/{Name}/Images/{Type} | 
[**head_persons_by_name_images_by_type_by_index**](ImageServiceApi.md#head_persons_by_name_images_by_type_by_index) | **HEAD** /Persons/{Name}/Images/{Type}/{Index} | 
[**head_studios_by_name_images_by_type**](ImageServiceApi.md#head_studios_by_name_images_by_type) | **HEAD** /Studios/{Name}/Images/{Type} | 
[**head_studios_by_name_images_by_type_by_index**](ImageServiceApi.md#head_studios_by_name_images_by_type_by_index) | **HEAD** /Studios/{Name}/Images/{Type}/{Index} | 
[**head_users_by_id_images_by_type**](ImageServiceApi.md#head_users_by_id_images_by_type) | **HEAD** /Users/{Id}/Images/{Type} | 
[**head_users_by_id_images_by_type_by_index**](ImageServiceApi.md#head_users_by_id_images_by_type_by_index) | **HEAD** /Users/{Id}/Images/{Type}/{Index} | 
[**post_items_by_id_images_by_type**](ImageServiceApi.md#post_items_by_id_images_by_type) | **POST** /Items/{Id}/Images/{Type} | 
[**post_items_by_id_images_by_type_by_index**](ImageServiceApi.md#post_items_by_id_images_by_type_by_index) | **POST** /Items/{Id}/Images/{Type}/{Index} | 
[**post_items_by_id_images_by_type_by_index_index**](ImageServiceApi.md#post_items_by_id_images_by_type_by_index_index) | **POST** /Items/{Id}/Images/{Type}/{Index}/Index | Updates the index for an item image
[**post_users_by_id_images_by_type**](ImageServiceApi.md#post_users_by_id_images_by_type) | **POST** /Users/{Id}/Images/{Type} | 
[**post_users_by_id_images_by_type_by_index**](ImageServiceApi.md#post_users_by_id_images_by_type_by_index) | **POST** /Users/{Id}/Images/{Type}/{Index} | 

# **delete_items_by_id_images_by_type**
> delete_items_by_id_images_by_type(id, type, index=index)



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
api_instance = embyapi.ImageServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Item Id
type = 'type_example' # str | Image Type
index = 56 # int | Image Index (optional)

try:
    api_instance.delete_items_by_id_images_by_type(id, type, index=index)
except ApiException as e:
    print("Exception when calling ImageServiceApi->delete_items_by_id_images_by_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **type** | **str**| Image Type | 
 **index** | **int**| Image Index | [optional] 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_items_by_id_images_by_type_by_index**
> delete_items_by_id_images_by_type_by_index(id, type, index)



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
api_instance = embyapi.ImageServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Item Id
type = 'type_example' # str | Image Type
index = 56 # int | Image Index

try:
    api_instance.delete_items_by_id_images_by_type_by_index(id, type, index)
except ApiException as e:
    print("Exception when calling ImageServiceApi->delete_items_by_id_images_by_type_by_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **type** | **str**| Image Type | 
 **index** | **int**| Image Index | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_users_by_id_images_by_type**
> delete_users_by_id_images_by_type(id, type, index=index)



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
api_instance = embyapi.ImageServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | User Id
type = 'type_example' # str | Image Type
index = 56 # int | Image Index (optional)

try:
    api_instance.delete_users_by_id_images_by_type(id, type, index=index)
except ApiException as e:
    print("Exception when calling ImageServiceApi->delete_users_by_id_images_by_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User Id | 
 **type** | **str**| Image Type | 
 **index** | **int**| Image Index | [optional] 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_users_by_id_images_by_type_by_index**
> delete_users_by_id_images_by_type_by_index(id, type, index)



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
api_instance = embyapi.ImageServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | User Id
type = 'type_example' # str | Image Type
index = 56 # int | Image Index

try:
    api_instance.delete_users_by_id_images_by_type_by_index(id, type, index)
except ApiException as e:
    print("Exception when calling ImageServiceApi->delete_users_by_id_images_by_type_by_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User Id | 
 **type** | **str**| Image Type | 
 **index** | **int**| Image Index | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artists_by_name_images_by_type**
> get_artists_by_name_images_by_type(name, type, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer, index=index)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.ImageServiceApi()
name = 'name_example' # str | Item name
type = 'type_example' # str | Image Type
max_width = 56 # int | The maximum image width to return. (optional)
max_height = 56 # int | The maximum image height to return. (optional)
width = 56 # int | The fixed image width to return. (optional)
height = 56 # int | The fixed image height to return. (optional)
quality = 56 # int | Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
crop_whitespace = true # bool | Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. (optional)
enable_image_enhancers = true # bool | Enable or disable image enhancers such as cover art. (optional)
format = 'format_example' # str | Determines the output foramt of the image - original,gif,jpg,png (optional)
add_played_indicator = true # bool | Optional. Add a played indicator (optional)
percent_played = 1.2 # float | Optional percent to render for the percent played overlay (optional)
unplayed_count = 56 # int | Optional unplayed count overlay to render (optional)
background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)
index = 56 # int | Image Index (optional)

try:
    api_instance.get_artists_by_name_images_by_type(name, type, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer, index=index)
except ApiException as e:
    print("Exception when calling ImageServiceApi->get_artists_by_name_images_by_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Item name | 
 **type** | **str**| Image Type | 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **crop_whitespace** | **bool**| Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **enable_image_enhancers** | **bool**| Enable or disable image enhancers such as cover art. | [optional] 
 **format** | **str**| Determines the output foramt of the image - original,gif,jpg,png | [optional] 
 **add_played_indicator** | **bool**| Optional. Add a played indicator | [optional] 
 **percent_played** | **float**| Optional percent to render for the percent played overlay | [optional] 
 **unplayed_count** | **int**| Optional unplayed count overlay to render | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 
 **index** | **int**| Image Index | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artists_by_name_images_by_type_by_index**
> get_artists_by_name_images_by_type_by_index(name, type, index, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.ImageServiceApi()
name = 'name_example' # str | Item name
type = 'type_example' # str | Image Type
index = 56 # int | Image Index
max_width = 56 # int | The maximum image width to return. (optional)
max_height = 56 # int | The maximum image height to return. (optional)
width = 56 # int | The fixed image width to return. (optional)
height = 56 # int | The fixed image height to return. (optional)
quality = 56 # int | Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
crop_whitespace = true # bool | Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. (optional)
enable_image_enhancers = true # bool | Enable or disable image enhancers such as cover art. (optional)
format = 'format_example' # str | Determines the output foramt of the image - original,gif,jpg,png (optional)
add_played_indicator = true # bool | Optional. Add a played indicator (optional)
percent_played = 1.2 # float | Optional percent to render for the percent played overlay (optional)
unplayed_count = 56 # int | Optional unplayed count overlay to render (optional)
background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)

try:
    api_instance.get_artists_by_name_images_by_type_by_index(name, type, index, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer)
except ApiException as e:
    print("Exception when calling ImageServiceApi->get_artists_by_name_images_by_type_by_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Item name | 
 **type** | **str**| Image Type | 
 **index** | **int**| Image Index | 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **crop_whitespace** | **bool**| Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **enable_image_enhancers** | **bool**| Enable or disable image enhancers such as cover art. | [optional] 
 **format** | **str**| Determines the output foramt of the image - original,gif,jpg,png | [optional] 
 **add_played_indicator** | **bool**| Optional. Add a played indicator | [optional] 
 **percent_played** | **float**| Optional percent to render for the percent played overlay | [optional] 
 **unplayed_count** | **int**| Optional unplayed count overlay to render | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gamegenres_by_name_images_by_type**
> get_gamegenres_by_name_images_by_type(name, type, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer, index=index)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.ImageServiceApi()
name = 'name_example' # str | Item name
type = 'type_example' # str | Image Type
max_width = 56 # int | The maximum image width to return. (optional)
max_height = 56 # int | The maximum image height to return. (optional)
width = 56 # int | The fixed image width to return. (optional)
height = 56 # int | The fixed image height to return. (optional)
quality = 56 # int | Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
crop_whitespace = true # bool | Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. (optional)
enable_image_enhancers = true # bool | Enable or disable image enhancers such as cover art. (optional)
format = 'format_example' # str | Determines the output foramt of the image - original,gif,jpg,png (optional)
add_played_indicator = true # bool | Optional. Add a played indicator (optional)
percent_played = 1.2 # float | Optional percent to render for the percent played overlay (optional)
unplayed_count = 56 # int | Optional unplayed count overlay to render (optional)
background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)
index = 56 # int | Image Index (optional)

try:
    api_instance.get_gamegenres_by_name_images_by_type(name, type, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer, index=index)
except ApiException as e:
    print("Exception when calling ImageServiceApi->get_gamegenres_by_name_images_by_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Item name | 
 **type** | **str**| Image Type | 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **crop_whitespace** | **bool**| Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **enable_image_enhancers** | **bool**| Enable or disable image enhancers such as cover art. | [optional] 
 **format** | **str**| Determines the output foramt of the image - original,gif,jpg,png | [optional] 
 **add_played_indicator** | **bool**| Optional. Add a played indicator | [optional] 
 **percent_played** | **float**| Optional percent to render for the percent played overlay | [optional] 
 **unplayed_count** | **int**| Optional unplayed count overlay to render | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 
 **index** | **int**| Image Index | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gamegenres_by_name_images_by_type_by_index**
> get_gamegenres_by_name_images_by_type_by_index(name, type, index, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.ImageServiceApi()
name = 'name_example' # str | Item name
type = 'type_example' # str | Image Type
index = 56 # int | Image Index
max_width = 56 # int | The maximum image width to return. (optional)
max_height = 56 # int | The maximum image height to return. (optional)
width = 56 # int | The fixed image width to return. (optional)
height = 56 # int | The fixed image height to return. (optional)
quality = 56 # int | Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
crop_whitespace = true # bool | Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. (optional)
enable_image_enhancers = true # bool | Enable or disable image enhancers such as cover art. (optional)
format = 'format_example' # str | Determines the output foramt of the image - original,gif,jpg,png (optional)
add_played_indicator = true # bool | Optional. Add a played indicator (optional)
percent_played = 1.2 # float | Optional percent to render for the percent played overlay (optional)
unplayed_count = 56 # int | Optional unplayed count overlay to render (optional)
background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)

try:
    api_instance.get_gamegenres_by_name_images_by_type_by_index(name, type, index, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer)
except ApiException as e:
    print("Exception when calling ImageServiceApi->get_gamegenres_by_name_images_by_type_by_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Item name | 
 **type** | **str**| Image Type | 
 **index** | **int**| Image Index | 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **crop_whitespace** | **bool**| Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **enable_image_enhancers** | **bool**| Enable or disable image enhancers such as cover art. | [optional] 
 **format** | **str**| Determines the output foramt of the image - original,gif,jpg,png | [optional] 
 **add_played_indicator** | **bool**| Optional. Add a played indicator | [optional] 
 **percent_played** | **float**| Optional percent to render for the percent played overlay | [optional] 
 **unplayed_count** | **int**| Optional unplayed count overlay to render | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_genres_by_name_images_by_type**
> get_genres_by_name_images_by_type(name, type, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer, index=index)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.ImageServiceApi()
name = 'name_example' # str | Item name
type = 'type_example' # str | Image Type
max_width = 56 # int | The maximum image width to return. (optional)
max_height = 56 # int | The maximum image height to return. (optional)
width = 56 # int | The fixed image width to return. (optional)
height = 56 # int | The fixed image height to return. (optional)
quality = 56 # int | Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
crop_whitespace = true # bool | Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. (optional)
enable_image_enhancers = true # bool | Enable or disable image enhancers such as cover art. (optional)
format = 'format_example' # str | Determines the output foramt of the image - original,gif,jpg,png (optional)
add_played_indicator = true # bool | Optional. Add a played indicator (optional)
percent_played = 1.2 # float | Optional percent to render for the percent played overlay (optional)
unplayed_count = 56 # int | Optional unplayed count overlay to render (optional)
background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)
index = 56 # int | Image Index (optional)

try:
    api_instance.get_genres_by_name_images_by_type(name, type, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer, index=index)
except ApiException as e:
    print("Exception when calling ImageServiceApi->get_genres_by_name_images_by_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Item name | 
 **type** | **str**| Image Type | 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **crop_whitespace** | **bool**| Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **enable_image_enhancers** | **bool**| Enable or disable image enhancers such as cover art. | [optional] 
 **format** | **str**| Determines the output foramt of the image - original,gif,jpg,png | [optional] 
 **add_played_indicator** | **bool**| Optional. Add a played indicator | [optional] 
 **percent_played** | **float**| Optional percent to render for the percent played overlay | [optional] 
 **unplayed_count** | **int**| Optional unplayed count overlay to render | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 
 **index** | **int**| Image Index | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_genres_by_name_images_by_type_by_index**
> get_genres_by_name_images_by_type_by_index(name, type, index, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.ImageServiceApi()
name = 'name_example' # str | Item name
type = 'type_example' # str | Image Type
index = 56 # int | Image Index
max_width = 56 # int | The maximum image width to return. (optional)
max_height = 56 # int | The maximum image height to return. (optional)
width = 56 # int | The fixed image width to return. (optional)
height = 56 # int | The fixed image height to return. (optional)
quality = 56 # int | Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
crop_whitespace = true # bool | Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. (optional)
enable_image_enhancers = true # bool | Enable or disable image enhancers such as cover art. (optional)
format = 'format_example' # str | Determines the output foramt of the image - original,gif,jpg,png (optional)
add_played_indicator = true # bool | Optional. Add a played indicator (optional)
percent_played = 1.2 # float | Optional percent to render for the percent played overlay (optional)
unplayed_count = 56 # int | Optional unplayed count overlay to render (optional)
background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)

try:
    api_instance.get_genres_by_name_images_by_type_by_index(name, type, index, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer)
except ApiException as e:
    print("Exception when calling ImageServiceApi->get_genres_by_name_images_by_type_by_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Item name | 
 **type** | **str**| Image Type | 
 **index** | **int**| Image Index | 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **crop_whitespace** | **bool**| Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **enable_image_enhancers** | **bool**| Enable or disable image enhancers such as cover art. | [optional] 
 **format** | **str**| Determines the output foramt of the image - original,gif,jpg,png | [optional] 
 **add_played_indicator** | **bool**| Optional. Add a played indicator | [optional] 
 **percent_played** | **float**| Optional percent to render for the percent played overlay | [optional] 
 **unplayed_count** | **int**| Optional unplayed count overlay to render | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items_by_id_images**
> list[ImageInfo] get_items_by_id_images(id)

Gets information about an item's images

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
api_instance = embyapi.ImageServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Item Id

try:
    # Gets information about an item's images
    api_response = api_instance.get_items_by_id_images(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageServiceApi->get_items_by_id_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 

### Return type

[**list[ImageInfo]**](ImageInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items_by_id_images_by_type**
> get_items_by_id_images_by_type(id, type, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer, index=index)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.ImageServiceApi()
id = 'id_example' # str | Item Id
type = 'type_example' # str | Image Type
max_width = 56 # int | The maximum image width to return. (optional)
max_height = 56 # int | The maximum image height to return. (optional)
width = 56 # int | The fixed image width to return. (optional)
height = 56 # int | The fixed image height to return. (optional)
quality = 56 # int | Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
crop_whitespace = true # bool | Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. (optional)
enable_image_enhancers = true # bool | Enable or disable image enhancers such as cover art. (optional)
format = 'format_example' # str | Determines the output foramt of the image - original,gif,jpg,png (optional)
add_played_indicator = true # bool | Optional. Add a played indicator (optional)
percent_played = 1.2 # float | Optional percent to render for the percent played overlay (optional)
unplayed_count = 56 # int | Optional unplayed count overlay to render (optional)
background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)
index = 56 # int | Image Index (optional)

try:
    api_instance.get_items_by_id_images_by_type(id, type, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer, index=index)
except ApiException as e:
    print("Exception when calling ImageServiceApi->get_items_by_id_images_by_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **type** | **str**| Image Type | 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **crop_whitespace** | **bool**| Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **enable_image_enhancers** | **bool**| Enable or disable image enhancers such as cover art. | [optional] 
 **format** | **str**| Determines the output foramt of the image - original,gif,jpg,png | [optional] 
 **add_played_indicator** | **bool**| Optional. Add a played indicator | [optional] 
 **percent_played** | **float**| Optional percent to render for the percent played overlay | [optional] 
 **unplayed_count** | **int**| Optional unplayed count overlay to render | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 
 **index** | **int**| Image Index | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items_by_id_images_by_type_by_index**
> get_items_by_id_images_by_type_by_index(id, type, index, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.ImageServiceApi()
id = 'id_example' # str | Item Id
type = 'type_example' # str | Image Type
index = 56 # int | Image Index
max_width = 56 # int | The maximum image width to return. (optional)
max_height = 56 # int | The maximum image height to return. (optional)
width = 56 # int | The fixed image width to return. (optional)
height = 56 # int | The fixed image height to return. (optional)
quality = 56 # int | Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
crop_whitespace = true # bool | Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. (optional)
enable_image_enhancers = true # bool | Enable or disable image enhancers such as cover art. (optional)
format = 'format_example' # str | Determines the output foramt of the image - original,gif,jpg,png (optional)
add_played_indicator = true # bool | Optional. Add a played indicator (optional)
percent_played = 1.2 # float | Optional percent to render for the percent played overlay (optional)
unplayed_count = 56 # int | Optional unplayed count overlay to render (optional)
background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)

try:
    api_instance.get_items_by_id_images_by_type_by_index(id, type, index, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer)
except ApiException as e:
    print("Exception when calling ImageServiceApi->get_items_by_id_images_by_type_by_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **type** | **str**| Image Type | 
 **index** | **int**| Image Index | 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **crop_whitespace** | **bool**| Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **enable_image_enhancers** | **bool**| Enable or disable image enhancers such as cover art. | [optional] 
 **format** | **str**| Determines the output foramt of the image - original,gif,jpg,png | [optional] 
 **add_played_indicator** | **bool**| Optional. Add a played indicator | [optional] 
 **percent_played** | **float**| Optional percent to render for the percent played overlay | [optional] 
 **unplayed_count** | **int**| Optional unplayed count overlay to render | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items_by_id_images_by_type_by_index_by_tag_by_format_by_maxwidth_by_maxheight_by_percentplayed_by_unplayedcount**
> get_items_by_id_images_by_type_by_index_by_tag_by_format_by_maxwidth_by_maxheight_by_percentplayed_by_unplayedcount(id, max_width, max_height, tag, format, percent_played, unplayed_count, type, index, width=width, height=height, quality=quality, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, add_played_indicator=add_played_indicator, background_color=background_color, foreground_layer=foreground_layer)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.ImageServiceApi()
id = 'id_example' # str | Item Id
max_width = 56 # int | The maximum image width to return.
max_height = 56 # int | The maximum image height to return.
tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers.
format = 'format_example' # str | Determines the output foramt of the image - original,gif,jpg,png
percent_played = 1.2 # float | Optional percent to render for the percent played overlay
unplayed_count = 56 # int | Optional unplayed count overlay to render
type = 'type_example' # str | Image Type
index = 56 # int | Image Index
width = 56 # int | The fixed image width to return. (optional)
height = 56 # int | The fixed image height to return. (optional)
quality = 56 # int | Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
crop_whitespace = true # bool | Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. (optional)
enable_image_enhancers = true # bool | Enable or disable image enhancers such as cover art. (optional)
add_played_indicator = true # bool | Optional. Add a played indicator (optional)
background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)

try:
    api_instance.get_items_by_id_images_by_type_by_index_by_tag_by_format_by_maxwidth_by_maxheight_by_percentplayed_by_unplayedcount(id, max_width, max_height, tag, format, percent_played, unplayed_count, type, index, width=width, height=height, quality=quality, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, add_played_indicator=add_played_indicator, background_color=background_color, foreground_layer=foreground_layer)
except ApiException as e:
    print("Exception when calling ImageServiceApi->get_items_by_id_images_by_type_by_index_by_tag_by_format_by_maxwidth_by_maxheight_by_percentplayed_by_unplayedcount: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **max_width** | **int**| The maximum image width to return. | 
 **max_height** | **int**| The maximum image height to return. | 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | 
 **format** | **str**| Determines the output foramt of the image - original,gif,jpg,png | 
 **percent_played** | **float**| Optional percent to render for the percent played overlay | 
 **unplayed_count** | **int**| Optional unplayed count overlay to render | 
 **type** | **str**| Image Type | 
 **index** | **int**| Image Index | 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **crop_whitespace** | **bool**| Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **enable_image_enhancers** | **bool**| Enable or disable image enhancers such as cover art. | [optional] 
 **add_played_indicator** | **bool**| Optional. Add a played indicator | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_musicgenres_by_name_images_by_type**
> get_musicgenres_by_name_images_by_type(name, type, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer, index=index)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.ImageServiceApi()
name = 'name_example' # str | Item name
type = 'type_example' # str | Image Type
max_width = 56 # int | The maximum image width to return. (optional)
max_height = 56 # int | The maximum image height to return. (optional)
width = 56 # int | The fixed image width to return. (optional)
height = 56 # int | The fixed image height to return. (optional)
quality = 56 # int | Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
crop_whitespace = true # bool | Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. (optional)
enable_image_enhancers = true # bool | Enable or disable image enhancers such as cover art. (optional)
format = 'format_example' # str | Determines the output foramt of the image - original,gif,jpg,png (optional)
add_played_indicator = true # bool | Optional. Add a played indicator (optional)
percent_played = 1.2 # float | Optional percent to render for the percent played overlay (optional)
unplayed_count = 56 # int | Optional unplayed count overlay to render (optional)
background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)
index = 56 # int | Image Index (optional)

try:
    api_instance.get_musicgenres_by_name_images_by_type(name, type, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer, index=index)
except ApiException as e:
    print("Exception when calling ImageServiceApi->get_musicgenres_by_name_images_by_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Item name | 
 **type** | **str**| Image Type | 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **crop_whitespace** | **bool**| Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **enable_image_enhancers** | **bool**| Enable or disable image enhancers such as cover art. | [optional] 
 **format** | **str**| Determines the output foramt of the image - original,gif,jpg,png | [optional] 
 **add_played_indicator** | **bool**| Optional. Add a played indicator | [optional] 
 **percent_played** | **float**| Optional percent to render for the percent played overlay | [optional] 
 **unplayed_count** | **int**| Optional unplayed count overlay to render | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 
 **index** | **int**| Image Index | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_musicgenres_by_name_images_by_type_by_index**
> get_musicgenres_by_name_images_by_type_by_index(name, type, index, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.ImageServiceApi()
name = 'name_example' # str | Item name
type = 'type_example' # str | Image Type
index = 56 # int | Image Index
max_width = 56 # int | The maximum image width to return. (optional)
max_height = 56 # int | The maximum image height to return. (optional)
width = 56 # int | The fixed image width to return. (optional)
height = 56 # int | The fixed image height to return. (optional)
quality = 56 # int | Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
crop_whitespace = true # bool | Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. (optional)
enable_image_enhancers = true # bool | Enable or disable image enhancers such as cover art. (optional)
format = 'format_example' # str | Determines the output foramt of the image - original,gif,jpg,png (optional)
add_played_indicator = true # bool | Optional. Add a played indicator (optional)
percent_played = 1.2 # float | Optional percent to render for the percent played overlay (optional)
unplayed_count = 56 # int | Optional unplayed count overlay to render (optional)
background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)

try:
    api_instance.get_musicgenres_by_name_images_by_type_by_index(name, type, index, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer)
except ApiException as e:
    print("Exception when calling ImageServiceApi->get_musicgenres_by_name_images_by_type_by_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Item name | 
 **type** | **str**| Image Type | 
 **index** | **int**| Image Index | 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **crop_whitespace** | **bool**| Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **enable_image_enhancers** | **bool**| Enable or disable image enhancers such as cover art. | [optional] 
 **format** | **str**| Determines the output foramt of the image - original,gif,jpg,png | [optional] 
 **add_played_indicator** | **bool**| Optional. Add a played indicator | [optional] 
 **percent_played** | **float**| Optional percent to render for the percent played overlay | [optional] 
 **unplayed_count** | **int**| Optional unplayed count overlay to render | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_persons_by_name_images_by_type**
> get_persons_by_name_images_by_type(name, type, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer, index=index)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.ImageServiceApi()
name = 'name_example' # str | Item name
type = 'type_example' # str | Image Type
max_width = 56 # int | The maximum image width to return. (optional)
max_height = 56 # int | The maximum image height to return. (optional)
width = 56 # int | The fixed image width to return. (optional)
height = 56 # int | The fixed image height to return. (optional)
quality = 56 # int | Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
crop_whitespace = true # bool | Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. (optional)
enable_image_enhancers = true # bool | Enable or disable image enhancers such as cover art. (optional)
format = 'format_example' # str | Determines the output foramt of the image - original,gif,jpg,png (optional)
add_played_indicator = true # bool | Optional. Add a played indicator (optional)
percent_played = 1.2 # float | Optional percent to render for the percent played overlay (optional)
unplayed_count = 56 # int | Optional unplayed count overlay to render (optional)
background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)
index = 56 # int | Image Index (optional)

try:
    api_instance.get_persons_by_name_images_by_type(name, type, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer, index=index)
except ApiException as e:
    print("Exception when calling ImageServiceApi->get_persons_by_name_images_by_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Item name | 
 **type** | **str**| Image Type | 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **crop_whitespace** | **bool**| Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **enable_image_enhancers** | **bool**| Enable or disable image enhancers such as cover art. | [optional] 
 **format** | **str**| Determines the output foramt of the image - original,gif,jpg,png | [optional] 
 **add_played_indicator** | **bool**| Optional. Add a played indicator | [optional] 
 **percent_played** | **float**| Optional percent to render for the percent played overlay | [optional] 
 **unplayed_count** | **int**| Optional unplayed count overlay to render | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 
 **index** | **int**| Image Index | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_persons_by_name_images_by_type_by_index**
> get_persons_by_name_images_by_type_by_index(name, type, index, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.ImageServiceApi()
name = 'name_example' # str | Item name
type = 'type_example' # str | Image Type
index = 56 # int | Image Index
max_width = 56 # int | The maximum image width to return. (optional)
max_height = 56 # int | The maximum image height to return. (optional)
width = 56 # int | The fixed image width to return. (optional)
height = 56 # int | The fixed image height to return. (optional)
quality = 56 # int | Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
crop_whitespace = true # bool | Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. (optional)
enable_image_enhancers = true # bool | Enable or disable image enhancers such as cover art. (optional)
format = 'format_example' # str | Determines the output foramt of the image - original,gif,jpg,png (optional)
add_played_indicator = true # bool | Optional. Add a played indicator (optional)
percent_played = 1.2 # float | Optional percent to render for the percent played overlay (optional)
unplayed_count = 56 # int | Optional unplayed count overlay to render (optional)
background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)

try:
    api_instance.get_persons_by_name_images_by_type_by_index(name, type, index, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer)
except ApiException as e:
    print("Exception when calling ImageServiceApi->get_persons_by_name_images_by_type_by_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Item name | 
 **type** | **str**| Image Type | 
 **index** | **int**| Image Index | 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **crop_whitespace** | **bool**| Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **enable_image_enhancers** | **bool**| Enable or disable image enhancers such as cover art. | [optional] 
 **format** | **str**| Determines the output foramt of the image - original,gif,jpg,png | [optional] 
 **add_played_indicator** | **bool**| Optional. Add a played indicator | [optional] 
 **percent_played** | **float**| Optional percent to render for the percent played overlay | [optional] 
 **unplayed_count** | **int**| Optional unplayed count overlay to render | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_studios_by_name_images_by_type**
> get_studios_by_name_images_by_type(name, type, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer, index=index)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.ImageServiceApi()
name = 'name_example' # str | Item name
type = 'type_example' # str | Image Type
max_width = 56 # int | The maximum image width to return. (optional)
max_height = 56 # int | The maximum image height to return. (optional)
width = 56 # int | The fixed image width to return. (optional)
height = 56 # int | The fixed image height to return. (optional)
quality = 56 # int | Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
crop_whitespace = true # bool | Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. (optional)
enable_image_enhancers = true # bool | Enable or disable image enhancers such as cover art. (optional)
format = 'format_example' # str | Determines the output foramt of the image - original,gif,jpg,png (optional)
add_played_indicator = true # bool | Optional. Add a played indicator (optional)
percent_played = 1.2 # float | Optional percent to render for the percent played overlay (optional)
unplayed_count = 56 # int | Optional unplayed count overlay to render (optional)
background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)
index = 56 # int | Image Index (optional)

try:
    api_instance.get_studios_by_name_images_by_type(name, type, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer, index=index)
except ApiException as e:
    print("Exception when calling ImageServiceApi->get_studios_by_name_images_by_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Item name | 
 **type** | **str**| Image Type | 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **crop_whitespace** | **bool**| Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **enable_image_enhancers** | **bool**| Enable or disable image enhancers such as cover art. | [optional] 
 **format** | **str**| Determines the output foramt of the image - original,gif,jpg,png | [optional] 
 **add_played_indicator** | **bool**| Optional. Add a played indicator | [optional] 
 **percent_played** | **float**| Optional percent to render for the percent played overlay | [optional] 
 **unplayed_count** | **int**| Optional unplayed count overlay to render | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 
 **index** | **int**| Image Index | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_studios_by_name_images_by_type_by_index**
> get_studios_by_name_images_by_type_by_index(name, type, index, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.ImageServiceApi()
name = 'name_example' # str | Item name
type = 'type_example' # str | Image Type
index = 56 # int | Image Index
max_width = 56 # int | The maximum image width to return. (optional)
max_height = 56 # int | The maximum image height to return. (optional)
width = 56 # int | The fixed image width to return. (optional)
height = 56 # int | The fixed image height to return. (optional)
quality = 56 # int | Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
crop_whitespace = true # bool | Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. (optional)
enable_image_enhancers = true # bool | Enable or disable image enhancers such as cover art. (optional)
format = 'format_example' # str | Determines the output foramt of the image - original,gif,jpg,png (optional)
add_played_indicator = true # bool | Optional. Add a played indicator (optional)
percent_played = 1.2 # float | Optional percent to render for the percent played overlay (optional)
unplayed_count = 56 # int | Optional unplayed count overlay to render (optional)
background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)

try:
    api_instance.get_studios_by_name_images_by_type_by_index(name, type, index, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer)
except ApiException as e:
    print("Exception when calling ImageServiceApi->get_studios_by_name_images_by_type_by_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Item name | 
 **type** | **str**| Image Type | 
 **index** | **int**| Image Index | 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **crop_whitespace** | **bool**| Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **enable_image_enhancers** | **bool**| Enable or disable image enhancers such as cover art. | [optional] 
 **format** | **str**| Determines the output foramt of the image - original,gif,jpg,png | [optional] 
 **add_played_indicator** | **bool**| Optional. Add a played indicator | [optional] 
 **percent_played** | **float**| Optional percent to render for the percent played overlay | [optional] 
 **unplayed_count** | **int**| Optional unplayed count overlay to render | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_by_id_images_by_type**
> get_users_by_id_images_by_type(id, type, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer, index=index)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.ImageServiceApi()
id = 'id_example' # str | User Id
type = 'type_example' # str | Image Type
max_width = 56 # int | The maximum image width to return. (optional)
max_height = 56 # int | The maximum image height to return. (optional)
width = 56 # int | The fixed image width to return. (optional)
height = 56 # int | The fixed image height to return. (optional)
quality = 56 # int | Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
crop_whitespace = true # bool | Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. (optional)
enable_image_enhancers = true # bool | Enable or disable image enhancers such as cover art. (optional)
format = 'format_example' # str | Determines the output foramt of the image - original,gif,jpg,png (optional)
add_played_indicator = true # bool | Optional. Add a played indicator (optional)
percent_played = 1.2 # float | Optional percent to render for the percent played overlay (optional)
unplayed_count = 56 # int | Optional unplayed count overlay to render (optional)
background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)
index = 56 # int | Image Index (optional)

try:
    api_instance.get_users_by_id_images_by_type(id, type, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer, index=index)
except ApiException as e:
    print("Exception when calling ImageServiceApi->get_users_by_id_images_by_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User Id | 
 **type** | **str**| Image Type | 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **crop_whitespace** | **bool**| Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **enable_image_enhancers** | **bool**| Enable or disable image enhancers such as cover art. | [optional] 
 **format** | **str**| Determines the output foramt of the image - original,gif,jpg,png | [optional] 
 **add_played_indicator** | **bool**| Optional. Add a played indicator | [optional] 
 **percent_played** | **float**| Optional percent to render for the percent played overlay | [optional] 
 **unplayed_count** | **int**| Optional unplayed count overlay to render | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 
 **index** | **int**| Image Index | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_by_id_images_by_type_by_index**
> get_users_by_id_images_by_type_by_index(id, type, index, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.ImageServiceApi()
id = 'id_example' # str | User Id
type = 'type_example' # str | Image Type
index = 56 # int | Image Index
max_width = 56 # int | The maximum image width to return. (optional)
max_height = 56 # int | The maximum image height to return. (optional)
width = 56 # int | The fixed image width to return. (optional)
height = 56 # int | The fixed image height to return. (optional)
quality = 56 # int | Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
crop_whitespace = true # bool | Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. (optional)
enable_image_enhancers = true # bool | Enable or disable image enhancers such as cover art. (optional)
format = 'format_example' # str | Determines the output foramt of the image - original,gif,jpg,png (optional)
add_played_indicator = true # bool | Optional. Add a played indicator (optional)
percent_played = 1.2 # float | Optional percent to render for the percent played overlay (optional)
unplayed_count = 56 # int | Optional unplayed count overlay to render (optional)
background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)

try:
    api_instance.get_users_by_id_images_by_type_by_index(id, type, index, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer)
except ApiException as e:
    print("Exception when calling ImageServiceApi->get_users_by_id_images_by_type_by_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User Id | 
 **type** | **str**| Image Type | 
 **index** | **int**| Image Index | 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **crop_whitespace** | **bool**| Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **enable_image_enhancers** | **bool**| Enable or disable image enhancers such as cover art. | [optional] 
 **format** | **str**| Determines the output foramt of the image - original,gif,jpg,png | [optional] 
 **add_played_indicator** | **bool**| Optional. Add a played indicator | [optional] 
 **percent_played** | **float**| Optional percent to render for the percent played overlay | [optional] 
 **unplayed_count** | **int**| Optional unplayed count overlay to render | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_artists_by_name_images_by_type**
> head_artists_by_name_images_by_type(name, type, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer, index=index)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.ImageServiceApi()
name = 'name_example' # str | Item name
type = 'type_example' # str | Image Type
max_width = 56 # int | The maximum image width to return. (optional)
max_height = 56 # int | The maximum image height to return. (optional)
width = 56 # int | The fixed image width to return. (optional)
height = 56 # int | The fixed image height to return. (optional)
quality = 56 # int | Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
crop_whitespace = true # bool | Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. (optional)
enable_image_enhancers = true # bool | Enable or disable image enhancers such as cover art. (optional)
format = 'format_example' # str | Determines the output foramt of the image - original,gif,jpg,png (optional)
add_played_indicator = true # bool | Optional. Add a played indicator (optional)
percent_played = 1.2 # float | Optional percent to render for the percent played overlay (optional)
unplayed_count = 56 # int | Optional unplayed count overlay to render (optional)
background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)
index = 56 # int | Image Index (optional)

try:
    api_instance.head_artists_by_name_images_by_type(name, type, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer, index=index)
except ApiException as e:
    print("Exception when calling ImageServiceApi->head_artists_by_name_images_by_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Item name | 
 **type** | **str**| Image Type | 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **crop_whitespace** | **bool**| Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **enable_image_enhancers** | **bool**| Enable or disable image enhancers such as cover art. | [optional] 
 **format** | **str**| Determines the output foramt of the image - original,gif,jpg,png | [optional] 
 **add_played_indicator** | **bool**| Optional. Add a played indicator | [optional] 
 **percent_played** | **float**| Optional percent to render for the percent played overlay | [optional] 
 **unplayed_count** | **int**| Optional unplayed count overlay to render | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 
 **index** | **int**| Image Index | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_artists_by_name_images_by_type_by_index**
> head_artists_by_name_images_by_type_by_index(name, type, index, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.ImageServiceApi()
name = 'name_example' # str | Item name
type = 'type_example' # str | Image Type
index = 56 # int | Image Index
max_width = 56 # int | The maximum image width to return. (optional)
max_height = 56 # int | The maximum image height to return. (optional)
width = 56 # int | The fixed image width to return. (optional)
height = 56 # int | The fixed image height to return. (optional)
quality = 56 # int | Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
crop_whitespace = true # bool | Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. (optional)
enable_image_enhancers = true # bool | Enable or disable image enhancers such as cover art. (optional)
format = 'format_example' # str | Determines the output foramt of the image - original,gif,jpg,png (optional)
add_played_indicator = true # bool | Optional. Add a played indicator (optional)
percent_played = 1.2 # float | Optional percent to render for the percent played overlay (optional)
unplayed_count = 56 # int | Optional unplayed count overlay to render (optional)
background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)

try:
    api_instance.head_artists_by_name_images_by_type_by_index(name, type, index, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer)
except ApiException as e:
    print("Exception when calling ImageServiceApi->head_artists_by_name_images_by_type_by_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Item name | 
 **type** | **str**| Image Type | 
 **index** | **int**| Image Index | 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **crop_whitespace** | **bool**| Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **enable_image_enhancers** | **bool**| Enable or disable image enhancers such as cover art. | [optional] 
 **format** | **str**| Determines the output foramt of the image - original,gif,jpg,png | [optional] 
 **add_played_indicator** | **bool**| Optional. Add a played indicator | [optional] 
 **percent_played** | **float**| Optional percent to render for the percent played overlay | [optional] 
 **unplayed_count** | **int**| Optional unplayed count overlay to render | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_gamegenres_by_name_images_by_type**
> head_gamegenres_by_name_images_by_type(name, type, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer, index=index)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.ImageServiceApi()
name = 'name_example' # str | Item name
type = 'type_example' # str | Image Type
max_width = 56 # int | The maximum image width to return. (optional)
max_height = 56 # int | The maximum image height to return. (optional)
width = 56 # int | The fixed image width to return. (optional)
height = 56 # int | The fixed image height to return. (optional)
quality = 56 # int | Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
crop_whitespace = true # bool | Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. (optional)
enable_image_enhancers = true # bool | Enable or disable image enhancers such as cover art. (optional)
format = 'format_example' # str | Determines the output foramt of the image - original,gif,jpg,png (optional)
add_played_indicator = true # bool | Optional. Add a played indicator (optional)
percent_played = 1.2 # float | Optional percent to render for the percent played overlay (optional)
unplayed_count = 56 # int | Optional unplayed count overlay to render (optional)
background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)
index = 56 # int | Image Index (optional)

try:
    api_instance.head_gamegenres_by_name_images_by_type(name, type, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer, index=index)
except ApiException as e:
    print("Exception when calling ImageServiceApi->head_gamegenres_by_name_images_by_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Item name | 
 **type** | **str**| Image Type | 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **crop_whitespace** | **bool**| Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **enable_image_enhancers** | **bool**| Enable or disable image enhancers such as cover art. | [optional] 
 **format** | **str**| Determines the output foramt of the image - original,gif,jpg,png | [optional] 
 **add_played_indicator** | **bool**| Optional. Add a played indicator | [optional] 
 **percent_played** | **float**| Optional percent to render for the percent played overlay | [optional] 
 **unplayed_count** | **int**| Optional unplayed count overlay to render | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 
 **index** | **int**| Image Index | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_gamegenres_by_name_images_by_type_by_index**
> head_gamegenres_by_name_images_by_type_by_index(name, type, index, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.ImageServiceApi()
name = 'name_example' # str | Item name
type = 'type_example' # str | Image Type
index = 56 # int | Image Index
max_width = 56 # int | The maximum image width to return. (optional)
max_height = 56 # int | The maximum image height to return. (optional)
width = 56 # int | The fixed image width to return. (optional)
height = 56 # int | The fixed image height to return. (optional)
quality = 56 # int | Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
crop_whitespace = true # bool | Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. (optional)
enable_image_enhancers = true # bool | Enable or disable image enhancers such as cover art. (optional)
format = 'format_example' # str | Determines the output foramt of the image - original,gif,jpg,png (optional)
add_played_indicator = true # bool | Optional. Add a played indicator (optional)
percent_played = 1.2 # float | Optional percent to render for the percent played overlay (optional)
unplayed_count = 56 # int | Optional unplayed count overlay to render (optional)
background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)

try:
    api_instance.head_gamegenres_by_name_images_by_type_by_index(name, type, index, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer)
except ApiException as e:
    print("Exception when calling ImageServiceApi->head_gamegenres_by_name_images_by_type_by_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Item name | 
 **type** | **str**| Image Type | 
 **index** | **int**| Image Index | 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **crop_whitespace** | **bool**| Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **enable_image_enhancers** | **bool**| Enable or disable image enhancers such as cover art. | [optional] 
 **format** | **str**| Determines the output foramt of the image - original,gif,jpg,png | [optional] 
 **add_played_indicator** | **bool**| Optional. Add a played indicator | [optional] 
 **percent_played** | **float**| Optional percent to render for the percent played overlay | [optional] 
 **unplayed_count** | **int**| Optional unplayed count overlay to render | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_genres_by_name_images_by_type**
> head_genres_by_name_images_by_type(name, type, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer, index=index)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.ImageServiceApi()
name = 'name_example' # str | Item name
type = 'type_example' # str | Image Type
max_width = 56 # int | The maximum image width to return. (optional)
max_height = 56 # int | The maximum image height to return. (optional)
width = 56 # int | The fixed image width to return. (optional)
height = 56 # int | The fixed image height to return. (optional)
quality = 56 # int | Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
crop_whitespace = true # bool | Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. (optional)
enable_image_enhancers = true # bool | Enable or disable image enhancers such as cover art. (optional)
format = 'format_example' # str | Determines the output foramt of the image - original,gif,jpg,png (optional)
add_played_indicator = true # bool | Optional. Add a played indicator (optional)
percent_played = 1.2 # float | Optional percent to render for the percent played overlay (optional)
unplayed_count = 56 # int | Optional unplayed count overlay to render (optional)
background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)
index = 56 # int | Image Index (optional)

try:
    api_instance.head_genres_by_name_images_by_type(name, type, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer, index=index)
except ApiException as e:
    print("Exception when calling ImageServiceApi->head_genres_by_name_images_by_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Item name | 
 **type** | **str**| Image Type | 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **crop_whitespace** | **bool**| Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **enable_image_enhancers** | **bool**| Enable or disable image enhancers such as cover art. | [optional] 
 **format** | **str**| Determines the output foramt of the image - original,gif,jpg,png | [optional] 
 **add_played_indicator** | **bool**| Optional. Add a played indicator | [optional] 
 **percent_played** | **float**| Optional percent to render for the percent played overlay | [optional] 
 **unplayed_count** | **int**| Optional unplayed count overlay to render | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 
 **index** | **int**| Image Index | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_genres_by_name_images_by_type_by_index**
> head_genres_by_name_images_by_type_by_index(name, type, index, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.ImageServiceApi()
name = 'name_example' # str | Item name
type = 'type_example' # str | Image Type
index = 56 # int | Image Index
max_width = 56 # int | The maximum image width to return. (optional)
max_height = 56 # int | The maximum image height to return. (optional)
width = 56 # int | The fixed image width to return. (optional)
height = 56 # int | The fixed image height to return. (optional)
quality = 56 # int | Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
crop_whitespace = true # bool | Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. (optional)
enable_image_enhancers = true # bool | Enable or disable image enhancers such as cover art. (optional)
format = 'format_example' # str | Determines the output foramt of the image - original,gif,jpg,png (optional)
add_played_indicator = true # bool | Optional. Add a played indicator (optional)
percent_played = 1.2 # float | Optional percent to render for the percent played overlay (optional)
unplayed_count = 56 # int | Optional unplayed count overlay to render (optional)
background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)

try:
    api_instance.head_genres_by_name_images_by_type_by_index(name, type, index, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer)
except ApiException as e:
    print("Exception when calling ImageServiceApi->head_genres_by_name_images_by_type_by_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Item name | 
 **type** | **str**| Image Type | 
 **index** | **int**| Image Index | 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **crop_whitespace** | **bool**| Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **enable_image_enhancers** | **bool**| Enable or disable image enhancers such as cover art. | [optional] 
 **format** | **str**| Determines the output foramt of the image - original,gif,jpg,png | [optional] 
 **add_played_indicator** | **bool**| Optional. Add a played indicator | [optional] 
 **percent_played** | **float**| Optional percent to render for the percent played overlay | [optional] 
 **unplayed_count** | **int**| Optional unplayed count overlay to render | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_items_by_id_images_by_type**
> head_items_by_id_images_by_type(id, type, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer, index=index)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.ImageServiceApi()
id = 'id_example' # str | Item Id
type = 'type_example' # str | Image Type
max_width = 56 # int | The maximum image width to return. (optional)
max_height = 56 # int | The maximum image height to return. (optional)
width = 56 # int | The fixed image width to return. (optional)
height = 56 # int | The fixed image height to return. (optional)
quality = 56 # int | Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
crop_whitespace = true # bool | Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. (optional)
enable_image_enhancers = true # bool | Enable or disable image enhancers such as cover art. (optional)
format = 'format_example' # str | Determines the output foramt of the image - original,gif,jpg,png (optional)
add_played_indicator = true # bool | Optional. Add a played indicator (optional)
percent_played = 1.2 # float | Optional percent to render for the percent played overlay (optional)
unplayed_count = 56 # int | Optional unplayed count overlay to render (optional)
background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)
index = 56 # int | Image Index (optional)

try:
    api_instance.head_items_by_id_images_by_type(id, type, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer, index=index)
except ApiException as e:
    print("Exception when calling ImageServiceApi->head_items_by_id_images_by_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **type** | **str**| Image Type | 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **crop_whitespace** | **bool**| Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **enable_image_enhancers** | **bool**| Enable or disable image enhancers such as cover art. | [optional] 
 **format** | **str**| Determines the output foramt of the image - original,gif,jpg,png | [optional] 
 **add_played_indicator** | **bool**| Optional. Add a played indicator | [optional] 
 **percent_played** | **float**| Optional percent to render for the percent played overlay | [optional] 
 **unplayed_count** | **int**| Optional unplayed count overlay to render | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 
 **index** | **int**| Image Index | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_items_by_id_images_by_type_by_index**
> head_items_by_id_images_by_type_by_index(id, type, index, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.ImageServiceApi()
id = 'id_example' # str | Item Id
type = 'type_example' # str | Image Type
index = 56 # int | Image Index
max_width = 56 # int | The maximum image width to return. (optional)
max_height = 56 # int | The maximum image height to return. (optional)
width = 56 # int | The fixed image width to return. (optional)
height = 56 # int | The fixed image height to return. (optional)
quality = 56 # int | Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
crop_whitespace = true # bool | Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. (optional)
enable_image_enhancers = true # bool | Enable or disable image enhancers such as cover art. (optional)
format = 'format_example' # str | Determines the output foramt of the image - original,gif,jpg,png (optional)
add_played_indicator = true # bool | Optional. Add a played indicator (optional)
percent_played = 1.2 # float | Optional percent to render for the percent played overlay (optional)
unplayed_count = 56 # int | Optional unplayed count overlay to render (optional)
background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)

try:
    api_instance.head_items_by_id_images_by_type_by_index(id, type, index, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer)
except ApiException as e:
    print("Exception when calling ImageServiceApi->head_items_by_id_images_by_type_by_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **type** | **str**| Image Type | 
 **index** | **int**| Image Index | 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **crop_whitespace** | **bool**| Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **enable_image_enhancers** | **bool**| Enable or disable image enhancers such as cover art. | [optional] 
 **format** | **str**| Determines the output foramt of the image - original,gif,jpg,png | [optional] 
 **add_played_indicator** | **bool**| Optional. Add a played indicator | [optional] 
 **percent_played** | **float**| Optional percent to render for the percent played overlay | [optional] 
 **unplayed_count** | **int**| Optional unplayed count overlay to render | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_items_by_id_images_by_type_by_index_by_tag_by_format_by_maxwidth_by_maxheight_by_percentplayed_by_unplayedcount**
> head_items_by_id_images_by_type_by_index_by_tag_by_format_by_maxwidth_by_maxheight_by_percentplayed_by_unplayedcount(id, max_width, max_height, tag, format, percent_played, unplayed_count, type, index, width=width, height=height, quality=quality, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, add_played_indicator=add_played_indicator, background_color=background_color, foreground_layer=foreground_layer)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.ImageServiceApi()
id = 'id_example' # str | Item Id
max_width = 56 # int | The maximum image width to return.
max_height = 56 # int | The maximum image height to return.
tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers.
format = 'format_example' # str | Determines the output foramt of the image - original,gif,jpg,png
percent_played = 1.2 # float | Optional percent to render for the percent played overlay
unplayed_count = 56 # int | Optional unplayed count overlay to render
type = 'type_example' # str | Image Type
index = 56 # int | Image Index
width = 56 # int | The fixed image width to return. (optional)
height = 56 # int | The fixed image height to return. (optional)
quality = 56 # int | Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
crop_whitespace = true # bool | Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. (optional)
enable_image_enhancers = true # bool | Enable or disable image enhancers such as cover art. (optional)
add_played_indicator = true # bool | Optional. Add a played indicator (optional)
background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)

try:
    api_instance.head_items_by_id_images_by_type_by_index_by_tag_by_format_by_maxwidth_by_maxheight_by_percentplayed_by_unplayedcount(id, max_width, max_height, tag, format, percent_played, unplayed_count, type, index, width=width, height=height, quality=quality, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, add_played_indicator=add_played_indicator, background_color=background_color, foreground_layer=foreground_layer)
except ApiException as e:
    print("Exception when calling ImageServiceApi->head_items_by_id_images_by_type_by_index_by_tag_by_format_by_maxwidth_by_maxheight_by_percentplayed_by_unplayedcount: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **max_width** | **int**| The maximum image width to return. | 
 **max_height** | **int**| The maximum image height to return. | 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | 
 **format** | **str**| Determines the output foramt of the image - original,gif,jpg,png | 
 **percent_played** | **float**| Optional percent to render for the percent played overlay | 
 **unplayed_count** | **int**| Optional unplayed count overlay to render | 
 **type** | **str**| Image Type | 
 **index** | **int**| Image Index | 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **crop_whitespace** | **bool**| Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **enable_image_enhancers** | **bool**| Enable or disable image enhancers such as cover art. | [optional] 
 **add_played_indicator** | **bool**| Optional. Add a played indicator | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_musicgenres_by_name_images_by_type**
> head_musicgenres_by_name_images_by_type(name, type, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer, index=index)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.ImageServiceApi()
name = 'name_example' # str | Item name
type = 'type_example' # str | Image Type
max_width = 56 # int | The maximum image width to return. (optional)
max_height = 56 # int | The maximum image height to return. (optional)
width = 56 # int | The fixed image width to return. (optional)
height = 56 # int | The fixed image height to return. (optional)
quality = 56 # int | Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
crop_whitespace = true # bool | Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. (optional)
enable_image_enhancers = true # bool | Enable or disable image enhancers such as cover art. (optional)
format = 'format_example' # str | Determines the output foramt of the image - original,gif,jpg,png (optional)
add_played_indicator = true # bool | Optional. Add a played indicator (optional)
percent_played = 1.2 # float | Optional percent to render for the percent played overlay (optional)
unplayed_count = 56 # int | Optional unplayed count overlay to render (optional)
background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)
index = 56 # int | Image Index (optional)

try:
    api_instance.head_musicgenres_by_name_images_by_type(name, type, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer, index=index)
except ApiException as e:
    print("Exception when calling ImageServiceApi->head_musicgenres_by_name_images_by_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Item name | 
 **type** | **str**| Image Type | 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **crop_whitespace** | **bool**| Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **enable_image_enhancers** | **bool**| Enable or disable image enhancers such as cover art. | [optional] 
 **format** | **str**| Determines the output foramt of the image - original,gif,jpg,png | [optional] 
 **add_played_indicator** | **bool**| Optional. Add a played indicator | [optional] 
 **percent_played** | **float**| Optional percent to render for the percent played overlay | [optional] 
 **unplayed_count** | **int**| Optional unplayed count overlay to render | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 
 **index** | **int**| Image Index | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_musicgenres_by_name_images_by_type_by_index**
> head_musicgenres_by_name_images_by_type_by_index(name, type, index, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.ImageServiceApi()
name = 'name_example' # str | Item name
type = 'type_example' # str | Image Type
index = 56 # int | Image Index
max_width = 56 # int | The maximum image width to return. (optional)
max_height = 56 # int | The maximum image height to return. (optional)
width = 56 # int | The fixed image width to return. (optional)
height = 56 # int | The fixed image height to return. (optional)
quality = 56 # int | Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
crop_whitespace = true # bool | Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. (optional)
enable_image_enhancers = true # bool | Enable or disable image enhancers such as cover art. (optional)
format = 'format_example' # str | Determines the output foramt of the image - original,gif,jpg,png (optional)
add_played_indicator = true # bool | Optional. Add a played indicator (optional)
percent_played = 1.2 # float | Optional percent to render for the percent played overlay (optional)
unplayed_count = 56 # int | Optional unplayed count overlay to render (optional)
background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)

try:
    api_instance.head_musicgenres_by_name_images_by_type_by_index(name, type, index, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer)
except ApiException as e:
    print("Exception when calling ImageServiceApi->head_musicgenres_by_name_images_by_type_by_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Item name | 
 **type** | **str**| Image Type | 
 **index** | **int**| Image Index | 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **crop_whitespace** | **bool**| Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **enable_image_enhancers** | **bool**| Enable or disable image enhancers such as cover art. | [optional] 
 **format** | **str**| Determines the output foramt of the image - original,gif,jpg,png | [optional] 
 **add_played_indicator** | **bool**| Optional. Add a played indicator | [optional] 
 **percent_played** | **float**| Optional percent to render for the percent played overlay | [optional] 
 **unplayed_count** | **int**| Optional unplayed count overlay to render | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_persons_by_name_images_by_type**
> head_persons_by_name_images_by_type(name, type, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer, index=index)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.ImageServiceApi()
name = 'name_example' # str | Item name
type = 'type_example' # str | Image Type
max_width = 56 # int | The maximum image width to return. (optional)
max_height = 56 # int | The maximum image height to return. (optional)
width = 56 # int | The fixed image width to return. (optional)
height = 56 # int | The fixed image height to return. (optional)
quality = 56 # int | Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
crop_whitespace = true # bool | Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. (optional)
enable_image_enhancers = true # bool | Enable or disable image enhancers such as cover art. (optional)
format = 'format_example' # str | Determines the output foramt of the image - original,gif,jpg,png (optional)
add_played_indicator = true # bool | Optional. Add a played indicator (optional)
percent_played = 1.2 # float | Optional percent to render for the percent played overlay (optional)
unplayed_count = 56 # int | Optional unplayed count overlay to render (optional)
background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)
index = 56 # int | Image Index (optional)

try:
    api_instance.head_persons_by_name_images_by_type(name, type, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer, index=index)
except ApiException as e:
    print("Exception when calling ImageServiceApi->head_persons_by_name_images_by_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Item name | 
 **type** | **str**| Image Type | 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **crop_whitespace** | **bool**| Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **enable_image_enhancers** | **bool**| Enable or disable image enhancers such as cover art. | [optional] 
 **format** | **str**| Determines the output foramt of the image - original,gif,jpg,png | [optional] 
 **add_played_indicator** | **bool**| Optional. Add a played indicator | [optional] 
 **percent_played** | **float**| Optional percent to render for the percent played overlay | [optional] 
 **unplayed_count** | **int**| Optional unplayed count overlay to render | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 
 **index** | **int**| Image Index | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_persons_by_name_images_by_type_by_index**
> head_persons_by_name_images_by_type_by_index(name, type, index, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.ImageServiceApi()
name = 'name_example' # str | Item name
type = 'type_example' # str | Image Type
index = 56 # int | Image Index
max_width = 56 # int | The maximum image width to return. (optional)
max_height = 56 # int | The maximum image height to return. (optional)
width = 56 # int | The fixed image width to return. (optional)
height = 56 # int | The fixed image height to return. (optional)
quality = 56 # int | Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
crop_whitespace = true # bool | Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. (optional)
enable_image_enhancers = true # bool | Enable or disable image enhancers such as cover art. (optional)
format = 'format_example' # str | Determines the output foramt of the image - original,gif,jpg,png (optional)
add_played_indicator = true # bool | Optional. Add a played indicator (optional)
percent_played = 1.2 # float | Optional percent to render for the percent played overlay (optional)
unplayed_count = 56 # int | Optional unplayed count overlay to render (optional)
background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)

try:
    api_instance.head_persons_by_name_images_by_type_by_index(name, type, index, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer)
except ApiException as e:
    print("Exception when calling ImageServiceApi->head_persons_by_name_images_by_type_by_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Item name | 
 **type** | **str**| Image Type | 
 **index** | **int**| Image Index | 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **crop_whitespace** | **bool**| Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **enable_image_enhancers** | **bool**| Enable or disable image enhancers such as cover art. | [optional] 
 **format** | **str**| Determines the output foramt of the image - original,gif,jpg,png | [optional] 
 **add_played_indicator** | **bool**| Optional. Add a played indicator | [optional] 
 **percent_played** | **float**| Optional percent to render for the percent played overlay | [optional] 
 **unplayed_count** | **int**| Optional unplayed count overlay to render | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_studios_by_name_images_by_type**
> head_studios_by_name_images_by_type(name, type, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer, index=index)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.ImageServiceApi()
name = 'name_example' # str | Item name
type = 'type_example' # str | Image Type
max_width = 56 # int | The maximum image width to return. (optional)
max_height = 56 # int | The maximum image height to return. (optional)
width = 56 # int | The fixed image width to return. (optional)
height = 56 # int | The fixed image height to return. (optional)
quality = 56 # int | Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
crop_whitespace = true # bool | Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. (optional)
enable_image_enhancers = true # bool | Enable or disable image enhancers such as cover art. (optional)
format = 'format_example' # str | Determines the output foramt of the image - original,gif,jpg,png (optional)
add_played_indicator = true # bool | Optional. Add a played indicator (optional)
percent_played = 1.2 # float | Optional percent to render for the percent played overlay (optional)
unplayed_count = 56 # int | Optional unplayed count overlay to render (optional)
background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)
index = 56 # int | Image Index (optional)

try:
    api_instance.head_studios_by_name_images_by_type(name, type, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer, index=index)
except ApiException as e:
    print("Exception when calling ImageServiceApi->head_studios_by_name_images_by_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Item name | 
 **type** | **str**| Image Type | 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **crop_whitespace** | **bool**| Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **enable_image_enhancers** | **bool**| Enable or disable image enhancers such as cover art. | [optional] 
 **format** | **str**| Determines the output foramt of the image - original,gif,jpg,png | [optional] 
 **add_played_indicator** | **bool**| Optional. Add a played indicator | [optional] 
 **percent_played** | **float**| Optional percent to render for the percent played overlay | [optional] 
 **unplayed_count** | **int**| Optional unplayed count overlay to render | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 
 **index** | **int**| Image Index | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_studios_by_name_images_by_type_by_index**
> head_studios_by_name_images_by_type_by_index(name, type, index, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.ImageServiceApi()
name = 'name_example' # str | Item name
type = 'type_example' # str | Image Type
index = 56 # int | Image Index
max_width = 56 # int | The maximum image width to return. (optional)
max_height = 56 # int | The maximum image height to return. (optional)
width = 56 # int | The fixed image width to return. (optional)
height = 56 # int | The fixed image height to return. (optional)
quality = 56 # int | Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
crop_whitespace = true # bool | Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. (optional)
enable_image_enhancers = true # bool | Enable or disable image enhancers such as cover art. (optional)
format = 'format_example' # str | Determines the output foramt of the image - original,gif,jpg,png (optional)
add_played_indicator = true # bool | Optional. Add a played indicator (optional)
percent_played = 1.2 # float | Optional percent to render for the percent played overlay (optional)
unplayed_count = 56 # int | Optional unplayed count overlay to render (optional)
background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)

try:
    api_instance.head_studios_by_name_images_by_type_by_index(name, type, index, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer)
except ApiException as e:
    print("Exception when calling ImageServiceApi->head_studios_by_name_images_by_type_by_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Item name | 
 **type** | **str**| Image Type | 
 **index** | **int**| Image Index | 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **crop_whitespace** | **bool**| Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **enable_image_enhancers** | **bool**| Enable or disable image enhancers such as cover art. | [optional] 
 **format** | **str**| Determines the output foramt of the image - original,gif,jpg,png | [optional] 
 **add_played_indicator** | **bool**| Optional. Add a played indicator | [optional] 
 **percent_played** | **float**| Optional percent to render for the percent played overlay | [optional] 
 **unplayed_count** | **int**| Optional unplayed count overlay to render | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_users_by_id_images_by_type**
> head_users_by_id_images_by_type(id, type, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer, index=index)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.ImageServiceApi()
id = 'id_example' # str | User Id
type = 'type_example' # str | Image Type
max_width = 56 # int | The maximum image width to return. (optional)
max_height = 56 # int | The maximum image height to return. (optional)
width = 56 # int | The fixed image width to return. (optional)
height = 56 # int | The fixed image height to return. (optional)
quality = 56 # int | Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
crop_whitespace = true # bool | Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. (optional)
enable_image_enhancers = true # bool | Enable or disable image enhancers such as cover art. (optional)
format = 'format_example' # str | Determines the output foramt of the image - original,gif,jpg,png (optional)
add_played_indicator = true # bool | Optional. Add a played indicator (optional)
percent_played = 1.2 # float | Optional percent to render for the percent played overlay (optional)
unplayed_count = 56 # int | Optional unplayed count overlay to render (optional)
background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)
index = 56 # int | Image Index (optional)

try:
    api_instance.head_users_by_id_images_by_type(id, type, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer, index=index)
except ApiException as e:
    print("Exception when calling ImageServiceApi->head_users_by_id_images_by_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User Id | 
 **type** | **str**| Image Type | 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **crop_whitespace** | **bool**| Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **enable_image_enhancers** | **bool**| Enable or disable image enhancers such as cover art. | [optional] 
 **format** | **str**| Determines the output foramt of the image - original,gif,jpg,png | [optional] 
 **add_played_indicator** | **bool**| Optional. Add a played indicator | [optional] 
 **percent_played** | **float**| Optional percent to render for the percent played overlay | [optional] 
 **unplayed_count** | **int**| Optional unplayed count overlay to render | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 
 **index** | **int**| Image Index | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_users_by_id_images_by_type_by_index**
> head_users_by_id_images_by_type_by_index(id, type, index, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.ImageServiceApi()
id = 'id_example' # str | User Id
type = 'type_example' # str | Image Type
index = 56 # int | Image Index
max_width = 56 # int | The maximum image width to return. (optional)
max_height = 56 # int | The maximum image height to return. (optional)
width = 56 # int | The fixed image width to return. (optional)
height = 56 # int | The fixed image height to return. (optional)
quality = 56 # int | Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
crop_whitespace = true # bool | Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. (optional)
enable_image_enhancers = true # bool | Enable or disable image enhancers such as cover art. (optional)
format = 'format_example' # str | Determines the output foramt of the image - original,gif,jpg,png (optional)
add_played_indicator = true # bool | Optional. Add a played indicator (optional)
percent_played = 1.2 # float | Optional percent to render for the percent played overlay (optional)
unplayed_count = 56 # int | Optional unplayed count overlay to render (optional)
background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)

try:
    api_instance.head_users_by_id_images_by_type_by_index(id, type, index, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, tag=tag, crop_whitespace=crop_whitespace, enable_image_enhancers=enable_image_enhancers, format=format, add_played_indicator=add_played_indicator, percent_played=percent_played, unplayed_count=unplayed_count, background_color=background_color, foreground_layer=foreground_layer)
except ApiException as e:
    print("Exception when calling ImageServiceApi->head_users_by_id_images_by_type_by_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User Id | 
 **type** | **str**| Image Type | 
 **index** | **int**| Image Index | 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **crop_whitespace** | **bool**| Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **enable_image_enhancers** | **bool**| Enable or disable image enhancers such as cover art. | [optional] 
 **format** | **str**| Determines the output foramt of the image - original,gif,jpg,png | [optional] 
 **add_played_indicator** | **bool**| Optional. Add a played indicator | [optional] 
 **percent_played** | **float**| Optional percent to render for the percent played overlay | [optional] 
 **unplayed_count** | **int**| Optional unplayed count overlay to render | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_items_by_id_images_by_type**
> post_items_by_id_images_by_type(body, id, type, index=index)



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
api_instance = embyapi.ImageServiceApi(embyapi.ApiClient(configuration))
body = embyapi.Object() # Object | Binary stream
id = 'id_example' # str | Item Id
type = 'type_example' # str | Image Type
index = 56 # int | Image Index (optional)

try:
    api_instance.post_items_by_id_images_by_type(body, id, type, index=index)
except ApiException as e:
    print("Exception when calling ImageServiceApi->post_items_by_id_images_by_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Object**| Binary stream | 
 **id** | **str**| Item Id | 
 **type** | **str**| Image Type | 
 **index** | **int**| Image Index | [optional] 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_items_by_id_images_by_type_by_index**
> post_items_by_id_images_by_type_by_index(body, id, type, index)



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
api_instance = embyapi.ImageServiceApi(embyapi.ApiClient(configuration))
body = embyapi.Object() # Object | Binary stream
id = 'id_example' # str | Item Id
type = 'type_example' # str | Image Type
index = 56 # int | Image Index

try:
    api_instance.post_items_by_id_images_by_type_by_index(body, id, type, index)
except ApiException as e:
    print("Exception when calling ImageServiceApi->post_items_by_id_images_by_type_by_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Object**| Binary stream | 
 **id** | **str**| Item Id | 
 **type** | **str**| Image Type | 
 **index** | **int**| Image Index | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_items_by_id_images_by_type_by_index_index**
> post_items_by_id_images_by_type_by_index_index(id, type, index, new_index)

Updates the index for an item image

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
api_instance = embyapi.ImageServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Item Id
type = 'type_example' # str | Image Type
index = 56 # int | Image Index
new_index = 56 # int | The new image index

try:
    # Updates the index for an item image
    api_instance.post_items_by_id_images_by_type_by_index_index(id, type, index, new_index)
except ApiException as e:
    print("Exception when calling ImageServiceApi->post_items_by_id_images_by_type_by_index_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **type** | **str**| Image Type | 
 **index** | **int**| Image Index | 
 **new_index** | **int**| The new image index | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_users_by_id_images_by_type**
> post_users_by_id_images_by_type(body, id, type, index=index)



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
api_instance = embyapi.ImageServiceApi(embyapi.ApiClient(configuration))
body = embyapi.Object() # Object | Binary stream
id = 'id_example' # str | User Id
type = 'type_example' # str | Image Type
index = 56 # int | Image Index (optional)

try:
    api_instance.post_users_by_id_images_by_type(body, id, type, index=index)
except ApiException as e:
    print("Exception when calling ImageServiceApi->post_users_by_id_images_by_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Object**| Binary stream | 
 **id** | **str**| User Id | 
 **type** | **str**| Image Type | 
 **index** | **int**| Image Index | [optional] 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_users_by_id_images_by_type_by_index**
> post_users_by_id_images_by_type_by_index(body, id, type, index)



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
api_instance = embyapi.ImageServiceApi(embyapi.ApiClient(configuration))
body = embyapi.Object() # Object | Binary stream
id = 'id_example' # str | User Id
type = 'type_example' # str | Image Type
index = 56 # int | Image Index

try:
    api_instance.post_users_by_id_images_by_type_by_index(body, id, type, index)
except ApiException as e:
    print("Exception when calling ImageServiceApi->post_users_by_id_images_by_type_by_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Object**| Binary stream | 
 **id** | **str**| User Id | 
 **type** | **str**| Image Type | 
 **index** | **int**| Image Index | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

