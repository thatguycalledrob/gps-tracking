import 'dart:io';
import 'dart:convert';

void main() {
  HttpClient()
      .getUrl(Uri.parse(
          'https://app-processing-lcn55j3ska-ew.a.run.app/app/v1/current-location')) // produces a request object
      .then((request) => request.close()) // sends the request
      .then((response) => response
          .transform(Utf8Decoder())
          .listen(print)); // transforms and prints the response
}
