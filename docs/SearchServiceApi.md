# embyapi.SearchServiceApi

All URIs are relative to *https://home.ourflix.de:32865/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_search_hints**](SearchServiceApi.md#get_search_hints) | **GET** /Search/Hints | Gets search hints based on a search term

# **get_search_hints**
> SearchSearchHintResult get_search_hints(search_term, start_index=start_index, limit=limit, user_id=user_id, include_people=include_people, include_media=include_media, include_genres=include_genres, include_studios=include_studios, include_artists=include_artists, include_item_types=include_item_types, exclude_item_types=exclude_item_types, media_types=media_types, is_movie=is_movie, is_series=is_series, is_news=is_news, is_kids=is_kids, is_sports=is_sports)

Gets search hints based on a search term

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
api_instance = embyapi.SearchServiceApi(embyapi.ApiClient(configuration))
search_term = 'search_term_example' # str | The search term to filter on
start_index = 56 # int | Optional. The record index to start at. All items with a lower index will be dropped from the results. (optional)
limit = 56 # int | Optional. The maximum number of records to return (optional)
user_id = 'user_id_example' # str | Optional. Supply a user id to search within a user's library or omit to search all. (optional)
include_people = true # bool |  (optional)
include_media = true # bool |  (optional)
include_genres = true # bool |  (optional)
include_studios = true # bool |  (optional)
include_artists = true # bool |  (optional)
include_item_types = 'include_item_types_example' # str | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. (optional)
exclude_item_types = 'exclude_item_types_example' # str | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. (optional)
media_types = 'media_types_example' # str | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. (optional)
is_movie = true # bool | Optional filter for movies. (optional)
is_series = true # bool | Optional filter for movies. (optional)
is_news = true # bool | Optional filter for news. (optional)
is_kids = true # bool | Optional filter for kids. (optional)
is_sports = true # bool | Optional filter for sports. (optional)

try:
    # Gets search hints based on a search term
    api_response = api_instance.get_search_hints(search_term, start_index=start_index, limit=limit, user_id=user_id, include_people=include_people, include_media=include_media, include_genres=include_genres, include_studios=include_studios, include_artists=include_artists, include_item_types=include_item_types, exclude_item_types=exclude_item_types, media_types=media_types, is_movie=is_movie, is_series=is_series, is_news=is_news, is_kids=is_kids, is_sports=is_sports)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchServiceApi->get_search_hints: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_term** | **str**| The search term to filter on | 
 **start_index** | **int**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return | [optional] 
 **user_id** | **str**| Optional. Supply a user id to search within a user&#x27;s library or omit to search all. | [optional] 
 **include_people** | **bool**|  | [optional] 
 **include_media** | **bool**|  | [optional] 
 **include_genres** | **bool**|  | [optional] 
 **include_studios** | **bool**|  | [optional] 
 **include_artists** | **bool**|  | [optional] 
 **include_item_types** | **str**| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. | [optional] 
 **exclude_item_types** | **str**| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. | [optional] 
 **media_types** | **str**| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. | [optional] 
 **is_movie** | **bool**| Optional filter for movies. | [optional] 
 **is_series** | **bool**| Optional filter for movies. | [optional] 
 **is_news** | **bool**| Optional filter for news. | [optional] 
 **is_kids** | **bool**| Optional filter for kids. | [optional] 
 **is_sports** | **bool**| Optional filter for sports. | [optional] 

### Return type

[**SearchSearchHintResult**](SearchSearchHintResult.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

