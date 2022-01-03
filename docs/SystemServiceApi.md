# embyapi.SystemServiceApi

All URIs are relative to *https://home.ourflix.de:32865/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_system_endpoint**](SystemServiceApi.md#get_system_endpoint) | **GET** /System/Endpoint | Gets information about the request endpoint
[**get_system_info**](SystemServiceApi.md#get_system_info) | **GET** /System/Info | Gets information about the server
[**get_system_info_public**](SystemServiceApi.md#get_system_info_public) | **GET** /System/Info/Public | Gets public information about the server
[**get_system_logs**](SystemServiceApi.md#get_system_logs) | **GET** /System/Logs | Gets a list of available server log files
[**get_system_logs_log**](SystemServiceApi.md#get_system_logs_log) | **GET** /System/Logs/Log | Gets a log file
[**get_system_ping**](SystemServiceApi.md#get_system_ping) | **GET** /System/Ping | 
[**get_system_wakeonlaninfo**](SystemServiceApi.md#get_system_wakeonlaninfo) | **GET** /System/WakeOnLanInfo | Gets wake on lan information
[**post_system_ping**](SystemServiceApi.md#post_system_ping) | **POST** /System/Ping | 
[**post_system_restart**](SystemServiceApi.md#post_system_restart) | **POST** /System/Restart | Restarts the application, if needed
[**post_system_shutdown**](SystemServiceApi.md#post_system_shutdown) | **POST** /System/Shutdown | Shuts down the application

# **get_system_endpoint**
> NetEndPointInfo get_system_endpoint()

Gets information about the request endpoint

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
api_instance = embyapi.SystemServiceApi(embyapi.ApiClient(configuration))

try:
    # Gets information about the request endpoint
    api_response = api_instance.get_system_endpoint()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemServiceApi->get_system_endpoint: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NetEndPointInfo**](NetEndPointInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_info**
> SystemInfo get_system_info()

Gets information about the server

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
api_instance = embyapi.SystemServiceApi(embyapi.ApiClient(configuration))

try:
    # Gets information about the server
    api_response = api_instance.get_system_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemServiceApi->get_system_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemInfo**](SystemInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_info_public**
> PublicSystemInfo get_system_info_public()

Gets public information about the server

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.SystemServiceApi()

try:
    # Gets public information about the server
    api_response = api_instance.get_system_info_public()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemServiceApi->get_system_info_public: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PublicSystemInfo**](PublicSystemInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_logs**
> list[LogFile] get_system_logs()

Gets a list of available server log files

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
api_instance = embyapi.SystemServiceApi(embyapi.ApiClient(configuration))

try:
    # Gets a list of available server log files
    api_response = api_instance.get_system_logs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemServiceApi->get_system_logs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[LogFile]**](LogFile.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_logs_log**
> get_system_logs_log(name)

Gets a log file

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
api_instance = embyapi.SystemServiceApi(embyapi.ApiClient(configuration))
name = 'name_example' # str | The log file name.

try:
    # Gets a log file
    api_instance.get_system_logs_log(name)
except ApiException as e:
    print("Exception when calling SystemServiceApi->get_system_logs_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The log file name. | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_ping**
> get_system_ping()



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.SystemServiceApi()

try:
    api_instance.get_system_ping()
except ApiException as e:
    print("Exception when calling SystemServiceApi->get_system_ping: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_wakeonlaninfo**
> list[WakeOnLanInfo] get_system_wakeonlaninfo()

Gets wake on lan information

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
api_instance = embyapi.SystemServiceApi(embyapi.ApiClient(configuration))

try:
    # Gets wake on lan information
    api_response = api_instance.get_system_wakeonlaninfo()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemServiceApi->get_system_wakeonlaninfo: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[WakeOnLanInfo]**](WakeOnLanInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_system_ping**
> post_system_ping()



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.SystemServiceApi()

try:
    api_instance.post_system_ping()
except ApiException as e:
    print("Exception when calling SystemServiceApi->post_system_ping: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_system_restart**
> post_system_restart()

Restarts the application, if needed

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
api_instance = embyapi.SystemServiceApi(embyapi.ApiClient(configuration))

try:
    # Restarts the application, if needed
    api_instance.post_system_restart()
except ApiException as e:
    print("Exception when calling SystemServiceApi->post_system_restart: %s\n" % e)
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

# **post_system_shutdown**
> post_system_shutdown()

Shuts down the application

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
api_instance = embyapi.SystemServiceApi(embyapi.ApiClient(configuration))

try:
    # Shuts down the application
    api_instance.post_system_shutdown()
except ApiException as e:
    print("Exception when calling SystemServiceApi->post_system_shutdown: %s\n" % e)
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

