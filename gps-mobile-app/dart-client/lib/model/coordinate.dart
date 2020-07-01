part of swagger.api;

class Coordinate {
  
  int time = null;
  

  num sats = null;
  

  num lat = null;
  

  num long = null;
  

  num alt = null;
  

  int order = null;
  

  int count = null;
  
  Coordinate();

  @override
  String toString() {
    return 'Coordinate[time=$time, sats=$sats, lat=$lat, long=$long, alt=$alt, order=$order, count=$count, ]';
  }

  Coordinate.fromJson(Map<String, dynamic> json) {
    if (json == null) return;
    time =
        json['time']
    ;
    sats =
        json['sats']
    ;
    lat =
        json['lat']
    ;
    long =
        json['long']
    ;
    alt =
        json['alt']
    ;
    order =
        json['order']
    ;
    count =
        json['count']
    ;
  }

  Map<String, dynamic> toJson() {
    return {
      'time': time,
      'sats': sats,
      'lat': lat,
      'long': long,
      'alt': alt,
      'order': order,
      'count': count
     };
  }

  static List<Coordinate> listFromJson(List<dynamic> json) {
    return json == null ? new List<Coordinate>() : json.map((value) => new Coordinate.fromJson(value)).toList();
  }

  static Map<String, Coordinate> mapFromJson(Map<String, Map<String, dynamic>> json) {
    var map = new Map<String, Coordinate>();
    if (json != null && json.length > 0) {
      json.forEach((String key, Map<String, dynamic> value) => map[key] = new Coordinate.fromJson(value));
    }
    return map;
  }
}

