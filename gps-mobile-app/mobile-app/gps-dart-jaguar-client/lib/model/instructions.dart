import 'package:jaguar_serializer/jaguar_serializer.dart';

part 'instructions.jser.dart';

class Instructions {
  
  final String instruction;
  //enum instructionEnum {  restart,  startVnc,  };

  Instructions(
    

{
    
     this.instruction = null 
    }
  );

  @override
  String toString() {
    return 'Instructions[instruction=$instruction, ]';
  }
}

@GenSerializer()
class InstructionsSerializer extends Serializer<Instructions> with _$InstructionsSerializer {

}
