import 'package:jaguar_serializer/jaguar_serializer.dart';

part 'query.jser.dart';

class Query {
  
  final int fromDate;
  
  final int toDate;
  
  final String algorithm;
  //enum algorithmEnum {  hourlyData,  onlyMovement,  };

  Query(
    

{
    
     this.fromDate = null,  
     this.toDate = null,  
     this.algorithm = null 
    }
  );

  @override
  String toString() {
    return 'Query[fromDate=$fromDate, toDate=$toDate, algorithm=$algorithm, ]';
  }
}

@GenSerializer()
class QuerySerializer extends Serializer<Query> with _$QuerySerializer {

}
