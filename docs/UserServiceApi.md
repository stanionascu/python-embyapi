# embyapi.UserServiceApi

All URIs are relative to *https://home.ourflix.de:32865/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_users_by_id**](UserServiceApi.md#delete_users_by_id) | **DELETE** /Users/{Id} | Deletes a user
[**get_users**](UserServiceApi.md#get_users) | **GET** /Users | Gets a list of users
[**get_users_by_id**](UserServiceApi.md#get_users_by_id) | **GET** /Users/{Id} | Gets a user by Id
[**get_users_public**](UserServiceApi.md#get_users_public) | **GET** /Users/Public | Gets a list of publicly visible users for display on a login screen.
[**post_users_authenticatebyname**](UserServiceApi.md#post_users_authenticatebyname) | **POST** /Users/AuthenticateByName | Authenticates a user
[**post_users_by_id**](UserServiceApi.md#post_users_by_id) | **POST** /Users/{Id} | Updates a user
[**post_users_by_id_authenticate**](UserServiceApi.md#post_users_by_id_authenticate) | **POST** /Users/{Id}/Authenticate | Authenticates a user
[**post_users_by_id_configuration**](UserServiceApi.md#post_users_by_id_configuration) | **POST** /Users/{Id}/Configuration | Updates a user configuration
[**post_users_by_id_easypassword**](UserServiceApi.md#post_users_by_id_easypassword) | **POST** /Users/{Id}/EasyPassword | Updates a user&#x27;s easy password
[**post_users_by_id_password**](UserServiceApi.md#post_users_by_id_password) | **POST** /Users/{Id}/Password | Updates a user&#x27;s password
[**post_users_by_id_policy**](UserServiceApi.md#post_users_by_id_policy) | **POST** /Users/{Id}/Policy | Updates a user policy
[**post_users_forgotpassword**](UserServiceApi.md#post_users_forgotpassword) | **POST** /Users/ForgotPassword | Initiates the forgot password process for a local user
[**post_users_forgotpassword_pin**](UserServiceApi.md#post_users_forgotpassword_pin) | **POST** /Users/ForgotPassword/Pin | Redeems a forgot password pin
[**post_users_new**](UserServiceApi.md#post_users_new) | **POST** /Users/New | Creates a user

# **delete_users_by_id**
> delete_users_by_id(id)

Deletes a user

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
api_instance = embyapi.UserServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Deletes a user
    api_instance.delete_users_by_id(id)
except ApiException as e:
    print("Exception when calling UserServiceApi->delete_users_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users**
> list[UserDto] get_users(is_hidden=is_hidden, is_disabled=is_disabled)

Gets a list of users

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
api_instance = embyapi.UserServiceApi(embyapi.ApiClient(configuration))
is_hidden = true # bool | Optional filter by IsHidden=true or false (optional)
is_disabled = true # bool | Optional filter by IsDisabled=true or false (optional)

try:
    # Gets a list of users
    api_response = api_instance.get_users(is_hidden=is_hidden, is_disabled=is_disabled)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserServiceApi->get_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_hidden** | **bool**| Optional filter by IsHidden&#x3D;true or false | [optional] 
 **is_disabled** | **bool**| Optional filter by IsDisabled&#x3D;true or false | [optional] 

### Return type

[**list[UserDto]**](UserDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_by_id**
> UserDto get_users_by_id(id)

Gets a user by Id

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
api_instance = embyapi.UserServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Gets a user by Id
    api_response = api_instance.get_users_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserServiceApi->get_users_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**UserDto**](UserDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_public**
> list[UserDto] get_users_public()

Gets a list of publicly visible users for display on a login screen.

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.UserServiceApi()

try:
    # Gets a list of publicly visible users for display on a login screen.
    api_response = api_instance.get_users_public()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserServiceApi->get_users_public: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[UserDto]**](UserDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_users_authenticatebyname**
> AuthenticationAuthenticationResult post_users_authenticatebyname(body, x_emby_authorization)

Authenticates a user

Authenticate a user by nane and password. A 200 status code indicates success, while anything in the 400 or 500 range indicates failure --- No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.UserServiceApi()
body = embyapi.AuthenticateUserByName() # AuthenticateUserByName | AuthenticateUserByName
x_emby_authorization = 'x_emby_authorization_example' # str | The authorization header can be either named 'Authorization' or 'X-Emby-Authorization'.    It must be of the following schema:     Emby UserId=\"(guid)\", Client=\"(string)\", Device=\"(string)\", DeviceId=\"(string)\", Version=\"string\", Token=\"(string)\"     Please consult the documentation for further details.

try:
    # Authenticates a user
    api_response = api_instance.post_users_authenticatebyname(body, x_emby_authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserServiceApi->post_users_authenticatebyname: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthenticateUserByName**](AuthenticateUserByName.md)| AuthenticateUserByName | 
 **x_emby_authorization** | **str**| The authorization header can be either named &#x27;Authorization&#x27; or &#x27;X-Emby-Authorization&#x27;.    It must be of the following schema:     Emby UserId&#x3D;\&quot;(guid)\&quot;, Client&#x3D;\&quot;(string)\&quot;, Device&#x3D;\&quot;(string)\&quot;, DeviceId&#x3D;\&quot;(string)\&quot;, Version&#x3D;\&quot;string\&quot;, Token&#x3D;\&quot;(string)\&quot;     Please consult the documentation for further details. | 

### Return type

[**AuthenticationAuthenticationResult**](AuthenticationAuthenticationResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_users_by_id**
> post_users_by_id(body, id)

Updates a user

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
api_instance = embyapi.UserServiceApi(embyapi.ApiClient(configuration))
body = embyapi.UserDto() # UserDto | UserDto: 
id = 'id_example' # str | 

try:
    # Updates a user
    api_instance.post_users_by_id(body, id)
except ApiException as e:
    print("Exception when calling UserServiceApi->post_users_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserDto**](UserDto.md)| UserDto:  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_users_by_id_authenticate**
> AuthenticationAuthenticationResult post_users_by_id_authenticate(body, id)

Authenticates a user

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.UserServiceApi()
body = embyapi.AuthenticateUser() # AuthenticateUser | AuthenticateUser
id = 'id_example' # str | 

try:
    # Authenticates a user
    api_response = api_instance.post_users_by_id_authenticate(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserServiceApi->post_users_by_id_authenticate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthenticateUser**](AuthenticateUser.md)| AuthenticateUser | 
 **id** | **str**|  | 

### Return type

[**AuthenticationAuthenticationResult**](AuthenticationAuthenticationResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_users_by_id_configuration**
> post_users_by_id_configuration(body, id)

Updates a user configuration

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
api_instance = embyapi.UserServiceApi(embyapi.ApiClient(configuration))
body = embyapi.ConfigurationUserConfiguration() # ConfigurationUserConfiguration | UserConfiguration: 
id = 'id_example' # str | 

try:
    # Updates a user configuration
    api_instance.post_users_by_id_configuration(body, id)
except ApiException as e:
    print("Exception when calling UserServiceApi->post_users_by_id_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConfigurationUserConfiguration**](ConfigurationUserConfiguration.md)| UserConfiguration:  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_users_by_id_easypassword**
> post_users_by_id_easypassword(body, id)

Updates a user's easy password

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
api_instance = embyapi.UserServiceApi(embyapi.ApiClient(configuration))
body = embyapi.UpdateUserEasyPassword() # UpdateUserEasyPassword | UpdateUserEasyPassword
id = 'id_example' # str | 

try:
    # Updates a user's easy password
    api_instance.post_users_by_id_easypassword(body, id)
except ApiException as e:
    print("Exception when calling UserServiceApi->post_users_by_id_easypassword: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateUserEasyPassword**](UpdateUserEasyPassword.md)| UpdateUserEasyPassword | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_users_by_id_password**
> post_users_by_id_password(body, id)

Updates a user's password

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
api_instance = embyapi.UserServiceApi(embyapi.ApiClient(configuration))
body = embyapi.UpdateUserPassword() # UpdateUserPassword | UpdateUserPassword
id = 'id_example' # str | 

try:
    # Updates a user's password
    api_instance.post_users_by_id_password(body, id)
except ApiException as e:
    print("Exception when calling UserServiceApi->post_users_by_id_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateUserPassword**](UpdateUserPassword.md)| UpdateUserPassword | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_users_by_id_policy**
> post_users_by_id_policy(body, id)

Updates a user policy

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
api_instance = embyapi.UserServiceApi(embyapi.ApiClient(configuration))
body = embyapi.UsersUserPolicy() # UsersUserPolicy | UserPolicy: 
id = 'id_example' # str | 

try:
    # Updates a user policy
    api_instance.post_users_by_id_policy(body, id)
except ApiException as e:
    print("Exception when calling UserServiceApi->post_users_by_id_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UsersUserPolicy**](UsersUserPolicy.md)| UserPolicy:  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_users_forgotpassword**
> UsersForgotPasswordResult post_users_forgotpassword(body)

Initiates the forgot password process for a local user

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.UserServiceApi()
body = embyapi.ForgotPassword() # ForgotPassword | ForgotPassword

try:
    # Initiates the forgot password process for a local user
    api_response = api_instance.post_users_forgotpassword(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserServiceApi->post_users_forgotpassword: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ForgotPassword**](ForgotPassword.md)| ForgotPassword | 

### Return type

[**UsersForgotPasswordResult**](UsersForgotPasswordResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_users_forgotpassword_pin**
> UsersPinRedeemResult post_users_forgotpassword_pin(body)

Redeems a forgot password pin

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.UserServiceApi()
body = embyapi.ForgotPasswordPin() # ForgotPasswordPin | ForgotPasswordPin

try:
    # Redeems a forgot password pin
    api_response = api_instance.post_users_forgotpassword_pin(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserServiceApi->post_users_forgotpassword_pin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ForgotPasswordPin**](ForgotPasswordPin.md)| ForgotPasswordPin | 

### Return type

[**UsersPinRedeemResult**](UsersPinRedeemResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_users_new**
> UserDto post_users_new(body)

Creates a user

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
api_instance = embyapi.UserServiceApi(embyapi.ApiClient(configuration))
body = embyapi.CreateUserByName() # CreateUserByName | CreateUserByName

try:
    # Creates a user
    api_response = api_instance.post_users_new(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserServiceApi->post_users_new: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateUserByName**](CreateUserByName.md)| CreateUserByName | 

### Return type

[**UserDto**](UserDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

