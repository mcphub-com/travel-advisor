import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/apidojo/api/travel-advisor'

mcp = FastMCP('travel-advisor')

@mcp.tool()
def v2_auto_complete(query: Annotated[str, Field(description='Name of cities, districts, places, etc...')],
                     lang: Annotated[Union[str, None], Field(description='The language code')] = None,
                     units: Annotated[Union[str, None], Field(description='One of the followings : km|mi')] = None) -> dict: 
    '''List suggested locations by term or phrase'''
    url = 'https://travel-advisor.p.rapidapi.com/locations/v2/auto-complete'
    headers = {'x-rapidapi-host': 'travel-advisor.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
        'lang': lang,
        'units': units,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_search(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Search for related cities, countries, and suggestions by term or phrase'''
    url = 'https://travel-advisor.p.rapidapi.com/locations/v2/search'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'travel-advisor.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def v2_list_nearby(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''List nearby to a location'''
    url = 'https://travel-advisor.p.rapidapi.com/locations/v2/list-nearby'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'travel-advisor.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def locations_auto_complete(query: Annotated[str, Field(description='Name of cities, districts, places, etc...')],
                            lang: Annotated[Union[str, None], Field(description='The language code')] = None,
                            units: Annotated[Union[str, None], Field(description='One of the followings : km|mi')] = None) -> dict: 
    '''List suggested locations by term or phrase'''
    url = 'https://travel-advisor.p.rapidapi.com/locations/auto-complete'
    headers = {'x-rapidapi-host': 'travel-advisor.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
        'lang': lang,
        'units': units,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def locations_search(query: Annotated[str, Field(description='Name of cities, districts, places, etc...')],
                     limit: Annotated[Union[int, float, None], Field(description='The number of items per response (max 30) Default: 30')] = None,
                     offset: Annotated[Union[int, float, None], Field(description='The number of items to ignore for paging purpose Default: 0')] = None,
                     units: Annotated[Union[str, None], Field(description='One of the followings : km|mi')] = None,
                     location_id: Annotated[Union[int, float, None], Field(description='The value of location_id field returned right in this endpoint or .../locations/auto-complete endpoint Default: 1')] = None,
                     currency: Annotated[Union[str, None], Field(description='The currency code')] = None,
                     sort: Annotated[Union[str, None], Field(description='One of the followings : relevance|distance')] = None,
                     lang: Annotated[Union[str, None], Field(description='The language code')] = None) -> dict: 
    '''Search for related cities, countries, and suggestions'''
    url = 'https://travel-advisor.p.rapidapi.com/locations/search'
    headers = {'x-rapidapi-host': 'travel-advisor.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
        'limit': limit,
        'offset': offset,
        'units': units,
        'location_id': location_id,
        'currency': currency,
        'sort': sort,
        'lang': lang,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_list(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Get available filters for listing restaurants'''
    url = 'https://travel-advisor.p.rapidapi.com/restaurant-filters/v2/list'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'travel-advisor.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def v2_get_details(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Get detail information of specific restaurant'''
    url = 'https://travel-advisor.p.rapidapi.com/restaurants/v2/get-details'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'travel-advisor.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def restaurants_list_by_latlng(latitude: Annotated[Union[int, float], Field(description='Latitude of coordinate Default: 12.91285')],
                               longitude: Annotated[Union[int, float], Field(description='Longitude of coordinate Default: 100.87808')],
                               limit: Annotated[Union[int, float, None], Field(description='The number of items per response (max 30) Default: 30')] = None,
                               currency: Annotated[Union[str, None], Field(description='The currency code')] = None,
                               restaurant_dining_options: Annotated[Union[str, None], Field(description='Restaurant Features - Check for suitable values of filters_v2/filter_sections/filter_groups/options/value field (separated by comma to specify multiple values) returned right in this endpoint')] = None,
                               prices_restaurants: Annotated[Union[str, None], Field(description='Prices - Check for suitable values of filters_v2/filter_sections/filter_groups/options/value field (separated by comma to specify multiple values) returned right in this endpoint')] = None,
                               restaurant_styles: Annotated[Union[str, None], Field(description='Restaurant Features - Check for suitable values of filters_v2/filter_sections/filter_groups/options/value field (separated by comma to specify multiple values) returned right in this endpoint')] = None,
                               combined_food: Annotated[Union[str, None], Field(description='Cuisine Type - Check for suitable values of filters_v2/filter_sections/filter_groups/options/value field (separated by comma to specify multiple values) returned right in this endpoint')] = None,
                               distance: Annotated[Union[int, float, None], Field(description='The radius around specified coordinate (max 10) Default: 2')] = None,
                               restaurant_tagcategory: Annotated[Union[str, None], Field(description='Establishment Type - Check for suitable values of filters_v2/filter_sections/filter_groups/options/value field (separated by comma to specify multiple values) returned right in this endpoint')] = None,
                               restaurant_mealtype: Annotated[Union[str, None], Field(description='Meals - Check for suitable values of filters_v2/filter_sections/filter_groups/options/value field (separated by comma to specify multiple values) returned right in this endpoint')] = None,
                               open_now: Annotated[Union[bool, None], Field(description='Only returns restaurants which are opening now Example: false')] = None,
                               offset: Annotated[Union[int, float, None], Field(description='The number of items to ignore for paging purpose Default: 0')] = None,
                               dietary_restrictions: Annotated[Union[str, None], Field(description='Dietary Restrictions - Check for suitable values of filters_v2/filter_sections/filter_groups/options/value field (separated by comma to specify multiple values) returned right in this endpoint')] = None,
                               lunit: Annotated[Union[str, None], Field(description='One of the followings km|mi')] = None,
                               lang: Annotated[Union[str, None], Field(description='The language code')] = None,
                               restaurant_tagcategory_standalone: Annotated[Union[str, None], Field(description='Establishment Type - Check for suitable values of filters_v2/filter_sections/filter_groups/options/value field (separated by comma to specify multiple values) returned right in this endpoint')] = None,
                               min_rating: Annotated[Union[str, None], Field(description='Min 3 - Max 5')] = None) -> dict:
    '''List restaurants by specifying an coordinate and radius'''
    url = 'https://travel-advisor.p.rapidapi.com/restaurants/list-by-latlng'
    headers = {'x-rapidapi-host': 'travel-advisor.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'latitude': latitude,
        'longitude': longitude,
        'limit': limit,
        'currency': currency,
        'restaurant_dining_options': restaurant_dining_options,
        'prices_restaurants': prices_restaurants,
        'restaurant_styles': restaurant_styles,
        'combined_food': combined_food,
        'distance': distance,
        'restaurant_tagcategory': restaurant_tagcategory,
        'restaurant_mealtype': restaurant_mealtype,
        'open_now': open_now,
        'offset': offset,
        'dietary_restrictions': dietary_restrictions,
        'lunit': lunit,
        'lang': lang,
        'restaurant_tagcategory_standalone': restaurant_tagcategory_standalone,
        'min_rating': min_rating,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def restaurants_list_in_boundary(bl_latitude: Annotated[Union[int, float], Field(description='Latitude of bottom left coordinate Default: 11.847676')],
                                 tr_latitude: Annotated[Union[int, float], Field(description='Latitude of top right coordinate Default: 12.838442')],
                                 bl_longitude: Annotated[Union[int, float], Field(description='Longitude of bottom left coordinate Default: 109.095887')],
                                 tr_longitude: Annotated[Union[int, float], Field(description='Longitude of top right coordinate Default: 109.149359')],
                                 dietary_restrictions: Annotated[Union[str, None], Field(description='Dietary Restrictions - Check for suitable values of filters_v2/filter_sections/filter_groups/options/value field (separated by comma to specify multiple values) returned right in this endpoint')] = None,
                                 min_rating: Annotated[Union[int, float, None], Field(description='Min 3 - Max 5 Default: 0')] = None,
                                 restaurant_tagcategory_standalone: Annotated[Union[str, None], Field(description='Establishment Type - Check for suitable values of filters_v2/filter_sections/filter_groups/options/value field (separated by comma to specify multiple values) returned right in this endpoint')] = None,
                                 restaurant_tagcategory: Annotated[Union[str, None], Field(description='Establishment Type - Check for suitable values of filters_v2/filter_sections/filter_groups/options/value field (separated by comma to specify multiple values) returned right in this endpoint')] = None,
                                 limit: Annotated[Union[int, float, None], Field(description='The number of items per response (max 30) Default: 30')] = None,
                                 currency: Annotated[Union[str, None], Field(description='The currency code')] = None,
                                 combined_food: Annotated[Union[str, None], Field(description='Cuisine Type - Check for suitable values of filters_v2/filter_sections/filter_groups/options/value field (separated by comma to specify multiple values) returned right in this endpoint')] = None,
                                 prices_restaurants: Annotated[Union[str, None], Field(description='Prices - Check for suitable values of filters_v2/filter_sections/filter_groups/options/value field (separated by comma to specify multiple values) returned right in this endpoint')] = None,
                                 restaurant_styles: Annotated[Union[str, None], Field(description='Restaurant Features - Check for suitable values of filters_v2/filter_sections/filter_groups/options/value field (separated by comma to specify multiple values) returned right in this endpoint')] = None,
                                 open_now: Annotated[Union[bool, None], Field(description='Only returns restaurants which are opening now Example: false')] = None,
                                 lunit: Annotated[Union[str, None], Field(description='One of the followings km|mi')] = None,
                                 offset: Annotated[Union[int, float, None], Field(description='The number of items to ignore for paging purpose Default: 0')] = None,
                                 restaurant_mealtype: Annotated[Union[str, None], Field(description='Meals - Check for suitable values of filters_v2/filter_sections/filter_groups/options/value field (separated by comma to filter by multiple values. Ex : 10598,10599) returned right in this endpoint')] = None,
                                 restaurant_dining_options: Annotated[Union[str, None], Field(description='Restaurant Features - Check for suitable values of filters_v2/filter_sections/filter_groups/options/value field (separated by comma to specify multiple values) returned right in this endpoint')] = None,
                                 lang: Annotated[Union[str, None], Field(description='The language code')] = None) -> dict:
    '''List restaurants by specifying coordinates of bottom left and top right of a boundary'''
    url = 'https://travel-advisor.p.rapidapi.com/restaurants/list-in-boundary'
    headers = {'x-rapidapi-host': 'travel-advisor.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'bl_latitude': bl_latitude,
        'tr_latitude': tr_latitude,
        'bl_longitude': bl_longitude,
        'tr_longitude': tr_longitude,
        'dietary_restrictions': dietary_restrictions,
        'min_rating': min_rating,
        'restaurant_tagcategory_standalone': restaurant_tagcategory_standalone,
        'restaurant_tagcategory': restaurant_tagcategory,
        'limit': limit,
        'currency': currency,
        'combined_food': combined_food,
        'prices_restaurants': prices_restaurants,
        'restaurant_styles': restaurant_styles,
        'open_now': open_now,
        'lunit': lunit,
        'offset': offset,
        'restaurant_mealtype': restaurant_mealtype,
        'restaurant_dining_options': restaurant_dining_options,
        'lang': lang,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def restaurants_list(location_id: Annotated[Union[int, float], Field(description='The value of location_id field that returned in locations/search endpoint Default: 293919')],
                     restaurant_tagcategory: Annotated[Union[str, None], Field(description='Establishment Type - Check for suitable values of filters_v2/filter_sections/filter_groups/options/value field (separated by comma to specify multiple values) returned right in this endpoint')] = None,
                     restaurant_tagcategory_standalone: Annotated[Union[str, None], Field(description='Establishment Type - Check for suitable values of filters_v2/filter_sections/filter_groups/options/value field (separated by comma to specify multiple values) returned right in this endpoint')] = None,
                     restaurant_mealtype: Annotated[Union[str, None], Field(description='Meals - Check for suitable values of filters_v2/filter_sections/filter_groups/options/value field (separated by comma to filter by multiple values. Ex : 10598,10599) returned right in this endpoint')] = None,
                     combined_food: Annotated[Union[str, None], Field(description='Cuisine Type - Check for suitable values of filters_v2/filter_sections/filter_groups/options/value field (separated by comma to specify multiple values) returned right in this endpoint')] = None,
                     currency: Annotated[Union[str, None], Field(description='The currency code')] = None,
                     lunit: Annotated[Union[str, None], Field(description='One of the followings km|mi')] = None,
                     dietary_restrictions: Annotated[Union[str, None], Field(description='Dietary Restrictions - Check for suitable values of filters_v2/filter_sections/filter_groups/options/value field (separated by comma to specify multiple values) returned right in this endpoint')] = None,
                     limit: Annotated[Union[int, float, None], Field(description='The number of items per response (max 30) Default: 30')] = None,
                     prices_restaurants: Annotated[Union[str, None], Field(description='Prices - Check for suitable values of filters_v2/filter_sections/filter_groups/options/value field (separated by comma to specify multiple values) returned right in this endpoint')] = None,
                     min_rating: Annotated[Union[str, None], Field(description='Min 3 - Max 5')] = None,
                     open_now: Annotated[Union[bool, None], Field(description='Only returns restaurants which are opening now Example: false')] = None,
                     offset: Annotated[Union[int, float, None], Field(description='The number of items to ignore for paging purpose Default: 0')] = None,
                     restaurant_styles: Annotated[Union[str, None], Field(description='Restaurant Features - Check for suitable values of filters_v2/filter_sections/filter_groups/options/value field (separated by comma to specify multiple values) returned right in this endpoint')] = None,
                     lang: Annotated[Union[str, None], Field(description='The language code')] = None,
                     restaurant_dining_options: Annotated[Union[str, None], Field(description='Restaurant Features - Check for suitable values of filters_v2/filter_sections/filter_groups/options/value field (separated by comma to specify multiple values) returned right in this endpoint')] = None) -> dict:
    '''List restaurants related to a location by location_id'''
    url = 'https://travel-advisor.p.rapidapi.com/restaurants/list'
    headers = {'x-rapidapi-host': 'travel-advisor.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'location_id': location_id,
        'restaurant_tagcategory': restaurant_tagcategory,
        'restaurant_tagcategory_standalone': restaurant_tagcategory_standalone,
        'restaurant_mealtype': restaurant_mealtype,
        'combined_food': combined_food,
        'currency': currency,
        'lunit': lunit,
        'dietary_restrictions': dietary_restrictions,
        'limit': limit,
        'prices_restaurants': prices_restaurants,
        'min_rating': min_rating,
        'open_now': open_now,
        'offset': offset,
        'restaurant_styles': restaurant_styles,
        'lang': lang,
        'restaurant_dining_options': restaurant_dining_options,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def restaurants_get_details(location_id: Annotated[Union[int, float], Field(description='The value of location_id field that returned in restaurants/list endpoint Default: 9782025')],
                            currency: Annotated[Union[str, None], Field(description='The currency code')] = None,
                            lang: Annotated[Union[str, None], Field(description='The language code')] = None) -> dict:
    '''Get all information of a specific restaurant by its location_id'''
    url = 'https://travel-advisor.p.rapidapi.com/restaurants/get-details'
    headers = {'x-rapidapi-host': 'travel-advisor.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'location_id': location_id,
        'currency': currency,
        'lang': lang,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_get_options(data: Annotated[dict, Field(description='')] = None) -> dict:
    '''Get all options of specific attraction * This endpoint is replaced by .../attraction-products/v2/check-availability endpoint.'''
    url = 'https://travel-advisor.p.rapidapi.com/attractions/v2/get-options'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'travel-advisor.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def attractions_list_by_latlng(longitude: Annotated[Union[int, float], Field(description='Longitude of coordinate Default: 109.19553')],
                               latitude: Annotated[Union[int, float], Field(description='Latitude of coordinate Default: 12.235588')],
                               lunit: Annotated[Union[str, None], Field(description='One of the followings km|mi')] = None,
                               currency: Annotated[Union[str, None], Field(description='The currency code')] = None,
                               limit: Annotated[Union[int, float, None], Field(description='The number of items per response (max 30) Default: 0')] = None,
                               distance: Annotated[Union[int, float, None], Field(description='The radius around specified coordinate (max 25) Default: 0')] = None,
                               lang: Annotated[Union[str, None], Field(description='The language code')] = None,
                               offset: Annotated[Union[int, float, None], Field(description='The number of items to ignore for paging purpose Default: 0')] = None) -> dict:
    '''List attractions by specifying an coordinate and radius'''
    url = 'https://travel-advisor.p.rapidapi.com/attractions/list-by-latlng'
    headers = {'x-rapidapi-host': 'travel-advisor.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'longitude': longitude,
        'latitude': latitude,
        'lunit': lunit,
        'currency': currency,
        'limit': limit,
        'distance': distance,
        'lang': lang,
        'offset': offset,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def attractions_list_in_boundary(tr_longitude: Annotated[Union[int, float], Field(description='Longitude of top right coordinate Default: 109.262909')],
                                 tr_latitude: Annotated[Union[int, float], Field(description='Latitude of top right coordinate Default: 12.346705')],
                                 bl_longitude: Annotated[Union[int, float], Field(description='Longitude of bottom left coordinate Default: 109.095887')],
                                 bl_latitude: Annotated[Union[int, float], Field(description='Latitude of bottom left coordinate Default: 12.113245')],
                                 offset: Annotated[Union[int, float, None], Field(description='The number of items to ignore for paging purpose Default: 0')] = None,
                                 min_rating: Annotated[Union[int, float, None], Field(description='Rating - Min 3 max 5 Default: 0')] = None,
                                 currency: Annotated[Union[str, None], Field(description='The currency code')] = None,
                                 bookable_first: Annotated[Union[bool, None], Field(description='Book online first Example: rapid_do_not_include_in_request_key')] = None,
                                 limit: Annotated[Union[int, float, None], Field(description='The number of items per response (max 30) Default: 0')] = None,
                                 lunit: Annotated[Union[str, None], Field(description='One of the followings km|mi')] = None,
                                 lang: Annotated[Union[str, None], Field(description='The language code')] = None,
                                 subcategory: Annotated[Union[int, float, None], Field(description='Attraction category - Check for suitable values of filters_v2/filter_sections/filter_groups/options/value field (only one value is allowed at a time) returned right in this endpoint Default: 0')] = None) -> dict:
    '''List attractions by specifying coordinates of bottom left and top right of a boundary'''
    url = 'https://travel-advisor.p.rapidapi.com/attractions/list-in-boundary'
    headers = {'x-rapidapi-host': 'travel-advisor.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'tr_longitude': tr_longitude,
        'tr_latitude': tr_latitude,
        'bl_longitude': bl_longitude,
        'bl_latitude': bl_latitude,
        'offset': offset,
        'min_rating': min_rating,
        'currency': currency,
        'bookable_first': bookable_first,
        'limit': limit,
        'lunit': lunit,
        'lang': lang,
        'subcategory': subcategory,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def attractions_list(location_id: Annotated[Union[int, float], Field(description='The value of location_id field that returned in locations/search endpoint Default: 298571')],
                     currency: Annotated[Union[str, None], Field(description='The currency code')] = None,
                     lang: Annotated[Union[str, None], Field(description='The language code')] = None,
                     lunit: Annotated[Union[str, None], Field(description='One of the followings km|mi')] = None,
                     min_rating: Annotated[Union[int, float, None], Field(description='Rating - Min 3 max 5 Default: 0')] = None,
                     limit: Annotated[Union[int, float, None], Field(description='The number of items per response (max 30) Default: 0')] = None,
                     sort: Annotated[Union[str, None], Field(description='One of following recommended|ranking')] = None,
                     bookable_first: Annotated[Union[bool, None], Field(description='Book online first Example: rapid_do_not_include_in_request_key')] = None,
                     subcategory: Annotated[Union[int, float, None], Field(description='Attraction category - Check for suitable values of filters_v2/filter_sections/filter_groups/options/value field (only one value is allowed at a time) returned right in this endpoint Default: 0')] = None,
                     offset: Annotated[Union[int, float, None], Field(description='The number of items to ignore for paging purpose Default: 0')] = None) -> dict:
    '''List attractions of specific location by location_id'''
    url = 'https://travel-advisor.p.rapidapi.com/attractions/list'
    headers = {'x-rapidapi-host': 'travel-advisor.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'location_id': location_id,
        'currency': currency,
        'lang': lang,
        'lunit': lunit,
        'min_rating': min_rating,
        'limit': limit,
        'sort': sort,
        'bookable_first': bookable_first,
        'subcategory': subcategory,
        'offset': offset,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def attractions_get_details(location_id: Annotated[Union[int, float], Field(description='The value of location_id field that returned in attractions/list endpoint Default: 1451754')],
                            currency: Annotated[Union[str, None], Field(description='The currency code')] = None,
                            lang: Annotated[Union[str, None], Field(description='The language code')] = None) -> dict:
    '''Get all information of specific attracting location by its location_id'''
    url = 'https://travel-advisor.p.rapidapi.com/attractions/get-details'
    headers = {'x-rapidapi-host': 'travel-advisor.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'location_id': location_id,
        'currency': currency,
        'lang': lang,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def keywords_list(location_id: Annotated[Union[int, float], Field(description='The value of location_id field that returned in hotels/list, restaurants/list, or attractions/list endpoints Default: 8014024')],
                  offset: Annotated[Union[int, float, None], Field(description='The number of items to ignore for paging purpose Default: 0')] = None,
                  limit: Annotated[Union[int, float, None], Field(description='The number of items per response (max 10) Default: 10')] = None) -> dict:
    '''List interesting keywords related to a specific location by its location_id'''
    url = 'https://travel-advisor.p.rapidapi.com/keywords/list'
    headers = {'x-rapidapi-host': 'travel-advisor.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'location_id': location_id,
        'offset': offset,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def tips_list(location_id: Annotated[Union[int, float], Field(description='The value of location_id field that returned in hotels/list endpoint Default: 8014024')],
              lang: Annotated[Union[str, None], Field(description='')] = None,
              currency: Annotated[Union[str, None], Field(description='The currency code')] = None,
              offset: Annotated[Union[int, float, None], Field(description='The number of items to ignore for paging purpose Default: 0')] = None,
              limit: Annotated[Union[int, float, None], Field(description='The number of items per response (max 20) Default: 20')] = None) -> dict:
    '''List tips of specific hotel by its location_id'''
    url = 'https://travel-advisor.p.rapidapi.com/tips/list'
    headers = {'x-rapidapi-host': 'travel-advisor.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'location_id': location_id,
        'lang': lang,
        'currency': currency,
        'offset': offset,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def reviews_list(location_id: Annotated[Union[int, float], Field(description='The value of location_id field that returned in hotels/list, restaurants/list, or attractions/list endpoints Default: 8014024')],
                 keyword: Annotated[Union[str, None], Field(description='Check for suitable value of text field returned in keywords/list endpoint')] = None,
                 limit: Annotated[Union[int, float, None], Field(description='The number of items per response (max 20) Default: 20')] = None,
                 currency: Annotated[Union[str, None], Field(description='The currency code')] = None,
                 offset: Annotated[Union[int, float, None], Field(description='The number of items to ignore for paging purpose Default: 0')] = None,
                 lang: Annotated[Union[str, None], Field(description='The language code')] = None) -> dict:
    '''List reviews related to a location by its location_id'''
    url = 'https://travel-advisor.p.rapidapi.com/reviews/list'
    headers = {'x-rapidapi-host': 'travel-advisor.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'location_id': location_id,
        'keyword': keyword,
        'limit': limit,
        'currency': currency,
        'offset': offset,
        'lang': lang,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def photos_list(location_id: Annotated[Union[int, float], Field(description='The value of location_id field that returned in hotels/list, restaurants/list, or attractions/list endpoints Default: 2233968')],
                currency: Annotated[Union[str, None], Field(description='The currency code')] = None,
                limit: Annotated[Union[int, float, None], Field(description='The number of items per response (max 50) Default: 50')] = None,
                offset: Annotated[Union[int, float, None], Field(description='The number of items to ignore for paging purpose Default: 0')] = None,
                lang: Annotated[Union[str, None], Field(description='The language code')] = None) -> dict:
    '''List photos related to a location by its id'''
    url = 'https://travel-advisor.p.rapidapi.com/photos/list'
    headers = {'x-rapidapi-host': 'travel-advisor.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'location_id': location_id,
        'currency': currency,
        'limit': limit,
        'offset': offset,
        'lang': lang,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def questions_list(location_id: Annotated[Union[int, float], Field(description='The value of location_id field that returned in hotels/list, restaurants/list, or attractions/list endpoints Default: 8014024')],
                   offset: Annotated[Union[int, float, None], Field(description='The number of items to ignore for paging purpose Default: 0')] = None,
                   limit: Annotated[Union[int, float, None], Field(description='The number of items per response (max 10) Default: 10')] = None) -> dict:
    '''List questions related to a location by its id'''
    url = 'https://travel-advisor.p.rapidapi.com/questions/list'
    headers = {'x-rapidapi-host': 'travel-advisor.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'location_id': location_id,
        'offset': offset,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def answers_list(question_id: Annotated[Union[int, float], Field(description='The value of id field that returned in questions/list endpoint Default: 5283833')],
                 offset: Annotated[Union[int, float, None], Field(description='The number of items to ignore for paging purpose Default: 0')] = None,
                 limit: Annotated[Union[int, float, None], Field(description='The number of items per response (max 10) Default: 0')] = None) -> dict:
    '''List answers related to a questions by its id'''
    url = 'https://travel-advisor.p.rapidapi.com/answers/list'
    headers = {'x-rapidapi-host': 'travel-advisor.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'question_id': question_id,
        'offset': offset,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_check_availability(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Check available products relating to an attraction'''
    url = 'https://travel-advisor.p.rapidapi.com/attraction-products/v2/check-availability'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'travel-advisor.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
