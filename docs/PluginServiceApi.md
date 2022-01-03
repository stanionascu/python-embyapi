# embyapi.PluginServiceApi

All URIs are relative to *https://home.ourflix.de:32865/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_plugins_by_id**](PluginServiceApi.md#delete_plugins_by_id) | **DELETE** /Plugins/{Id} | Uninstalls a plugin
[**get_plugins**](PluginServiceApi.md#get_plugins) | **GET** /Plugins | Gets a list of currently installed plugins
[**get_plugins_by_id_configuration**](PluginServiceApi.md#get_plugins_by_id_configuration) | **GET** /Plugins/{Id}/Configuration | Gets a plugin&#x27;s configuration
[**get_plugins_by_id_thumb**](PluginServiceApi.md#get_plugins_by_id_thumb) | **GET** /Plugins/{Id}/Thumb | Gets a plugin thumb image
[**post_plugins_by_id_configuration**](PluginServiceApi.md#post_plugins_by_id_configuration) | **POST** /Plugins/{Id}/Configuration | Updates a plugin&#x27;s configuration

# **delete_plugins_by_id**
> delete_plugins_by_id(id)

Uninstalls a plugin

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
api_instance = embyapi.PluginServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Plugin Id

try:
    # Uninstalls a plugin
    api_instance.delete_plugins_by_id(id)
except ApiException as e:
    print("Exception when calling PluginServiceApi->delete_plugins_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Plugin Id | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plugins**
> list[PluginsPluginInfo] get_plugins()

Gets a list of currently installed plugins

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
api_instance = embyapi.PluginServiceApi(embyapi.ApiClient(configuration))

try:
    # Gets a list of currently installed plugins
    api_response = api_instance.get_plugins()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginServiceApi->get_plugins: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PluginsPluginInfo]**](PluginsPluginInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plugins_by_id_configuration**
> get_plugins_by_id_configuration(id)

Gets a plugin's configuration

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
api_instance = embyapi.PluginServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Plugin Id

try:
    # Gets a plugin's configuration
    api_instance.get_plugins_by_id_configuration(id)
except ApiException as e:
    print("Exception when calling PluginServiceApi->get_plugins_by_id_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Plugin Id | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plugins_by_id_thumb**
> get_plugins_by_id_thumb(id)

Gets a plugin thumb image

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.PluginServiceApi()
id = 'id_example' # str | Plugin Id

try:
    # Gets a plugin thumb image
    api_instance.get_plugins_by_id_thumb(id)
except ApiException as e:
    print("Exception when calling PluginServiceApi->get_plugins_by_id_thumb: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Plugin Id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_plugins_by_id_configuration**
> post_plugins_by_id_configuration(body, id)

Updates a plugin's configuration

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
api_instance = embyapi.PluginServiceApi(embyapi.ApiClient(configuration))
body = embyapi.Object() # Object | Binary stream
id = 'id_example' # str | Plugin Id

try:
    # Updates a plugin's configuration
    api_instance.post_plugins_by_id_configuration(body, id)
except ApiException as e:
    print("Exception when calling PluginServiceApi->post_plugins_by_id_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Object**| Binary stream | 
 **id** | **str**| Plugin Id | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

