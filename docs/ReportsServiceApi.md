# embyapi.ReportsServiceApi

All URIs are relative to *https://home.ourflix.de:32865/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_reports_activities**](ReportsServiceApi.md#get_reports_activities) | **GET** /Reports/Activities | Gets activities entries
[**get_reports_headers**](ReportsServiceApi.md#get_reports_headers) | **GET** /Reports/Headers | Gets reports headers based on library items
[**get_reports_items**](ReportsServiceApi.md#get_reports_items) | **GET** /Reports/Items | Gets reports based on library items
[**get_reports_items_download**](ReportsServiceApi.md#get_reports_items_download) | **GET** /Reports/Items/Download | Downloads report

# **get_reports_activities**
> EmbyReportsApiModelReportResult get_reports_activities(report_view, display_type, has_query_limit=has_query_limit, group_by=group_by, report_columns=report_columns, start_index=start_index, limit=limit, include_item_types=include_item_types)

Gets activities entries

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.ReportsServiceApi()
report_view = 'report_view_example' # str | The report view. Values (ReportData, ReportActivities)
display_type = 'display_type_example' # str | The report display type. Values (None, Screen, Export, ScreenExport)
has_query_limit = true # bool | Optional. If specified, results will include all records. (optional)
group_by = 'group_by_example' # str | Optional. If specified, results will include grouped records. (optional)
report_columns = 'report_columns_example' # str | Optional. The columns to show. (optional)
start_index = 56 # int | Optional. The record index to start at. All items with a lower index will be dropped from the results. (optional)
limit = 56 # int | Optional. The maximum number of records to return (optional)
include_item_types = 'include_item_types_example' # str | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. (optional)

try:
    # Gets activities entries
    api_response = api_instance.get_reports_activities(report_view, display_type, has_query_limit=has_query_limit, group_by=group_by, report_columns=report_columns, start_index=start_index, limit=limit, include_item_types=include_item_types)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsServiceApi->get_reports_activities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_view** | **str**| The report view. Values (ReportData, ReportActivities) | 
 **display_type** | **str**| The report display type. Values (None, Screen, Export, ScreenExport) | 
 **has_query_limit** | **bool**| Optional. If specified, results will include all records. | [optional] 
 **group_by** | **str**| Optional. If specified, results will include grouped records. | [optional] 
 **report_columns** | **str**| Optional. The columns to show. | [optional] 
 **start_index** | **int**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return | [optional] 
 **include_item_types** | **str**| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. | [optional] 

### Return type

[**EmbyReportsApiModelReportResult**](EmbyReportsApiModelReportResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reports_headers**
> list[EmbyReportsApiModelReportHeader] get_reports_headers(report_view, display_type, include_item_types=include_item_types, report_columns=report_columns)

Gets reports headers based on library items

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.ReportsServiceApi()
report_view = 'report_view_example' # str | The report view. Values (ReportData, ReportActivities)
display_type = 'display_type_example' # str | The report display type. Values (None, Screen, Export, ScreenExport)
include_item_types = 'include_item_types_example' # str | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. (optional)
report_columns = 'report_columns_example' # str | Optional. The columns to show. (optional)

try:
    # Gets reports headers based on library items
    api_response = api_instance.get_reports_headers(report_view, display_type, include_item_types=include_item_types, report_columns=report_columns)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsServiceApi->get_reports_headers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_view** | **str**| The report view. Values (ReportData, ReportActivities) | 
 **display_type** | **str**| The report display type. Values (None, Screen, Export, ScreenExport) | 
 **include_item_types** | **str**| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. | [optional] 
 **report_columns** | **str**| Optional. The columns to show. | [optional] 

### Return type

[**list[EmbyReportsApiModelReportHeader]**](EmbyReportsApiModelReportHeader.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reports_items**
> EmbyReportsApiModelReportResult get_reports_items(report_view, display_type, max_official_rating=max_official_rating, has_theme_song=has_theme_song, has_theme_video=has_theme_video, has_subtitles=has_subtitles, has_special_feature=has_special_feature, has_trailer=has_trailer, adjacent_to=adjacent_to, min_index_number=min_index_number, min_players=min_players, max_players=max_players, parent_index_number=parent_index_number, has_parental_rating=has_parental_rating, is_hd=is_hd, location_types=location_types, exclude_location_types=exclude_location_types, is_missing=is_missing, is_unaired=is_unaired, min_community_rating=min_community_rating, min_critic_rating=min_critic_rating, aired_during_season=aired_during_season, min_premiere_date=min_premiere_date, min_date_last_saved=min_date_last_saved, min_date_last_saved_for_user=min_date_last_saved_for_user, max_premiere_date=max_premiere_date, has_overview=has_overview, has_imdb_id=has_imdb_id, has_tmdb_id=has_tmdb_id, has_tvdb_id=has_tvdb_id, exclude_item_ids=exclude_item_ids, start_index=start_index, limit=limit, recursive=recursive, sort_order=sort_order, parent_id=parent_id, fields=fields, exclude_item_types=exclude_item_types, include_item_types=include_item_types, filters=filters, is_favorite=is_favorite, is_movie=is_movie, is_series=is_series, is_news=is_news, is_kids=is_kids, is_sports=is_sports, media_types=media_types, image_types=image_types, sort_by=sort_by, is_played=is_played, genres=genres, official_ratings=official_ratings, tags=tags, years=years, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, person=person, person_ids=person_ids, person_types=person_types, studios=studios, studio_ids=studio_ids, artists=artists, artist_ids=artist_ids, albums=albums, ids=ids, video_types=video_types, containers=containers, user_id=user_id, min_official_rating=min_official_rating, is_locked=is_locked, is_place_holder=is_place_holder, has_official_rating=has_official_rating, collapse_box_set_items=collapse_box_set_items, is3_d=is3_d, series_status=series_status, name_starts_with_or_greater=name_starts_with_or_greater, name_starts_with=name_starts_with, name_less_than=name_less_than, has_query_limit=has_query_limit, group_by=group_by, report_columns=report_columns)

Gets reports based on library items

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.ReportsServiceApi()
report_view = 'report_view_example' # str | The report view. Values (ReportData, ReportActivities)
display_type = 'display_type_example' # str | The report display type. Values (None, Screen, Export, ScreenExport)
max_official_rating = 'max_official_rating_example' # str | Optional filter by maximum official rating (PG, PG-13, TV-MA, etc). (optional)
has_theme_song = true # bool | Optional filter by items with theme songs. (optional)
has_theme_video = true # bool | Optional filter by items with theme videos. (optional)
has_subtitles = true # bool | Optional filter by items with subtitles. (optional)
has_special_feature = true # bool | Optional filter by items with special features. (optional)
has_trailer = true # bool | Optional filter by items with trailers. (optional)
adjacent_to = 'adjacent_to_example' # str | Optional. Return items that are siblings of a supplied item. (optional)
min_index_number = 56 # int | Optional filter by minimum index number. (optional)
min_players = 56 # int | Optional filter by minimum number of game players. (optional)
max_players = 56 # int | Optional filter by maximum number of game players. (optional)
parent_index_number = 56 # int | Optional filter by parent index number. (optional)
has_parental_rating = true # bool | Optional filter by items that have or do not have a parental rating (optional)
is_hd = true # bool | Optional filter by items that are HD or not. (optional)
location_types = 'location_types_example' # str | Optional. If specified, results will be filtered based on LocationType. This allows multiple, comma delimeted. (optional)
exclude_location_types = 'exclude_location_types_example' # str | Optional. If specified, results will be filtered based on LocationType. This allows multiple, comma delimeted. (optional)
is_missing = true # bool | Optional filter by items that are missing episodes or not. (optional)
is_unaired = true # bool | Optional filter by items that are unaired episodes or not. (optional)
min_community_rating = 1.2 # float | Optional filter by minimum community rating. (optional)
min_critic_rating = 1.2 # float | Optional filter by minimum critic rating. (optional)
aired_during_season = 56 # int | Gets all episodes that aired during a season, including specials. (optional)
min_premiere_date = 'min_premiere_date_example' # str | Optional. The minimum premiere date. Format = ISO (optional)
min_date_last_saved = 'min_date_last_saved_example' # str | Optional. The minimum premiere date. Format = ISO (optional)
min_date_last_saved_for_user = 'min_date_last_saved_for_user_example' # str | Optional. The minimum premiere date. Format = ISO (optional)
max_premiere_date = 'max_premiere_date_example' # str | Optional. The maximum premiere date. Format = ISO (optional)
has_overview = true # bool | Optional filter by items that have an overview or not. (optional)
has_imdb_id = true # bool | Optional filter by items that have an imdb id or not. (optional)
has_tmdb_id = true # bool | Optional filter by items that have a tmdb id or not. (optional)
has_tvdb_id = true # bool | Optional filter by items that have a tvdb id or not. (optional)
exclude_item_ids = 'exclude_item_ids_example' # str | Optional. If specified, results will be filtered by exxcluding item ids. This allows multiple, comma delimeted. (optional)
start_index = 56 # int | Optional. The record index to start at. All items with a lower index will be dropped from the results. (optional)
limit = 56 # int | Optional. The maximum number of records to return (optional)
recursive = true # bool | When searching within folders, this determines whether or not the search will be recursive. true/false (optional)
sort_order = 'sort_order_example' # str | Sort Order - Ascending,Descending (optional)
parent_id = 'parent_id_example' # str | Specify this to localize the search to a specific item or folder. Omit to use the root (optional)
fields = 'fields_example' # str | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines (optional)
exclude_item_types = 'exclude_item_types_example' # str | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. (optional)
include_item_types = 'include_item_types_example' # str | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. (optional)
filters = 'filters_example' # str | Optional. Specify additional filters to apply. This allows multiple, comma delimeted. Options: IsFolder, IsNotFolder, IsUnplayed, IsPlayed, IsFavorite, IsResumable, Likes, Dislikes (optional)
is_favorite = true # bool | Optional filter by items that are marked as favorite, or not. (optional)
is_movie = true # bool | Optional filter for movies. (optional)
is_series = true # bool | Optional filter for movies. (optional)
is_news = true # bool | Optional filter for news. (optional)
is_kids = true # bool | Optional filter for kids. (optional)
is_sports = true # bool | Optional filter for sports. (optional)
media_types = 'media_types_example' # str | Optional filter by MediaType. Allows multiple, comma delimited. (optional)
image_types = 'image_types_example' # str | Optional. If specified, results will be filtered based on those containing image types. This allows multiple, comma delimited. (optional)
sort_by = 'sort_by_example' # str | Optional. Specify one or more sort orders, comma delimeted. Options: Album, AlbumArtist, Artist, Budget, CommunityRating, CriticRating, DateCreated, DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName, Random, Revenue, Runtime (optional)
is_played = true # bool | Optional filter by items that are played, or not. (optional)
genres = 'genres_example' # str | Optional. If specified, results will be filtered based on genre. This allows multiple, pipe delimeted. (optional)
official_ratings = 'official_ratings_example' # str | Optional. If specified, results will be filtered based on OfficialRating. This allows multiple, pipe delimeted. (optional)
tags = 'tags_example' # str | Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimeted. (optional)
years = 'years_example' # str | Optional. If specified, results will be filtered based on production year. This allows multiple, comma delimeted. (optional)
enable_images = true # bool | Optional, include image information in output (optional)
enable_user_data = true # bool | Optional, include user data (optional)
image_type_limit = 56 # int | Optional, the max number of images to return, per image type (optional)
enable_image_types = 'enable_image_types_example' # str | Optional. The image types to include in the output. (optional)
person = 'person_example' # str | Optional. If specified, results will be filtered to include only those containing the specified person. (optional)
person_ids = 'person_ids_example' # str | Optional. If specified, results will be filtered to include only those containing the specified person. (optional)
person_types = 'person_types_example' # str | Optional. If specified, along with Person, results will be filtered to include only those containing the specified person and PersonType. Allows multiple, comma-delimited (optional)
studios = 'studios_example' # str | Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimeted. (optional)
studio_ids = 'studio_ids_example' # str | Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimeted. (optional)
artists = 'artists_example' # str | Optional. If specified, results will be filtered based on artist. This allows multiple, pipe delimeted. (optional)
artist_ids = 'artist_ids_example' # str | Optional. If specified, results will be filtered based on artist. This allows multiple, pipe delimeted. (optional)
albums = 'albums_example' # str | Optional. If specified, results will be filtered based on album. This allows multiple, pipe delimeted. (optional)
ids = 'ids_example' # str | Optional. If specific items are needed, specify a list of item id's to retrieve. This allows multiple, comma delimited. (optional)
video_types = 'video_types_example' # str | Optional filter by VideoType (videofile, dvd, bluray, iso). Allows multiple, comma delimeted. (optional)
containers = 'containers_example' # str | Optional filter by Container. Allows multiple, comma delimeted. (optional)
user_id = 'user_id_example' # str | User Id (optional)
min_official_rating = 'min_official_rating_example' # str | Optional filter by minimum official rating (PG, PG-13, TV-MA, etc). (optional)
is_locked = true # bool | Optional filter by items that are locked. (optional)
is_place_holder = true # bool | Optional filter by items that are placeholders (optional)
has_official_rating = true # bool | Optional filter by items that have official ratings (optional)
collapse_box_set_items = true # bool | Whether or not to hide items behind their boxsets. (optional)
is3_d = true # bool | Optional filter by items that are 3D, or not. (optional)
series_status = 'series_status_example' # str | Optional filter by Series Status. Allows multiple, comma delimeted. (optional)
name_starts_with_or_greater = 'name_starts_with_or_greater_example' # str | Optional filter by items whose name is sorted equally or greater than a given input string. (optional)
name_starts_with = 'name_starts_with_example' # str | Optional filter by items whose name is sorted equally than a given input string. (optional)
name_less_than = 'name_less_than_example' # str | Optional filter by items whose name is equally or lesser than a given input string. (optional)
has_query_limit = true # bool | Optional. If specified, results will include all records. (optional)
group_by = 'group_by_example' # str | Optional. If specified, results will include grouped records. (optional)
report_columns = 'report_columns_example' # str | Optional. The columns to show. (optional)

try:
    # Gets reports based on library items
    api_response = api_instance.get_reports_items(report_view, display_type, max_official_rating=max_official_rating, has_theme_song=has_theme_song, has_theme_video=has_theme_video, has_subtitles=has_subtitles, has_special_feature=has_special_feature, has_trailer=has_trailer, adjacent_to=adjacent_to, min_index_number=min_index_number, min_players=min_players, max_players=max_players, parent_index_number=parent_index_number, has_parental_rating=has_parental_rating, is_hd=is_hd, location_types=location_types, exclude_location_types=exclude_location_types, is_missing=is_missing, is_unaired=is_unaired, min_community_rating=min_community_rating, min_critic_rating=min_critic_rating, aired_during_season=aired_during_season, min_premiere_date=min_premiere_date, min_date_last_saved=min_date_last_saved, min_date_last_saved_for_user=min_date_last_saved_for_user, max_premiere_date=max_premiere_date, has_overview=has_overview, has_imdb_id=has_imdb_id, has_tmdb_id=has_tmdb_id, has_tvdb_id=has_tvdb_id, exclude_item_ids=exclude_item_ids, start_index=start_index, limit=limit, recursive=recursive, sort_order=sort_order, parent_id=parent_id, fields=fields, exclude_item_types=exclude_item_types, include_item_types=include_item_types, filters=filters, is_favorite=is_favorite, is_movie=is_movie, is_series=is_series, is_news=is_news, is_kids=is_kids, is_sports=is_sports, media_types=media_types, image_types=image_types, sort_by=sort_by, is_played=is_played, genres=genres, official_ratings=official_ratings, tags=tags, years=years, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, person=person, person_ids=person_ids, person_types=person_types, studios=studios, studio_ids=studio_ids, artists=artists, artist_ids=artist_ids, albums=albums, ids=ids, video_types=video_types, containers=containers, user_id=user_id, min_official_rating=min_official_rating, is_locked=is_locked, is_place_holder=is_place_holder, has_official_rating=has_official_rating, collapse_box_set_items=collapse_box_set_items, is3_d=is3_d, series_status=series_status, name_starts_with_or_greater=name_starts_with_or_greater, name_starts_with=name_starts_with, name_less_than=name_less_than, has_query_limit=has_query_limit, group_by=group_by, report_columns=report_columns)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsServiceApi->get_reports_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_view** | **str**| The report view. Values (ReportData, ReportActivities) | 
 **display_type** | **str**| The report display type. Values (None, Screen, Export, ScreenExport) | 
 **max_official_rating** | **str**| Optional filter by maximum official rating (PG, PG-13, TV-MA, etc). | [optional] 
 **has_theme_song** | **bool**| Optional filter by items with theme songs. | [optional] 
 **has_theme_video** | **bool**| Optional filter by items with theme videos. | [optional] 
 **has_subtitles** | **bool**| Optional filter by items with subtitles. | [optional] 
 **has_special_feature** | **bool**| Optional filter by items with special features. | [optional] 
 **has_trailer** | **bool**| Optional filter by items with trailers. | [optional] 
 **adjacent_to** | **str**| Optional. Return items that are siblings of a supplied item. | [optional] 
 **min_index_number** | **int**| Optional filter by minimum index number. | [optional] 
 **min_players** | **int**| Optional filter by minimum number of game players. | [optional] 
 **max_players** | **int**| Optional filter by maximum number of game players. | [optional] 
 **parent_index_number** | **int**| Optional filter by parent index number. | [optional] 
 **has_parental_rating** | **bool**| Optional filter by items that have or do not have a parental rating | [optional] 
 **is_hd** | **bool**| Optional filter by items that are HD or not. | [optional] 
 **location_types** | **str**| Optional. If specified, results will be filtered based on LocationType. This allows multiple, comma delimeted. | [optional] 
 **exclude_location_types** | **str**| Optional. If specified, results will be filtered based on LocationType. This allows multiple, comma delimeted. | [optional] 
 **is_missing** | **bool**| Optional filter by items that are missing episodes or not. | [optional] 
 **is_unaired** | **bool**| Optional filter by items that are unaired episodes or not. | [optional] 
 **min_community_rating** | **float**| Optional filter by minimum community rating. | [optional] 
 **min_critic_rating** | **float**| Optional filter by minimum critic rating. | [optional] 
 **aired_during_season** | **int**| Gets all episodes that aired during a season, including specials. | [optional] 
 **min_premiere_date** | **str**| Optional. The minimum premiere date. Format &#x3D; ISO | [optional] 
 **min_date_last_saved** | **str**| Optional. The minimum premiere date. Format &#x3D; ISO | [optional] 
 **min_date_last_saved_for_user** | **str**| Optional. The minimum premiere date. Format &#x3D; ISO | [optional] 
 **max_premiere_date** | **str**| Optional. The maximum premiere date. Format &#x3D; ISO | [optional] 
 **has_overview** | **bool**| Optional filter by items that have an overview or not. | [optional] 
 **has_imdb_id** | **bool**| Optional filter by items that have an imdb id or not. | [optional] 
 **has_tmdb_id** | **bool**| Optional filter by items that have a tmdb id or not. | [optional] 
 **has_tvdb_id** | **bool**| Optional filter by items that have a tvdb id or not. | [optional] 
 **exclude_item_ids** | **str**| Optional. If specified, results will be filtered by exxcluding item ids. This allows multiple, comma delimeted. | [optional] 
 **start_index** | **int**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return | [optional] 
 **recursive** | **bool**| When searching within folders, this determines whether or not the search will be recursive. true/false | [optional] 
 **sort_order** | **str**| Sort Order - Ascending,Descending | [optional] 
 **parent_id** | **str**| Specify this to localize the search to a specific item or folder. Omit to use the root | [optional] 
 **fields** | **str**| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines | [optional] 
 **exclude_item_types** | **str**| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. | [optional] 
 **include_item_types** | **str**| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. | [optional] 
 **filters** | **str**| Optional. Specify additional filters to apply. This allows multiple, comma delimeted. Options: IsFolder, IsNotFolder, IsUnplayed, IsPlayed, IsFavorite, IsResumable, Likes, Dislikes | [optional] 
 **is_favorite** | **bool**| Optional filter by items that are marked as favorite, or not. | [optional] 
 **is_movie** | **bool**| Optional filter for movies. | [optional] 
 **is_series** | **bool**| Optional filter for movies. | [optional] 
 **is_news** | **bool**| Optional filter for news. | [optional] 
 **is_kids** | **bool**| Optional filter for kids. | [optional] 
 **is_sports** | **bool**| Optional filter for sports. | [optional] 
 **media_types** | **str**| Optional filter by MediaType. Allows multiple, comma delimited. | [optional] 
 **image_types** | **str**| Optional. If specified, results will be filtered based on those containing image types. This allows multiple, comma delimited. | [optional] 
 **sort_by** | **str**| Optional. Specify one or more sort orders, comma delimeted. Options: Album, AlbumArtist, Artist, Budget, CommunityRating, CriticRating, DateCreated, DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName, Random, Revenue, Runtime | [optional] 
 **is_played** | **bool**| Optional filter by items that are played, or not. | [optional] 
 **genres** | **str**| Optional. If specified, results will be filtered based on genre. This allows multiple, pipe delimeted. | [optional] 
 **official_ratings** | **str**| Optional. If specified, results will be filtered based on OfficialRating. This allows multiple, pipe delimeted. | [optional] 
 **tags** | **str**| Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimeted. | [optional] 
 **years** | **str**| Optional. If specified, results will be filtered based on production year. This allows multiple, comma delimeted. | [optional] 
 **enable_images** | **bool**| Optional, include image information in output | [optional] 
 **enable_user_data** | **bool**| Optional, include user data | [optional] 
 **image_type_limit** | **int**| Optional, the max number of images to return, per image type | [optional] 
 **enable_image_types** | **str**| Optional. The image types to include in the output. | [optional] 
 **person** | **str**| Optional. If specified, results will be filtered to include only those containing the specified person. | [optional] 
 **person_ids** | **str**| Optional. If specified, results will be filtered to include only those containing the specified person. | [optional] 
 **person_types** | **str**| Optional. If specified, along with Person, results will be filtered to include only those containing the specified person and PersonType. Allows multiple, comma-delimited | [optional] 
 **studios** | **str**| Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimeted. | [optional] 
 **studio_ids** | **str**| Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimeted. | [optional] 
 **artists** | **str**| Optional. If specified, results will be filtered based on artist. This allows multiple, pipe delimeted. | [optional] 
 **artist_ids** | **str**| Optional. If specified, results will be filtered based on artist. This allows multiple, pipe delimeted. | [optional] 
 **albums** | **str**| Optional. If specified, results will be filtered based on album. This allows multiple, pipe delimeted. | [optional] 
 **ids** | **str**| Optional. If specific items are needed, specify a list of item id&#x27;s to retrieve. This allows multiple, comma delimited. | [optional] 
 **video_types** | **str**| Optional filter by VideoType (videofile, dvd, bluray, iso). Allows multiple, comma delimeted. | [optional] 
 **containers** | **str**| Optional filter by Container. Allows multiple, comma delimeted. | [optional] 
 **user_id** | **str**| User Id | [optional] 
 **min_official_rating** | **str**| Optional filter by minimum official rating (PG, PG-13, TV-MA, etc). | [optional] 
 **is_locked** | **bool**| Optional filter by items that are locked. | [optional] 
 **is_place_holder** | **bool**| Optional filter by items that are placeholders | [optional] 
 **has_official_rating** | **bool**| Optional filter by items that have official ratings | [optional] 
 **collapse_box_set_items** | **bool**| Whether or not to hide items behind their boxsets. | [optional] 
 **is3_d** | **bool**| Optional filter by items that are 3D, or not. | [optional] 
 **series_status** | **str**| Optional filter by Series Status. Allows multiple, comma delimeted. | [optional] 
 **name_starts_with_or_greater** | **str**| Optional filter by items whose name is sorted equally or greater than a given input string. | [optional] 
 **name_starts_with** | **str**| Optional filter by items whose name is sorted equally than a given input string. | [optional] 
 **name_less_than** | **str**| Optional filter by items whose name is equally or lesser than a given input string. | [optional] 
 **has_query_limit** | **bool**| Optional. If specified, results will include all records. | [optional] 
 **group_by** | **str**| Optional. If specified, results will include grouped records. | [optional] 
 **report_columns** | **str**| Optional. The columns to show. | [optional] 

### Return type

[**EmbyReportsApiModelReportResult**](EmbyReportsApiModelReportResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reports_items_download**
> get_reports_items_download(report_view, display_type, max_official_rating=max_official_rating, has_theme_song=has_theme_song, has_theme_video=has_theme_video, has_subtitles=has_subtitles, has_special_feature=has_special_feature, has_trailer=has_trailer, adjacent_to=adjacent_to, min_index_number=min_index_number, min_players=min_players, max_players=max_players, parent_index_number=parent_index_number, has_parental_rating=has_parental_rating, is_hd=is_hd, location_types=location_types, exclude_location_types=exclude_location_types, is_missing=is_missing, is_unaired=is_unaired, min_community_rating=min_community_rating, min_critic_rating=min_critic_rating, aired_during_season=aired_during_season, min_premiere_date=min_premiere_date, min_date_last_saved=min_date_last_saved, min_date_last_saved_for_user=min_date_last_saved_for_user, max_premiere_date=max_premiere_date, has_overview=has_overview, has_imdb_id=has_imdb_id, has_tmdb_id=has_tmdb_id, has_tvdb_id=has_tvdb_id, exclude_item_ids=exclude_item_ids, start_index=start_index, limit=limit, recursive=recursive, sort_order=sort_order, parent_id=parent_id, fields=fields, exclude_item_types=exclude_item_types, include_item_types=include_item_types, filters=filters, is_favorite=is_favorite, is_movie=is_movie, is_series=is_series, is_news=is_news, is_kids=is_kids, is_sports=is_sports, media_types=media_types, image_types=image_types, sort_by=sort_by, is_played=is_played, genres=genres, official_ratings=official_ratings, tags=tags, years=years, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, person=person, person_ids=person_ids, person_types=person_types, studios=studios, studio_ids=studio_ids, artists=artists, artist_ids=artist_ids, albums=albums, ids=ids, video_types=video_types, containers=containers, user_id=user_id, min_official_rating=min_official_rating, is_locked=is_locked, is_place_holder=is_place_holder, has_official_rating=has_official_rating, collapse_box_set_items=collapse_box_set_items, is3_d=is3_d, series_status=series_status, name_starts_with_or_greater=name_starts_with_or_greater, name_starts_with=name_starts_with, name_less_than=name_less_than, has_query_limit=has_query_limit, group_by=group_by, report_columns=report_columns)

Downloads report

No authentication required

### Example
```python
from __future__ import print_function
import time
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = embyapi.ReportsServiceApi()
report_view = 'report_view_example' # str | The report view. Values (ReportData, ReportActivities)
display_type = 'display_type_example' # str | The report display type. Values (None, Screen, Export, ScreenExport)
max_official_rating = 'max_official_rating_example' # str | Optional filter by maximum official rating (PG, PG-13, TV-MA, etc). (optional)
has_theme_song = true # bool | Optional filter by items with theme songs. (optional)
has_theme_video = true # bool | Optional filter by items with theme videos. (optional)
has_subtitles = true # bool | Optional filter by items with subtitles. (optional)
has_special_feature = true # bool | Optional filter by items with special features. (optional)
has_trailer = true # bool | Optional filter by items with trailers. (optional)
adjacent_to = 'adjacent_to_example' # str | Optional. Return items that are siblings of a supplied item. (optional)
min_index_number = 56 # int | Optional filter by minimum index number. (optional)
min_players = 56 # int | Optional filter by minimum number of game players. (optional)
max_players = 56 # int | Optional filter by maximum number of game players. (optional)
parent_index_number = 56 # int | Optional filter by parent index number. (optional)
has_parental_rating = true # bool | Optional filter by items that have or do not have a parental rating (optional)
is_hd = true # bool | Optional filter by items that are HD or not. (optional)
location_types = 'location_types_example' # str | Optional. If specified, results will be filtered based on LocationType. This allows multiple, comma delimeted. (optional)
exclude_location_types = 'exclude_location_types_example' # str | Optional. If specified, results will be filtered based on LocationType. This allows multiple, comma delimeted. (optional)
is_missing = true # bool | Optional filter by items that are missing episodes or not. (optional)
is_unaired = true # bool | Optional filter by items that are unaired episodes or not. (optional)
min_community_rating = 1.2 # float | Optional filter by minimum community rating. (optional)
min_critic_rating = 1.2 # float | Optional filter by minimum critic rating. (optional)
aired_during_season = 56 # int | Gets all episodes that aired during a season, including specials. (optional)
min_premiere_date = 'min_premiere_date_example' # str | Optional. The minimum premiere date. Format = ISO (optional)
min_date_last_saved = 'min_date_last_saved_example' # str | Optional. The minimum premiere date. Format = ISO (optional)
min_date_last_saved_for_user = 'min_date_last_saved_for_user_example' # str | Optional. The minimum premiere date. Format = ISO (optional)
max_premiere_date = 'max_premiere_date_example' # str | Optional. The maximum premiere date. Format = ISO (optional)
has_overview = true # bool | Optional filter by items that have an overview or not. (optional)
has_imdb_id = true # bool | Optional filter by items that have an imdb id or not. (optional)
has_tmdb_id = true # bool | Optional filter by items that have a tmdb id or not. (optional)
has_tvdb_id = true # bool | Optional filter by items that have a tvdb id or not. (optional)
exclude_item_ids = 'exclude_item_ids_example' # str | Optional. If specified, results will be filtered by exxcluding item ids. This allows multiple, comma delimeted. (optional)
start_index = 56 # int | Optional. The record index to start at. All items with a lower index will be dropped from the results. (optional)
limit = 56 # int | Optional. The maximum number of records to return (optional)
recursive = true # bool | When searching within folders, this determines whether or not the search will be recursive. true/false (optional)
sort_order = 'sort_order_example' # str | Sort Order - Ascending,Descending (optional)
parent_id = 'parent_id_example' # str | Specify this to localize the search to a specific item or folder. Omit to use the root (optional)
fields = 'fields_example' # str | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines (optional)
exclude_item_types = 'exclude_item_types_example' # str | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. (optional)
include_item_types = 'include_item_types_example' # str | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. (optional)
filters = 'filters_example' # str | Optional. Specify additional filters to apply. This allows multiple, comma delimeted. Options: IsFolder, IsNotFolder, IsUnplayed, IsPlayed, IsFavorite, IsResumable, Likes, Dislikes (optional)
is_favorite = true # bool | Optional filter by items that are marked as favorite, or not. (optional)
is_movie = true # bool | Optional filter for movies. (optional)
is_series = true # bool | Optional filter for movies. (optional)
is_news = true # bool | Optional filter for news. (optional)
is_kids = true # bool | Optional filter for kids. (optional)
is_sports = true # bool | Optional filter for sports. (optional)
media_types = 'media_types_example' # str | Optional filter by MediaType. Allows multiple, comma delimited. (optional)
image_types = 'image_types_example' # str | Optional. If specified, results will be filtered based on those containing image types. This allows multiple, comma delimited. (optional)
sort_by = 'sort_by_example' # str | Optional. Specify one or more sort orders, comma delimeted. Options: Album, AlbumArtist, Artist, Budget, CommunityRating, CriticRating, DateCreated, DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName, Random, Revenue, Runtime (optional)
is_played = true # bool | Optional filter by items that are played, or not. (optional)
genres = 'genres_example' # str | Optional. If specified, results will be filtered based on genre. This allows multiple, pipe delimeted. (optional)
official_ratings = 'official_ratings_example' # str | Optional. If specified, results will be filtered based on OfficialRating. This allows multiple, pipe delimeted. (optional)
tags = 'tags_example' # str | Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimeted. (optional)
years = 'years_example' # str | Optional. If specified, results will be filtered based on production year. This allows multiple, comma delimeted. (optional)
enable_images = true # bool | Optional, include image information in output (optional)
enable_user_data = true # bool | Optional, include user data (optional)
image_type_limit = 56 # int | Optional, the max number of images to return, per image type (optional)
enable_image_types = 'enable_image_types_example' # str | Optional. The image types to include in the output. (optional)
person = 'person_example' # str | Optional. If specified, results will be filtered to include only those containing the specified person. (optional)
person_ids = 'person_ids_example' # str | Optional. If specified, results will be filtered to include only those containing the specified person. (optional)
person_types = 'person_types_example' # str | Optional. If specified, along with Person, results will be filtered to include only those containing the specified person and PersonType. Allows multiple, comma-delimited (optional)
studios = 'studios_example' # str | Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimeted. (optional)
studio_ids = 'studio_ids_example' # str | Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimeted. (optional)
artists = 'artists_example' # str | Optional. If specified, results will be filtered based on artist. This allows multiple, pipe delimeted. (optional)
artist_ids = 'artist_ids_example' # str | Optional. If specified, results will be filtered based on artist. This allows multiple, pipe delimeted. (optional)
albums = 'albums_example' # str | Optional. If specified, results will be filtered based on album. This allows multiple, pipe delimeted. (optional)
ids = 'ids_example' # str | Optional. If specific items are needed, specify a list of item id's to retrieve. This allows multiple, comma delimited. (optional)
video_types = 'video_types_example' # str | Optional filter by VideoType (videofile, dvd, bluray, iso). Allows multiple, comma delimeted. (optional)
containers = 'containers_example' # str | Optional filter by Container. Allows multiple, comma delimeted. (optional)
user_id = 'user_id_example' # str | User Id (optional)
min_official_rating = 'min_official_rating_example' # str | Optional filter by minimum official rating (PG, PG-13, TV-MA, etc). (optional)
is_locked = true # bool | Optional filter by items that are locked. (optional)
is_place_holder = true # bool | Optional filter by items that are placeholders (optional)
has_official_rating = true # bool | Optional filter by items that have official ratings (optional)
collapse_box_set_items = true # bool | Whether or not to hide items behind their boxsets. (optional)
is3_d = true # bool | Optional filter by items that are 3D, or not. (optional)
series_status = 'series_status_example' # str | Optional filter by Series Status. Allows multiple, comma delimeted. (optional)
name_starts_with_or_greater = 'name_starts_with_or_greater_example' # str | Optional filter by items whose name is sorted equally or greater than a given input string. (optional)
name_starts_with = 'name_starts_with_example' # str | Optional filter by items whose name is sorted equally than a given input string. (optional)
name_less_than = 'name_less_than_example' # str | Optional filter by items whose name is equally or lesser than a given input string. (optional)
has_query_limit = true # bool | Optional. If specified, results will include all records. (optional)
group_by = 'group_by_example' # str | Optional. If specified, results will include grouped records. (optional)
report_columns = 'report_columns_example' # str | Optional. The columns to show. (optional)

try:
    # Downloads report
    api_instance.get_reports_items_download(report_view, display_type, max_official_rating=max_official_rating, has_theme_song=has_theme_song, has_theme_video=has_theme_video, has_subtitles=has_subtitles, has_special_feature=has_special_feature, has_trailer=has_trailer, adjacent_to=adjacent_to, min_index_number=min_index_number, min_players=min_players, max_players=max_players, parent_index_number=parent_index_number, has_parental_rating=has_parental_rating, is_hd=is_hd, location_types=location_types, exclude_location_types=exclude_location_types, is_missing=is_missing, is_unaired=is_unaired, min_community_rating=min_community_rating, min_critic_rating=min_critic_rating, aired_during_season=aired_during_season, min_premiere_date=min_premiere_date, min_date_last_saved=min_date_last_saved, min_date_last_saved_for_user=min_date_last_saved_for_user, max_premiere_date=max_premiere_date, has_overview=has_overview, has_imdb_id=has_imdb_id, has_tmdb_id=has_tmdb_id, has_tvdb_id=has_tvdb_id, exclude_item_ids=exclude_item_ids, start_index=start_index, limit=limit, recursive=recursive, sort_order=sort_order, parent_id=parent_id, fields=fields, exclude_item_types=exclude_item_types, include_item_types=include_item_types, filters=filters, is_favorite=is_favorite, is_movie=is_movie, is_series=is_series, is_news=is_news, is_kids=is_kids, is_sports=is_sports, media_types=media_types, image_types=image_types, sort_by=sort_by, is_played=is_played, genres=genres, official_ratings=official_ratings, tags=tags, years=years, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, person=person, person_ids=person_ids, person_types=person_types, studios=studios, studio_ids=studio_ids, artists=artists, artist_ids=artist_ids, albums=albums, ids=ids, video_types=video_types, containers=containers, user_id=user_id, min_official_rating=min_official_rating, is_locked=is_locked, is_place_holder=is_place_holder, has_official_rating=has_official_rating, collapse_box_set_items=collapse_box_set_items, is3_d=is3_d, series_status=series_status, name_starts_with_or_greater=name_starts_with_or_greater, name_starts_with=name_starts_with, name_less_than=name_less_than, has_query_limit=has_query_limit, group_by=group_by, report_columns=report_columns)
except ApiException as e:
    print("Exception when calling ReportsServiceApi->get_reports_items_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_view** | **str**| The report view. Values (ReportData, ReportActivities) | 
 **display_type** | **str**| The report display type. Values (None, Screen, Export, ScreenExport) | 
 **max_official_rating** | **str**| Optional filter by maximum official rating (PG, PG-13, TV-MA, etc). | [optional] 
 **has_theme_song** | **bool**| Optional filter by items with theme songs. | [optional] 
 **has_theme_video** | **bool**| Optional filter by items with theme videos. | [optional] 
 **has_subtitles** | **bool**| Optional filter by items with subtitles. | [optional] 
 **has_special_feature** | **bool**| Optional filter by items with special features. | [optional] 
 **has_trailer** | **bool**| Optional filter by items with trailers. | [optional] 
 **adjacent_to** | **str**| Optional. Return items that are siblings of a supplied item. | [optional] 
 **min_index_number** | **int**| Optional filter by minimum index number. | [optional] 
 **min_players** | **int**| Optional filter by minimum number of game players. | [optional] 
 **max_players** | **int**| Optional filter by maximum number of game players. | [optional] 
 **parent_index_number** | **int**| Optional filter by parent index number. | [optional] 
 **has_parental_rating** | **bool**| Optional filter by items that have or do not have a parental rating | [optional] 
 **is_hd** | **bool**| Optional filter by items that are HD or not. | [optional] 
 **location_types** | **str**| Optional. If specified, results will be filtered based on LocationType. This allows multiple, comma delimeted. | [optional] 
 **exclude_location_types** | **str**| Optional. If specified, results will be filtered based on LocationType. This allows multiple, comma delimeted. | [optional] 
 **is_missing** | **bool**| Optional filter by items that are missing episodes or not. | [optional] 
 **is_unaired** | **bool**| Optional filter by items that are unaired episodes or not. | [optional] 
 **min_community_rating** | **float**| Optional filter by minimum community rating. | [optional] 
 **min_critic_rating** | **float**| Optional filter by minimum critic rating. | [optional] 
 **aired_during_season** | **int**| Gets all episodes that aired during a season, including specials. | [optional] 
 **min_premiere_date** | **str**| Optional. The minimum premiere date. Format &#x3D; ISO | [optional] 
 **min_date_last_saved** | **str**| Optional. The minimum premiere date. Format &#x3D; ISO | [optional] 
 **min_date_last_saved_for_user** | **str**| Optional. The minimum premiere date. Format &#x3D; ISO | [optional] 
 **max_premiere_date** | **str**| Optional. The maximum premiere date. Format &#x3D; ISO | [optional] 
 **has_overview** | **bool**| Optional filter by items that have an overview or not. | [optional] 
 **has_imdb_id** | **bool**| Optional filter by items that have an imdb id or not. | [optional] 
 **has_tmdb_id** | **bool**| Optional filter by items that have a tmdb id or not. | [optional] 
 **has_tvdb_id** | **bool**| Optional filter by items that have a tvdb id or not. | [optional] 
 **exclude_item_ids** | **str**| Optional. If specified, results will be filtered by exxcluding item ids. This allows multiple, comma delimeted. | [optional] 
 **start_index** | **int**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return | [optional] 
 **recursive** | **bool**| When searching within folders, this determines whether or not the search will be recursive. true/false | [optional] 
 **sort_order** | **str**| Sort Order - Ascending,Descending | [optional] 
 **parent_id** | **str**| Specify this to localize the search to a specific item or folder. Omit to use the root | [optional] 
 **fields** | **str**| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines | [optional] 
 **exclude_item_types** | **str**| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. | [optional] 
 **include_item_types** | **str**| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. | [optional] 
 **filters** | **str**| Optional. Specify additional filters to apply. This allows multiple, comma delimeted. Options: IsFolder, IsNotFolder, IsUnplayed, IsPlayed, IsFavorite, IsResumable, Likes, Dislikes | [optional] 
 **is_favorite** | **bool**| Optional filter by items that are marked as favorite, or not. | [optional] 
 **is_movie** | **bool**| Optional filter for movies. | [optional] 
 **is_series** | **bool**| Optional filter for movies. | [optional] 
 **is_news** | **bool**| Optional filter for news. | [optional] 
 **is_kids** | **bool**| Optional filter for kids. | [optional] 
 **is_sports** | **bool**| Optional filter for sports. | [optional] 
 **media_types** | **str**| Optional filter by MediaType. Allows multiple, comma delimited. | [optional] 
 **image_types** | **str**| Optional. If specified, results will be filtered based on those containing image types. This allows multiple, comma delimited. | [optional] 
 **sort_by** | **str**| Optional. Specify one or more sort orders, comma delimeted. Options: Album, AlbumArtist, Artist, Budget, CommunityRating, CriticRating, DateCreated, DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName, Random, Revenue, Runtime | [optional] 
 **is_played** | **bool**| Optional filter by items that are played, or not. | [optional] 
 **genres** | **str**| Optional. If specified, results will be filtered based on genre. This allows multiple, pipe delimeted. | [optional] 
 **official_ratings** | **str**| Optional. If specified, results will be filtered based on OfficialRating. This allows multiple, pipe delimeted. | [optional] 
 **tags** | **str**| Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimeted. | [optional] 
 **years** | **str**| Optional. If specified, results will be filtered based on production year. This allows multiple, comma delimeted. | [optional] 
 **enable_images** | **bool**| Optional, include image information in output | [optional] 
 **enable_user_data** | **bool**| Optional, include user data | [optional] 
 **image_type_limit** | **int**| Optional, the max number of images to return, per image type | [optional] 
 **enable_image_types** | **str**| Optional. The image types to include in the output. | [optional] 
 **person** | **str**| Optional. If specified, results will be filtered to include only those containing the specified person. | [optional] 
 **person_ids** | **str**| Optional. If specified, results will be filtered to include only those containing the specified person. | [optional] 
 **person_types** | **str**| Optional. If specified, along with Person, results will be filtered to include only those containing the specified person and PersonType. Allows multiple, comma-delimited | [optional] 
 **studios** | **str**| Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimeted. | [optional] 
 **studio_ids** | **str**| Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimeted. | [optional] 
 **artists** | **str**| Optional. If specified, results will be filtered based on artist. This allows multiple, pipe delimeted. | [optional] 
 **artist_ids** | **str**| Optional. If specified, results will be filtered based on artist. This allows multiple, pipe delimeted. | [optional] 
 **albums** | **str**| Optional. If specified, results will be filtered based on album. This allows multiple, pipe delimeted. | [optional] 
 **ids** | **str**| Optional. If specific items are needed, specify a list of item id&#x27;s to retrieve. This allows multiple, comma delimited. | [optional] 
 **video_types** | **str**| Optional filter by VideoType (videofile, dvd, bluray, iso). Allows multiple, comma delimeted. | [optional] 
 **containers** | **str**| Optional filter by Container. Allows multiple, comma delimeted. | [optional] 
 **user_id** | **str**| User Id | [optional] 
 **min_official_rating** | **str**| Optional filter by minimum official rating (PG, PG-13, TV-MA, etc). | [optional] 
 **is_locked** | **bool**| Optional filter by items that are locked. | [optional] 
 **is_place_holder** | **bool**| Optional filter by items that are placeholders | [optional] 
 **has_official_rating** | **bool**| Optional filter by items that have official ratings | [optional] 
 **collapse_box_set_items** | **bool**| Whether or not to hide items behind their boxsets. | [optional] 
 **is3_d** | **bool**| Optional filter by items that are 3D, or not. | [optional] 
 **series_status** | **str**| Optional filter by Series Status. Allows multiple, comma delimeted. | [optional] 
 **name_starts_with_or_greater** | **str**| Optional filter by items whose name is sorted equally or greater than a given input string. | [optional] 
 **name_starts_with** | **str**| Optional filter by items whose name is sorted equally than a given input string. | [optional] 
 **name_less_than** | **str**| Optional filter by items whose name is equally or lesser than a given input string. | [optional] 
 **has_query_limit** | **bool**| Optional. If specified, results will include all records. | [optional] 
 **group_by** | **str**| Optional. If specified, results will include grouped records. | [optional] 
 **report_columns** | **str**| Optional. The columns to show. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

