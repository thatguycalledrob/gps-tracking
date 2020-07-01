part of swagger.api;

class Instructions {
  
  String instruction = null;
  //enum instructionEnum {  restart,  startVnc,  };
  Instructions();

  @override
  String toString() {
    return 'Instructions[instruction=$instruction, ]';
  }

  Instructions.fromJson(Map<String, dynamic> json) {
    if (json == null) return;
    instruction =
        json['instruction']
    ;
  }

  Map<String, dynamic> toJson() {
    return {
      'instruction': instruction
     };
  }

  static List<Instructions> listFromJson(List<dynamic> json) {
    return json == null ? new List<Instructions>() : json.map((value) => new Instructions.fromJson(value)).toList();
  }

  static Map<String, Instructions> mapFromJson(Map<String, Map<String, dynamic>> json) {
    var map = new Map<String, Instructions>();
    if (json != null && json.length > 0) {
      json.forEach((String key, Map<String, dynamic> value) => map[key] = new Instructions.fromJson(value));
    }
    return map;
  }
}

