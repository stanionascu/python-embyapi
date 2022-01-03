# embyapi.DashboardServiceApi

All URIs are relative to *https://home.ourflix.de:32865/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_web_configurationpage**](DashboardServiceApi.md#get_web_configurationpage) | **GET** /web/ConfigurationPage | 
[**get_web_configurationpages**](DashboardServiceApi.md#get_web_configurationpages) | **GET** /web/ConfigurationPages | 

# **get_web_configurationpage**
> get_web_configurationpage()



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.DashboardServiceApi()

try:
    api_instance.get_web_configurationpage()
except ApiException as e:
    print("Exception when calling DashboardServiceApi->get_web_configurationpage: %s\n" % e)
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

# **get_web_configurationpages**
> list[WebDashboardApiConfigurationPageInfo] get_web_configurationpages()



No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.DashboardServiceApi()

try:
    api_response = api_instance.get_web_configurationpages()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardServiceApi->get_web_configurationpages: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[WebDashboardApiConfigurationPageInfo]**](WebDashboardApiConfigurationPageInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

