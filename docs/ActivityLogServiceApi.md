# embyapi.ActivityLogServiceApi

All URIs are relative to *https://home.ourflix.de:32865/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_system_activitylog_entries**](ActivityLogServiceApi.md#get_system_activitylog_entries) | **GET** /System/ActivityLog/Entries | Gets activity log entries

# **get_system_activitylog_entries**
> QueryResultActivityLogEntry get_system_activitylog_entries(start_index=start_index, limit=limit, min_date=min_date)

Gets activity log entries

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
api_instance = embyapi.ActivityLogServiceApi(embyapi.ApiClient(configuration))
start_index = 56 # int | Optional. The record index to start at. All items with a lower index will be dropped from the results. (optional)
limit = 56 # int | Optional. The maximum number of records to return (optional)
min_date = 'min_date_example' # str | Optional. The minimum date. Format = ISO (optional)

try:
    # Gets activity log entries
    api_response = api_instance.get_system_activitylog_entries(start_index=start_index, limit=limit, min_date=min_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityLogServiceApi->get_system_activitylog_entries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_index** | **int**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return | [optional] 
 **min_date** | **str**| Optional. The minimum date. Format &#x3D; ISO | [optional] 

### Return type

[**QueryResultActivityLogEntry**](QueryResultActivityLogEntry.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

