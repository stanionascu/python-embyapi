# embyapi.BrandingServiceApi

All URIs are relative to *https://home.ourflix.de:32865/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_branding_configuration**](BrandingServiceApi.md#get_branding_configuration) | **GET** /Branding/Configuration | Gets branding configuration
[**get_branding_css**](BrandingServiceApi.md#get_branding_css) | **GET** /Branding/Css | Gets custom css
[**get_branding_css_css**](BrandingServiceApi.md#get_branding_css_css) | **GET** /Branding/Css.css | Gets custom css

# **get_branding_configuration**
> BrandingBrandingOptions get_branding_configuration()

Gets branding configuration

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.BrandingServiceApi()

try:
    # Gets branding configuration
    api_response = api_instance.get_branding_configuration()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BrandingServiceApi->get_branding_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BrandingBrandingOptions**](BrandingBrandingOptions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_branding_css**
> get_branding_css()

Gets custom css

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.BrandingServiceApi()

try:
    # Gets custom css
    api_instance.get_branding_css()
except ApiException as e:
    print("Exception when calling BrandingServiceApi->get_branding_css: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_branding_css_css**
> get_branding_css_css()

Gets custom css

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.BrandingServiceApi()

try:
    # Gets custom css
    api_instance.get_branding_css_css()
except ApiException as e:
    print("Exception when calling BrandingServiceApi->get_branding_css_css: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

