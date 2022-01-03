# embyapi.UserViewsServiceApi

All URIs are relative to *https://home.ourflix.de:32865/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_users_by_userid_groupingoptions**](UserViewsServiceApi.md#get_users_by_userid_groupingoptions) | **GET** /Users/{UserId}/GroupingOptions | 
[**get_users_by_userid_views**](UserViewsServiceApi.md#get_users_by_userid_views) | **GET** /Users/{UserId}/Views | 

# **get_users_by_userid_groupingoptions**
> list[BaseItemDto] get_users_by_userid_groupingoptions(user_id)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.UserViewsServiceApi()
user_id = 'user_id_example' # str | User Id

try:
    api_response = api_instance.get_users_by_userid_groupingoptions(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserViewsServiceApi->get_users_by_userid_groupingoptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | 

### Return type

[**list[BaseItemDto]**](BaseItemDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_by_userid_views**
> QueryResultBaseItemDto get_users_by_userid_views(user_id, include_external_content)



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.UserViewsServiceApi()
user_id = 'user_id_example' # str | User Id
include_external_content = true # bool | Whether or not to include external views such as channels or live tv

try:
    api_response = api_instance.get_users_by_userid_views(user_id, include_external_content)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserViewsServiceApi->get_users_by_userid_views: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | 
 **include_external_content** | **bool**| Whether or not to include external views such as channels or live tv | 

### Return type

[**QueryResultBaseItemDto**](QueryResultBaseItemDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

