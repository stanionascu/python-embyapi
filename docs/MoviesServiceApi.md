# embyapi.MoviesServiceApi

All URIs are relative to *https://home.ourflix.de:32865/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_movies_recommendations**](MoviesServiceApi.md#get_movies_recommendations) | **GET** /Movies/Recommendations | Gets movie recommendations

# **get_movies_recommendations**
> list[RecommendationDto] get_movies_recommendations(category_limit=category_limit, item_limit=item_limit, user_id=user_id, parent_id=parent_id, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types)

Gets movie recommendations

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
api_instance = embyapi.MoviesServiceApi(embyapi.ApiClient(configuration))
category_limit = 56 # int | The max number of categories to return (optional)
item_limit = 56 # int | The max number of items to return per category (optional)
user_id = 'user_id_example' # str | Optional. Filter by user id, and attach user data (optional)
parent_id = 'parent_id_example' # str | Specify this to localize the search to a specific item or folder. Omit to use the root (optional)
enable_images = true # bool | Optional, include image information in output (optional)
enable_user_data = true # bool | Optional, include user data (optional)
image_type_limit = 56 # int | Optional, the max number of images to return, per image type (optional)
enable_image_types = 'enable_image_types_example' # str | Optional. The image types to include in the output. (optional)

try:
    # Gets movie recommendations
    api_response = api_instance.get_movies_recommendations(category_limit=category_limit, item_limit=item_limit, user_id=user_id, parent_id=parent_id, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MoviesServiceApi->get_movies_recommendations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_limit** | **int**| The max number of categories to return | [optional] 
 **item_limit** | **int**| The max number of items to return per category | [optional] 
 **user_id** | **str**| Optional. Filter by user id, and attach user data | [optional] 
 **parent_id** | **str**| Specify this to localize the search to a specific item or folder. Omit to use the root | [optional] 
 **enable_images** | **bool**| Optional, include image information in output | [optional] 
 **enable_user_data** | **bool**| Optional, include user data | [optional] 
 **image_type_limit** | **int**| Optional, the max number of images to return, per image type | [optional] 
 **enable_image_types** | **str**| Optional. The image types to include in the output. | [optional] 

### Return type

[**list[RecommendationDto]**](RecommendationDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

