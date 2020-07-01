# swagger.api.DefaultApi

## Load the API package
```dart
import 'package:swagger/api.dart';
```

All URIs are relative to *https://localhost/app/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**currentLocation**](DefaultApi.md#currentLocation) | **GET** /current-location | 
[**queryHistory**](DefaultApi.md#queryHistory) | **POST** /history-query | 
[**retriveParkingSpots**](DefaultApi.md#retriveParkingSpots) | **GET** /parking-spots | 


# **currentLocation**
> Coordinate currentLocation()



latest location

### Example 
```dart
import 'package:swagger/api.dart';

var api_instance = new DefaultApi();

try { 
    var result = api_instance.currentLocation();
    print(result);
} catch (e) {
    print("Exception when calling DefaultApi->currentLocation: $e\n");
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Coordinate**](Coordinate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **queryHistory**
> List<Coordinate> queryHistory(query)



Post a query for a history

### Example 
```dart
import 'package:swagger/api.dart';

var api_instance = new DefaultApi();
var query = new Query(); // Query | 

try { 
    var result = api_instance.queryHistory(query);
    print(result);
} catch (e) {
    print("Exception when calling DefaultApi->queryHistory: $e\n");
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**Query**](Query.md)|  | 

### Return type

[**List<Coordinate>**](Coordinate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retriveParkingSpots**
> List<Coordinate> retriveParkingSpots()



previous parking spots

### Example 
```dart
import 'package:swagger/api.dart';

var api_instance = new DefaultApi();

try { 
    var result = api_instance.retriveParkingSpots();
    print(result);
} catch (e) {
    print("Exception when calling DefaultApi->retriveParkingSpots: $e\n");
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List<Coordinate>**](Coordinate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

