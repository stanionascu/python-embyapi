# embyapi.ConfigurationServiceApi

All URIs are relative to *https://home.ourflix.de:32865/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_system_configuration**](ConfigurationServiceApi.md#get_system_configuration) | **GET** /System/Configuration | Gets application configuration
[**get_system_configuration_by_key**](ConfigurationServiceApi.md#get_system_configuration_by_key) | **GET** /System/Configuration/{Key} | Gets a named configuration
[**post_system_configuration**](ConfigurationServiceApi.md#post_system_configuration) | **POST** /System/Configuration | Updates application configuration
[**post_system_configuration_by_key**](ConfigurationServiceApi.md#post_system_configuration_by_key) | **POST** /System/Configuration/{Key} | Updates named configuration

# **get_system_configuration**
> ConfigurationServerConfiguration get_system_configuration()

Gets application configuration

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
api_instance = embyapi.ConfigurationServiceApi(embyapi.ApiClient(configuration))

try:
    # Gets application configuration
    api_response = api_instance.get_system_configuration()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationServiceApi->get_system_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConfigurationServerConfiguration**](ConfigurationServerConfiguration.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_configuration_by_key**
> get_system_configuration_by_key(key)

Gets a named configuration

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
api_instance = embyapi.ConfigurationServiceApi(embyapi.ApiClient(configuration))
key = 'key_example' # str | Key

try:
    # Gets a named configuration
    api_instance.get_system_configuration_by_key(key)
except ApiException as e:
    print("Exception when calling ConfigurationServiceApi->get_system_configuration_by_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Key | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_system_configuration**
> post_system_configuration(body)

Updates application configuration

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
api_instance = embyapi.ConfigurationServiceApi(embyapi.ApiClient(configuration))
body = embyapi.ConfigurationServerConfiguration() # ConfigurationServerConfiguration | ServerConfiguration: 

try:
    # Updates application configuration
    api_instance.post_system_configuration(body)
except ApiException as e:
    print("Exception when calling ConfigurationServiceApi->post_system_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConfigurationServerConfiguration**](ConfigurationServerConfiguration.md)| ServerConfiguration:  | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_system_configuration_by_key**
> post_system_configuration_by_key(body, key)

Updates named configuration

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
api_instance = embyapi.ConfigurationServiceApi(embyapi.ApiClient(configuration))
body = embyapi.Object() # Object | Binary stream
key = 'key_example' # str | Key

try:
    # Updates named configuration
    api_instance.post_system_configuration_by_key(body, key)
except ApiException as e:
    print("Exception when calling ConfigurationServiceApi->post_system_configuration_by_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Object**| Binary stream | 
 **key** | **str**| Key | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

