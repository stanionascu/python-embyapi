# embyapi.LiveTvServiceApi

All URIs are relative to *https://home.ourflix.de:32865/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_livetv_channelmappingoptions**](LiveTvServiceApi.md#delete_livetv_channelmappingoptions) | **DELETE** /LiveTv/ChannelMappingOptions | 
[**delete_livetv_channelmappings**](LiveTvServiceApi.md#delete_livetv_channelmappings) | **DELETE** /LiveTv/ChannelMappings | 
[**delete_livetv_listingproviders**](LiveTvServiceApi.md#delete_livetv_listingproviders) | **DELETE** /LiveTv/ListingProviders | Deletes a listing provider
[**delete_livetv_recordings_by_id**](LiveTvServiceApi.md#delete_livetv_recordings_by_id) | **DELETE** /LiveTv/Recordings/{Id} | Deletes a live tv recording
[**delete_livetv_seriestimers_by_id**](LiveTvServiceApi.md#delete_livetv_seriestimers_by_id) | **DELETE** /LiveTv/SeriesTimers/{Id} | Cancels a live tv series timer
[**delete_livetv_timers_by_id**](LiveTvServiceApi.md#delete_livetv_timers_by_id) | **DELETE** /LiveTv/Timers/{Id} | Cancels a live tv timer
[**delete_livetv_tunerhosts**](LiveTvServiceApi.md#delete_livetv_tunerhosts) | **DELETE** /LiveTv/TunerHosts | Deletes a tuner host
[**get_livetv_channelmappingoptions**](LiveTvServiceApi.md#get_livetv_channelmappingoptions) | **GET** /LiveTv/ChannelMappingOptions | 
[**get_livetv_channelmappings**](LiveTvServiceApi.md#get_livetv_channelmappings) | **GET** /LiveTv/ChannelMappings | 
[**get_livetv_channels**](LiveTvServiceApi.md#get_livetv_channels) | **GET** /LiveTv/Channels | Gets available live tv channels.
[**get_livetv_channels_by_id**](LiveTvServiceApi.md#get_livetv_channels_by_id) | **GET** /LiveTv/Channels/{Id} | Gets a live tv channel
[**get_livetv_guideinfo**](LiveTvServiceApi.md#get_livetv_guideinfo) | **GET** /LiveTv/GuideInfo | Gets guide info
[**get_livetv_info**](LiveTvServiceApi.md#get_livetv_info) | **GET** /LiveTv/Info | Gets available live tv services.
[**get_livetv_listingproviders**](LiveTvServiceApi.md#get_livetv_listingproviders) | **GET** /LiveTv/ListingProviders | Gets current listing providers
[**get_livetv_listingproviders_available**](LiveTvServiceApi.md#get_livetv_listingproviders_available) | **GET** /LiveTv/ListingProviders/Available | Gets listing provider
[**get_livetv_listingproviders_default**](LiveTvServiceApi.md#get_livetv_listingproviders_default) | **GET** /LiveTv/ListingProviders/Default | 
[**get_livetv_listingproviders_lineups**](LiveTvServiceApi.md#get_livetv_listingproviders_lineups) | **GET** /LiveTv/ListingProviders/Lineups | Gets available lineups
[**get_livetv_listingproviders_schedulesdirect_countries**](LiveTvServiceApi.md#get_livetv_listingproviders_schedulesdirect_countries) | **GET** /LiveTv/ListingProviders/SchedulesDirect/Countries | Gets available lineups
[**get_livetv_liverecordings_by_id_stream**](LiveTvServiceApi.md#get_livetv_liverecordings_by_id_stream) | **GET** /LiveTv/LiveRecordings/{Id}/stream | Gets a live tv channel
[**get_livetv_livestreamfiles_by_id_by_container**](LiveTvServiceApi.md#get_livetv_livestreamfiles_by_id_by_container) | **GET** /LiveTv/LiveStreamFiles/{Id}/stream.{Container} | Gets a live tv channel
[**get_livetv_programs**](LiveTvServiceApi.md#get_livetv_programs) | **GET** /LiveTv/Programs | Gets available live tv epgs..
[**get_livetv_programs_recommended**](LiveTvServiceApi.md#get_livetv_programs_recommended) | **GET** /LiveTv/Programs/Recommended | Gets available live tv epgs..
[**get_livetv_recordings**](LiveTvServiceApi.md#get_livetv_recordings) | **GET** /LiveTv/Recordings | Gets live tv recordings
[**get_livetv_recordings_by_id**](LiveTvServiceApi.md#get_livetv_recordings_by_id) | **GET** /LiveTv/Recordings/{Id} | Gets a live tv recording
[**get_livetv_recordings_folders**](LiveTvServiceApi.md#get_livetv_recordings_folders) | **GET** /LiveTv/Recordings/Folders | Gets recording folders
[**get_livetv_recordings_groups**](LiveTvServiceApi.md#get_livetv_recordings_groups) | **GET** /LiveTv/Recordings/Groups | Gets live tv recording groups
[**get_livetv_recordings_groups_by_id**](LiveTvServiceApi.md#get_livetv_recordings_groups_by_id) | **GET** /LiveTv/Recordings/Groups/{Id} | Gets a recording group
[**get_livetv_recordings_series**](LiveTvServiceApi.md#get_livetv_recordings_series) | **GET** /LiveTv/Recordings/Series | Gets live tv recordings
[**get_livetv_seriestimers**](LiveTvServiceApi.md#get_livetv_seriestimers) | **GET** /LiveTv/SeriesTimers | Gets live tv series timers
[**get_livetv_seriestimers_by_id**](LiveTvServiceApi.md#get_livetv_seriestimers_by_id) | **GET** /LiveTv/SeriesTimers/{Id} | Gets a live tv series timer
[**get_livetv_timers**](LiveTvServiceApi.md#get_livetv_timers) | **GET** /LiveTv/Timers | Gets live tv timers
[**get_livetv_timers_by_id**](LiveTvServiceApi.md#get_livetv_timers_by_id) | **GET** /LiveTv/Timers/{Id} | Gets a live tv timer
[**get_livetv_timers_defaults**](LiveTvServiceApi.md#get_livetv_timers_defaults) | **GET** /LiveTv/Timers/Defaults | Gets default values for a new timer
[**get_livetv_tunerhosts**](LiveTvServiceApi.md#get_livetv_tunerhosts) | **GET** /LiveTv/TunerHosts | Gets tuner hosts
[**get_livetv_tunerhosts_types**](LiveTvServiceApi.md#get_livetv_tunerhosts_types) | **GET** /LiveTv/TunerHosts/Types | 
[**get_livetv_tuners_discvover**](LiveTvServiceApi.md#get_livetv_tuners_discvover) | **GET** /LiveTv/Tuners/Discvover | 
[**head_livetv_channelmappingoptions**](LiveTvServiceApi.md#head_livetv_channelmappingoptions) | **HEAD** /LiveTv/ChannelMappingOptions | 
[**head_livetv_channelmappings**](LiveTvServiceApi.md#head_livetv_channelmappings) | **HEAD** /LiveTv/ChannelMappings | 
[**options_livetv_channelmappingoptions**](LiveTvServiceApi.md#options_livetv_channelmappingoptions) | **OPTIONS** /LiveTv/ChannelMappingOptions | 
[**options_livetv_channelmappings**](LiveTvServiceApi.md#options_livetv_channelmappings) | **OPTIONS** /LiveTv/ChannelMappings | 
[**patch_livetv_channelmappingoptions**](LiveTvServiceApi.md#patch_livetv_channelmappingoptions) | **PATCH** /LiveTv/ChannelMappingOptions | 
[**patch_livetv_channelmappings**](LiveTvServiceApi.md#patch_livetv_channelmappings) | **PATCH** /LiveTv/ChannelMappings | 
[**post_livetv_channelmappingoptions**](LiveTvServiceApi.md#post_livetv_channelmappingoptions) | **POST** /LiveTv/ChannelMappingOptions | 
[**post_livetv_channelmappings**](LiveTvServiceApi.md#post_livetv_channelmappings) | **POST** /LiveTv/ChannelMappings | 
[**post_livetv_listingproviders**](LiveTvServiceApi.md#post_livetv_listingproviders) | **POST** /LiveTv/ListingProviders | Adds a listing provider
[**post_livetv_programs**](LiveTvServiceApi.md#post_livetv_programs) | **POST** /LiveTv/Programs | Gets available live tv epgs..
[**post_livetv_seriestimers**](LiveTvServiceApi.md#post_livetv_seriestimers) | **POST** /LiveTv/SeriesTimers | Creates a live tv series timer
[**post_livetv_seriestimers_by_id**](LiveTvServiceApi.md#post_livetv_seriestimers_by_id) | **POST** /LiveTv/SeriesTimers/{Id} | Updates a live tv series timer
[**post_livetv_timers**](LiveTvServiceApi.md#post_livetv_timers) | **POST** /LiveTv/Timers | Creates a live tv timer
[**post_livetv_timers_by_id**](LiveTvServiceApi.md#post_livetv_timers_by_id) | **POST** /LiveTv/Timers/{Id} | Updates a live tv timer
[**post_livetv_tunerhosts**](LiveTvServiceApi.md#post_livetv_tunerhosts) | **POST** /LiveTv/TunerHosts | Adds a tuner host
[**post_livetv_tuners_by_id_reset**](LiveTvServiceApi.md#post_livetv_tuners_by_id_reset) | **POST** /LiveTv/Tuners/{Id}/Reset | Resets a tv tuner
[**put_livetv_channelmappingoptions**](LiveTvServiceApi.md#put_livetv_channelmappingoptions) | **PUT** /LiveTv/ChannelMappingOptions | 
[**put_livetv_channelmappings**](LiveTvServiceApi.md#put_livetv_channelmappings) | **PUT** /LiveTv/ChannelMappings | 

# **delete_livetv_channelmappingoptions**
> delete_livetv_channelmappingoptions(provider_id)



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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))
provider_id = 'provider_id_example' # str | Provider id

try:
    api_instance.delete_livetv_channelmappingoptions(provider_id)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->delete_livetv_channelmappingoptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| Provider id | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_livetv_channelmappings**
> delete_livetv_channelmappings(provider_id)



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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))
provider_id = 'provider_id_example' # str | Provider id

try:
    api_instance.delete_livetv_channelmappings(provider_id)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->delete_livetv_channelmappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| Provider id | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_livetv_listingproviders**
> delete_livetv_listingproviders(id=id)

Deletes a listing provider

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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Provider id (optional)

try:
    # Deletes a listing provider
    api_instance.delete_livetv_listingproviders(id=id)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->delete_livetv_listingproviders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Provider id | [optional] 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_livetv_recordings_by_id**
> delete_livetv_recordings_by_id(id)

Deletes a live tv recording

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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Recording Id

try:
    # Deletes a live tv recording
    api_instance.delete_livetv_recordings_by_id(id)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->delete_livetv_recordings_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Recording Id | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_livetv_seriestimers_by_id**
> delete_livetv_seriestimers_by_id(id)

Cancels a live tv series timer

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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Timer Id

try:
    # Cancels a live tv series timer
    api_instance.delete_livetv_seriestimers_by_id(id)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->delete_livetv_seriestimers_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Timer Id | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_livetv_timers_by_id**
> delete_livetv_timers_by_id(id)

Cancels a live tv timer

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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Timer Id

try:
    # Cancels a live tv timer
    api_instance.delete_livetv_timers_by_id(id)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->delete_livetv_timers_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Timer Id | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_livetv_tunerhosts**
> delete_livetv_tunerhosts(id=id)

Deletes a tuner host

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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Tuner host id (optional)

try:
    # Deletes a tuner host
    api_instance.delete_livetv_tunerhosts(id=id)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->delete_livetv_tunerhosts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tuner host id | [optional] 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_channelmappingoptions**
> get_livetv_channelmappingoptions(provider_id)



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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))
provider_id = 'provider_id_example' # str | Provider id

try:
    api_instance.get_livetv_channelmappingoptions(provider_id)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->get_livetv_channelmappingoptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| Provider id | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_channelmappings**
> get_livetv_channelmappings(provider_id)



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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))
provider_id = 'provider_id_example' # str | Provider id

try:
    api_instance.get_livetv_channelmappings(provider_id)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->get_livetv_channelmappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| Provider id | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_channels**
> QueryResultBaseItemDto get_livetv_channels(type=type, user_id=user_id, start_index=start_index, is_movie=is_movie, is_series=is_series, is_news=is_news, is_kids=is_kids, is_sports=is_sports, limit=limit, is_favorite=is_favorite, is_liked=is_liked, is_disliked=is_disliked, enable_favorite_sorting=enable_favorite_sorting, enable_images=enable_images, image_type_limit=image_type_limit, enable_image_types=enable_image_types, fields=fields, add_current_program=add_current_program, enable_user_data=enable_user_data)

Gets available live tv channels.

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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))
type = 'type_example' # str | Optional filter by channel type. (optional)
user_id = 'user_id_example' # str | Optional filter by user and attach user data. (optional)
start_index = 56 # int | Optional. The record index to start at. All items with a lower index will be dropped from the results. (optional)
is_movie = true # bool | Optional filter for movies. (optional)
is_series = true # bool | Optional filter for movies. (optional)
is_news = true # bool | Optional filter for news. (optional)
is_kids = true # bool | Optional filter for kids. (optional)
is_sports = true # bool | Optional filter for sports. (optional)
limit = 56 # int | Optional. The maximum number of records to return (optional)
is_favorite = true # bool | Filter by channels that are favorites, or not. (optional)
is_liked = true # bool | Filter by channels that are liked, or not. (optional)
is_disliked = true # bool | Filter by channels that are disliked, or not. (optional)
enable_favorite_sorting = true # bool | Incorporate favorite and like status into channel sorting. (optional)
enable_images = true # bool | Optional, include image information in output (optional)
image_type_limit = 56 # int | Optional, the max number of images to return, per image type (optional)
enable_image_types = 'enable_image_types_example' # str | Optional. The image types to include in the output. (optional)
fields = 'fields_example' # str | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines (optional)
add_current_program = true # bool | Optional. Adds current program info to each channel (optional)
enable_user_data = true # bool | Optional, include user data (optional)

try:
    # Gets available live tv channels.
    api_response = api_instance.get_livetv_channels(type=type, user_id=user_id, start_index=start_index, is_movie=is_movie, is_series=is_series, is_news=is_news, is_kids=is_kids, is_sports=is_sports, limit=limit, is_favorite=is_favorite, is_liked=is_liked, is_disliked=is_disliked, enable_favorite_sorting=enable_favorite_sorting, enable_images=enable_images, image_type_limit=image_type_limit, enable_image_types=enable_image_types, fields=fields, add_current_program=add_current_program, enable_user_data=enable_user_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->get_livetv_channels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Optional filter by channel type. | [optional] 
 **user_id** | **str**| Optional filter by user and attach user data. | [optional] 
 **start_index** | **int**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **is_movie** | **bool**| Optional filter for movies. | [optional] 
 **is_series** | **bool**| Optional filter for movies. | [optional] 
 **is_news** | **bool**| Optional filter for news. | [optional] 
 **is_kids** | **bool**| Optional filter for kids. | [optional] 
 **is_sports** | **bool**| Optional filter for sports. | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return | [optional] 
 **is_favorite** | **bool**| Filter by channels that are favorites, or not. | [optional] 
 **is_liked** | **bool**| Filter by channels that are liked, or not. | [optional] 
 **is_disliked** | **bool**| Filter by channels that are disliked, or not. | [optional] 
 **enable_favorite_sorting** | **bool**| Incorporate favorite and like status into channel sorting. | [optional] 
 **enable_images** | **bool**| Optional, include image information in output | [optional] 
 **image_type_limit** | **int**| Optional, the max number of images to return, per image type | [optional] 
 **enable_image_types** | **str**| Optional. The image types to include in the output. | [optional] 
 **fields** | **str**| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines | [optional] 
 **add_current_program** | **bool**| Optional. Adds current program info to each channel | [optional] 
 **enable_user_data** | **bool**| Optional, include user data | [optional] 

### Return type

[**QueryResultBaseItemDto**](QueryResultBaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_channels_by_id**
> BaseItemDto get_livetv_channels_by_id(id, user_id=user_id)

Gets a live tv channel

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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Channel Id
user_id = 'user_id_example' # str | Optional attach user data. (optional)

try:
    # Gets a live tv channel
    api_response = api_instance.get_livetv_channels_by_id(id, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->get_livetv_channels_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Channel Id | 
 **user_id** | **str**| Optional attach user data. | [optional] 

### Return type

[**BaseItemDto**](BaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_guideinfo**
> LiveTvGuideInfo get_livetv_guideinfo()

Gets guide info

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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))

try:
    # Gets guide info
    api_response = api_instance.get_livetv_guideinfo()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->get_livetv_guideinfo: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LiveTvGuideInfo**](LiveTvGuideInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_info**
> LiveTvLiveTvInfo get_livetv_info()

Gets available live tv services.

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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))

try:
    # Gets available live tv services.
    api_response = api_instance.get_livetv_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->get_livetv_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LiveTvLiveTvInfo**](LiveTvLiveTvInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_listingproviders**
> list[LiveTvListingsProviderInfo] get_livetv_listingproviders()

Gets current listing providers

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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))

try:
    # Gets current listing providers
    api_response = api_instance.get_livetv_listingproviders()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->get_livetv_listingproviders: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[LiveTvListingsProviderInfo]**](LiveTvListingsProviderInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_listingproviders_available**
> list[LiveTvListingProviderTypeInfo] get_livetv_listingproviders_available()

Gets listing provider

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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))

try:
    # Gets listing provider
    api_response = api_instance.get_livetv_listingproviders_available()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->get_livetv_listingproviders_available: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[LiveTvListingProviderTypeInfo]**](LiveTvListingProviderTypeInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_listingproviders_default**
> LiveTvListingsProviderInfo get_livetv_listingproviders_default()



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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))

try:
    api_response = api_instance.get_livetv_listingproviders_default()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->get_livetv_listingproviders_default: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LiveTvListingsProviderInfo**](LiveTvListingsProviderInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_listingproviders_lineups**
> list[NameIdPair] get_livetv_listingproviders_lineups(id=id, type=type, location=location, country=country)

Gets available lineups

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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Provider id (optional)
type = 'type_example' # str | Provider Type (optional)
location = 'location_example' # str | Location (optional)
country = 'country_example' # str | Country (optional)

try:
    # Gets available lineups
    api_response = api_instance.get_livetv_listingproviders_lineups(id=id, type=type, location=location, country=country)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->get_livetv_listingproviders_lineups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Provider id | [optional] 
 **type** | **str**| Provider Type | [optional] 
 **location** | **str**| Location | [optional] 
 **country** | **str**| Country | [optional] 

### Return type

[**list[NameIdPair]**](NameIdPair.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_listingproviders_schedulesdirect_countries**
> get_livetv_listingproviders_schedulesdirect_countries()

Gets available lineups

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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))

try:
    # Gets available lineups
    api_instance.get_livetv_listingproviders_schedulesdirect_countries()
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->get_livetv_listingproviders_schedulesdirect_countries: %s\n" % e)
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

# **get_livetv_liverecordings_by_id_stream**
> get_livetv_liverecordings_by_id_stream(id)

Gets a live tv channel

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.LiveTvServiceApi()
id = 'id_example' # str | 

try:
    # Gets a live tv channel
    api_instance.get_livetv_liverecordings_by_id_stream(id)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->get_livetv_liverecordings_by_id_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_livestreamfiles_by_id_by_container**
> get_livetv_livestreamfiles_by_id_by_container(id, container)

Gets a live tv channel

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.LiveTvServiceApi()
id = 'id_example' # str | 
container = 'container_example' # str | 

try:
    # Gets a live tv channel
    api_instance.get_livetv_livestreamfiles_by_id_by_container(id, container)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->get_livetv_livestreamfiles_by_id_by_container: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **container** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_programs**
> QueryResultBaseItemDto get_livetv_programs(channel_ids=channel_ids, user_id=user_id, min_start_date=min_start_date, has_aired=has_aired, max_start_date=max_start_date, min_end_date=min_end_date, max_end_date=max_end_date, is_movie=is_movie, is_series=is_series, is_news=is_news, is_kids=is_kids, is_sports=is_sports, start_index=start_index, limit=limit, sort_by=sort_by, sort_order=sort_order, genre_ids=genre_ids, enable_images=enable_images, image_type_limit=image_type_limit, enable_image_types=enable_image_types, enable_user_data=enable_user_data, fields=fields)

Gets available live tv epgs..

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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))
channel_ids = 'channel_ids_example' # str | The channels to return guide information for. (optional)
user_id = 'user_id_example' # str | Optional filter by user id. (optional)
min_start_date = 'min_start_date_example' # str | Optional. The minimum premiere date. Format = ISO (optional)
has_aired = true # bool | Optional. Filter by programs that have completed airing, or not. (optional)
max_start_date = 'max_start_date_example' # str | Optional. The maximum premiere date. Format = ISO (optional)
min_end_date = 'min_end_date_example' # str | Optional. The minimum premiere date. Format = ISO (optional)
max_end_date = 'max_end_date_example' # str | Optional. The maximum premiere date. Format = ISO (optional)
is_movie = true # bool | Optional filter for movies. (optional)
is_series = true # bool | Optional filter for movies. (optional)
is_news = true # bool | Optional filter for news. (optional)
is_kids = true # bool | Optional filter for kids. (optional)
is_sports = true # bool | Optional filter for sports. (optional)
start_index = 56 # int | Optional. The record index to start at. All items with a lower index will be dropped from the results. (optional)
limit = 56 # int | Optional. The maximum number of records to return (optional)
sort_by = 'sort_by_example' # str | Optional. Specify one or more sort orders, comma delimeted. Options: Name, StartDate (optional)
sort_order = 'sort_order_example' # str | Sort Order - Ascending,Descending (optional)
genre_ids = 'genre_ids_example' # str | The genres to return guide information for. (optional)
enable_images = true # bool | Optional, include image information in output (optional)
image_type_limit = 56 # int | Optional, the max number of images to return, per image type (optional)
enable_image_types = 'enable_image_types_example' # str | Optional. The image types to include in the output. (optional)
enable_user_data = true # bool | Optional, include user data (optional)
fields = 'fields_example' # str | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines (optional)

try:
    # Gets available live tv epgs..
    api_response = api_instance.get_livetv_programs(channel_ids=channel_ids, user_id=user_id, min_start_date=min_start_date, has_aired=has_aired, max_start_date=max_start_date, min_end_date=min_end_date, max_end_date=max_end_date, is_movie=is_movie, is_series=is_series, is_news=is_news, is_kids=is_kids, is_sports=is_sports, start_index=start_index, limit=limit, sort_by=sort_by, sort_order=sort_order, genre_ids=genre_ids, enable_images=enable_images, image_type_limit=image_type_limit, enable_image_types=enable_image_types, enable_user_data=enable_user_data, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->get_livetv_programs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_ids** | **str**| The channels to return guide information for. | [optional] 
 **user_id** | **str**| Optional filter by user id. | [optional] 
 **min_start_date** | **str**| Optional. The minimum premiere date. Format &#x3D; ISO | [optional] 
 **has_aired** | **bool**| Optional. Filter by programs that have completed airing, or not. | [optional] 
 **max_start_date** | **str**| Optional. The maximum premiere date. Format &#x3D; ISO | [optional] 
 **min_end_date** | **str**| Optional. The minimum premiere date. Format &#x3D; ISO | [optional] 
 **max_end_date** | **str**| Optional. The maximum premiere date. Format &#x3D; ISO | [optional] 
 **is_movie** | **bool**| Optional filter for movies. | [optional] 
 **is_series** | **bool**| Optional filter for movies. | [optional] 
 **is_news** | **bool**| Optional filter for news. | [optional] 
 **is_kids** | **bool**| Optional filter for kids. | [optional] 
 **is_sports** | **bool**| Optional filter for sports. | [optional] 
 **start_index** | **int**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return | [optional] 
 **sort_by** | **str**| Optional. Specify one or more sort orders, comma delimeted. Options: Name, StartDate | [optional] 
 **sort_order** | **str**| Sort Order - Ascending,Descending | [optional] 
 **genre_ids** | **str**| The genres to return guide information for. | [optional] 
 **enable_images** | **bool**| Optional, include image information in output | [optional] 
 **image_type_limit** | **int**| Optional, the max number of images to return, per image type | [optional] 
 **enable_image_types** | **str**| Optional. The image types to include in the output. | [optional] 
 **enable_user_data** | **bool**| Optional, include user data | [optional] 
 **fields** | **str**| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines | [optional] 

### Return type

[**QueryResultBaseItemDto**](QueryResultBaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_programs_recommended**
> QueryResultBaseItemDto get_livetv_programs_recommended(user_id=user_id, limit=limit, is_airing=is_airing, has_aired=has_aired, is_series=is_series, is_movie=is_movie, is_news=is_news, is_kids=is_kids, is_sports=is_sports, enable_images=enable_images, image_type_limit=image_type_limit, enable_image_types=enable_image_types, genre_ids=genre_ids, fields=fields, enable_user_data=enable_user_data)

Gets available live tv epgs..

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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))
user_id = 'user_id_example' # str | Optional filter by user id. (optional)
limit = 56 # int | Optional. The maximum number of records to return (optional)
is_airing = true # bool | Optional. Filter by programs that are currently airing, or not. (optional)
has_aired = true # bool | Optional. Filter by programs that have completed airing, or not. (optional)
is_series = true # bool | Optional filter for movies. (optional)
is_movie = true # bool | Optional filter for movies. (optional)
is_news = true # bool | Optional filter for news. (optional)
is_kids = true # bool | Optional filter for kids. (optional)
is_sports = true # bool | Optional filter for sports. (optional)
enable_images = true # bool | Optional, include image information in output (optional)
image_type_limit = 56 # int | Optional, the max number of images to return, per image type (optional)
enable_image_types = 'enable_image_types_example' # str | Optional. The image types to include in the output. (optional)
genre_ids = 'genre_ids_example' # str | The genres to return guide information for. (optional)
fields = 'fields_example' # str | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines (optional)
enable_user_data = true # bool | Optional, include user data (optional)

try:
    # Gets available live tv epgs..
    api_response = api_instance.get_livetv_programs_recommended(user_id=user_id, limit=limit, is_airing=is_airing, has_aired=has_aired, is_series=is_series, is_movie=is_movie, is_news=is_news, is_kids=is_kids, is_sports=is_sports, enable_images=enable_images, image_type_limit=image_type_limit, enable_image_types=enable_image_types, genre_ids=genre_ids, fields=fields, enable_user_data=enable_user_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->get_livetv_programs_recommended: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Optional filter by user id. | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return | [optional] 
 **is_airing** | **bool**| Optional. Filter by programs that are currently airing, or not. | [optional] 
 **has_aired** | **bool**| Optional. Filter by programs that have completed airing, or not. | [optional] 
 **is_series** | **bool**| Optional filter for movies. | [optional] 
 **is_movie** | **bool**| Optional filter for movies. | [optional] 
 **is_news** | **bool**| Optional filter for news. | [optional] 
 **is_kids** | **bool**| Optional filter for kids. | [optional] 
 **is_sports** | **bool**| Optional filter for sports. | [optional] 
 **enable_images** | **bool**| Optional, include image information in output | [optional] 
 **image_type_limit** | **int**| Optional, the max number of images to return, per image type | [optional] 
 **enable_image_types** | **str**| Optional. The image types to include in the output. | [optional] 
 **genre_ids** | **str**| The genres to return guide information for. | [optional] 
 **fields** | **str**| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines | [optional] 
 **enable_user_data** | **bool**| Optional, include user data | [optional] 

### Return type

[**QueryResultBaseItemDto**](QueryResultBaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_recordings**
> get_livetv_recordings(channel_id=channel_id, status=status, is_in_progress=is_in_progress, series_timer_id=series_timer_id, artist_type=artist_type, max_official_rating=max_official_rating, has_theme_song=has_theme_song, has_theme_video=has_theme_video, has_subtitles=has_subtitles, has_special_feature=has_special_feature, has_trailer=has_trailer, adjacent_to=adjacent_to, min_index_number=min_index_number, min_players=min_players, max_players=max_players, parent_index_number=parent_index_number, has_parental_rating=has_parental_rating, is_hd=is_hd, location_types=location_types, exclude_location_types=exclude_location_types, is_missing=is_missing, is_unaired=is_unaired, min_community_rating=min_community_rating, min_critic_rating=min_critic_rating, aired_during_season=aired_during_season, min_premiere_date=min_premiere_date, min_date_last_saved=min_date_last_saved, min_date_last_saved_for_user=min_date_last_saved_for_user, max_premiere_date=max_premiere_date, has_overview=has_overview, has_imdb_id=has_imdb_id, has_tmdb_id=has_tmdb_id, has_tvdb_id=has_tvdb_id, exclude_item_ids=exclude_item_ids, start_index=start_index, limit=limit, recursive=recursive, sort_order=sort_order, parent_id=parent_id, fields=fields, exclude_item_types=exclude_item_types, include_item_types=include_item_types, any_provider_id_equals=any_provider_id_equals, filters=filters, is_favorite=is_favorite, is_movie=is_movie, is_series=is_series, is_news=is_news, is_kids=is_kids, is_sports=is_sports, media_types=media_types, image_types=image_types, sort_by=sort_by, is_played=is_played, genres=genres, official_ratings=official_ratings, tags=tags, years=years, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, person=person, person_ids=person_ids, person_types=person_types, studios=studios, studio_ids=studio_ids, artists=artists, artist_ids=artist_ids, albums=albums, ids=ids, video_types=video_types, containers=containers, audio_codecs=audio_codecs, video_codecs=video_codecs, subtitle_codecs=subtitle_codecs, path=path, user_id=user_id, min_official_rating=min_official_rating, is_locked=is_locked, is_place_holder=is_place_holder, has_official_rating=has_official_rating, group_items_into_collections=group_items_into_collections, is3_d=is3_d, series_status=series_status, name_starts_with_or_greater=name_starts_with_or_greater, name_starts_with=name_starts_with, name_less_than=name_less_than)

Gets live tv recordings

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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))
channel_id = 'channel_id_example' # str | Optional filter by channel id. (optional)
status = 'status_example' # str | Optional filter by recording status. (optional)
is_in_progress = true # bool | Optional filter by recordings that are in progress, or not. (optional)
series_timer_id = 'series_timer_id_example' # str | Optional filter by recordings belonging to a series timer (optional)
artist_type = 'artist_type_example' # str | Artist or AlbumArtist (optional)
max_official_rating = 'max_official_rating_example' # str | Optional filter by maximum official rating (PG, PG-13, TV-MA, etc). (optional)
has_theme_song = true # bool | Optional filter by items with theme songs. (optional)
has_theme_video = true # bool | Optional filter by items with theme videos. (optional)
has_subtitles = true # bool | Optional filter by items with subtitles. (optional)
has_special_feature = true # bool | Optional filter by items with special features. (optional)
has_trailer = true # bool | Optional filter by items with trailers. (optional)
adjacent_to = 'adjacent_to_example' # str | Optional. Return items that are siblings of a supplied item. (optional)
min_index_number = 56 # int | Optional filter by minimum index number. (optional)
min_players = 56 # int | Optional filter by minimum number of game players. (optional)
max_players = 56 # int | Optional filter by maximum number of game players. (optional)
parent_index_number = 56 # int | Optional filter by parent index number. (optional)
has_parental_rating = true # bool | Optional filter by items that have or do not have a parental rating (optional)
is_hd = true # bool | Optional filter by items that are HD or not. (optional)
location_types = 'location_types_example' # str | Optional. If specified, results will be filtered based on LocationType. This allows multiple, comma delimeted. (optional)
exclude_location_types = 'exclude_location_types_example' # str | Optional. If specified, results will be filtered based on LocationType. This allows multiple, comma delimeted. (optional)
is_missing = true # bool | Optional filter by items that are missing episodes or not. (optional)
is_unaired = true # bool | Optional filter by items that are unaired episodes or not. (optional)
min_community_rating = 1.2 # float | Optional filter by minimum community rating. (optional)
min_critic_rating = 1.2 # float | Optional filter by minimum critic rating. (optional)
aired_during_season = 56 # int | Gets all episodes that aired during a season, including specials. (optional)
min_premiere_date = 'min_premiere_date_example' # str | Optional. The minimum premiere date. Format = ISO (optional)
min_date_last_saved = 'min_date_last_saved_example' # str | Optional. The minimum premiere date. Format = ISO (optional)
min_date_last_saved_for_user = 'min_date_last_saved_for_user_example' # str | Optional. The minimum premiere date. Format = ISO (optional)
max_premiere_date = 'max_premiere_date_example' # str | Optional. The maximum premiere date. Format = ISO (optional)
has_overview = true # bool | Optional filter by items that have an overview or not. (optional)
has_imdb_id = true # bool | Optional filter by items that have an imdb id or not. (optional)
has_tmdb_id = true # bool | Optional filter by items that have a tmdb id or not. (optional)
has_tvdb_id = true # bool | Optional filter by items that have a tvdb id or not. (optional)
exclude_item_ids = 'exclude_item_ids_example' # str | Optional. If specified, results will be filtered by exxcluding item ids. This allows multiple, comma delimeted. (optional)
start_index = 56 # int | Optional. The record index to start at. All items with a lower index will be dropped from the results. (optional)
limit = 56 # int | Optional. The maximum number of records to return (optional)
recursive = true # bool | When searching within folders, this determines whether or not the search will be recursive. true/false (optional)
sort_order = 'sort_order_example' # str | Sort Order - Ascending,Descending (optional)
parent_id = 'parent_id_example' # str | Specify this to localize the search to a specific item or folder. Omit to use the root (optional)
fields = 'fields_example' # str | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines (optional)
exclude_item_types = 'exclude_item_types_example' # str | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. (optional)
include_item_types = 'include_item_types_example' # str | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. (optional)
any_provider_id_equals = 'any_provider_id_equals_example' # str | Optional. If specified, result will be filtered to contain only items which match at least one of the specified IDs. Each provider ID must be in the form 'prov.id', e.g. 'imdb.tt123456'. This allows multiple, comma delimeted value pairs. (optional)
filters = 'filters_example' # str | Optional. Specify additional filters to apply. This allows multiple, comma delimeted. Options: IsFolder, IsNotFolder, IsUnplayed, IsPlayed, IsFavorite, IsResumable, Likes, Dislikes (optional)
is_favorite = true # bool | Optional filter by items that are marked as favorite, or not. (optional)
is_movie = true # bool | Optional filter for movies. (optional)
is_series = true # bool | Optional filter for movies. (optional)
is_news = true # bool | Optional filter for news. (optional)
is_kids = true # bool | Optional filter for kids. (optional)
is_sports = true # bool | Optional filter for sports. (optional)
media_types = 'media_types_example' # str | Optional filter by MediaType. Allows multiple, comma delimited. (optional)
image_types = 'image_types_example' # str | Optional. If specified, results will be filtered based on those containing image types. This allows multiple, comma delimited. (optional)
sort_by = 'sort_by_example' # str | Optional. Specify one or more sort orders, comma delimeted. Options: Album, AlbumArtist, Artist, Budget, CommunityRating, CriticRating, DateCreated, DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName, Random, Revenue, Runtime (optional)
is_played = true # bool | Optional filter by items that are played, or not. (optional)
genres = 'genres_example' # str | Optional. If specified, results will be filtered based on genre. This allows multiple, pipe delimeted. (optional)
official_ratings = 'official_ratings_example' # str | Optional. If specified, results will be filtered based on OfficialRating. This allows multiple, pipe delimeted. (optional)
tags = 'tags_example' # str | Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimeted. (optional)
years = 'years_example' # str | Optional. If specified, results will be filtered based on production year. This allows multiple, comma delimeted. (optional)
enable_images = true # bool | Optional, include image information in output (optional)
enable_user_data = true # bool | Optional, include user data (optional)
image_type_limit = 56 # int | Optional, the max number of images to return, per image type (optional)
enable_image_types = 'enable_image_types_example' # str | Optional. The image types to include in the output. (optional)
person = 'person_example' # str | Optional. If specified, results will be filtered to include only those containing the specified person. (optional)
person_ids = 'person_ids_example' # str | Optional. If specified, results will be filtered to include only those containing the specified person. (optional)
person_types = 'person_types_example' # str | Optional. If specified, along with Person, results will be filtered to include only those containing the specified person and PersonType. Allows multiple, comma-delimited (optional)
studios = 'studios_example' # str | Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimeted. (optional)
studio_ids = 'studio_ids_example' # str | Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimeted. (optional)
artists = 'artists_example' # str | Optional. If specified, results will be filtered based on artist. This allows multiple, pipe delimeted. (optional)
artist_ids = 'artist_ids_example' # str | Optional. If specified, results will be filtered based on artist. This allows multiple, pipe delimeted. (optional)
albums = 'albums_example' # str | Optional. If specified, results will be filtered based on album. This allows multiple, pipe delimeted. (optional)
ids = 'ids_example' # str | Optional. If specific items are needed, specify a list of item id's to retrieve. This allows multiple, comma delimited. (optional)
video_types = 'video_types_example' # str | Optional filter by VideoType (videofile, dvd, bluray, iso). Allows multiple, comma delimeted. (optional)
containers = 'containers_example' # str | Optional filter by Container. Allows multiple, comma delimeted. (optional)
audio_codecs = 'audio_codecs_example' # str | Optional filter by AudioCodec. Allows multiple, comma delimeted. (optional)
video_codecs = 'video_codecs_example' # str | Optional filter by VideoCodec. Allows multiple, comma delimeted. (optional)
subtitle_codecs = 'subtitle_codecs_example' # str | Optional filter by SubtitleCodec. Allows multiple, comma delimeted. (optional)
path = 'path_example' # str | Optional filter by Path. (optional)
user_id = 'user_id_example' # str | User Id (optional)
min_official_rating = 'min_official_rating_example' # str | Optional filter by minimum official rating (PG, PG-13, TV-MA, etc). (optional)
is_locked = true # bool | Optional filter by items that are locked. (optional)
is_place_holder = true # bool | Optional filter by items that are placeholders (optional)
has_official_rating = true # bool | Optional filter by items that have official ratings (optional)
group_items_into_collections = true # bool | Whether or not to hide items behind their boxsets. (optional)
is3_d = true # bool | Optional filter by items that are 3D, or not. (optional)
series_status = 'series_status_example' # str | Optional filter by Series Status. Allows multiple, comma delimeted. (optional)
name_starts_with_or_greater = 'name_starts_with_or_greater_example' # str | Optional filter by items whose name is sorted equally or greater than a given input string. (optional)
name_starts_with = 'name_starts_with_example' # str | Optional filter by items whose name is sorted equally than a given input string. (optional)
name_less_than = 'name_less_than_example' # str | Optional filter by items whose name is equally or lesser than a given input string. (optional)

try:
    # Gets live tv recordings
    api_instance.get_livetv_recordings(channel_id=channel_id, status=status, is_in_progress=is_in_progress, series_timer_id=series_timer_id, artist_type=artist_type, max_official_rating=max_official_rating, has_theme_song=has_theme_song, has_theme_video=has_theme_video, has_subtitles=has_subtitles, has_special_feature=has_special_feature, has_trailer=has_trailer, adjacent_to=adjacent_to, min_index_number=min_index_number, min_players=min_players, max_players=max_players, parent_index_number=parent_index_number, has_parental_rating=has_parental_rating, is_hd=is_hd, location_types=location_types, exclude_location_types=exclude_location_types, is_missing=is_missing, is_unaired=is_unaired, min_community_rating=min_community_rating, min_critic_rating=min_critic_rating, aired_during_season=aired_during_season, min_premiere_date=min_premiere_date, min_date_last_saved=min_date_last_saved, min_date_last_saved_for_user=min_date_last_saved_for_user, max_premiere_date=max_premiere_date, has_overview=has_overview, has_imdb_id=has_imdb_id, has_tmdb_id=has_tmdb_id, has_tvdb_id=has_tvdb_id, exclude_item_ids=exclude_item_ids, start_index=start_index, limit=limit, recursive=recursive, sort_order=sort_order, parent_id=parent_id, fields=fields, exclude_item_types=exclude_item_types, include_item_types=include_item_types, any_provider_id_equals=any_provider_id_equals, filters=filters, is_favorite=is_favorite, is_movie=is_movie, is_series=is_series, is_news=is_news, is_kids=is_kids, is_sports=is_sports, media_types=media_types, image_types=image_types, sort_by=sort_by, is_played=is_played, genres=genres, official_ratings=official_ratings, tags=tags, years=years, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, person=person, person_ids=person_ids, person_types=person_types, studios=studios, studio_ids=studio_ids, artists=artists, artist_ids=artist_ids, albums=albums, ids=ids, video_types=video_types, containers=containers, audio_codecs=audio_codecs, video_codecs=video_codecs, subtitle_codecs=subtitle_codecs, path=path, user_id=user_id, min_official_rating=min_official_rating, is_locked=is_locked, is_place_holder=is_place_holder, has_official_rating=has_official_rating, group_items_into_collections=group_items_into_collections, is3_d=is3_d, series_status=series_status, name_starts_with_or_greater=name_starts_with_or_greater, name_starts_with=name_starts_with, name_less_than=name_less_than)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->get_livetv_recordings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Optional filter by channel id. | [optional] 
 **status** | **str**| Optional filter by recording status. | [optional] 
 **is_in_progress** | **bool**| Optional filter by recordings that are in progress, or not. | [optional] 
 **series_timer_id** | **str**| Optional filter by recordings belonging to a series timer | [optional] 
 **artist_type** | **str**| Artist or AlbumArtist | [optional] 
 **max_official_rating** | **str**| Optional filter by maximum official rating (PG, PG-13, TV-MA, etc). | [optional] 
 **has_theme_song** | **bool**| Optional filter by items with theme songs. | [optional] 
 **has_theme_video** | **bool**| Optional filter by items with theme videos. | [optional] 
 **has_subtitles** | **bool**| Optional filter by items with subtitles. | [optional] 
 **has_special_feature** | **bool**| Optional filter by items with special features. | [optional] 
 **has_trailer** | **bool**| Optional filter by items with trailers. | [optional] 
 **adjacent_to** | **str**| Optional. Return items that are siblings of a supplied item. | [optional] 
 **min_index_number** | **int**| Optional filter by minimum index number. | [optional] 
 **min_players** | **int**| Optional filter by minimum number of game players. | [optional] 
 **max_players** | **int**| Optional filter by maximum number of game players. | [optional] 
 **parent_index_number** | **int**| Optional filter by parent index number. | [optional] 
 **has_parental_rating** | **bool**| Optional filter by items that have or do not have a parental rating | [optional] 
 **is_hd** | **bool**| Optional filter by items that are HD or not. | [optional] 
 **location_types** | **str**| Optional. If specified, results will be filtered based on LocationType. This allows multiple, comma delimeted. | [optional] 
 **exclude_location_types** | **str**| Optional. If specified, results will be filtered based on LocationType. This allows multiple, comma delimeted. | [optional] 
 **is_missing** | **bool**| Optional filter by items that are missing episodes or not. | [optional] 
 **is_unaired** | **bool**| Optional filter by items that are unaired episodes or not. | [optional] 
 **min_community_rating** | **float**| Optional filter by minimum community rating. | [optional] 
 **min_critic_rating** | **float**| Optional filter by minimum critic rating. | [optional] 
 **aired_during_season** | **int**| Gets all episodes that aired during a season, including specials. | [optional] 
 **min_premiere_date** | **str**| Optional. The minimum premiere date. Format &#x3D; ISO | [optional] 
 **min_date_last_saved** | **str**| Optional. The minimum premiere date. Format &#x3D; ISO | [optional] 
 **min_date_last_saved_for_user** | **str**| Optional. The minimum premiere date. Format &#x3D; ISO | [optional] 
 **max_premiere_date** | **str**| Optional. The maximum premiere date. Format &#x3D; ISO | [optional] 
 **has_overview** | **bool**| Optional filter by items that have an overview or not. | [optional] 
 **has_imdb_id** | **bool**| Optional filter by items that have an imdb id or not. | [optional] 
 **has_tmdb_id** | **bool**| Optional filter by items that have a tmdb id or not. | [optional] 
 **has_tvdb_id** | **bool**| Optional filter by items that have a tvdb id or not. | [optional] 
 **exclude_item_ids** | **str**| Optional. If specified, results will be filtered by exxcluding item ids. This allows multiple, comma delimeted. | [optional] 
 **start_index** | **int**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return | [optional] 
 **recursive** | **bool**| When searching within folders, this determines whether or not the search will be recursive. true/false | [optional] 
 **sort_order** | **str**| Sort Order - Ascending,Descending | [optional] 
 **parent_id** | **str**| Specify this to localize the search to a specific item or folder. Omit to use the root | [optional] 
 **fields** | **str**| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines | [optional] 
 **exclude_item_types** | **str**| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. | [optional] 
 **include_item_types** | **str**| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. | [optional] 
 **any_provider_id_equals** | **str**| Optional. If specified, result will be filtered to contain only items which match at least one of the specified IDs. Each provider ID must be in the form &#x27;prov.id&#x27;, e.g. &#x27;imdb.tt123456&#x27;. This allows multiple, comma delimeted value pairs. | [optional] 
 **filters** | **str**| Optional. Specify additional filters to apply. This allows multiple, comma delimeted. Options: IsFolder, IsNotFolder, IsUnplayed, IsPlayed, IsFavorite, IsResumable, Likes, Dislikes | [optional] 
 **is_favorite** | **bool**| Optional filter by items that are marked as favorite, or not. | [optional] 
 **is_movie** | **bool**| Optional filter for movies. | [optional] 
 **is_series** | **bool**| Optional filter for movies. | [optional] 
 **is_news** | **bool**| Optional filter for news. | [optional] 
 **is_kids** | **bool**| Optional filter for kids. | [optional] 
 **is_sports** | **bool**| Optional filter for sports. | [optional] 
 **media_types** | **str**| Optional filter by MediaType. Allows multiple, comma delimited. | [optional] 
 **image_types** | **str**| Optional. If specified, results will be filtered based on those containing image types. This allows multiple, comma delimited. | [optional] 
 **sort_by** | **str**| Optional. Specify one or more sort orders, comma delimeted. Options: Album, AlbumArtist, Artist, Budget, CommunityRating, CriticRating, DateCreated, DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName, Random, Revenue, Runtime | [optional] 
 **is_played** | **bool**| Optional filter by items that are played, or not. | [optional] 
 **genres** | **str**| Optional. If specified, results will be filtered based on genre. This allows multiple, pipe delimeted. | [optional] 
 **official_ratings** | **str**| Optional. If specified, results will be filtered based on OfficialRating. This allows multiple, pipe delimeted. | [optional] 
 **tags** | **str**| Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimeted. | [optional] 
 **years** | **str**| Optional. If specified, results will be filtered based on production year. This allows multiple, comma delimeted. | [optional] 
 **enable_images** | **bool**| Optional, include image information in output | [optional] 
 **enable_user_data** | **bool**| Optional, include user data | [optional] 
 **image_type_limit** | **int**| Optional, the max number of images to return, per image type | [optional] 
 **enable_image_types** | **str**| Optional. The image types to include in the output. | [optional] 
 **person** | **str**| Optional. If specified, results will be filtered to include only those containing the specified person. | [optional] 
 **person_ids** | **str**| Optional. If specified, results will be filtered to include only those containing the specified person. | [optional] 
 **person_types** | **str**| Optional. If specified, along with Person, results will be filtered to include only those containing the specified person and PersonType. Allows multiple, comma-delimited | [optional] 
 **studios** | **str**| Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimeted. | [optional] 
 **studio_ids** | **str**| Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimeted. | [optional] 
 **artists** | **str**| Optional. If specified, results will be filtered based on artist. This allows multiple, pipe delimeted. | [optional] 
 **artist_ids** | **str**| Optional. If specified, results will be filtered based on artist. This allows multiple, pipe delimeted. | [optional] 
 **albums** | **str**| Optional. If specified, results will be filtered based on album. This allows multiple, pipe delimeted. | [optional] 
 **ids** | **str**| Optional. If specific items are needed, specify a list of item id&#x27;s to retrieve. This allows multiple, comma delimited. | [optional] 
 **video_types** | **str**| Optional filter by VideoType (videofile, dvd, bluray, iso). Allows multiple, comma delimeted. | [optional] 
 **containers** | **str**| Optional filter by Container. Allows multiple, comma delimeted. | [optional] 
 **audio_codecs** | **str**| Optional filter by AudioCodec. Allows multiple, comma delimeted. | [optional] 
 **video_codecs** | **str**| Optional filter by VideoCodec. Allows multiple, comma delimeted. | [optional] 
 **subtitle_codecs** | **str**| Optional filter by SubtitleCodec. Allows multiple, comma delimeted. | [optional] 
 **path** | **str**| Optional filter by Path. | [optional] 
 **user_id** | **str**| User Id | [optional] 
 **min_official_rating** | **str**| Optional filter by minimum official rating (PG, PG-13, TV-MA, etc). | [optional] 
 **is_locked** | **bool**| Optional filter by items that are locked. | [optional] 
 **is_place_holder** | **bool**| Optional filter by items that are placeholders | [optional] 
 **has_official_rating** | **bool**| Optional filter by items that have official ratings | [optional] 
 **group_items_into_collections** | **bool**| Whether or not to hide items behind their boxsets. | [optional] 
 **is3_d** | **bool**| Optional filter by items that are 3D, or not. | [optional] 
 **series_status** | **str**| Optional filter by Series Status. Allows multiple, comma delimeted. | [optional] 
 **name_starts_with_or_greater** | **str**| Optional filter by items whose name is sorted equally or greater than a given input string. | [optional] 
 **name_starts_with** | **str**| Optional filter by items whose name is sorted equally than a given input string. | [optional] 
 **name_less_than** | **str**| Optional filter by items whose name is equally or lesser than a given input string. | [optional] 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_recordings_by_id**
> BaseItemDto get_livetv_recordings_by_id(id, user_id=user_id)

Gets a live tv recording

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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Recording Id
user_id = 'user_id_example' # str | Optional attach user data. (optional)

try:
    # Gets a live tv recording
    api_response = api_instance.get_livetv_recordings_by_id(id, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->get_livetv_recordings_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Recording Id | 
 **user_id** | **str**| Optional attach user data. | [optional] 

### Return type

[**BaseItemDto**](BaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_recordings_folders**
> list[BaseItemDto] get_livetv_recordings_folders(user_id=user_id)

Gets recording folders

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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))
user_id = 'user_id_example' # str | Optional filter by user and attach user data. (optional)

try:
    # Gets recording folders
    api_response = api_instance.get_livetv_recordings_folders(user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->get_livetv_recordings_folders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Optional filter by user and attach user data. | [optional] 

### Return type

[**list[BaseItemDto]**](BaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_recordings_groups**
> QueryResultBaseItemDto get_livetv_recordings_groups(user_id=user_id)

Gets live tv recording groups

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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))
user_id = 'user_id_example' # str | Optional filter by user and attach user data. (optional)

try:
    # Gets live tv recording groups
    api_response = api_instance.get_livetv_recordings_groups(user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->get_livetv_recordings_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Optional filter by user and attach user data. | [optional] 

### Return type

[**QueryResultBaseItemDto**](QueryResultBaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_recordings_groups_by_id**
> BaseItemDto get_livetv_recordings_groups_by_id(id)

Gets a recording group

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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Recording group Id

try:
    # Gets a recording group
    api_response = api_instance.get_livetv_recordings_groups_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->get_livetv_recordings_groups_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Recording group Id | 

### Return type

[**BaseItemDto**](BaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_recordings_series**
> QueryResultBaseItemDto get_livetv_recordings_series(channel_id=channel_id, user_id=user_id, group_id=group_id, start_index=start_index, limit=limit, status=status, is_in_progress=is_in_progress, series_timer_id=series_timer_id, enable_images=enable_images, image_type_limit=image_type_limit, enable_image_types=enable_image_types, fields=fields, enable_user_data=enable_user_data)

Gets live tv recordings

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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))
channel_id = 'channel_id_example' # str | Optional filter by channel id. (optional)
user_id = 'user_id_example' # str | Optional filter by user and attach user data. (optional)
group_id = 'group_id_example' # str | Optional filter by recording group. (optional)
start_index = 56 # int | Optional. The record index to start at. All items with a lower index will be dropped from the results. (optional)
limit = 56 # int | Optional. The maximum number of records to return (optional)
status = 'status_example' # str | Optional filter by recording status. (optional)
is_in_progress = true # bool | Optional filter by recordings that are in progress, or not. (optional)
series_timer_id = 'series_timer_id_example' # str | Optional filter by recordings belonging to a series timer (optional)
enable_images = true # bool | Optional, include image information in output (optional)
image_type_limit = 56 # int | Optional, the max number of images to return, per image type (optional)
enable_image_types = 'enable_image_types_example' # str | Optional. The image types to include in the output. (optional)
fields = 'fields_example' # str | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines (optional)
enable_user_data = true # bool | Optional, include user data (optional)

try:
    # Gets live tv recordings
    api_response = api_instance.get_livetv_recordings_series(channel_id=channel_id, user_id=user_id, group_id=group_id, start_index=start_index, limit=limit, status=status, is_in_progress=is_in_progress, series_timer_id=series_timer_id, enable_images=enable_images, image_type_limit=image_type_limit, enable_image_types=enable_image_types, fields=fields, enable_user_data=enable_user_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->get_livetv_recordings_series: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Optional filter by channel id. | [optional] 
 **user_id** | **str**| Optional filter by user and attach user data. | [optional] 
 **group_id** | **str**| Optional filter by recording group. | [optional] 
 **start_index** | **int**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return | [optional] 
 **status** | **str**| Optional filter by recording status. | [optional] 
 **is_in_progress** | **bool**| Optional filter by recordings that are in progress, or not. | [optional] 
 **series_timer_id** | **str**| Optional filter by recordings belonging to a series timer | [optional] 
 **enable_images** | **bool**| Optional, include image information in output | [optional] 
 **image_type_limit** | **int**| Optional, the max number of images to return, per image type | [optional] 
 **enable_image_types** | **str**| Optional. The image types to include in the output. | [optional] 
 **fields** | **str**| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines | [optional] 
 **enable_user_data** | **bool**| Optional, include user data | [optional] 

### Return type

[**QueryResultBaseItemDto**](QueryResultBaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_seriestimers**
> QueryResultLiveTvSeriesTimerInfoDto get_livetv_seriestimers(sort_by=sort_by, sort_order=sort_order)

Gets live tv series timers

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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))
sort_by = 'sort_by_example' # str | Optional. Sort by SortName or Priority (optional)
sort_order = 'sort_order_example' # str | Optional. Sort in Ascending or Descending order (optional)

try:
    # Gets live tv series timers
    api_response = api_instance.get_livetv_seriestimers(sort_by=sort_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->get_livetv_seriestimers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort_by** | **str**| Optional. Sort by SortName or Priority | [optional] 
 **sort_order** | **str**| Optional. Sort in Ascending or Descending order | [optional] 

### Return type

[**QueryResultLiveTvSeriesTimerInfoDto**](QueryResultLiveTvSeriesTimerInfoDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_seriestimers_by_id**
> LiveTvTimerInfoDto get_livetv_seriestimers_by_id(id)

Gets a live tv series timer

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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Timer Id

try:
    # Gets a live tv series timer
    api_response = api_instance.get_livetv_seriestimers_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->get_livetv_seriestimers_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Timer Id | 

### Return type

[**LiveTvTimerInfoDto**](LiveTvTimerInfoDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_timers**
> QueryResultLiveTvTimerInfoDto get_livetv_timers(channel_id=channel_id, series_timer_id=series_timer_id)

Gets live tv timers

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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))
channel_id = 'channel_id_example' # str | Optional filter by channel id. (optional)
series_timer_id = 'series_timer_id_example' # str | Optional filter by timers belonging to a series timer (optional)

try:
    # Gets live tv timers
    api_response = api_instance.get_livetv_timers(channel_id=channel_id, series_timer_id=series_timer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->get_livetv_timers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Optional filter by channel id. | [optional] 
 **series_timer_id** | **str**| Optional filter by timers belonging to a series timer | [optional] 

### Return type

[**QueryResultLiveTvTimerInfoDto**](QueryResultLiveTvTimerInfoDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_timers_by_id**
> LiveTvTimerInfoDto get_livetv_timers_by_id(id)

Gets a live tv timer

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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Timer Id

try:
    # Gets a live tv timer
    api_response = api_instance.get_livetv_timers_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->get_livetv_timers_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Timer Id | 

### Return type

[**LiveTvTimerInfoDto**](LiveTvTimerInfoDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_timers_defaults**
> LiveTvSeriesTimerInfoDto get_livetv_timers_defaults(program_id=program_id)

Gets default values for a new timer

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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))
program_id = 'program_id_example' # str | Optional, to attach default values based on a program. (optional)

try:
    # Gets default values for a new timer
    api_response = api_instance.get_livetv_timers_defaults(program_id=program_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->get_livetv_timers_defaults: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Optional, to attach default values based on a program. | [optional] 

### Return type

[**LiveTvSeriesTimerInfoDto**](LiveTvSeriesTimerInfoDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_tunerhosts**
> list[LiveTvTunerHostInfo] get_livetv_tunerhosts()

Gets tuner hosts

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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))

try:
    # Gets tuner hosts
    api_response = api_instance.get_livetv_tunerhosts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->get_livetv_tunerhosts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[LiveTvTunerHostInfo]**](LiveTvTunerHostInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_tunerhosts_types**
> list[NameIdPair] get_livetv_tunerhosts_types()



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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))

try:
    api_response = api_instance.get_livetv_tunerhosts_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->get_livetv_tunerhosts_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[NameIdPair]**](NameIdPair.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_tuners_discvover**
> list[LiveTvTunerHostInfo] get_livetv_tuners_discvover()



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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))

try:
    api_response = api_instance.get_livetv_tuners_discvover()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->get_livetv_tuners_discvover: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[LiveTvTunerHostInfo]**](LiveTvTunerHostInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_livetv_channelmappingoptions**
> head_livetv_channelmappingoptions(provider_id)



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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))
provider_id = 'provider_id_example' # str | Provider id

try:
    api_instance.head_livetv_channelmappingoptions(provider_id)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->head_livetv_channelmappingoptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| Provider id | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_livetv_channelmappings**
> head_livetv_channelmappings(provider_id)



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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))
provider_id = 'provider_id_example' # str | Provider id

try:
    api_instance.head_livetv_channelmappings(provider_id)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->head_livetv_channelmappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| Provider id | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **options_livetv_channelmappingoptions**
> options_livetv_channelmappingoptions(provider_id)



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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))
provider_id = 'provider_id_example' # str | Provider id

try:
    api_instance.options_livetv_channelmappingoptions(provider_id)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->options_livetv_channelmappingoptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| Provider id | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **options_livetv_channelmappings**
> options_livetv_channelmappings(provider_id)



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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))
provider_id = 'provider_id_example' # str | Provider id

try:
    api_instance.options_livetv_channelmappings(provider_id)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->options_livetv_channelmappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| Provider id | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_livetv_channelmappingoptions**
> patch_livetv_channelmappingoptions(provider_id)



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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))
provider_id = 'provider_id_example' # str | Provider id

try:
    api_instance.patch_livetv_channelmappingoptions(provider_id)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->patch_livetv_channelmappingoptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| Provider id | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_livetv_channelmappings**
> patch_livetv_channelmappings(provider_id)



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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))
provider_id = 'provider_id_example' # str | Provider id

try:
    api_instance.patch_livetv_channelmappings(provider_id)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->patch_livetv_channelmappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| Provider id | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_livetv_channelmappingoptions**
> post_livetv_channelmappingoptions(provider_id)



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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))
provider_id = 'provider_id_example' # str | Provider id

try:
    api_instance.post_livetv_channelmappingoptions(provider_id)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->post_livetv_channelmappingoptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| Provider id | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_livetv_channelmappings**
> post_livetv_channelmappings(body, provider_id)



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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))
body = embyapi.LiveTvSetChannelMapping() # LiveTvSetChannelMapping | SetChannelMapping
provider_id = 'provider_id_example' # str | Provider id

try:
    api_instance.post_livetv_channelmappings(body, provider_id)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->post_livetv_channelmappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LiveTvSetChannelMapping**](LiveTvSetChannelMapping.md)| SetChannelMapping | 
 **provider_id** | **str**| Provider id | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_livetv_listingproviders**
> LiveTvListingsProviderInfo post_livetv_listingproviders(body)

Adds a listing provider

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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))
body = embyapi.LiveTvListingsProviderInfo() # LiveTvListingsProviderInfo | ListingsProviderInfo: 

try:
    # Adds a listing provider
    api_response = api_instance.post_livetv_listingproviders(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->post_livetv_listingproviders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LiveTvListingsProviderInfo**](LiveTvListingsProviderInfo.md)| ListingsProviderInfo:  | 

### Return type

[**LiveTvListingsProviderInfo**](LiveTvListingsProviderInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_livetv_programs**
> QueryResultBaseItemDto post_livetv_programs(body, channel_ids=channel_ids, user_id=user_id, min_start_date=min_start_date, max_start_date=max_start_date, min_end_date=min_end_date, max_end_date=max_end_date, is_movie=is_movie, is_series=is_series, is_news=is_news, is_kids=is_kids, is_sports=is_sports, genre_ids=genre_ids)

Gets available live tv epgs..

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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))
body = embyapi.LiveTvGetPrograms() # LiveTvGetPrograms | GetPrograms
channel_ids = 'channel_ids_example' # str | The channels to return guide information for. (optional)
user_id = 'user_id_example' # str | Optional filter by user id. (optional)
min_start_date = 'min_start_date_example' # str | Optional. The minimum premiere date. Format = ISO (optional)
max_start_date = 'max_start_date_example' # str | Optional. The maximum premiere date. Format = ISO (optional)
min_end_date = 'min_end_date_example' # str | Optional. The minimum premiere date. Format = ISO (optional)
max_end_date = 'max_end_date_example' # str | Optional. The maximum premiere date. Format = ISO (optional)
is_movie = true # bool | Optional filter for movies. (optional)
is_series = true # bool | Optional filter for movies. (optional)
is_news = true # bool | Optional filter for news. (optional)
is_kids = true # bool | Optional filter for kids. (optional)
is_sports = true # bool | Optional filter for sports. (optional)
genre_ids = 'genre_ids_example' # str | The genres to return guide information for. (optional)

try:
    # Gets available live tv epgs..
    api_response = api_instance.post_livetv_programs(body, channel_ids=channel_ids, user_id=user_id, min_start_date=min_start_date, max_start_date=max_start_date, min_end_date=min_end_date, max_end_date=max_end_date, is_movie=is_movie, is_series=is_series, is_news=is_news, is_kids=is_kids, is_sports=is_sports, genre_ids=genre_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->post_livetv_programs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LiveTvGetPrograms**](LiveTvGetPrograms.md)| GetPrograms | 
 **channel_ids** | **str**| The channels to return guide information for. | [optional] 
 **user_id** | **str**| Optional filter by user id. | [optional] 
 **min_start_date** | **str**| Optional. The minimum premiere date. Format &#x3D; ISO | [optional] 
 **max_start_date** | **str**| Optional. The maximum premiere date. Format &#x3D; ISO | [optional] 
 **min_end_date** | **str**| Optional. The minimum premiere date. Format &#x3D; ISO | [optional] 
 **max_end_date** | **str**| Optional. The maximum premiere date. Format &#x3D; ISO | [optional] 
 **is_movie** | **bool**| Optional filter for movies. | [optional] 
 **is_series** | **bool**| Optional filter for movies. | [optional] 
 **is_news** | **bool**| Optional filter for news. | [optional] 
 **is_kids** | **bool**| Optional filter for kids. | [optional] 
 **is_sports** | **bool**| Optional filter for sports. | [optional] 
 **genre_ids** | **str**| The genres to return guide information for. | [optional] 

### Return type

[**QueryResultBaseItemDto**](QueryResultBaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_livetv_seriestimers**
> post_livetv_seriestimers(body)

Creates a live tv series timer

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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))
body = embyapi.LiveTvSeriesTimerInfoDto() # LiveTvSeriesTimerInfoDto | SeriesTimerInfoDto: 

try:
    # Creates a live tv series timer
    api_instance.post_livetv_seriestimers(body)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->post_livetv_seriestimers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LiveTvSeriesTimerInfoDto**](LiveTvSeriesTimerInfoDto.md)| SeriesTimerInfoDto:  | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_livetv_seriestimers_by_id**
> post_livetv_seriestimers_by_id(body, id)

Updates a live tv series timer

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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))
body = embyapi.LiveTvSeriesTimerInfoDto() # LiveTvSeriesTimerInfoDto | SeriesTimerInfoDto: 
id = 'id_example' # str | 

try:
    # Updates a live tv series timer
    api_instance.post_livetv_seriestimers_by_id(body, id)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->post_livetv_seriestimers_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LiveTvSeriesTimerInfoDto**](LiveTvSeriesTimerInfoDto.md)| SeriesTimerInfoDto:  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_livetv_timers**
> post_livetv_timers(body)

Creates a live tv timer

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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))
body = embyapi.LiveTvTimerInfoDto() # LiveTvTimerInfoDto | TimerInfoDto: 

try:
    # Creates a live tv timer
    api_instance.post_livetv_timers(body)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->post_livetv_timers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LiveTvTimerInfoDto**](LiveTvTimerInfoDto.md)| TimerInfoDto:  | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_livetv_timers_by_id**
> post_livetv_timers_by_id(body, id)

Updates a live tv timer

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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))
body = embyapi.LiveTvTimerInfoDto() # LiveTvTimerInfoDto | TimerInfoDto: 
id = 'id_example' # str | 

try:
    # Updates a live tv timer
    api_instance.post_livetv_timers_by_id(body, id)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->post_livetv_timers_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LiveTvTimerInfoDto**](LiveTvTimerInfoDto.md)| TimerInfoDto:  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_livetv_tunerhosts**
> LiveTvTunerHostInfo post_livetv_tunerhosts(body)

Adds a tuner host

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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))
body = embyapi.LiveTvTunerHostInfo() # LiveTvTunerHostInfo | TunerHostInfo: 

