# embyapi.DlnaServiceApi

All URIs are relative to *https://home.ourflix.de:32865/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_dlna_profiles_by_id**](DlnaServiceApi.md#delete_dlna_profiles_by_id) | **DELETE** /Dlna/Profiles/{Id} | Deletes a profile
[**get_dlna_profileinfos**](DlnaServiceApi.md#get_dlna_profileinfos) | **GET** /Dlna/ProfileInfos | Gets a list of profiles
[**get_dlna_profiles_by_id**](DlnaServiceApi.md#get_dlna_profiles_by_id) | **GET** /Dlna/Profiles/{Id} | Gets a single profile
[**get_dlna_profiles_default**](DlnaServiceApi.md#get_dlna_profiles_default) | **GET** /Dlna/Profiles/Default | Gets the default profile
[**post_dlna_profiles**](DlnaServiceApi.md#post_dlna_profiles) | **POST** /Dlna/Profiles | Creates a profile
[**post_dlna_profiles_by_id**](DlnaServiceApi.md#post_dlna_profiles_by_id) | **POST** /Dlna/Profiles/{Id} | Updates a profile

# **delete_dlna_profiles_by_id**
> delete_dlna_profiles_by_id(id)

Deletes a profile

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
api_instance = embyapi.DlnaServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Profile Id

try:
    # Deletes a profile
    api_instance.delete_dlna_profiles_by_id(id)
except ApiException as e:
    print("Exception when calling DlnaServiceApi->delete_dlna_profiles_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Profile Id | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dlna_profileinfos**
> list[DlnaDeviceProfileInfo] get_dlna_profileinfos()

Gets a list of profiles

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
api_instance = embyapi.DlnaServiceApi(embyapi.ApiClient(configuration))

try:
    # Gets a list of profiles
    api_response = api_instance.get_dlna_profileinfos()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DlnaServiceApi->get_dlna_profileinfos: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[DlnaDeviceProfileInfo]**](DlnaDeviceProfileInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dlna_profiles_by_id**
> DlnaDeviceProfile get_dlna_profiles_by_id(id)

Gets a single profile

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
api_instance = embyapi.DlnaServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Profile Id

try:
    # Gets a single profile
    api_response = api_instance.get_dlna_profiles_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DlnaServiceApi->get_dlna_profiles_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Profile Id | 

### Return type

[**DlnaDeviceProfile**](DlnaDeviceProfile.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dlna_profiles_default**
> DlnaDeviceProfile get_dlna_profiles_default()

Gets the default profile

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
api_instance = embyapi.DlnaServiceApi(embyapi.ApiClient(configuration))

try:
    # Gets the default profile
    api_response = api_instance.get_dlna_profiles_default()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DlnaServiceApi->get_dlna_profiles_default: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DlnaDeviceProfile**](DlnaDeviceProfile.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_dlna_profiles**
> post_dlna_profiles(body)

Creates a profile

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
api_instance = embyapi.DlnaServiceApi(embyapi.ApiClient(configuration))
body = embyapi.DlnaDeviceProfile() # DlnaDeviceProfile | DeviceProfile: 

try:
    # Creates a profile
    api_instance.post_dlna_profiles(body)
except ApiException as e:
    print("Exception when calling DlnaServiceApi->post_dlna_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DlnaDeviceProfile**](DlnaDeviceProfile.md)| DeviceProfile:  | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_dlna_profiles_by_id**
> post_dlna_profiles_by_id(body, id)

Updates a profile

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
api_instance = embyapi.DlnaServiceApi(embyapi.ApiClient(configuration))
body = embyapi.DlnaDeviceProfile() # DlnaDeviceProfile | DeviceProfile: 
id = 'id_example' # str | 

try:
    # Updates a profile
    api_instance.post_dlna_profiles_by_id(body, id)
except ApiException as e:
    print("Exception when calling DlnaServiceApi->post_dlna_profiles_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DlnaDeviceProfile**](DlnaDeviceProfile.md)| DeviceProfile:  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

