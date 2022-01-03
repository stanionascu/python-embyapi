# embyapi.LocalizationServiceApi

All URIs are relative to *https://home.ourflix.de:32865/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_localization_countries**](LocalizationServiceApi.md#get_localization_countries) | **GET** /Localization/Countries | Gets known countries
[**get_localization_cultures**](LocalizationServiceApi.md#get_localization_cultures) | **GET** /Localization/Cultures | Gets known cultures
[**get_localization_options**](LocalizationServiceApi.md#get_localization_options) | **GET** /Localization/Options | Gets localization options
[**get_localization_parentalratings**](LocalizationServiceApi.md#get_localization_parentalratings) | **GET** /Localization/ParentalRatings | Gets known parental ratings

# **get_localization_countries**
> list[GlobalizationCountryInfo] get_localization_countries()

Gets known countries

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
api_instance = embyapi.LocalizationServiceApi(embyapi.ApiClient(configuration))

try:
    # Gets known countries
    api_response = api_instance.get_localization_countries()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocalizationServiceApi->get_localization_countries: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[GlobalizationCountryInfo]**](GlobalizationCountryInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_localization_cultures**
> list[GlobalizationCultureDto] get_localization_cultures()

Gets known cultures

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
api_instance = embyapi.LocalizationServiceApi(embyapi.ApiClient(configuration))

try:
    # Gets known cultures
    api_response = api_instance.get_localization_cultures()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocalizationServiceApi->get_localization_cultures: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[GlobalizationCultureDto]**](GlobalizationCultureDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_localization_options**
> list[GlobalizationLocalizatonOption] get_localization_options()

Gets localization options

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
api_instance = embyapi.LocalizationServiceApi(embyapi.ApiClient(configuration))

try:
    # Gets localization options
    api_response = api_instance.get_localization_options()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocalizationServiceApi->get_localization_options: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[GlobalizationLocalizatonOption]**](GlobalizationLocalizatonOption.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_localization_parentalratings**
> list[ParentalRating] get_localization_parentalratings()

Gets known parental ratings

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
api_instance = embyapi.LocalizationServiceApi(embyapi.ApiClient(configuration))

try:
    # Gets known parental ratings
    api_response = api_instance.get_localization_parentalratings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocalizationServiceApi->get_localization_parentalratings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ParentalRating]**](ParentalRating.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

