# embyapi.UserActivityAPIApi

All URIs are relative to *https://home.ourflix.de:32865/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_usage_stats_by_breakdowntype_breakdownreport**](UserActivityAPIApi.md#get_user_usage_stats_by_breakdowntype_breakdownreport) | **GET** /user_usage_stats/{BreakdownType}/BreakdownReport | Gets a breakdown of a usage metric
[**get_user_usage_stats_by_userid_by_date_getitems**](UserActivityAPIApi.md#get_user_usage_stats_by_userid_by_date_getitems) | **GET** /user_usage_stats/{UserID}/{Date}/GetItems | Gets activity for {USER} for {Date} formatted as yyyy-MM-dd
[**get_user_usage_stats_durationhistogramreport**](UserActivityAPIApi.md#get_user_usage_stats_durationhistogramreport) | **GET** /user_usage_stats/DurationHistogramReport | Gets duration histogram
[**get_user_usage_stats_hourlyreport**](UserActivityAPIApi.md#get_user_usage_stats_hourlyreport) | **GET** /user_usage_stats/HourlyReport | Gets a report of the available activity per hour
[**get_user_usage_stats_load_backup**](UserActivityAPIApi.md#get_user_usage_stats_load_backup) | **GET** /user_usage_stats/load_backup | Loads a backup from a file
[**get_user_usage_stats_moviesreport**](UserActivityAPIApi.md#get_user_usage_stats_moviesreport) | **GET** /user_usage_stats/MoviesReport | Gets Movies counts
[**get_user_usage_stats_playactivity**](UserActivityAPIApi.md#get_user_usage_stats_playactivity) | **GET** /user_usage_stats/PlayActivity | Gets play activity for number of days
[**get_user_usage_stats_process_list**](UserActivityAPIApi.md#get_user_usage_stats_process_list) | **GET** /user_usage_stats/process_list | Gets a list of process Info
[**get_user_usage_stats_resource_usage**](UserActivityAPIApi.md#get_user_usage_stats_resource_usage) | **GET** /user_usage_stats/resource_usage | Gets Resource Usage Info
[**get_user_usage_stats_save_backup**](UserActivityAPIApi.md#get_user_usage_stats_save_backup) | **GET** /user_usage_stats/save_backup | Saves a backup of the playback report data to the backup path
[**get_user_usage_stats_session_list**](UserActivityAPIApi.md#get_user_usage_stats_session_list) | **GET** /user_usage_stats/session_list | Gets Session Info
[**get_user_usage_stats_tvshowsreport**](UserActivityAPIApi.md#get_user_usage_stats_tvshowsreport) | **GET** /user_usage_stats/TvShowsReport | Gets TV Shows counts
[**get_user_usage_stats_type_filter_list**](UserActivityAPIApi.md#get_user_usage_stats_type_filter_list) | **GET** /user_usage_stats/type_filter_list | Gets types filter list items
[**get_user_usage_stats_user_activity**](UserActivityAPIApi.md#get_user_usage_stats_user_activity) | **GET** /user_usage_stats/user_activity | Gets a report of the available activity per hour
[**get_user_usage_stats_user_list**](UserActivityAPIApi.md#get_user_usage_stats_user_list) | **GET** /user_usage_stats/user_list | Get users
[**get_user_usage_stats_user_manage_by_action_by_id**](UserActivityAPIApi.md#get_user_usage_stats_user_manage_by_action_by_id) | **GET** /user_usage_stats/user_manage/{Action}/{Id} | Get users
[**get_user_usage_stats_userplaylist**](UserActivityAPIApi.md#get_user_usage_stats_userplaylist) | **GET** /user_usage_stats/UserPlaylist | Gets a report of all played items for a user in a date period
[**post_user_usage_stats_import_backup**](UserActivityAPIApi.md#post_user_usage_stats_import_backup) | **POST** /user_usage_stats/import_backup | Post a backup for importing
[**post_user_usage_stats_submit_custom_query**](UserActivityAPIApi.md#post_user_usage_stats_submit_custom_query) | **POST** /user_usage_stats/submit_custom_query | Submit an SQL query

# **get_user_usage_stats_by_breakdowntype_breakdownreport**
> object get_user_usage_stats_by_breakdowntype_breakdownreport(breakdown_type, days=days, end_date=end_date)

Gets a breakdown of a usage metric

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.UserActivityAPIApi()
breakdown_type = 'breakdown_type_example' # str | Breakdown type
days = 56 # int | Number of Days (optional)
end_date = 'end_date_example' # str | End date of the report in yyyy-MM-dd format (optional)

try:
    # Gets a breakdown of a usage metric
    api_response = api_instance.get_user_usage_stats_by_breakdowntype_breakdownreport(breakdown_type, days=days, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserActivityAPIApi->get_user_usage_stats_by_breakdowntype_breakdownreport: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **breakdown_type** | **str**| Breakdown type | 
 **days** | **int**| Number of Days | [optional] 
 **end_date** | **str**| End date of the report in yyyy-MM-dd format | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_usage_stats_by_userid_by_date_getitems**
> object get_user_usage_stats_by_userid_by_date_getitems(user_id, _date, filter=filter)

Gets activity for {USER} for {Date} formatted as yyyy-MM-dd

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.UserActivityAPIApi()
user_id = 'user_id_example' # str | User Id
_date = '_date_example' # str | UTC DateTime, Format yyyy-MM-dd
filter = 'filter_example' # str | Comma separated list of media types to filter (movies,series) (optional)

try:
    # Gets activity for {USER} for {Date} formatted as yyyy-MM-dd
    api_response = api_instance.get_user_usage_stats_by_userid_by_date_getitems(user_id, _date, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserActivityAPIApi->get_user_usage_stats_by_userid_by_date_getitems: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | 
 **_date** | **str**| UTC DateTime, Format yyyy-MM-dd | 
 **filter** | **str**| Comma separated list of media types to filter (movies,series) | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_usage_stats_durationhistogramreport**
> object get_user_usage_stats_durationhistogramreport(days=days, end_date=end_date, filter=filter)

Gets duration histogram

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.UserActivityAPIApi()
days = 56 # int | Number of Days (optional)
end_date = 'end_date_example' # str | End date of the report in yyyy-MM-dd format (optional)
filter = 'filter_example' # str | Comma separated list of media types to filter (movies,series) (optional)

try:
    # Gets duration histogram
    api_response = api_instance.get_user_usage_stats_durationhistogramreport(days=days, end_date=end_date, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserActivityAPIApi->get_user_usage_stats_durationhistogramreport: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **days** | **int**| Number of Days | [optional] 
 **end_date** | **str**| End date of the report in yyyy-MM-dd format | [optional] 
 **filter** | **str**| Comma separated list of media types to filter (movies,series) | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_usage_stats_hourlyreport**
> object get_user_usage_stats_hourlyreport(days=days, end_date=end_date, filter=filter)

Gets a report of the available activity per hour

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.UserActivityAPIApi()
days = 56 # int | Number of Days (optional)
end_date = 'end_date_example' # str | End date of the report in yyyy-MM-dd format (optional)
filter = 'filter_example' # str | Comma separated list of media types to filter (movies,series) (optional)

try:
    # Gets a report of the available activity per hour
    api_response = api_instance.get_user_usage_stats_hourlyreport(days=days, end_date=end_date, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserActivityAPIApi->get_user_usage_stats_hourlyreport: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **days** | **int**| Number of Days | [optional] 
 **end_date** | **str**| End date of the report in yyyy-MM-dd format | [optional] 
 **filter** | **str**| Comma separated list of media types to filter (movies,series) | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_usage_stats_load_backup**
> object get_user_usage_stats_load_backup(backupfile)

Loads a backup from a file

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.UserActivityAPIApi()
backupfile = 'backupfile_example' # str | File name of file to load

try:
    # Loads a backup from a file
    api_response = api_instance.get_user_usage_stats_load_backup(backupfile)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserActivityAPIApi->get_user_usage_stats_load_backup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backupfile** | **str**| File name of file to load | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_usage_stats_moviesreport**
> object get_user_usage_stats_moviesreport(days=days, end_date=end_date)

Gets Movies counts

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.UserActivityAPIApi()
days = 56 # int | Number of Days (optional)
end_date = 'end_date_example' # str | End date of the report in yyyy-MM-dd format (optional)

try:
    # Gets Movies counts
    api_response = api_instance.get_user_usage_stats_moviesreport(days=days, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserActivityAPIApi->get_user_usage_stats_moviesreport: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **days** | **int**| Number of Days | [optional] 
 **end_date** | **str**| End date of the report in yyyy-MM-dd format | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_usage_stats_playactivity**
> object get_user_usage_stats_playactivity(days=days, end_date=end_date, filter=filter, data_type=data_type)

Gets play activity for number of days

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.UserActivityAPIApi()
days = 56 # int | Number of Days (optional)
end_date = 'end_date_example' # str | End date of the report in yyyy-MM-dd format (optional)
filter = 'filter_example' # str | Comma separated list of media types to filter (movies,series) (optional)
data_type = 'data_type_example' # str | Data type to return (count,time) (optional)

try:
    # Gets play activity for number of days
    api_response = api_instance.get_user_usage_stats_playactivity(days=days, end_date=end_date, filter=filter, data_type=data_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserActivityAPIApi->get_user_usage_stats_playactivity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **days** | **int**| Number of Days | [optional] 
 **end_date** | **str**| End date of the report in yyyy-MM-dd format | [optional] 
 **filter** | **str**| Comma separated list of media types to filter (movies,series) | [optional] 
 **data_type** | **str**| Data type to return (count,time) | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_usage_stats_process_list**
> object get_user_usage_stats_process_list()

Gets a list of process Info

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.UserActivityAPIApi()

try:
    # Gets a list of process Info
    api_response = api_instance.get_user_usage_stats_process_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserActivityAPIApi->get_user_usage_stats_process_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_usage_stats_resource_usage**
> object get_user_usage_stats_resource_usage(hours=hours)

Gets Resource Usage Info

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.UserActivityAPIApi()
hours = 56 # int | Number of Hours (optional)

try:
    # Gets Resource Usage Info
    api_response = api_instance.get_user_usage_stats_resource_usage(hours=hours)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserActivityAPIApi->get_user_usage_stats_resource_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hours** | **int**| Number of Hours | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_usage_stats_save_backup**
> object get_user_usage_stats_save_backup()

Saves a backup of the playback report data to the backup path

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.UserActivityAPIApi()

try:
    # Saves a backup of the playback report data to the backup path
    api_response = api_instance.get_user_usage_stats_save_backup()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserActivityAPIApi->get_user_usage_stats_save_backup: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_usage_stats_session_list**
> object get_user_usage_stats_session_list()

Gets Session Info

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.UserActivityAPIApi()

try:
    # Gets Session Info
    api_response = api_instance.get_user_usage_stats_session_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserActivityAPIApi->get_user_usage_stats_session_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_usage_stats_tvshowsreport**
> object get_user_usage_stats_tvshowsreport(days=days, end_date=end_date)

Gets TV Shows counts

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.UserActivityAPIApi()
days = 56 # int | Number of Days (optional)
end_date = 'end_date_example' # str | End date of the report in yyyy-MM-dd format (optional)

try:
    # Gets TV Shows counts
    api_response = api_instance.get_user_usage_stats_tvshowsreport(days=days, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserActivityAPIApi->get_user_usage_stats_tvshowsreport: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **days** | **int**| Number of Days | [optional] 
 **end_date** | **str**| End date of the report in yyyy-MM-dd format | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_usage_stats_type_filter_list**
> object get_user_usage_stats_type_filter_list()

Gets types filter list items

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.UserActivityAPIApi()

try:
    # Gets types filter list items
    api_response = api_instance.get_user_usage_stats_type_filter_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserActivityAPIApi->get_user_usage_stats_type_filter_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_usage_stats_user_activity**
> object get_user_usage_stats_user_activity(days=days, end_date=end_date)

Gets a report of the available activity per hour

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.UserActivityAPIApi()
days = 56 # int | Number of Days (optional)
end_date = 'end_date_example' # str | End date of the report in yyyy-MM-dd format (optional)

try:
    # Gets a report of the available activity per hour
    api_response = api_instance.get_user_usage_stats_user_activity(days=days, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserActivityAPIApi->get_user_usage_stats_user_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **days** | **int**| Number of Days | [optional] 
 **end_date** | **str**| End date of the report in yyyy-MM-dd format | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_usage_stats_user_list**
> object get_user_usage_stats_user_list()

Get users

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.UserActivityAPIApi()

try:
    # Get users
    api_response = api_instance.get_user_usage_stats_user_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserActivityAPIApi->get_user_usage_stats_user_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_usage_stats_user_manage_by_action_by_id**
> object get_user_usage_stats_user_manage_by_action_by_id(action, id)

Get users

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.UserActivityAPIApi()
action = 'action_example' # str | action to perform
id = 'id_example' # str | user Id to perform the action on

try:
    # Get users
    api_response = api_instance.get_user_usage_stats_user_manage_by_action_by_id(action, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserActivityAPIApi->get_user_usage_stats_user_manage_by_action_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **str**| action to perform | 
 **id** | **str**| user Id to perform the action on | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_usage_stats_userplaylist**
> object get_user_usage_stats_userplaylist(user_id, days=days, end_date=end_date, filter=filter)

Gets a report of all played items for a user in a date period

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.UserActivityAPIApi()
user_id = 'user_id_example' # str | User Id
days = 56 # int | Number of Days (optional)
end_date = 'end_date_example' # str | End date of the report in yyyy-MM-dd format (optional)
filter = 'filter_example' # str | Comma separated list of media types to filter (movies,series) (optional)

try:
    # Gets a report of all played items for a user in a date period
    api_response = api_instance.get_user_usage_stats_userplaylist(user_id, days=days, end_date=end_date, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserActivityAPIApi->get_user_usage_stats_userplaylist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | 
 **days** | **int**| Number of Days | [optional] 
 **end_date** | **str**| End date of the report in yyyy-MM-dd format | [optional] 
 **filter** | **str**| Comma separated list of media types to filter (movies,series) | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_user_usage_stats_import_backup**
> post_user_usage_stats_import_backup(body)

Post a backup for importing

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.UserActivityAPIApi()
body = embyapi.Object() # Object | Binary stream

try:
    # Post a backup for importing
    api_instance.post_user_usage_stats_import_backup(body)
except ApiException as e:
    print("Exception when calling UserActivityAPIApi->post_user_usage_stats_import_backup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Object**| Binary stream | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_user_usage_stats_submit_custom_query**
> object post_user_usage_stats_submit_custom_query(body)

Submit an SQL query

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.UserActivityAPIApi()
body = embyapi.PlaybackReportingApiCustomQuery() # PlaybackReportingApiCustomQuery | CustomQuery

try:
    # Submit an SQL query
    api_response = api_instance.post_user_usage_stats_submit_custom_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserActivityAPIApi->post_user_usage_stats_submit_custom_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PlaybackReportingApiCustomQuery**](PlaybackReportingApiCustomQuery.md)| CustomQuery | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

