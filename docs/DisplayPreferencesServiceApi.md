# embyapi.DisplayPreferencesServiceApi

All URIs are relative to *https://home.ourflix.de:32865/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_displaypreferences_by_id**](DisplayPreferencesServiceApi.md#get_displaypreferences_by_id) | **GET** /DisplayPreferences/{Id} | Gets a user&#x27;s display preferences for an item
[**post_displaypreferences_by_displaypreferencesid**](DisplayPreferencesServiceApi.md#post_displaypreferences_by_displaypreferencesid) | **POST** /DisplayPreferences/{DisplayPreferencesId} | Updates a user&#x27;s display preferences for an item

# **get_displaypreferences_by_id**
> DisplayPreferences get_displaypreferences_by_id(id, user_id, client)

Gets a user's display preferences for an item

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
api_instance = embyapi.DisplayPreferencesServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Item Id
user_id = 'user_id_example' # str | User Id
client = 'client_example' # str | Client

try:
    # Gets a user's display preferences for an item
    api_response = api_instance.get_displaypreferences_by_id(id, user_id, client)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisplayPreferencesServiceApi->get_displaypreferences_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **user_id** | **str**| User Id | 
 **client** | **str**| Client | 

### Return type

[**DisplayPreferences**](DisplayPreferences.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_displaypreferences_by_displaypreferencesid**
> post_displaypreferences_by_displaypreferencesid(body, user_id, display_preferences_id)

Updates a user's display preferences for an item

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
api_instance = embyapi.DisplayPreferencesServiceApi(embyapi.ApiClient(configuration))
body = embyapi.DisplayPreferences() # DisplayPreferences | DisplayPreferences: 
user_id = 'user_id_example' # str | User Id
display_preferences_id = 'display_preferences_id_example' # str | DisplayPreferences Id

try:
    # Updates a user's display preferences for an item
    api_instance.post_displaypreferences_by_displaypreferencesid(body, user_id, display_preferences_id)
except ApiException as e:
    print("Exception when calling DisplayPreferencesServiceApi->post_displaypreferences_by_displaypreferencesid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DisplayPreferences**](DisplayPreferences.md)| DisplayPreferences:  | 
 **user_id** | **str**| User Id | 
 **display_preferences_id** | **str**| DisplayPreferences Id | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

