
import 'package:latlong/latlong.dart';
import 'dart:async';
import 'package:http/http.dart' as http;
import 'dart:convert';

class ApiResponse {
  final int time;
  final double sats;
  final double lat;
  final double long;
  final double alt;
  ApiResponse({this.time, this.sats, this.lat, this.long, this.alt});
  factory ApiResponse.fromJson(Map<String, dynamic> json) {
    return ApiResponse(
      time: checkInt(json['time']),
      sats: checkDouble(json['sats']),
      lat: checkDouble(json['lat']),
      long: checkDouble(json['long']),
      alt: checkDouble(json['alt']),
    );
  }

  static double checkDouble(dynamic value) {
    if (value is String) {
      print("val: " + value);
      return double.parse(value);
    } else if (value is! double) {
      return value.toDouble();
    } else {
      return value;
    }
  }

  static int checkInt(dynamic value) {
    if (value is String) {
      return int.parse(value);
    } else if (value is! int) {
      return value.toInt();
    } else {
      return value;
    }
  }
}




Future<LatLng> fetchVanLocation() async {
  final response = await http.get('https://app-processing-lcn55j3ska-ew.a.run.app/app/v1/current-location');
  if (response.statusCode == 200) {
    final a =  ApiResponse.fromJson(json.decode(response.body));
    return LatLng(a.lat, a.long);
  } else {
    throw Exception('Failed to load Van location');
  }

}