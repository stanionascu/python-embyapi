# embyapi.GamesServiceApi

All URIs are relative to *https://home.ourflix.de:32865/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_games_systemsummaries**](GamesServiceApi.md#get_games_systemsummaries) | **GET** /Games/SystemSummaries | Finds games similar to a given game.

# **get_games_systemsummaries**
> list[GameSystemSummary] get_games_systemsummaries(user_id=user_id)

Finds games similar to a given game.

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
api_instance = embyapi.GamesServiceApi(embyapi.ApiClient(configuration))
user_id = 'user_id_example' # str | Optional. Filter by user id (optional)

try:
    # Finds games similar to a given game.
    api_response = api_instance.get_games_systemsummaries(user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamesServiceApi->get_games_systemsummaries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Optional. Filter by user id | [optional] 

### Return type

[**list[GameSystemSummary]**](GameSystemSummary.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

