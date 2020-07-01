part of swagger.api;

class Query {
  
  int fromDate = null;
  

  int toDate = null;
  

  String algorithm = null;
  //enum algorithmEnum {  hourlyData,  onlyMovement,  };
  Query();

  @override
  String toString() {
    return 'Query[fromDate=$fromDate, toDate=$toDate, algorithm=$algorithm, ]';
  }

  Query.fromJson(Map<String, dynamic> json) {
    if (json == null) return;
    fromDate =
        json['fromDate']
    ;
    toDate =
        json['toDate']
    ;
    algorithm =
        json['algorithm']
    ;
  }

  Map<String, dynamic> toJson() {
    return {
      'fromDate': fromDate,
      'toDate': toDate,
      'algorithm': algorithm
     };
  }

  static List<Query> listFromJson(List<dynamic> json) {
    return json == null ? new List<Query>() : json.map((value) => new Query.fromJson(value)).toList();
  }

  static Map<String, Query> mapFromJson(Map<String, Map<String, dynamic>> json) {
    var map = new Map<String, Query>();
    if (json != null && json.length > 0) {
      json.forEach((String key, Map<String, dynamic> value) => map[key] = new Query.fromJson(value));
    }
    return map;
  }
}

