# embyapi.DynamicHlsServiceApi

All URIs are relative to *https://home.ourflix.de:32865/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer**](DynamicHlsServiceApi.md#get_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer) | **GET** /Audio/{Id}/hls1/{PlaylistId}/{SegmentId}.{SegmentContainer} | 
[**get_audio_by_id_main_m3u8**](DynamicHlsServiceApi.md#get_audio_by_id_main_m3u8) | **GET** /Audio/{Id}/main.m3u8 | Gets an audio stream using HTTP live streaming.
[**get_audio_by_id_master_m3u8**](DynamicHlsServiceApi.md#get_audio_by_id_master_m3u8) | **GET** /Audio/{Id}/master.m3u8 | Gets an audio stream using HTTP live streaming.
[**get_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer**](DynamicHlsServiceApi.md#get_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer) | **GET** /Videos/{Id}/hls1/{PlaylistId}/{SegmentId}.{SegmentContainer} | 
[**get_videos_by_id_main_m3u8**](DynamicHlsServiceApi.md#get_videos_by_id_main_m3u8) | **GET** /Videos/{Id}/main.m3u8 | Gets a video stream using HTTP live streaming.
[**get_videos_by_id_master_m3u8**](DynamicHlsServiceApi.md#get_videos_by_id_master_m3u8) | **GET** /Videos/{Id}/master.m3u8 | Gets a video stream using HTTP live streaming.
[**get_videos_by_id_subtitles_m3u8**](DynamicHlsServiceApi.md#get_videos_by_id_subtitles_m3u8) | **GET** /Videos/{Id}/subtitles.m3u8 | Gets an HLS subtitle playlist.
[**head_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer**](DynamicHlsServiceApi.md#head_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer) | **HEAD** /Audio/{Id}/hls1/{PlaylistId}/{SegmentId}.{SegmentContainer} | 
[**head_audio_by_id_master_m3u8**](DynamicHlsServiceApi.md#head_audio_by_id_master_m3u8) | **HEAD** /Audio/{Id}/master.m3u8 | Gets an audio stream using HTTP live streaming.
[**head_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer**](DynamicHlsServiceApi.md#head_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer) | **HEAD** /Videos/{Id}/hls1/{PlaylistId}/{SegmentId}.{SegmentContainer} | 
[**head_videos_by_id_master_m3u8**](DynamicHlsServiceApi.md#head_videos_by_id_master_m3u8) | **HEAD** /Videos/{Id}/master.m3u8 | Gets a video stream using HTTP live streaming.

# **get_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer**
> get_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer(playlist_id, segment_id, segment_container, id, container, device_profile_id=device_profile_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, audio_sample_rate=audio_sample_rate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, static=static, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, video_codec=video_codec, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.DynamicHlsServiceApi()
playlist_id = 'playlist_id_example' # str | 
segment_id = 'segment_id_example' # str | 
segment_container = 'segment_container_example' # str | SegmentContainer
id = 'id_example' # str | Item Id
container = 'container_example' # str | Container
device_profile_id = 'device_profile_id_example' # str | Optional. The dlna device profile id to utilize. (optional)
device_id = 'device_id_example' # str | The device id of the client requesting. Used to stop encoding processes when needed. (optional)
audio_codec = 'audio_codec_example' # str | Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma. (optional)
enable_auto_stream_copy = true # bool | Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. (optional)
audio_sample_rate = 56 # int | Optional. Specify a specific audio sample rate, e.g. 44100 (optional)
audio_bit_rate = 56 # int | Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. (optional)
audio_channels = 56 # int | Optional. Specify a specific number of audio channels to encode to, e.g. 2 (optional)
max_audio_channels = 56 # int | Optional. Specify a maximum number of audio channels to encode to, e.g. 2 (optional)
static = true # bool | Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false (optional)
profile = 'profile_example' # str | Optional. Specify a specific h264 profile, e.g. main, baseline, high. (optional)
level = 'level_example' # str | Optional. Specify a level for the h264 profile, e.g. 3, 3.1. (optional)
framerate = 3.4 # float | Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. (optional)
max_framerate = 3.4 # float | Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. (optional)
copy_timestamps = true # bool | Whether or not to copy timestamps when transcoding with an offset. Defaults to false. (optional)
start_time_ticks = 789 # int | Optional. Specify a starting offset, in ticks. 1 tick = 10000 ms (optional)
width = 56 # int | Optional. The fixed horizontal resolution of the encoded video. (optional)
height = 56 # int | Optional. The fixed vertical resolution of the encoded video. (optional)
max_width = 56 # int | Optional. The maximum horizontal resolution of the encoded video. (optional)
max_height = 56 # int | Optional. The maximum vertical resolution of the encoded video. (optional)
video_bit_rate = 56 # int | Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. (optional)
subtitle_stream_index = 56 # int | Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. (optional)
subtitle_method = 'subtitle_method_example' # str | Optional. Specify the subtitle delivery method. (optional)
max_ref_frames = 56 # int | Optional. (optional)
max_video_bit_depth = 56 # int | Optional. (optional)
video_codec = 'video_codec_example' # str | Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h264, mpeg4, theora, vpx, wmv. (optional)
audio_stream_index = 56 # int | Optional. The index of the audio stream to use. If omitted the first audio stream will be used. (optional)
video_stream_index = 56 # int | Optional. The index of the video stream to use. If omitted the first video stream will be used. (optional)

try:
    api_instance.get_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer(playlist_id, segment_id, segment_container, id, container, device_profile_id=device_profile_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, audio_sample_rate=audio_sample_rate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, static=static, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, video_codec=video_codec, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index)
except ApiException as e:
    print("Exception when calling DynamicHlsServiceApi->get_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **str**|  | 
 **segment_id** | **str**|  | 
 **segment_container** | **str**| SegmentContainer | 
 **id** | **str**| Item Id | 
 **container** | **str**| Container | 
 **device_profile_id** | **str**| Optional. The dlna device profile id to utilize. | [optional] 
 **device_id** | **str**| The device id of the client requesting. Used to stop encoding processes when needed. | [optional] 
 **audio_codec** | **str**| Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url&#x27;s extension. Options: aac, mp3, vorbis, wma. | [optional] 
 **enable_auto_stream_copy** | **bool**| Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. | [optional] 
 **audio_sample_rate** | **int**| Optional. Specify a specific audio sample rate, e.g. 44100 | [optional] 
 **audio_bit_rate** | **int**| Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. | [optional] 
 **audio_channels** | **int**| Optional. Specify a specific number of audio channels to encode to, e.g. 2 | [optional] 
 **max_audio_channels** | **int**| Optional. Specify a maximum number of audio channels to encode to, e.g. 2 | [optional] 
 **static** | **bool**| Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false | [optional] 
 **profile** | **str**| Optional. Specify a specific h264 profile, e.g. main, baseline, high. | [optional] 
 **level** | **str**| Optional. Specify a level for the h264 profile, e.g. 3, 3.1. | [optional] 
 **framerate** | **float**| Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. | [optional] 
 **max_framerate** | **float**| Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. | [optional] 
 **copy_timestamps** | **bool**| Whether or not to copy timestamps when transcoding with an offset. Defaults to false. | [optional] 
 **start_time_ticks** | **int**| Optional. Specify a starting offset, in ticks. 1 tick &#x3D; 10000 ms | [optional] 
 **width** | **int**| Optional. The fixed horizontal resolution of the encoded video. | [optional] 
 **height** | **int**| Optional. The fixed vertical resolution of the encoded video. | [optional] 
 **max_width** | **int**| Optional. The maximum horizontal resolution of the encoded video. | [optional] 
 **max_height** | **int**| Optional. The maximum vertical resolution of the encoded video. | [optional] 
 **video_bit_rate** | **int**| Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. | [optional] 
 **subtitle_stream_index** | **int**| Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. | [optional] 
 **subtitle_method** | **str**| Optional. Specify the subtitle delivery method. | [optional] 
 **max_ref_frames** | **int**| Optional. | [optional] 
 **max_video_bit_depth** | **int**| Optional. | [optional] 
 **video_codec** | **str**| Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url&#x27;s extension. Options: h264, mpeg4, theora, vpx, wmv. | [optional] 
 **audio_stream_index** | **int**| Optional. The index of the audio stream to use. If omitted the first audio stream will be used. | [optional] 
 **video_stream_index** | **int**| Optional. The index of the video stream to use. If omitted the first video stream will be used. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audio_by_id_main_m3u8**
> get_audio_by_id_main_m3u8(id, container, device_profile_id=device_profile_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, audio_sample_rate=audio_sample_rate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, static=static, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, video_codec=video_codec, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index)

Gets an audio stream using HTTP live streaming.

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.DynamicHlsServiceApi()
id = 'id_example' # str | Item Id
container = 'container_example' # str | Container
device_profile_id = 'device_profile_id_example' # str | Optional. The dlna device profile id to utilize. (optional)
device_id = 'device_id_example' # str | The device id of the client requesting. Used to stop encoding processes when needed. (optional)
audio_codec = 'audio_codec_example' # str | Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma. (optional)
enable_auto_stream_copy = true # bool | Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. (optional)
audio_sample_rate = 56 # int | Optional. Specify a specific audio sample rate, e.g. 44100 (optional)
audio_bit_rate = 56 # int | Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. (optional)
audio_channels = 56 # int | Optional. Specify a specific number of audio channels to encode to, e.g. 2 (optional)
max_audio_channels = 56 # int | Optional. Specify a maximum number of audio channels to encode to, e.g. 2 (optional)
static = true # bool | Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false (optional)
profile = 'profile_example' # str | Optional. Specify a specific h264 profile, e.g. main, baseline, high. (optional)
level = 'level_example' # str | Optional. Specify a level for the h264 profile, e.g. 3, 3.1. (optional)
framerate = 3.4 # float | Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. (optional)
max_framerate = 3.4 # float | Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. (optional)
copy_timestamps = true # bool | Whether or not to copy timestamps when transcoding with an offset. Defaults to false. (optional)
start_time_ticks = 789 # int | Optional. Specify a starting offset, in ticks. 1 tick = 10000 ms (optional)
width = 56 # int | Optional. The fixed horizontal resolution of the encoded video. (optional)
height = 56 # int | Optional. The fixed vertical resolution of the encoded video. (optional)
max_width = 56 # int | Optional. The maximum horizontal resolution of the encoded video. (optional)
max_height = 56 # int | Optional. The maximum vertical resolution of the encoded video. (optional)
video_bit_rate = 56 # int | Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. (optional)
subtitle_stream_index = 56 # int | Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. (optional)
subtitle_method = 'subtitle_method_example' # str | Optional. Specify the subtitle delivery method. (optional)
max_ref_frames = 56 # int | Optional. (optional)
max_video_bit_depth = 56 # int | Optional. (optional)
video_codec = 'video_codec_example' # str | Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h264, mpeg4, theora, vpx, wmv. (optional)
audio_stream_index = 56 # int | Optional. The index of the audio stream to use. If omitted the first audio stream will be used. (optional)
video_stream_index = 56 # int | Optional. The index of the video stream to use. If omitted the first video stream will be used. (optional)

try:
    # Gets an audio stream using HTTP live streaming.
    api_instance.get_audio_by_id_main_m3u8(id, container, device_profile_id=device_profile_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, audio_sample_rate=audio_sample_rate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, static=static, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, video_codec=video_codec, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index)
except ApiException as e:
    print("Exception when calling DynamicHlsServiceApi->get_audio_by_id_main_m3u8: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **container** | **str**| Container | 
 **device_profile_id** | **str**| Optional. The dlna device profile id to utilize. | [optional] 
 **device_id** | **str**| The device id of the client requesting. Used to stop encoding processes when needed. | [optional] 
 **audio_codec** | **str**| Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url&#x27;s extension. Options: aac, mp3, vorbis, wma. | [optional] 
 **enable_auto_stream_copy** | **bool**| Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. | [optional] 
 **audio_sample_rate** | **int**| Optional. Specify a specific audio sample rate, e.g. 44100 | [optional] 
 **audio_bit_rate** | **int**| Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. | [optional] 
 **audio_channels** | **int**| Optional. Specify a specific number of audio channels to encode to, e.g. 2 | [optional] 
 **max_audio_channels** | **int**| Optional. Specify a maximum number of audio channels to encode to, e.g. 2 | [optional] 
 **static** | **bool**| Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false | [optional] 
 **profile** | **str**| Optional. Specify a specific h264 profile, e.g. main, baseline, high. | [optional] 
 **level** | **str**| Optional. Specify a level for the h264 profile, e.g. 3, 3.1. | [optional] 
 **framerate** | **float**| Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. | [optional] 
 **max_framerate** | **float**| Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. | [optional] 
 **copy_timestamps** | **bool**| Whether or not to copy timestamps when transcoding with an offset. Defaults to false. | [optional] 
 **start_time_ticks** | **int**| Optional. Specify a starting offset, in ticks. 1 tick &#x3D; 10000 ms | [optional] 
 **width** | **int**| Optional. The fixed horizontal resolution of the encoded video. | [optional] 
 **height** | **int**| Optional. The fixed vertical resolution of the encoded video. | [optional] 
 **max_width** | **int**| Optional. The maximum horizontal resolution of the encoded video. | [optional] 
 **max_height** | **int**| Optional. The maximum vertical resolution of the encoded video. | [optional] 
 **video_bit_rate** | **int**| Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. | [optional] 
 **subtitle_stream_index** | **int**| Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. | [optional] 
 **subtitle_method** | **str**| Optional. Specify the subtitle delivery method. | [optional] 
 **max_ref_frames** | **int**| Optional. | [optional] 
 **max_video_bit_depth** | **int**| Optional. | [optional] 
 **video_codec** | **str**| Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url&#x27;s extension. Options: h264, mpeg4, theora, vpx, wmv. | [optional] 
 **audio_stream_index** | **int**| Optional. The index of the audio stream to use. If omitted the first audio stream will be used. | [optional] 
 **video_stream_index** | **int**| Optional. The index of the video stream to use. If omitted the first video stream will be used. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audio_by_id_master_m3u8**
> get_audio_by_id_master_m3u8(id, container, device_profile_id=device_profile_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, audio_sample_rate=audio_sample_rate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, static=static, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, video_codec=video_codec, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index)

Gets an audio stream using HTTP live streaming.

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.DynamicHlsServiceApi()
id = 'id_example' # str | Item Id
container = 'container_example' # str | Container
device_profile_id = 'device_profile_id_example' # str | Optional. The dlna device profile id to utilize. (optional)
device_id = 'device_id_example' # str | The device id of the client requesting. Used to stop encoding processes when needed. (optional)
audio_codec = 'audio_codec_example' # str | Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma. (optional)
enable_auto_stream_copy = true # bool | Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. (optional)
audio_sample_rate = 56 # int | Optional. Specify a specific audio sample rate, e.g. 44100 (optional)
audio_bit_rate = 56 # int | Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. (optional)
audio_channels = 56 # int | Optional. Specify a specific number of audio channels to encode to, e.g. 2 (optional)
max_audio_channels = 56 # int | Optional. Specify a maximum number of audio channels to encode to, e.g. 2 (optional)
static = true # bool | Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false (optional)
profile = 'profile_example' # str | Optional. Specify a specific h264 profile, e.g. main, baseline, high. (optional)
level = 'level_example' # str | Optional. Specify a level for the h264 profile, e.g. 3, 3.1. (optional)
framerate = 3.4 # float | Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. (optional)
max_framerate = 3.4 # float | Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. (optional)
copy_timestamps = true # bool | Whether or not to copy timestamps when transcoding with an offset. Defaults to false. (optional)
start_time_ticks = 789 # int | Optional. Specify a starting offset, in ticks. 1 tick = 10000 ms (optional)
width = 56 # int | Optional. The fixed horizontal resolution of the encoded video. (optional)
height = 56 # int | Optional. The fixed vertical resolution of the encoded video. (optional)
max_width = 56 # int | Optional. The maximum horizontal resolution of the encoded video. (optional)
max_height = 56 # int | Optional. The maximum vertical resolution of the encoded video. (optional)
video_bit_rate = 56 # int | Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. (optional)
subtitle_stream_index = 56 # int | Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. (optional)
subtitle_method = 'subtitle_method_example' # str | Optional. Specify the subtitle delivery method. (optional)
max_ref_frames = 56 # int | Optional. (optional)
max_video_bit_depth = 56 # int | Optional. (optional)
video_codec = 'video_codec_example' # str | Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h264, mpeg4, theora, vpx, wmv. (optional)
audio_stream_index = 56 # int | Optional. The index of the audio stream to use. If omitted the first audio stream will be used. (optional)
video_stream_index = 56 # int | Optional. The index of the video stream to use. If omitted the first video stream will be used. (optional)

try:
    # Gets an audio stream using HTTP live streaming.
    api_instance.get_audio_by_id_master_m3u8(id, container, device_profile_id=device_profile_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, audio_sample_rate=audio_sample_rate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, static=static, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, video_codec=video_codec, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index)
except ApiException as e:
    print("Exception when calling DynamicHlsServiceApi->get_audio_by_id_master_m3u8: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **container** | **str**| Container | 
 **device_profile_id** | **str**| Optional. The dlna device profile id to utilize. | [optional] 
 **device_id** | **str**| The device id of the client requesting. Used to stop encoding processes when needed. | [optional] 
 **audio_codec** | **str**| Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url&#x27;s extension. Options: aac, mp3, vorbis, wma. | [optional] 
 **enable_auto_stream_copy** | **bool**| Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. | [optional] 
 **audio_sample_rate** | **int**| Optional. Specify a specific audio sample rate, e.g. 44100 | [optional] 
 **audio_bit_rate** | **int**| Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. | [optional] 
 **audio_channels** | **int**| Optional. Specify a specific number of audio channels to encode to, e.g. 2 | [optional] 
 **max_audio_channels** | **int**| Optional. Specify a maximum number of audio channels to encode to, e.g. 2 | [optional] 
 **static** | **bool**| Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false | [optional] 
 **profile** | **str**| Optional. Specify a specific h264 profile, e.g. main, baseline, high. | [optional] 
 **level** | **str**| Optional. Specify a level for the h264 profile, e.g. 3, 3.1. | [optional] 
 **framerate** | **float**| Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. | [optional] 
 **max_framerate** | **float**| Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. | [optional] 
 **copy_timestamps** | **bool**| Whether or not to copy timestamps when transcoding with an offset. Defaults to false. | [optional] 
 **start_time_ticks** | **int**| Optional. Specify a starting offset, in ticks. 1 tick &#x3D; 10000 ms | [optional] 
 **width** | **int**| Optional. The fixed horizontal resolution of the encoded video. | [optional] 
 **height** | **int**| Optional. The fixed vertical resolution of the encoded video. | [optional] 
 **max_width** | **int**| Optional. The maximum horizontal resolution of the encoded video. | [optional] 
 **max_height** | **int**| Optional. The maximum vertical resolution of the encoded video. | [optional] 
 **video_bit_rate** | **int**| Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. | [optional] 
 **subtitle_stream_index** | **int**| Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. | [optional] 
 **subtitle_method** | **str**| Optional. Specify the subtitle delivery method. | [optional] 
 **max_ref_frames** | **int**| Optional. | [optional] 
 **max_video_bit_depth** | **int**| Optional. | [optional] 
 **video_codec** | **str**| Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url&#x27;s extension. Options: h264, mpeg4, theora, vpx, wmv. | [optional] 
 **audio_stream_index** | **int**| Optional. The index of the audio stream to use. If omitted the first audio stream will be used. | [optional] 
 **video_stream_index** | **int**| Optional. The index of the video stream to use. If omitted the first video stream will be used. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer**
> get_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer(playlist_id, segment_id, segment_container, id, container, device_profile_id=device_profile_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, audio_sample_rate=audio_sample_rate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, static=static, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, video_codec=video_codec, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.DynamicHlsServiceApi()
playlist_id = 'playlist_id_example' # str | 
segment_id = 'segment_id_example' # str | 
segment_container = 'segment_container_example' # str | SegmentContainer
id = 'id_example' # str | Item Id
container = 'container_example' # str | Container
device_profile_id = 'device_profile_id_example' # str | Optional. The dlna device profile id to utilize. (optional)
device_id = 'device_id_example' # str | The device id of the client requesting. Used to stop encoding processes when needed. (optional)
audio_codec = 'audio_codec_example' # str | Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma. (optional)
enable_auto_stream_copy = true # bool | Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. (optional)
audio_sample_rate = 56 # int | Optional. Specify a specific audio sample rate, e.g. 44100 (optional)
audio_bit_rate = 56 # int | Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. (optional)
audio_channels = 56 # int | Optional. Specify a specific number of audio channels to encode to, e.g. 2 (optional)
max_audio_channels = 56 # int | Optional. Specify a maximum number of audio channels to encode to, e.g. 2 (optional)
static = true # bool | Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false (optional)
profile = 'profile_example' # str | Optional. Specify a specific h264 profile, e.g. main, baseline, high. (optional)
level = 'level_example' # str | Optional. Specify a level for the h264 profile, e.g. 3, 3.1. (optional)
framerate = 3.4 # float | Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. (optional)
max_framerate = 3.4 # float | Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. (optional)
copy_timestamps = true # bool | Whether or not to copy timestamps when transcoding with an offset. Defaults to false. (optional)
start_time_ticks = 789 # int | Optional. Specify a starting offset, in ticks. 1 tick = 10000 ms (optional)
width = 56 # int | Optional. The fixed horizontal resolution of the encoded video. (optional)
height = 56 # int | Optional. The fixed vertical resolution of the encoded video. (optional)
max_width = 56 # int | Optional. The maximum horizontal resolution of the encoded video. (optional)
max_height = 56 # int | Optional. The maximum vertical resolution of the encoded video. (optional)
video_bit_rate = 56 # int | Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. (optional)
subtitle_stream_index = 56 # int | Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. (optional)
subtitle_method = 'subtitle_method_example' # str | Optional. Specify the subtitle delivery method. (optional)
max_ref_frames = 56 # int | Optional. (optional)
max_video_bit_depth = 56 # int | Optional. (optional)
video_codec = 'video_codec_example' # str | Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h264, mpeg4, theora, vpx, wmv. (optional)
audio_stream_index = 56 # int | Optional. The index of the audio stream to use. If omitted the first audio stream will be used. (optional)
video_stream_index = 56 # int | Optional. The index of the video stream to use. If omitted the first video stream will be used. (optional)

try:
    api_instance.get_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer(playlist_id, segment_id, segment_container, id, container, device_profile_id=device_profile_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, audio_sample_rate=audio_sample_rate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, static=static, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, video_codec=video_codec, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index)
except ApiException as e:
    print("Exception when calling DynamicHlsServiceApi->get_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **str**|  | 
 **segment_id** | **str**|  | 
 **segment_container** | **str**| SegmentContainer | 
 **id** | **str**| Item Id | 
 **container** | **str**| Container | 
 **device_profile_id** | **str**| Optional. The dlna device profile id to utilize. | [optional] 
 **device_id** | **str**| The device id of the client requesting. Used to stop encoding processes when needed. | [optional] 
 **audio_codec** | **str**| Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url&#x27;s extension. Options: aac, mp3, vorbis, wma. | [optional] 
 **enable_auto_stream_copy** | **bool**| Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. | [optional] 
 **audio_sample_rate** | **int**| Optional. Specify a specific audio sample rate, e.g. 44100 | [optional] 
 **audio_bit_rate** | **int**| Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. | [optional] 
 **audio_channels** | **int**| Optional. Specify a specific number of audio channels to encode to, e.g. 2 | [optional] 
 **max_audio_channels** | **int**| Optional. Specify a maximum number of audio channels to encode to, e.g. 2 | [optional] 
 **static** | **bool**| Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false | [optional] 
 **profile** | **str**| Optional. Specify a specific h264 profile, e.g. main, baseline, high. | [optional] 
 **level** | **str**| Optional. Specify a level for the h264 profile, e.g. 3, 3.1. | [optional] 
 **framerate** | **float**| Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. | [optional] 
 **max_framerate** | **float**| Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. | [optional] 
 **copy_timestamps** | **bool**| Whether or not to copy timestamps when transcoding with an offset. Defaults to false. | [optional] 
 **start_time_ticks** | **int**| Optional. Specify a starting offset, in ticks. 1 tick &#x3D; 10000 ms | [optional] 
 **width** | **int**| Optional. The fixed horizontal resolution of the encoded video. | [optional] 
 **height** | **int**| Optional. The fixed vertical resolution of the encoded video. | [optional] 
 **max_width** | **int**| Optional. The maximum horizontal resolution of the encoded video. | [optional] 
 **max_height** | **int**| Optional. The maximum vertical resolution of the encoded video. | [optional] 
 **video_bit_rate** | **int**| Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. | [optional] 
 **subtitle_stream_index** | **int**| Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. | [optional] 
 **subtitle_method** | **str**| Optional. Specify the subtitle delivery method. | [optional] 
 **max_ref_frames** | **int**| Optional. | [optional] 
 **max_video_bit_depth** | **int**| Optional. | [optional] 
 **video_codec** | **str**| Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url&#x27;s extension. Options: h264, mpeg4, theora, vpx, wmv. | [optional] 
 **audio_stream_index** | **int**| Optional. The index of the audio stream to use. If omitted the first audio stream will be used. | [optional] 
 **video_stream_index** | **int**| Optional. The index of the video stream to use. If omitted the first video stream will be used. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_videos_by_id_main_m3u8**
> get_videos_by_id_main_m3u8(id, container, device_profile_id=device_profile_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, audio_sample_rate=audio_sample_rate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, static=static, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, video_codec=video_codec, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index)

Gets a video stream using HTTP live streaming.

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.DynamicHlsServiceApi()
id = 'id_example' # str | Item Id
container = 'container_example' # str | Container
device_profile_id = 'device_profile_id_example' # str | Optional. The dlna device profile id to utilize. (optional)
device_id = 'device_id_example' # str | The device id of the client requesting. Used to stop encoding processes when needed. (optional)
audio_codec = 'audio_codec_example' # str | Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma. (optional)
enable_auto_stream_copy = true # bool | Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. (optional)
audio_sample_rate = 56 # int | Optional. Specify a specific audio sample rate, e.g. 44100 (optional)
audio_bit_rate = 56 # int | Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. (optional)
audio_channels = 56 # int | Optional. Specify a specific number of audio channels to encode to, e.g. 2 (optional)
max_audio_channels = 56 # int | Optional. Specify a maximum number of audio channels to encode to, e.g. 2 (optional)
static = true # bool | Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false (optional)
profile = 'profile_example' # str | Optional. Specify a specific h264 profile, e.g. main, baseline, high. (optional)
level = 'level_example' # str | Optional. Specify a level for the h264 profile, e.g. 3, 3.1. (optional)
framerate = 3.4 # float | Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. (optional)
max_framerate = 3.4 # float | Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. (optional)
copy_timestamps = true # bool | Whether or not to copy timestamps when transcoding with an offset. Defaults to false. (optional)
start_time_ticks = 789 # int | Optional. Specify a starting offset, in ticks. 1 tick = 10000 ms (optional)
width = 56 # int | Optional. The fixed horizontal resolution of the encoded video. (optional)
height = 56 # int | Optional. The fixed vertical resolution of the encoded video. (optional)
max_width = 56 # int | Optional. The maximum horizontal resolution of the encoded video. (optional)
max_height = 56 # int | Optional. The maximum vertical resolution of the encoded video. (optional)
video_bit_rate = 56 # int | Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. (optional)
subtitle_stream_index = 56 # int | Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. (optional)
subtitle_method = 'subtitle_method_example' # str | Optional. Specify the subtitle delivery method. (optional)
max_ref_frames = 56 # int | Optional. (optional)
max_video_bit_depth = 56 # int | Optional. (optional)
video_codec = 'video_codec_example' # str | Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h264, mpeg4, theora, vpx, wmv. (optional)
audio_stream_index = 56 # int | Optional. The index of the audio stream to use. If omitted the first audio stream will be used. (optional)
video_stream_index = 56 # int | Optional. The index of the video stream to use. If omitted the first video stream will be used. (optional)

try:
    # Gets a video stream using HTTP live streaming.
    api_instance.get_videos_by_id_main_m3u8(id, container, device_profile_id=device_profile_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, audio_sample_rate=audio_sample_rate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, static=static, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, video_codec=video_codec, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index)
except ApiException as e:
    print("Exception when calling DynamicHlsServiceApi->get_videos_by_id_main_m3u8: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **container** | **str**| Container | 
 **device_profile_id** | **str**| Optional. The dlna device profile id to utilize. | [optional] 
 **device_id** | **str**| The device id of the client requesting. Used to stop encoding processes when needed. | [optional] 
 **audio_codec** | **str**| Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url&#x27;s extension. Options: aac, mp3, vorbis, wma. | [optional] 
 **enable_auto_stream_copy** | **bool**| Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. | [optional] 
 **audio_sample_rate** | **int**| Optional. Specify a specific audio sample rate, e.g. 44100 | [optional] 
 **audio_bit_rate** | **int**| Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. | [optional] 
 **audio_channels** | **int**| Optional. Specify a specific number of audio channels to encode to, e.g. 2 | [optional] 
 **max_audio_channels** | **int**| Optional. Specify a maximum number of audio channels to encode to, e.g. 2 | [optional] 
 **static** | **bool**| Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false | [optional] 
 **profile** | **str**| Optional. Specify a specific h264 profile, e.g. main, baseline, high. | [optional] 
 **level** | **str**| Optional. Specify a level for the h264 profile, e.g. 3, 3.1. | [optional] 
 **framerate** | **float**| Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. | [optional] 
 **max_framerate** | **float**| Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. | [optional] 
 **copy_timestamps** | **bool**| Whether or not to copy timestamps when transcoding with an offset. Defaults to false. | [optional] 
 **start_time_ticks** | **int**| Optional. Specify a starting offset, in ticks. 1 tick &#x3D; 10000 ms | [optional] 
 **width** | **int**| Optional. The fixed horizontal resolution of the encoded video. | [optional] 
 **height** | **int**| Optional. The fixed vertical resolution of the encoded video. | [optional] 
 **max_width** | **int**| Optional. The maximum horizontal resolution of the encoded video. | [optional] 
 **max_height** | **int**| Optional. The maximum vertical resolution of the encoded video. | [optional] 
 **video_bit_rate** | **int**| Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. | [optional] 
 **subtitle_stream_index** | **int**| Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. | [optional] 
 **subtitle_method** | **str**| Optional. Specify the subtitle delivery method. | [optional] 
 **max_ref_frames** | **int**| Optional. | [optional] 
 **max_video_bit_depth** | **int**| Optional. | [optional] 
 **video_codec** | **str**| Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url&#x27;s extension. Options: h264, mpeg4, theora, vpx, wmv. | [optional] 
 **audio_stream_index** | **int**| Optional. The index of the audio stream to use. If omitted the first audio stream will be used. | [optional] 
 **video_stream_index** | **int**| Optional. The index of the video stream to use. If omitted the first video stream will be used. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_videos_by_id_master_m3u8**
> get_videos_by_id_master_m3u8(id, container, device_profile_id=device_profile_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, audio_sample_rate=audio_sample_rate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, static=static, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, video_codec=video_codec, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index)

Gets a video stream using HTTP live streaming.

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.DynamicHlsServiceApi()
id = 'id_example' # str | Item Id
container = 'container_example' # str | Container
device_profile_id = 'device_profile_id_example' # str | Optional. The dlna device profile id to utilize. (optional)
device_id = 'device_id_example' # str | The device id of the client requesting. Used to stop encoding processes when needed. (optional)
audio_codec = 'audio_codec_example' # str | Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma. (optional)
enable_auto_stream_copy = true # bool | Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. (optional)
audio_sample_rate = 56 # int | Optional. Specify a specific audio sample rate, e.g. 44100 (optional)
audio_bit_rate = 56 # int | Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. (optional)
audio_channels = 56 # int | Optional. Specify a specific number of audio channels to encode to, e.g. 2 (optional)
max_audio_channels = 56 # int | Optional. Specify a maximum number of audio channels to encode to, e.g. 2 (optional)
static = true # bool | Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false (optional)
profile = 'profile_example' # str | Optional. Specify a specific h264 profile, e.g. main, baseline, high. (optional)
level = 'level_example' # str | Optional. Specify a level for the h264 profile, e.g. 3, 3.1. (optional)
framerate = 3.4 # float | Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. (optional)
max_framerate = 3.4 # float | Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. (optional)
copy_timestamps = true # bool | Whether or not to copy timestamps when transcoding with an offset. Defaults to false. (optional)
start_time_ticks = 789 # int | Optional. Specify a starting offset, in ticks. 1 tick = 10000 ms (optional)
width = 56 # int | Optional. The fixed horizontal resolution of the encoded video. (optional)
height = 56 # int | Optional. The fixed vertical resolution of the encoded video. (optional)
max_width = 56 # int | Optional. The maximum horizontal resolution of the encoded video. (optional)
max_height = 56 # int | Optional. The maximum vertical resolution of the encoded video. (optional)
video_bit_rate = 56 # int | Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. (optional)
subtitle_stream_index = 56 # int | Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. (optional)
subtitle_method = 'subtitle_method_example' # str | Optional. Specify the subtitle delivery method. (optional)
max_ref_frames = 56 # int | Optional. (optional)
max_video_bit_depth = 56 # int | Optional. (optional)
video_codec = 'video_codec_example' # str | Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h264, mpeg4, theora, vpx, wmv. (optional)
audio_stream_index = 56 # int | Optional. The index of the audio stream to use. If omitted the first audio stream will be used. (optional)
video_stream_index = 56 # int | Optional. The index of the video stream to use. If omitted the first video stream will be used. (optional)

try:
    # Gets a video stream using HTTP live streaming.
    api_instance.get_videos_by_id_master_m3u8(id, container, device_profile_id=device_profile_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, audio_sample_rate=audio_sample_rate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, static=static, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, video_codec=video_codec, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index)
except ApiException as e:
    print("Exception when calling DynamicHlsServiceApi->get_videos_by_id_master_m3u8: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **container** | **str**| Container | 
 **device_profile_id** | **str**| Optional. The dlna device profile id to utilize. | [optional] 
 **device_id** | **str**| The device id of the client requesting. Used to stop encoding processes when needed. | [optional] 
 **audio_codec** | **str**| Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url&#x27;s extension. Options: aac, mp3, vorbis, wma. | [optional] 
 **enable_auto_stream_copy** | **bool**| Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. | [optional] 
 **audio_sample_rate** | **int**| Optional. Specify a specific audio sample rate, e.g. 44100 | [optional] 
 **audio_bit_rate** | **int**| Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. | [optional] 
 **audio_channels** | **int**| Optional. Specify a specific number of audio channels to encode to, e.g. 2 | [optional] 
 **max_audio_channels** | **int**| Optional. Specify a maximum number of audio channels to encode to, e.g. 2 | [optional] 
 **static** | **bool**| Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false | [optional] 
 **profile** | **str**| Optional. Specify a specific h264 profile, e.g. main, baseline, high. | [optional] 
 **level** | **str**| Optional. Specify a level for the h264 profile, e.g. 3, 3.1. | [optional] 
 **framerate** | **float**| Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. | [optional] 
 **max_framerate** | **float**| Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. | [optional] 
 **copy_timestamps** | **bool**| Whether or not to copy timestamps when transcoding with an offset. Defaults to false. | [optional] 
 **start_time_ticks** | **int**| Optional. Specify a starting offset, in ticks. 1 tick &#x3D; 10000 ms | [optional] 
 **width** | **int**| Optional. The fixed horizontal resolution of the encoded video. | [optional] 
 **height** | **int**| Optional. The fixed vertical resolution of the encoded video. | [optional] 
 **max_width** | **int**| Optional. The maximum horizontal resolution of the encoded video. | [optional] 
 **max_height** | **int**| Optional. The maximum vertical resolution of the encoded video. | [optional] 
 **video_bit_rate** | **int**| Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. | [optional] 
 **subtitle_stream_index** | **int**| Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. | [optional] 
 **subtitle_method** | **str**| Optional. Specify the subtitle delivery method. | [optional] 
 **max_ref_frames** | **int**| Optional. | [optional] 
 **max_video_bit_depth** | **int**| Optional. | [optional] 
 **video_codec** | **str**| Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url&#x27;s extension. Options: h264, mpeg4, theora, vpx, wmv. | [optional] 
 **audio_stream_index** | **int**| Optional. The index of the audio stream to use. If omitted the first audio stream will be used. | [optional] 
 **video_stream_index** | **int**| Optional. The index of the video stream to use. If omitted the first video stream will be used. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_videos_by_id_subtitles_m3u8**
> get_videos_by_id_subtitles_m3u8(id, subtitle_segment_length, manifest_subtitles)

Gets an HLS subtitle playlist.

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.DynamicHlsServiceApi()
id = 'id_example' # str | Item Id
subtitle_segment_length = 56 # int | The subtitle segment length
manifest_subtitles = 'manifest_subtitles_example' # str | The subtitle segment format

try:
    # Gets an HLS subtitle playlist.
    api_instance.get_videos_by_id_subtitles_m3u8(id, subtitle_segment_length, manifest_subtitles)
except ApiException as e:
    print("Exception when calling DynamicHlsServiceApi->get_videos_by_id_subtitles_m3u8: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **subtitle_segment_length** | **int**| The subtitle segment length | 
 **manifest_subtitles** | **str**| The subtitle segment format | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer**
> head_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer(playlist_id, segment_id, segment_container, id, container, device_profile_id=device_profile_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, audio_sample_rate=audio_sample_rate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, static=static, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, video_codec=video_codec, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.DynamicHlsServiceApi()
playlist_id = 'playlist_id_example' # str | 
segment_id = 'segment_id_example' # str | 
segment_container = 'segment_container_example' # str | SegmentContainer
id = 'id_example' # str | Item Id
container = 'container_example' # str | Container
device_profile_id = 'device_profile_id_example' # str | Optional. The dlna device profile id to utilize. (optional)
device_id = 'device_id_example' # str | The device id of the client requesting. Used to stop encoding processes when needed. (optional)
audio_codec = 'audio_codec_example' # str | Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma. (optional)
enable_auto_stream_copy = true # bool | Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. (optional)
audio_sample_rate = 56 # int | Optional. Specify a specific audio sample rate, e.g. 44100 (optional)
audio_bit_rate = 56 # int | Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. (optional)
audio_channels = 56 # int | Optional. Specify a specific number of audio channels to encode to, e.g. 2 (optional)
max_audio_channels = 56 # int | Optional. Specify a maximum number of audio channels to encode to, e.g. 2 (optional)
static = true # bool | Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false (optional)
profile = 'profile_example' # str | Optional. Specify a specific h264 profile, e.g. main, baseline, high. (optional)
level = 'level_example' # str | Optional. Specify a level for the h264 profile, e.g. 3, 3.1. (optional)
framerate = 3.4 # float | Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. (optional)
max_framerate = 3.4 # float | Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. (optional)
copy_timestamps = true # bool | Whether or not to copy timestamps when transcoding with an offset. Defaults to false. (optional)
start_time_ticks = 789 # int | Optional. Specify a starting offset, in ticks. 1 tick = 10000 ms (optional)
width = 56 # int | Optional. The fixed horizontal resolution of the encoded video. (optional)
height = 56 # int | Optional. The fixed vertical resolution of the encoded video. (optional)
max_width = 56 # int | Optional. The maximum horizontal resolution of the encoded video. (optional)
max_height = 56 # int | Optional. The maximum vertical resolution of the encoded video. (optional)
video_bit_rate = 56 # int | Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. (optional)
subtitle_stream_index = 56 # int | Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. (optional)
subtitle_method = 'subtitle_method_example' # str | Optional. Specify the subtitle delivery method. (optional)
max_ref_frames = 56 # int | Optional. (optional)
max_video_bit_depth = 56 # int | Optional. (optional)
video_codec = 'video_codec_example' # str | Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h264, mpeg4, theora, vpx, wmv. (optional)
audio_stream_index = 56 # int | Optional. The index of the audio stream to use. If omitted the first audio stream will be used. (optional)
video_stream_index = 56 # int | Optional. The index of the video stream to use. If omitted the first video stream will be used. (optional)

try:
    api_instance.head_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer(playlist_id, segment_id, segment_container, id, container, device_profile_id=device_profile_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, audio_sample_rate=audio_sample_rate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, static=static, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, video_codec=video_codec, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index)
except ApiException as e:
    print("Exception when calling DynamicHlsServiceApi->head_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **str**|  | 
 **segment_id** | **str**|  | 
 **segment_container** | **str**| SegmentContainer | 
 **id** | **str**| Item Id | 
 **container** | **str**| Container | 
 **device_profile_id** | **str**| Optional. The dlna device profile id to utilize. | [optional] 
 **device_id** | **str**| The device id of the client requesting. Used to stop encoding processes when needed. | [optional] 
 **audio_codec** | **str**| Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url&#x27;s extension. Options: aac, mp3, vorbis, wma. | [optional] 
 **enable_auto_stream_copy** | **bool**| Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. | [optional] 
 **audio_sample_rate** | **int**| Optional. Specify a specific audio sample rate, e.g. 44100 | [optional] 
 **audio_bit_rate** | **int**| Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. | [optional] 
 **audio_channels** | **int**| Optional. Specify a specific number of audio channels to encode to, e.g. 2 | [optional] 
 **max_audio_channels** | **int**| Optional. Specify a maximum number of audio channels to encode to, e.g. 2 | [optional] 
 **static** | **bool**| Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false | [optional] 
 **profile** | **str**| Optional. Specify a specific h264 profile, e.g. main, baseline, high. | [optional] 
 **level** | **str**| Optional. Specify a level for the h264 profile, e.g. 3, 3.1. | [optional] 
 **framerate** | **float**| Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. | [optional] 
 **max_framerate** | **float**| Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. | [optional] 
 **copy_timestamps** | **bool**| Whether or not to copy timestamps when transcoding with an offset. Defaults to false. | [optional] 
 **start_time_ticks** | **int**| Optional. Specify a starting offset, in ticks. 1 tick &#x3D; 10000 ms | [optional] 
 **width** | **int**| Optional. The fixed horizontal resolution of the encoded video. | [optional] 
 **height** | **int**| Optional. The fixed vertical resolution of the encoded video. | [optional] 
 **max_width** | **int**| Optional. The maximum horizontal resolution of the encoded video. | [optional] 
 **max_height** | **int**| Optional. The maximum vertical resolution of the encoded video. | [optional] 
 **video_bit_rate** | **int**| Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. | [optional] 
 **subtitle_stream_index** | **int**| Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. | [optional] 
 **subtitle_method** | **str**| Optional. Specify the subtitle delivery method. | [optional] 
 **max_ref_frames** | **int**| Optional. | [optional] 
 **max_video_bit_depth** | **int**| Optional. | [optional] 
 **video_codec** | **str**| Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url&#x27;s extension. Options: h264, mpeg4, theora, vpx, wmv. | [optional] 
 **audio_stream_index** | **int**| Optional. The index of the audio stream to use. If omitted the first audio stream will be used. | [optional] 
 **video_stream_index** | **int**| Optional. The index of the video stream to use. If omitted the first video stream will be used. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_audio_by_id_master_m3u8**
> head_audio_by_id_master_m3u8(id, container, device_profile_id=device_profile_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, audio_sample_rate=audio_sample_rate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, static=static, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, video_codec=video_codec, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index)

Gets an audio stream using HTTP live streaming.

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.DynamicHlsServiceApi()
id = 'id_example' # str | Item Id
container = 'container_example' # str | Container
device_profile_id = 'device_profile_id_example' # str | Optional. The dlna device profile id to utilize. (optional)
device_id = 'device_id_example' # str | The device id of the client requesting. Used to stop encoding processes when needed. (optional)
audio_codec = 'audio_codec_example' # str | Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma. (optional)
enable_auto_stream_copy = true # bool | Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. (optional)
audio_sample_rate = 56 # int | Optional. Specify a specific audio sample rate, e.g. 44100 (optional)
audio_bit_rate = 56 # int | Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. (optional)
audio_channels = 56 # int | Optional. Specify a specific number of audio channels to encode to, e.g. 2 (optional)
max_audio_channels = 56 # int | Optional. Specify a maximum number of audio channels to encode to, e.g. 2 (optional)
static = true # bool | Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false (optional)
profile = 'profile_example' # str | Optional. Specify a specific h264 profile, e.g. main, baseline, high. (optional)
level = 'level_example' # str | Optional. Specify a level for the h264 profile, e.g. 3, 3.1. (optional)
framerate = 3.4 # float | Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. (optional)
max_framerate = 3.4 # float | Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. (optional)
copy_timestamps = true # bool | Whether or not to copy timestamps when transcoding with an offset. Defaults to false. (optional)
start_time_ticks = 789 # int | Optional. Specify a starting offset, in ticks. 1 tick = 10000 ms (optional)
width = 56 # int | Optional. The fixed horizontal resolution of the encoded video. (optional)
height = 56 # int | Optional. The fixed vertical resolution of the encoded video. (optional)
max_width = 56 # int | Optional. The maximum horizontal resolution of the encoded video. (optional)
max_height = 56 # int | Optional. The maximum vertical resolution of the encoded video. (optional)
video_bit_rate = 56 # int | Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. (optional)
subtitle_stream_index = 56 # int | Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. (optional)
subtitle_method = 'subtitle_method_example' # str | Optional. Specify the subtitle delivery method. (optional)
max_ref_frames = 56 # int | Optional. (optional)
max_video_bit_depth = 56 # int | Optional. (optional)
video_codec = 'video_codec_example' # str | Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h264, mpeg4, theora, vpx, wmv. (optional)
audio_stream_index = 56 # int | Optional. The index of the audio stream to use. If omitted the first audio stream will be used. (optional)
video_stream_index = 56 # int | Optional. The index of the video stream to use. If omitted the first video stream will be used. (optional)

try:
    # Gets an audio stream using HTTP live streaming.
    api_instance.head_audio_by_id_master_m3u8(id, container, device_profile_id=device_profile_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, audio_sample_rate=audio_sample_rate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, static=static, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, video_codec=video_codec, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index)
except ApiException as e:
    print("Exception when calling DynamicHlsServiceApi->head_audio_by_id_master_m3u8: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **container** | **str**| Container | 
 **device_profile_id** | **str**| Optional. The dlna device profile id to utilize. | [optional] 
 **device_id** | **str**| The device id of the client requesting. Used to stop encoding processes when needed. | [optional] 
 **audio_codec** | **str**| Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url&#x27;s extension. Options: aac, mp3, vorbis, wma. | [optional] 
 **enable_auto_stream_copy** | **bool**| Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. | [optional] 
 **audio_sample_rate** | **int**| Optional. Specify a specific audio sample rate, e.g. 44100 | [optional] 
 **audio_bit_rate** | **int**| Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. | [optional] 
 **audio_channels** | **int**| Optional. Specify a specific number of audio channels to encode to, e.g. 2 | [optional] 
 **max_audio_channels** | **int**| Optional. Specify a maximum number of audio channels to encode to, e.g. 2 | [optional] 
 **static** | **bool**| Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false | [optional] 
 **profile** | **str**| Optional. Specify a specific h264 profile, e.g. main, baseline, high. | [optional] 
 **level** | **str**| Optional. Specify a level for the h264 profile, e.g. 3, 3.1. | [optional] 
 **framerate** | **float**| Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. | [optional] 
 **max_framerate** | **float**| Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. | [optional] 
 **copy_timestamps** | **bool**| Whether or not to copy timestamps when transcoding with an offset. Defaults to false. | [optional] 
 **start_time_ticks** | **int**| Optional. Specify a starting offset, in ticks. 1 tick &#x3D; 10000 ms | [optional] 
 **width** | **int**| Optional. The fixed horizontal resolution of the encoded video. | [optional] 
 **height** | **int**| Optional. The fixed vertical resolution of the encoded video. | [optional] 
 **max_width** | **int**| Optional. The maximum horizontal resolution of the encoded video. | [optional] 
 **max_height** | **int**| Optional. The maximum vertical resolution of the encoded video. | [optional] 
 **video_bit_rate** | **int**| Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. | [optional] 
 **subtitle_stream_index** | **int**| Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. | [optional] 
 **subtitle_method** | **str**| Optional. Specify the subtitle delivery method. | [optional] 
 **max_ref_frames** | **int**| Optional. | [optional] 
 **max_video_bit_depth** | **int**| Optional. | [optional] 
 **video_codec** | **str**| Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url&#x27;s extension. Options: h264, mpeg4, theora, vpx, wmv. | [optional] 
 **audio_stream_index** | **int**| Optional. The index of the audio stream to use. If omitted the first audio stream will be used. | [optional] 
 **video_stream_index** | **int**| Optional. The index of the video stream to use. If omitted the first video stream will be used. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer**
> head_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer(playlist_id, segment_id, segment_container, id, container, device_profile_id=device_profile_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, audio_sample_rate=audio_sample_rate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, static=static, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, video_codec=video_codec, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.DynamicHlsServiceApi()
playlist_id = 'playlist_id_example' # str | 
segment_id = 'segment_id_example' # str | 
segment_container = 'segment_container_example' # str | SegmentContainer
id = 'id_example' # str | Item Id
container = 'container_example' # str | Container
device_profile_id = 'device_profile_id_example' # str | Optional. The dlna device profile id to utilize. (optional)
device_id = 'device_id_example' # str | The device id of the client requesting. Used to stop encoding processes when needed. (optional)
audio_codec = 'audio_codec_example' # str | Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma. (optional)
enable_auto_stream_copy = true # bool | Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. (optional)
audio_sample_rate = 56 # int | Optional. Specify a specific audio sample rate, e.g. 44100 (optional)
audio_bit_rate = 56 # int | Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. (optional)
audio_channels = 56 # int | Optional. Specify a specific number of audio channels to encode to, e.g. 2 (optional)
max_audio_channels = 56 # int | Optional. Specify a maximum number of audio channels to encode to, e.g. 2 (optional)
static = true # bool | Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false (optional)
profile = 'profile_example' # str | Optional. Specify a specific h264 profile, e.g. main, baseline, high. (optional)
level = 'level_example' # str | Optional. Specify a level for the h264 profile, e.g. 3, 3.1. (optional)
framerate = 3.4 # float | Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. (optional)
max_framerate = 3.4 # float | Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. (optional)
copy_timestamps = true # bool | Whether or not to copy timestamps when transcoding with an offset. Defaults to false. (optional)
start_time_ticks = 789 # int | Optional. Specify a starting offset, in ticks. 1 tick = 10000 ms (optional)
width = 56 # int | Optional. The fixed horizontal resolution of the encoded video. (optional)
height = 56 # int | Optional. The fixed vertical resolution of the encoded video. (optional)
max_width = 56 # int | Optional. The maximum horizontal resolution of the encoded video. (optional)
max_height = 56 # int | Optional. The maximum vertical resolution of the encoded video. (optional)
video_bit_rate = 56 # int | Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. (optional)
subtitle_stream_index = 56 # int | Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. (optional)
subtitle_method = 'subtitle_method_example' # str | Optional. Specify the subtitle delivery method. (optional)
max_ref_frames = 56 # int | Optional. (optional)
max_video_bit_depth = 56 # int | Optional. (optional)
video_codec = 'video_codec_example' # str | Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h264, mpeg4, theora, vpx, wmv. (optional)
audio_stream_index = 56 # int | Optional. The index of the audio stream to use. If omitted the first audio stream will be used. (optional)
video_stream_index = 56 # int | Optional. The index of the video stream to use. If omitted the first video stream will be used. (optional)

try:
    api_instance.head_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer(playlist_id, segment_id, segment_container, id, container, device_profile_id=device_profile_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, audio_sample_rate=audio_sample_rate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, static=static, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, video_codec=video_codec, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index)
except ApiException as e:
    print("Exception when calling DynamicHlsServiceApi->head_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **str**|  | 
 **segment_id** | **str**|  | 
 **segment_container** | **str**| SegmentContainer | 
 **id** | **str**| Item Id | 
 **container** | **str**| Container | 
 **device_profile_id** | **str**| Optional. The dlna device profile id to utilize. | [optional] 
 **device_id** | **str**| The device id of the client requesting. Used to stop encoding processes when needed. | [optional] 
 **audio_codec** | **str**| Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url&#x27;s extension. Options: aac, mp3, vorbis, wma. | [optional] 
 **enable_auto_stream_copy** | **bool**| Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. | [optional] 
 **audio_sample_rate** | **int**| Optional. Specify a specific audio sample rate, e.g. 44100 | [optional] 
 **audio_bit_rate** | **int**| Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. | [optional] 
 **audio_channels** | **int**| Optional. Specify a specific number of audio channels to encode to, e.g. 2 | [optional] 
 **max_audio_channels** | **int**| Optional. Specify a maximum number of audio channels to encode to, e.g. 2 | [optional] 
 **static** | **bool**| Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false | [optional] 
 **profile** | **str**| Optional. Specify a specific h264 profile, e.g. main, baseline, high. | [optional] 
 **level** | **str**| Optional. Specify a level for the h264 profile, e.g. 3, 3.1. | [optional] 
 **framerate** | **float**| Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. | [optional] 
 **max_framerate** | **float**| Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. | [optional] 
 **copy_timestamps** | **bool**| Whether or not to copy timestamps when transcoding with an offset. Defaults to false. | [optional] 
 **start_time_ticks** | **int**| Optional. Specify a starting offset, in ticks. 1 tick &#x3D; 10000 ms | [optional] 
 **width** | **int**| Optional. The fixed horizontal resolution of the encoded video. | [optional] 
 **height** | **int**| Optional. The fixed vertical resolution of the encoded video. | [optional] 
 **max_width** | **int**| Optional. The maximum horizontal resolution of the encoded video. | [optional] 
 **max_height** | **int**| Optional. The maximum vertical resolution of the encoded video. | [optional] 
 **video_bit_rate** | **int**| Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. | [optional] 
 **subtitle_stream_index** | **int**| Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. | [optional] 
 **subtitle_method** | **str**| Optional. Specify the subtitle delivery method. | [optional] 
 **max_ref_frames** | **int**| Optional. | [optional] 
 **max_video_bit_depth** | **int**| Optional. | [optional] 
 **video_codec** | **str**| Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url&#x27;s extension. Options: h264, mpeg4, theora, vpx, wmv. | [optional] 
 **audio_stream_index** | **int**| Optional. The index of the audio stream to use. If omitted the first audio stream will be used. | [optional] 
 **video_stream_index** | **int**| Optional. The index of the video stream to use. If omitted the first video stream will be used. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_videos_by_id_master_m3u8**
> head_videos_by_id_master_m3u8(id, container, device_profile_id=device_profile_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, audio_sample_rate=audio_sample_rate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, static=static, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, video_codec=video_codec, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index)

Gets a video stream using HTTP live streaming.

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.DynamicHlsServiceApi()
id = 'id_example' # str | Item Id
container = 'container_example' # str | Container
device_profile_id = 'device_profile_id_example' # str | Optional. The dlna device profile id to utilize. (optional)
device_id = 'device_id_example' # str | The device id of the client requesting. Used to stop encoding processes when needed. (optional)
audio_codec = 'audio_codec_example' # str | Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma. (optional)
enable_auto_stream_copy = true # bool | Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. (optional)
audio_sample_rate = 56 # int | Optional. Specify a specific audio sample rate, e.g. 44100 (optional)
audio_bit_rate = 56 # int | Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. (optional)
audio_channels = 56 # int | Optional. Specify a specific number of audio channels to encode to, e.g. 2 (optional)
max_audio_channels = 56 # int | Optional. Specify a maximum number of audio channels to encode to, e.g. 2 (optional)
static = true # bool | Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false (optional)
profile = 'profile_example' # str | Optional. Specify a specific h264 profile, e.g. main, baseline, high. (optional)
level = 'level_example' # str | Optional. Specify a level for the h264 profile, e.g. 3, 3.1. (optional)
framerate = 3.4 # float | Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. (optional)
max_framerate = 3.4 # float | Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. (optional)
copy_timestamps = true # bool | Whether or not to copy timestamps when transcoding with an offset. Defaults to false. (optional)
start_time_ticks = 789 # int | Optional. Specify a starting offset, in ticks. 1 tick = 10000 ms (optional)
width = 56 # int | Optional. The fixed horizontal resolution of the encoded video. (optional)
height = 56 # int | Optional. The fixed vertical resolution of the encoded video. (optional)
max_width = 56 # int | Optional. The maximum horizontal resolution of the encoded video. (optional)
max_height = 56 # int | Optional. The maximum vertical resolution of the encoded video. (optional)
video_bit_rate = 56 # int | Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. (optional)
subtitle_stream_index = 56 # int | Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. (optional)
subtitle_method = 'subtitle_method_example' # str | Optional. Specify the subtitle delivery method. (optional)
max_ref_frames = 56 # int | Optional. (optional)
max_video_bit_depth = 56 # int | Optional. (optional)
video_codec = 'video_codec_example' # str | Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h264, mpeg4, theora, vpx, wmv. (optional)
audio_stream_index = 56 # int | Optional. The index of the audio stream to use. If omitted the first audio stream will be used. (optional)
video_stream_index = 56 # int | Optional. The index of the video stream to use. If omitted the first video stream will be used. (optional)

try:
    # Gets a video stream using HTTP live streaming.
    api_instance.head_videos_by_id_master_m3u8(id, container, device_profile_id=device_profile_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, audio_sample_rate=audio_sample_rate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, static=static, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, video_codec=video_codec, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index)
except ApiException as e:
    print("Exception when calling DynamicHlsServiceApi->head_videos_by_id_master_m3u8: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **container** | **str**| Container | 
 **device_profile_id** | **str**| Optional. The dlna device profile id to utilize. | [optional] 
 **device_id** | **str**| The device id of the client requesting. Used to stop encoding processes when needed. | [optional] 
 **audio_codec** | **str**| Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url&#x27;s extension. Options: aac, mp3, vorbis, wma. | [optional] 
 **enable_auto_stream_copy** | **bool**| Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. | [optional] 
 **audio_sample_rate** | **int**| Optional. Specify a specific audio sample rate, e.g. 44100 | [optional] 
 **audio_bit_rate** | **int**| Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. | [optional] 
 **audio_channels** | **int**| Optional. Specify a specific number of audio channels to encode to, e.g. 2 | [optional] 
 **max_audio_channels** | **int**| Optional. Specify a maximum number of audio channels to encode to, e.g. 2 | [optional] 
 **static** | **bool**| Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false | [optional] 
 **profile** | **str**| Optional. Specify a specific h264 profile, e.g. main, baseline, high. | [optional] 
 **level** | **str**| Optional. Specify a level for the h264 profile, e.g. 3, 3.1. | [optional] 
 **framerate** | **float**| Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. | [optional] 
 **max_framerate** | **float**| Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. | [optional] 
 **copy_timestamps** | **bool**| Whether or not to copy timestamps when transcoding with an offset. Defaults to false. | [optional] 
 **start_time_ticks** | **int**| Optional. Specify a starting offset, in ticks. 1 tick &#x3D; 10000 ms | [optional] 
 **width** | **int**| Optional. The fixed horizontal resolution of the encoded video. | [optional] 
 **height** | **int**| Optional. The fixed vertical resolution of the encoded video. | [optional] 
 **max_width** | **int**| Optional. The maximum horizontal resolution of the encoded video. | [optional] 
 **max_height** | **int**| Optional. The maximum vertical resolution of the encoded video. | [optional] 
 **video_bit_rate** | **int**| Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. | [optional] 
 **subtitle_stream_index** | **int**| Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. | [optional] 
 **subtitle_method** | **str**| Optional. Specify the subtitle delivery method. | [optional] 
 **max_ref_frames** | **int**| Optional. | [optional] 
 **max_video_bit_depth** | **int**| Optional. | [optional] 
 **video_codec** | **str**| Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url&#x27;s extension. Options: h264, mpeg4, theora, vpx, wmv. | [optional] 
 **audio_stream_index** | **int**| Optional. The index of the audio stream to use. If omitted the first audio stream will be used. | [optional] 
 **video_stream_index** | **int**| Optional. The index of the video stream to use. If omitted the first video stream will be used. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

