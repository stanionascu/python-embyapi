# embyapi.MediaInfoServiceApi

All URIs are relative to *https://home.ourflix.de:32865/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_items_by_id_playbackinfo**](MediaInfoServiceApi.md#get_items_by_id_playbackinfo) | **GET** /Items/{Id}/PlaybackInfo | Gets live playback media info for an item
[**get_playback_bitratetest**](MediaInfoServiceApi.md#get_playback_bitratetest) | **GET** /Playback/BitrateTest | 
[**post_items_by_id_playbackinfo**](MediaInfoServiceApi.md#post_items_by_id_playbackinfo) | **POST** /Items/{Id}/PlaybackInfo | Gets live playback media info for an item
[**post_livestreams_close**](MediaInfoServiceApi.md#post_livestreams_close) | **POST** /LiveStreams/Close | Closes a media source
[**post_livestreams_mediainfo**](MediaInfoServiceApi.md#post_livestreams_mediainfo) | **POST** /LiveStreams/MediaInfo | Closes a media source
[**post_livestreams_open**](MediaInfoServiceApi.md#post_livestreams_open) | **POST** /LiveStreams/Open | Opens a media source

# **get_items_by_id_playbackinfo**
> MediaInfoPlaybackInfoResponse get_items_by_id_playbackinfo(id, user_id)

Gets live playback media info for an item

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
api_instance = embyapi.MediaInfoServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Item Id
user_id = 'user_id_example' # str | User Id

try:
    # Gets live playback media info for an item
    api_response = api_instance.get_items_by_id_playbackinfo(id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaInfoServiceApi->get_items_by_id_playbackinfo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **user_id** | **str**| User Id | 

### Return type

[**MediaInfoPlaybackInfoResponse**](MediaInfoPlaybackInfoResponse.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_playback_bitratetest**
> get_playback_bitratetest(size)



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
api_instance = embyapi.MediaInfoServiceApi(embyapi.ApiClient(configuration))
size = 789 # int | Size

try:
    api_instance.get_playback_bitratetest(size)
except ApiException as e:
    print("Exception when calling MediaInfoServiceApi->get_playback_bitratetest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| Size | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_items_by_id_playbackinfo**
> MediaInfoPlaybackInfoResponse post_items_by_id_playbackinfo(body, id)

Gets live playback media info for an item

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
api_instance = embyapi.MediaInfoServiceApi(embyapi.ApiClient(configuration))
body = embyapi.MediaInfoPlaybackInfoRequest() # MediaInfoPlaybackInfoRequest | PlaybackInfoRequest: 
id = 'id_example' # str | 

try:
    # Gets live playback media info for an item
    api_response = api_instance.post_items_by_id_playbackinfo(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaInfoServiceApi->post_items_by_id_playbackinfo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MediaInfoPlaybackInfoRequest**](MediaInfoPlaybackInfoRequest.md)| PlaybackInfoRequest:  | 
 **id** | **str**|  | 

### Return type

[**MediaInfoPlaybackInfoResponse**](MediaInfoPlaybackInfoResponse.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_livestreams_close**
> post_livestreams_close(live_stream_id)

Closes a media source

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
api_instance = embyapi.MediaInfoServiceApi(embyapi.ApiClient(configuration))
live_stream_id = 'live_stream_id_example' # str | LiveStreamId

try:
    # Closes a media source
    api_instance.post_livestreams_close(live_stream_id)
except ApiException as e:
    print("Exception when calling MediaInfoServiceApi->post_livestreams_close: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_stream_id** | **str**| LiveStreamId | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_livestreams_mediainfo**
> post_livestreams_mediainfo(live_stream_id)

Closes a media source

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
api_instance = embyapi.MediaInfoServiceApi(embyapi.ApiClient(configuration))
live_stream_id = 'live_stream_id_example' # str | LiveStreamId

try:
    # Closes a media source
    api_instance.post_livestreams_mediainfo(live_stream_id)
except ApiException as e:
    print("Exception when calling MediaInfoServiceApi->post_livestreams_mediainfo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_stream_id** | **str**| LiveStreamId | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_livestreams_open**
> MediaInfoLiveStreamResponse post_livestreams_open(body)

Opens a media source

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
api_instance = embyapi.MediaInfoServiceApi(embyapi.ApiClient(configuration))
body = embyapi.MediaInfoLiveStreamRequest() # MediaInfoLiveStreamRequest | LiveStreamRequest: 

try:
    # Opens a media source
    api_response = api_instance.post_livestreams_open(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaInfoServiceApi->post_livestreams_open: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MediaInfoLiveStreamRequest**](MediaInfoLiveStreamRequest.md)| LiveStreamRequest:  | 

### Return type

[**MediaInfoLiveStreamResponse**](MediaInfoLiveStreamResponse.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

