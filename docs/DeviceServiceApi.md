# embyapi.DeviceServiceApi

All URIs are relative to *https://home.ourflix.de:32865/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_devices**](DeviceServiceApi.md#delete_devices) | **DELETE** /Devices | Deletes a device
[**get_devices**](DeviceServiceApi.md#get_devices) | **GET** /Devices | Gets all devices
[**get_devices_camerauploads**](DeviceServiceApi.md#get_devices_camerauploads) | **GET** /Devices/CameraUploads | Gets camera upload history for a device
[**get_devices_info**](DeviceServiceApi.md#get_devices_info) | **GET** /Devices/Info | Gets info for a device
[**get_devices_options**](DeviceServiceApi.md#get_devices_options) | **GET** /Devices/Options | Gets options for a device
[**post_devices_camerauploads**](DeviceServiceApi.md#post_devices_camerauploads) | **POST** /Devices/CameraUploads | Uploads content
[**post_devices_options**](DeviceServiceApi.md#post_devices_options) | **POST** /Devices/Options | Updates device options

# **delete_devices**
> delete_devices(id)

Deletes a device

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.DeviceServiceApi()
id = 'id_example' # str | Device Id

try:
    # Deletes a device
    api_instance.delete_devices(id)
except ApiException as e:
    print("Exception when calling DeviceServiceApi->delete_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device Id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_devices**
> QueryResultDevicesDeviceInfo get_devices()

Gets all devices

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
api_instance = embyapi.DeviceServiceApi(embyapi.ApiClient(configuration))

try:
    # Gets all devices
    api_response = api_instance.get_devices()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceServiceApi->get_devices: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**QueryResultDevicesDeviceInfo**](QueryResultDevicesDeviceInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_devices_camerauploads**
> DevicesContentUploadHistory get_devices_camerauploads(device_id)

Gets camera upload history for a device

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
api_instance = embyapi.DeviceServiceApi(embyapi.ApiClient(configuration))
device_id = 'device_id_example' # str | Device Id

try:
    # Gets camera upload history for a device
    api_response = api_instance.get_devices_camerauploads(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceServiceApi->get_devices_camerauploads: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device Id | 

### Return type

[**DevicesContentUploadHistory**](DevicesContentUploadHistory.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_devices_info**
> DevicesDeviceInfo get_devices_info(id)

Gets info for a device

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
api_instance = embyapi.DeviceServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Device Id

try:
    # Gets info for a device
    api_response = api_instance.get_devices_info(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceServiceApi->get_devices_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device Id | 

### Return type

[**DevicesDeviceInfo**](DevicesDeviceInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_devices_options**
> DevicesDeviceOptions get_devices_options(id)

Gets options for a device

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
api_instance = embyapi.DeviceServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Device Id

try:
    # Gets options for a device
    api_response = api_instance.get_devices_options(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceServiceApi->get_devices_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device Id | 

### Return type

[**DevicesDeviceOptions**](DevicesDeviceOptions.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_devices_camerauploads**
> post_devices_camerauploads(body, device_id, album, name, id)

Uploads content

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
api_instance = embyapi.DeviceServiceApi(embyapi.ApiClient(configuration))
body = embyapi.Object() # Object | Binary stream
device_id = 'device_id_example' # str | Device Id
album = 'album_example' # str | Album
name = 'name_example' # str | Name
id = 'id_example' # str | Id

try:
    # Uploads content
    api_instance.post_devices_camerauploads(body, device_id, album, name, id)
except ApiException as e:
    print("Exception when calling DeviceServiceApi->post_devices_camerauploads: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Object**| Binary stream | 
 **device_id** | **str**| Device Id | 
 **album** | **str**| Album | 
 **name** | **str**| Name | 
 **id** | **str**| Id | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_devices_options**
> post_devices_options(body)

Updates device options

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
api_instance = embyapi.DeviceServiceApi(embyapi.ApiClient(configuration))
body = embyapi.DevicesDeviceOptions() # DevicesDeviceOptions | DeviceOptions: 

try:
    # Updates device options
    api_instance.post_devices_options(body)
except ApiException as e:
    print("Exception when calling DeviceServiceApi->post_devices_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DevicesDeviceOptions**](DevicesDeviceOptions.md)| DeviceOptions:  | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

