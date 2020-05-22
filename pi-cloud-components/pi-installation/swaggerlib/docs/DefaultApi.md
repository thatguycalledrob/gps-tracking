# swagger_client.DefaultApi

All URIs are relative to *https://localhost/pi/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_coordinates**](DefaultApi.md#add_coordinates) | **POST** /coordinates | 
[**retrive_instructions**](DefaultApi.md#retrive_instructions) | **GET** /instructions | 


# **add_coordinates**
> Added add_coordinates(coordinates)



Adds the latest coordinate data to quick storage

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
coordinates = [swagger_client.Coordinate()] # list[Coordinate] | 

try:
    api_response = api_instance.add_coordinates(coordinates)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->add_coordinates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coordinates** | [**list[Coordinate]**](Coordinate.md)|  | 

### Return type

[**Added**](Added.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrive_instructions**
> Instructions retrive_instructions()



gets instructions for the Pi to execute

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.retrive_instructions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrive_instructions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Instructions**](Instructions.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

