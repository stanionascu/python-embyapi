# embyapi.EncodingInfoServiceApi

All URIs are relative to *https://home.ourflix.de:32865/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_encoding_codecconfiguration_defaults**](EncodingInfoServiceApi.md#get_encoding_codecconfiguration_defaults) | **GET** /Encoding/CodecConfiguration/Defaults | Gets default codec configurations
[**get_encoding_codecinformation_video**](EncodingInfoServiceApi.md#get_encoding_codecinformation_video) | **GET** /Encoding/CodecInformation/Video | Gets details about available video encoders and decoders

# **get_encoding_codecconfiguration_defaults**
> list[ConfigurationCodecConfiguration] get_encoding_codecconfiguration_defaults()

Gets default codec configurations

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
api_instance = embyapi.EncodingInfoServiceApi(embyapi.ApiClient(configuration))

try:
    # Gets default codec configurations
    api_response = api_instance.get_encoding_codecconfiguration_defaults()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EncodingInfoServiceApi->get_encoding_codecconfiguration_defaults: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ConfigurationCodecConfiguration]**](ConfigurationCodecConfiguration.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_encoding_codecinformation_video**
> list[MediaEncodingCodecsVideoCodecsVideoCodecBase] get_encoding_codecinformation_video()

Gets details about available video encoders and decoders

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
api_instance = embyapi.EncodingInfoServiceApi(embyapi.ApiClient(configuration))

try:
    # Gets details about available video encoders and decoders
    api_response = api_instance.get_encoding_codecinformation_video()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EncodingInfoServiceApi->get_encoding_codecinformation_video: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[MediaEncodingCodecsVideoCodecsVideoCodecBase]**](MediaEncodingCodecsVideoCodecsVideoCodecBase.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

