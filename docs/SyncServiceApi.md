# embyapi.SyncServiceApi

All URIs are relative to *https://home.ourflix.de:32865/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_sync_by_targetid_items**](SyncServiceApi.md#delete_sync_by_targetid_items) | **DELETE** /Sync/{TargetId}/Items | Cancels items from a sync target
[**delete_sync_jobitems_by_id**](SyncServiceApi.md#delete_sync_jobitems_by_id) | **DELETE** /Sync/JobItems/{Id} | Cancels a sync job item
[**delete_sync_jobs_by_id**](SyncServiceApi.md#delete_sync_jobs_by_id) | **DELETE** /Sync/Jobs/{Id} | Cancels a sync job.
[**get_sync_items_ready**](SyncServiceApi.md#get_sync_items_ready) | **GET** /Sync/Items/Ready | Gets ready to download sync items.
[**get_sync_jobitems**](SyncServiceApi.md#get_sync_jobitems) | **GET** /Sync/JobItems | Gets sync job items.
[**get_sync_jobitems_by_id_additionalfiles**](SyncServiceApi.md#get_sync_jobitems_by_id_additionalfiles) | **GET** /Sync/JobItems/{Id}/AdditionalFiles | Gets a sync job item file
[**get_sync_jobitems_by_id_file**](SyncServiceApi.md#get_sync_jobitems_by_id_file) | **GET** /Sync/JobItems/{Id}/File | Gets a sync job item file
[**get_sync_jobs**](SyncServiceApi.md#get_sync_jobs) | **GET** /Sync/Jobs | Gets sync jobs.
[**get_sync_jobs_by_id**](SyncServiceApi.md#get_sync_jobs_by_id) | **GET** /Sync/Jobs/{Id} | Gets a sync job.
[**get_sync_options**](SyncServiceApi.md#get_sync_options) | **GET** /Sync/Options | Gets a list of available sync targets.
[**get_sync_targets**](SyncServiceApi.md#get_sync_targets) | **GET** /Sync/Targets | Gets a list of available sync targets.
[**post_sync_by_itemid_status**](SyncServiceApi.md#post_sync_by_itemid_status) | **POST** /Sync/{ItemId}/Status | Gets sync status for an item.
[**post_sync_data**](SyncServiceApi.md#post_sync_data) | **POST** /Sync/Data | Syncs data between device and server
[**post_sync_items_cancel**](SyncServiceApi.md#post_sync_items_cancel) | **POST** /Sync/Items/Cancel | Cancels items from a sync target
[**post_sync_jobitems_by_id_enable**](SyncServiceApi.md#post_sync_jobitems_by_id_enable) | **POST** /Sync/JobItems/{Id}/Enable | Enables a cancelled or queued sync job item
[**post_sync_jobitems_by_id_markforremoval**](SyncServiceApi.md#post_sync_jobitems_by_id_markforremoval) | **POST** /Sync/JobItems/{Id}/MarkForRemoval | Marks a job item for removal
[**post_sync_jobitems_by_id_transferred**](SyncServiceApi.md#post_sync_jobitems_by_id_transferred) | **POST** /Sync/JobItems/{Id}/Transferred | Reports that a sync job item has successfully been transferred.
[**post_sync_jobitems_by_id_unmarkforremoval**](SyncServiceApi.md#post_sync_jobitems_by_id_unmarkforremoval) | **POST** /Sync/JobItems/{Id}/UnmarkForRemoval | Unmarks a job item for removal
[**post_sync_jobs**](SyncServiceApi.md#post_sync_jobs) | **POST** /Sync/Jobs | Gets sync jobs.
[**post_sync_jobs_by_id**](SyncServiceApi.md#post_sync_jobs_by_id) | **POST** /Sync/Jobs/{Id} | Updates a sync job.
[**post_sync_offlineactions**](SyncServiceApi.md#post_sync_offlineactions) | **POST** /Sync/OfflineActions | Reports an action that occurred while offline.

# **delete_sync_by_targetid_items**
> delete_sync_by_targetid_items(target_id)

Cancels items from a sync target

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
api_instance = embyapi.SyncServiceApi(embyapi.ApiClient(configuration))
target_id = 'target_id_example' # str | TargetId

try:
    # Cancels items from a sync target
    api_instance.delete_sync_by_targetid_items(target_id)
except ApiException as e:
    print("Exception when calling SyncServiceApi->delete_sync_by_targetid_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_id** | **str**| TargetId | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sync_jobitems_by_id**
> delete_sync_jobitems_by_id(id)

Cancels a sync job item

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
api_instance = embyapi.SyncServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Id

try:
    # Cancels a sync job item
    api_instance.delete_sync_jobitems_by_id(id)
except ApiException as e:
    print("Exception when calling SyncServiceApi->delete_sync_jobitems_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sync_jobs_by_id**
> delete_sync_jobs_by_id(id)

Cancels a sync job.

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
api_instance = embyapi.SyncServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Id

try:
    # Cancels a sync job.
    api_instance.delete_sync_jobs_by_id(id)
except ApiException as e:
    print("Exception when calling SyncServiceApi->delete_sync_jobs_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sync_items_ready**
> list[SyncModelSyncedItem] get_sync_items_ready(target_id)

Gets ready to download sync items.

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
api_instance = embyapi.SyncServiceApi(embyapi.ApiClient(configuration))
target_id = 'target_id_example' # str | TargetId

try:
    # Gets ready to download sync items.
    api_response = api_instance.get_sync_items_ready(target_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncServiceApi->get_sync_items_ready: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_id** | **str**| TargetId | 

### Return type

[**list[SyncModelSyncedItem]**](SyncModelSyncedItem.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sync_jobitems**
> QueryResultSyncModelSyncJobItem get_sync_jobitems()

Gets sync job items.

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
api_instance = embyapi.SyncServiceApi(embyapi.ApiClient(configuration))

try:
    # Gets sync job items.
    api_response = api_instance.get_sync_jobitems()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncServiceApi->get_sync_jobitems: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**QueryResultSyncModelSyncJobItem**](QueryResultSyncModelSyncJobItem.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sync_jobitems_by_id_additionalfiles**
> get_sync_jobitems_by_id_additionalfiles(id, name)

Gets a sync job item file

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
api_instance = embyapi.SyncServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Id
name = 'name_example' # str | Name

try:
    # Gets a sync job item file
    api_instance.get_sync_jobitems_by_id_additionalfiles(id, name)
except ApiException as e:
    print("Exception when calling SyncServiceApi->get_sync_jobitems_by_id_additionalfiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id | 
 **name** | **str**| Name | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sync_jobitems_by_id_file**
> get_sync_jobitems_by_id_file(id)

Gets a sync job item file

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
api_instance = embyapi.SyncServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Id

try:
    # Gets a sync job item file
    api_instance.get_sync_jobitems_by_id_file(id)
except ApiException as e:
    print("Exception when calling SyncServiceApi->get_sync_jobitems_by_id_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sync_jobs**
> QueryResultSyncSyncJob get_sync_jobs()

Gets sync jobs.

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
api_instance = embyapi.SyncServiceApi(embyapi.ApiClient(configuration))

try:
    # Gets sync jobs.
    api_response = api_instance.get_sync_jobs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncServiceApi->get_sync_jobs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**QueryResultSyncSyncJob**](QueryResultSyncSyncJob.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sync_jobs_by_id**
> SyncSyncJob get_sync_jobs_by_id(id)

Gets a sync job.

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
api_instance = embyapi.SyncServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Id

try:
    # Gets a sync job.
    api_response = api_instance.get_sync_jobs_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncServiceApi->get_sync_jobs_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id | 

### Return type

[**SyncSyncJob**](SyncSyncJob.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sync_options**
> SyncModelSyncDialogOptions get_sync_options(user_id, item_ids=item_ids, parent_id=parent_id, target_id=target_id, category=category)

Gets a list of available sync targets.

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
api_instance = embyapi.SyncServiceApi(embyapi.ApiClient(configuration))
user_id = 'user_id_example' # str | UserId
item_ids = 'item_ids_example' # str | ItemIds (optional)
parent_id = 'parent_id_example' # str | ParentId (optional)
target_id = 'target_id_example' # str | TargetId (optional)
category = 'category_example' # str | Category (optional)

try:
    # Gets a list of available sync targets.
    api_response = api_instance.get_sync_options(user_id, item_ids=item_ids, parent_id=parent_id, target_id=target_id, category=category)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncServiceApi->get_sync_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| UserId | 
 **item_ids** | **str**| ItemIds | [optional] 
 **parent_id** | **str**| ParentId | [optional] 
 **target_id** | **str**| TargetId | [optional] 
 **category** | **str**| Category | [optional] 

### Return type

[**SyncModelSyncDialogOptions**](SyncModelSyncDialogOptions.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sync_targets**
> list[SyncSyncTarget] get_sync_targets(user_id)

Gets a list of available sync targets.

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
api_instance = embyapi.SyncServiceApi(embyapi.ApiClient(configuration))
user_id = 'user_id_example' # str | UserId

try:
    # Gets a list of available sync targets.
    api_response = api_instance.get_sync_targets(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncServiceApi->get_sync_targets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| UserId | 

### Return type

[**list[SyncSyncTarget]**](SyncSyncTarget.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sync_by_itemid_status**
> post_sync_by_itemid_status(body, item_id)

Gets sync status for an item.

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
api_instance = embyapi.SyncServiceApi(embyapi.ApiClient(configuration))
body = embyapi.SyncModelSyncedItemProgress() # SyncModelSyncedItemProgress | SyncedItemProgress: 
item_id = 'item_id_example' # str | 

try:
    # Gets sync status for an item.
    api_instance.post_sync_by_itemid_status(body, item_id)
except ApiException as e:
    print("Exception when calling SyncServiceApi->post_sync_by_itemid_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SyncModelSyncedItemProgress**](SyncModelSyncedItemProgress.md)| SyncedItemProgress:  | 
 **item_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sync_data**
> SyncModelSyncDataResponse post_sync_data(body)

Syncs data between device and server

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
api_instance = embyapi.SyncServiceApi(embyapi.ApiClient(configuration))
body = embyapi.SyncModelSyncDataRequest() # SyncModelSyncDataRequest | SyncDataRequest: 

try:
    # Syncs data between device and server
    api_response = api_instance.post_sync_data(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncServiceApi->post_sync_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SyncModelSyncDataRequest**](SyncModelSyncDataRequest.md)| SyncDataRequest:  | 

### Return type

[**SyncModelSyncDataResponse**](SyncModelSyncDataResponse.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sync_items_cancel**
> post_sync_items_cancel(item_ids=item_ids)

Cancels items from a sync target

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
api_instance = embyapi.SyncServiceApi(embyapi.ApiClient(configuration))
item_ids = 'item_ids_example' # str | ItemIds (optional)

try:
    # Cancels items from a sync target
    api_instance.post_sync_items_cancel(item_ids=item_ids)
except ApiException as e:
    print("Exception when calling SyncServiceApi->post_sync_items_cancel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_ids** | **str**| ItemIds | [optional] 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sync_jobitems_by_id_enable**
> post_sync_jobitems_by_id_enable(id)

Enables a cancelled or queued sync job item

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
api_instance = embyapi.SyncServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Id

try:
    # Enables a cancelled or queued sync job item
    api_instance.post_sync_jobitems_by_id_enable(id)
except ApiException as e:
    print("Exception when calling SyncServiceApi->post_sync_jobitems_by_id_enable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sync_jobitems_by_id_markforremoval**
> post_sync_jobitems_by_id_markforremoval(id)

Marks a job item for removal

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
api_instance = embyapi.SyncServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Id

try:
    # Marks a job item for removal
    api_instance.post_sync_jobitems_by_id_markforremoval(id)
except ApiException as e:
    print("Exception when calling SyncServiceApi->post_sync_jobitems_by_id_markforremoval: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sync_jobitems_by_id_transferred**
> post_sync_jobitems_by_id_transferred(id)

Reports that a sync job item has successfully been transferred.

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
api_instance = embyapi.SyncServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Id

try:
    # Reports that a sync job item has successfully been transferred.
    api_instance.post_sync_jobitems_by_id_transferred(id)
except ApiException as e:
    print("Exception when calling SyncServiceApi->post_sync_jobitems_by_id_transferred: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sync_jobitems_by_id_unmarkforremoval**
> post_sync_jobitems_by_id_unmarkforremoval(id)

Unmarks a job item for removal

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
api_instance = embyapi.SyncServiceApi(embyapi.ApiClient(configuration))
id = 'id_example' # str | Id

try:
    # Unmarks a job item for removal
    api_instance.post_sync_jobitems_by_id_unmarkforremoval(id)
except ApiException as e:
    print("Exception when calling SyncServiceApi->post_sync_jobitems_by_id_unmarkforremoval: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sync_jobs**
> SyncModelSyncJobCreationResult post_sync_jobs(body)

Gets sync jobs.

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
api_instance = embyapi.SyncServiceApi(embyapi.ApiClient(configuration))
body = embyapi.SyncModelSyncJobRequest() # SyncModelSyncJobRequest | SyncJobRequest: 

try:
    # Gets sync jobs.
    api_response = api_instance.post_sync_jobs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncServiceApi->post_sync_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SyncModelSyncJobRequest**](SyncModelSyncJobRequest.md)| SyncJobRequest:  | 

### Return type

[**SyncModelSyncJobCreationResult**](SyncModelSyncJobCreationResult.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sync_jobs_by_id**
> post_sync_jobs_by_id(body, id)

Updates a sync job.

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
api_instance = embyapi.SyncServiceApi(embyapi.ApiClient(configuration))
body = embyapi.SyncSyncJob() # SyncSyncJob | SyncJob: 
id = 789 # int | 

try:
    # Updates a sync job.
    api_instance.post_sync_jobs_by_id(body, id)
except ApiException as e:
    print("Exception when calling SyncServiceApi->post_sync_jobs_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SyncSyncJob**](SyncSyncJob.md)| SyncJob:  | 
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sync_offlineactions**
> post_sync_offlineactions(body)

Reports an action that occurred while offline.

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
api_instance = embyapi.SyncServiceApi(embyapi.ApiClient(configuration))
body = [embyapi.UsersUserAction()] # list[UsersUserAction] | List`1: 

try:
    # Reports an action that occurred while offline.
    api_instance.post_sync_offlineactions(body)
except ApiException as e:
    print("Exception when calling SyncServiceApi->post_sync_offlineactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[UsersUserAction]**](UsersUserAction.md)| List&#x60;1:  | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

