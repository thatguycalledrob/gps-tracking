import 'package:jaguar_serializer/jaguar_serializer.dart';

part 'coordinate.jser.dart';

class Coordinate {
  
  final int time;
  
  final num sats;
  
  final num lat;
  
  final num long;
  
  final num alt;
  
  final int order;
  
  final int count;
  

  Coordinate(
    

{
     this.time = null,  
     this.sats = null,  
    
     this.lat = null,  
     this.long = null,  
     this.alt = null,  
     this.order = null,   this.count = null 
    
    }
  );

  @override
  String toString() {
    return 'Coordinate[time=$time, sats=$sats, lat=$lat, long=$long, alt=$alt, order=$order, count=$count, ]';
  }
}

@GenSerializer()
class CoordinateSerializer extends Serializer<Coordinate> with _$CoordinateSerializer {

}