try:
    # Adds a tuner host
    api_response = api_instance.post_livetv_tunerhosts(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->post_livetv_tunerhosts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LiveTvTunerHostInfo**](LiveTvTunerHostInfo.md)| TunerHostInfo:  | 

### Return type

[**LiveTvTunerHostInfo**](LiveTvTunerHostInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_livetv_tuners_by_id_reset**
> post_livetv_tuners_by_id_reset(id)

Resets a tv tuner

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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Tuner Id

try:
    # Resets a tv tuner
    api_instance.post_livetv_tuners_by_id_reset(id)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->post_livetv_tuners_by_id_reset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tuner Id | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_livetv_channelmappingoptions**
> put_livetv_channelmappingoptions(provider_id)



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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))
provider_id = 'provider_id_example' # str | Provider id

try:
    api_instance.put_livetv_channelmappingoptions(provider_id)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->put_livetv_channelmappingoptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| Provider id | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_livetv_channelmappings**
> put_livetv_channelmappings(body, provider_id)



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
api_instance = embyapi.LiveTvServiceApi(embyapi.ApiClient(configuration))
body = embyapi.LiveTvSetChannelMapping() # LiveTvSetChannelMapping | SetChannelMapping
provider_id = 'provider_id_example' # str | Provider id

try:
    api_instance.put_livetv_channelmappings(body, provider_id)
except ApiException as e:
    print("Exception when calling LiveTvServiceApi->put_livetv_channelmappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LiveTvSetChannelMapping**](LiveTvSetChannelMapping.md)| SetChannelMapping | 
 **provider_id** | **str**| Provider id | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

