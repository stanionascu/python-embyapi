# embyapi.SuggestionsServiceApi

All URIs are relative to *https://home.ourflix.de:32865/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_users_by_userid_suggestions**](SuggestionsServiceApi.md#get_users_by_userid_suggestions) | **GET** /Users/{UserId}/Suggestions | Gets items based on a query.

# **get_users_by_userid_suggestions**
> QueryResultBaseItemDto get_users_by_userid_suggestions(user_id)

Gets items based on a query.

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.SuggestionsServiceApi()
user_id = 'user_id_example' # str | 

try:
    # Gets items based on a query.
    api_response = api_instance.get_users_by_userid_suggestions(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SuggestionsServiceApi->get_users_by_userid_suggestions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**QueryResultBaseItemDto**](QueryResultBaseItemDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

