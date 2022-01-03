# embyapi.NewsServiceApi

All URIs are relative to *https://home.ourflix.de:32865/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_news_product**](NewsServiceApi.md#get_news_product) | **GET** /News/Product | Gets the latest product news.

# **get_news_product**
> QueryResultNewsNewsItem get_news_product(start_index=start_index, limit=limit)

Gets the latest product news.

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.NewsServiceApi()
start_index = 56 # int | Optional. The record index to start at. All items with a lower index will be dropped from the results. (optional)
limit = 56 # int | Optional. The maximum number of records to return (optional)

try:
    # Gets the latest product news.
    api_response = api_instance.get_news_product(start_index=start_index, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NewsServiceApi->get_news_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_index** | **int**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return | [optional] 

### Return type

[**QueryResultNewsNewsItem**](QueryResultNewsNewsItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

