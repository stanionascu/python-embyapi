# embyapi.OpenApiServiceApi

All URIs are relative to *https://home.ourflix.de:32865/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_openapi**](OpenApiServiceApi.md#get_openapi) | **GET** /openapi | Gets the OpenAPI 3 specifications
[**get_openapi_json**](OpenApiServiceApi.md#get_openapi_json) | **GET** /openapi.json | Gets OpenAPI 3 specifications
[**get_swagger**](OpenApiServiceApi.md#get_swagger) | **GET** /swagger | Gets the swagger specifications
[**get_swagger_json**](OpenApiServiceApi.md#get_swagger_json) | **GET** /swagger.json | Gets the swagger specifications

# **get_openapi**
> str get_openapi()

Gets the OpenAPI 3 specifications

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.OpenApiServiceApi()

try:
    # Gets the OpenAPI 3 specifications
    api_response = api_instance.get_openapi()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpenApiServiceApi->get_openapi: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_openapi_json**
> str get_openapi_json()

Gets OpenAPI 3 specifications

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.OpenApiServiceApi()

try:
    # Gets OpenAPI 3 specifications
    api_response = api_instance.get_openapi_json()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpenApiServiceApi->get_openapi_json: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_swagger**
> str get_swagger()

Gets the swagger specifications

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.OpenApiServiceApi()

try:
    # Gets the swagger specifications
    api_response = api_instance.get_swagger()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpenApiServiceApi->get_swagger: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_swagger_json**
> str get_swagger_json()

Gets the swagger specifications

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.OpenApiServiceApi()

try:
    # Gets the swagger specifications
    api_response = api_instance.get_swagger_json()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpenApiServiceApi->get_swagger_json: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

