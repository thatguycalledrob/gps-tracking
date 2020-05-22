import 'package:jaguar_serializer/jaguar_serializer.dart';

part 'error.jser.dart';

class Error {
  
  final int code;
  
  final String message;
  

  Error(
    

{
    
     this.code = null,  
     this.message = null 
    }
  );

  @override
  String toString() {
    return 'Error[code=$code, message=$message, ]';
  }
}

@GenSerializer()
class ErrorSerializer extends Serializer<Error> with _$ErrorSerializer {

}
