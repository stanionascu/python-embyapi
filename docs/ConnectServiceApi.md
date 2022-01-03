# embyapi.ConnectServiceApi

All URIs are relative to *https://home.ourflix.de:32865/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_users_by_id_connect_link**](ConnectServiceApi.md#delete_users_by_id_connect_link) | **DELETE** /Users/{Id}/Connect/Link | Removes a Connect link for a user
[**get_connect_exchange**](ConnectServiceApi.md#get_connect_exchange) | **GET** /Connect/Exchange | Gets the corresponding local user from a connect user id
[**get_connect_pending**](ConnectServiceApi.md#get_connect_pending) | **GET** /Connect/Pending | Creates a Connect link for a user
[**post_users_by_id_connect_link**](ConnectServiceApi.md#post_users_by_id_connect_link) | **POST** /Users/{Id}/Connect/Link | Creates a Connect link for a user

# **delete_users_by_id_connect_link**
> delete_users_by_id_connect_link(id)

Removes a Connect link for a user

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
api_instance = embyapi.ConnectServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | User Id

try:
    # Removes a Connect link for a user
    api_instance.delete_users_by_id_connect_link(id)
except ApiException as e:
    print("Exception when calling ConnectServiceApi->delete_users_by_id_connect_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User Id | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connect_exchange**
> ConnectConnectAuthenticationExchangeResult get_connect_exchange(connect_user_id)

Gets the corresponding local user from a connect user id

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
api_instance = embyapi.ConnectServiceApi(embyapi.ApiClient(configuration))
connect_user_id = 'connect_user_id_example' # str | ConnectUserId

try:
    # Gets the corresponding local user from a connect user id
    api_response = api_instance.get_connect_exchange(connect_user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectServiceApi->get_connect_exchange: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connect_user_id** | **str**| ConnectUserId | 

### Return type

[**ConnectConnectAuthenticationExchangeResult**](ConnectConnectAuthenticationExchangeResult.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connect_pending**
> get_connect_pending()

Creates a Connect link for a user

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
api_instance = embyapi.ConnectServiceApi(embyapi.ApiClient(configuration))

try:
    # Creates a Connect link for a user
    api_instance.get_connect_pending()
except ApiException as e:
    print("Exception when calling ConnectServiceApi->get_connect_pending: %s\n" % e)
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

# **post_users_by_id_connect_link**
> ConnectUserLinkResult post_users_by_id_connect_link(id, connect_username)

Creates a Connect link for a user

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
api_instance = embyapi.ConnectServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | User Id
connect_username = 'connect_username_example' # str | Connect username

try:
    # Creates a Connect link for a user
    api_response = api_instance.post_users_by_id_connect_link(id, connect_username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectServiceApi->post_users_by_id_connect_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User Id | 
 **connect_username** | **str**| Connect username | 

### Return type

[**ConnectUserLinkResult**](ConnectUserLinkResult.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

