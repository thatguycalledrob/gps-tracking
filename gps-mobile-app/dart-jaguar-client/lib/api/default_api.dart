import 'package:jaguar_retrofit/annotations/annotations.dart';
import 'package:jaguar_retrofit/jaguar_retrofit.dart';
import 'package:jaguar_serializer/jaguar_serializer.dart';
import 'package:jaguar_serializer/src/repo/repo.dart';
import 'dart:async';

import 'package:swagger/model/coordinate.dart';
import 'package:swagger/model/query.dart';
import 'package:swagger/model/error.dart';


part 'default_api.jretro.dart';

@GenApiClient()
class DefaultApi extends _$DefaultApiClient implements ApiClient {
    final Route base;
    final SerializerRepo serializers;

    DefaultApi({this.base, this.serializers});

    /// 
    ///
    /// latest location
    @GetReq(path: "/current-location")
    Future<Coordinate> currentLocation(
    );

    /// 
    ///
    /// Post a query for a history
    @PostReq(path: "/history-query")
    Future<List<Coordinate>> queryHistory(
        
        @AsJson() Query query
    );

    /// 
    ///
    /// previous parking spots
    @GetReq(path: "/parking-spots")
    Future<List<Coordinate>> retriveParkingSpots(
    );


}
