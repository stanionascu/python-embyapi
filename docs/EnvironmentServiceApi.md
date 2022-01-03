# embyapi.EnvironmentServiceApi

All URIs are relative to *https://home.ourflix.de:32865/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_environment_defaultdirectorybrowser**](EnvironmentServiceApi.md#get_environment_defaultdirectorybrowser) | **GET** /Environment/DefaultDirectoryBrowser | Gets the parent path of a given path
[**get_environment_directorycontents**](EnvironmentServiceApi.md#get_environment_directorycontents) | **GET** /Environment/DirectoryContents | Gets the contents of a given directory in the file system
[**get_environment_drives**](EnvironmentServiceApi.md#get_environment_drives) | **GET** /Environment/Drives | Gets available drives from the server&#x27;s file system
[**get_environment_networkdevices**](EnvironmentServiceApi.md#get_environment_networkdevices) | **GET** /Environment/NetworkDevices | Gets a list of devices on the network
[**get_environment_networkshares**](EnvironmentServiceApi.md#get_environment_networkshares) | **GET** /Environment/NetworkShares | Gets shares from a network device
[**get_environment_parentpath**](EnvironmentServiceApi.md#get_environment_parentpath) | **GET** /Environment/ParentPath | Gets the parent path of a given path
[**post_environment_validatepath**](EnvironmentServiceApi.md#post_environment_validatepath) | **POST** /Environment/ValidatePath | Gets the contents of a given directory in the file system

# **get_environment_defaultdirectorybrowser**
> DefaultDirectoryBrowserInfo get_environment_defaultdirectorybrowser()

Gets the parent path of a given path

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
api_instance = embyapi.EnvironmentServiceApi(embyapi.ApiClient(configuration))

try:
    # Gets the parent path of a given path
    api_response = api_instance.get_environment_defaultdirectorybrowser()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentServiceApi->get_environment_defaultdirectorybrowser: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DefaultDirectoryBrowserInfo**](DefaultDirectoryBrowserInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_environment_directorycontents**
> list[IOFileSystemEntryInfo] get_environment_directorycontents(path, include_files=include_files, include_directories=include_directories)

Gets the contents of a given directory in the file system

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
api_instance = embyapi.EnvironmentServiceApi(embyapi.ApiClient(configuration))
path = 'path_example' # str | 
include_files = true # bool | An optional filter to include or exclude files from the results. true/false (optional)
include_directories = true # bool | An optional filter to include or exclude folders from the results. true/false (optional)

try:
    # Gets the contents of a given directory in the file system
    api_response = api_instance.get_environment_directorycontents(path, include_files=include_files, include_directories=include_directories)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentServiceApi->get_environment_directorycontents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **include_files** | **bool**| An optional filter to include or exclude files from the results. true/false | [optional] 
 **include_directories** | **bool**| An optional filter to include or exclude folders from the results. true/false | [optional] 

### Return type

[**list[IOFileSystemEntryInfo]**](IOFileSystemEntryInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_environment_drives**
> list[IOFileSystemEntryInfo] get_environment_drives()

Gets available drives from the server's file system

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
api_instance = embyapi.EnvironmentServiceApi(embyapi.ApiClient(configuration))

try:
    # Gets available drives from the server's file system
    api_response = api_instance.get_environment_drives()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentServiceApi->get_environment_drives: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[IOFileSystemEntryInfo]**](IOFileSystemEntryInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_environment_networkdevices**
> list[IOFileSystemEntryInfo] get_environment_networkdevices()

Gets a list of devices on the network

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
api_instance = embyapi.EnvironmentServiceApi(embyapi.ApiClient(configuration))

try:
    # Gets a list of devices on the network
    api_response = api_instance.get_environment_networkdevices()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentServiceApi->get_environment_networkdevices: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[IOFileSystemEntryInfo]**](IOFileSystemEntryInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_environment_networkshares**
> list[IOFileSystemEntryInfo] get_environment_networkshares(path)

Gets shares from a network device

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
api_instance = embyapi.EnvironmentServiceApi(embyapi.ApiClient(configuration))
path = 'path_example' # str | 

try:
    # Gets shares from a network device
    api_response = api_instance.get_environment_networkshares(path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentServiceApi->get_environment_networkshares: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 

### Return type

[**list[IOFileSystemEntryInfo]**](IOFileSystemEntryInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_environment_parentpath**
> str get_environment_parentpath(path)

Gets the parent path of a given path

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
api_instance = embyapi.EnvironmentServiceApi(embyapi.ApiClient(configuration))
path = 'path_example' # str | 

try:
    # Gets the parent path of a given path
    api_response = api_instance.get_environment_parentpath(path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentServiceApi->get_environment_parentpath: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 

### Return type

**str**

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_environment_validatepath**
> post_environment_validatepath(body, path)

Gets the contents of a given directory in the file system

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
api_instance = embyapi.EnvironmentServiceApi(embyapi.ApiClient(configuration))
body = embyapi.ValidatePath() # ValidatePath | ValidatePath
path = 'path_example' # str | 

try:
    # Gets the contents of a given directory in the file system
    api_instance.post_environment_validatepath(body, path)
except ApiException as e:
    print("Exception when calling EnvironmentServiceApi->post_environment_validatepath: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ValidatePath**](ValidatePath.md)| ValidatePath | 
 **path** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

