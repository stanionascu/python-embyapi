# embyapi.PackageServiceApi

All URIs are relative to *https://home.ourflix.de:32865/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_packages_installing_by_id**](PackageServiceApi.md#delete_packages_installing_by_id) | **DELETE** /Packages/Installing/{Id} | Cancels a package installation
[**get_packages**](PackageServiceApi.md#get_packages) | **GET** /Packages | Gets available packages
[**get_packages_by_name**](PackageServiceApi.md#get_packages_by_name) | **GET** /Packages/{Name} | Gets a package, by name or assembly guid
[**get_packages_updates**](PackageServiceApi.md#get_packages_updates) | **GET** /Packages/Updates | Gets available package updates for currently installed packages
[**post_packages_installed_by_name**](PackageServiceApi.md#post_packages_installed_by_name) | **POST** /Packages/Installed/{Name} | Installs a package

# **delete_packages_installing_by_id**
> delete_packages_installing_by_id(id)

Cancels a package installation

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
api_instance = embyapi.PackageServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Installation Id

try:
    # Cancels a package installation
    api_instance.delete_packages_installing_by_id(id)
except ApiException as e:
    print("Exception when calling PackageServiceApi->delete_packages_installing_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Installation Id | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_packages**
> list[UpdatesPackageInfo] get_packages(package_type=package_type, target_systems=target_systems, is_premium=is_premium, is_adult=is_adult)

Gets available packages

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
api_instance = embyapi.PackageServiceApi(embyapi.ApiClient(configuration))
package_type = 'package_type_example' # str | Optional package type filter (System/UserInstalled) (optional)
target_systems = 'target_systems_example' # str | Optional. Filter by target system type. Allows multiple, comma delimited. (optional)
is_premium = true # bool | Optional. Filter by premium status (optional)
is_adult = true # bool | Optional. Filter by package that contain adult content. (optional)

try:
    # Gets available packages
    api_response = api_instance.get_packages(package_type=package_type, target_systems=target_systems, is_premium=is_premium, is_adult=is_adult)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackageServiceApi->get_packages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package_type** | **str**| Optional package type filter (System/UserInstalled) | [optional] 
 **target_systems** | **str**| Optional. Filter by target system type. Allows multiple, comma delimited. | [optional] 
 **is_premium** | **bool**| Optional. Filter by premium status | [optional] 
 **is_adult** | **bool**| Optional. Filter by package that contain adult content. | [optional] 

### Return type

[**list[UpdatesPackageInfo]**](UpdatesPackageInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_packages_by_name**
> UpdatesPackageInfo get_packages_by_name(name, assembly_guid=assembly_guid)

Gets a package, by name or assembly guid

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
api_instance = embyapi.PackageServiceApi(embyapi.ApiClient(configuration))
name = 'name_example' # str | The name of the package
assembly_guid = 'assembly_guid_example' # str | The guid of the associated assembly (optional)

try:
    # Gets a package, by name or assembly guid
    api_response = api_instance.get_packages_by_name(name, assembly_guid=assembly_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackageServiceApi->get_packages_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the package | 
 **assembly_guid** | **str**| The guid of the associated assembly | [optional] 

### Return type

[**UpdatesPackageInfo**](UpdatesPackageInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_packages_updates**
> list[UpdatesPackageVersionInfo] get_packages_updates(package_type)

Gets available package updates for currently installed packages

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
api_instance = embyapi.PackageServiceApi(embyapi.ApiClient(configuration))
package_type = 'package_type_example' # str | Package type filter (System/UserInstalled)

try:
    # Gets available package updates for currently installed packages
    api_response = api_instance.get_packages_updates(package_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackageServiceApi->get_packages_updates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package_type** | **str**| Package type filter (System/UserInstalled) | 

### Return type

[**list[UpdatesPackageVersionInfo]**](UpdatesPackageVersionInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_packages_installed_by_name**
> post_packages_installed_by_name(name, assembly_guid=assembly_guid, version=version, update_class=update_class)

Installs a package

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
api_instance = embyapi.PackageServiceApi(embyapi.ApiClient(configuration))
name = 'name_example' # str | Package name
assembly_guid = 'assembly_guid_example' # str | Guid of the associated assembly (optional)
version = 'version_example' # str | Optional version. Defaults to latest version. (optional)
update_class = 'update_class_example' # str | Optional update class (Dev, Beta, Release). Defaults to Release. (optional)

try:
    # Installs a package
    api_instance.post_packages_installed_by_name(name, assembly_guid=assembly_guid, version=version, update_class=update_class)
except ApiException as e:
    print("Exception when calling PackageServiceApi->post_packages_installed_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Package name | 
 **assembly_guid** | **str**| Guid of the associated assembly | [optional] 
 **version** | **str**| Optional version. Defaults to latest version. | [optional] 
 **update_class** | **str**| Optional update class (Dev, Beta, Release). Defaults to Release. | [optional] 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

