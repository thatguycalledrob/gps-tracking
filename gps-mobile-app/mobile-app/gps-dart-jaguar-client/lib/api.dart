library swagger.api;

import 'package:http/http.dart';
import 'package:jaguar_serializer/jaguar_serializer.dart';
import 'package:jaguar_retrofit/jaguar_retrofit.dart';
import 'package:swagger/auth/api_key_auth.dart';
import 'package:swagger/auth/basic_auth.dart';
import 'package:swagger/auth/oauth.dart';

import 'package:swagger/api/default_api.dart';

import 'package:swagger/model/coordinate.dart';
import 'package:swagger/model/error.dart';
import 'package:swagger/model/instructions.dart';
import 'package:swagger/model/query.dart';


final jsonJaguarRepo = JsonRepo()
..add(CoordinateSerializer())
..add(ErrorSerializer())
..add(InstructionsSerializer())
..add(QuerySerializer())
;

final _defaultInterceptors = [OAuthInterceptor(), BasicAuthInterceptor(), ApiKeyAuthInterceptor()];

class JaguarApiGen {
    List<Interceptor> interceptors;
    String basePath = "https://localhost/app/v1";
    Route _baseRoute;

    /**
     * Add custom global interceptors, put overrideInterceptors to true to set your interceptors only (auth interceptors will not be added)
     */
    JaguarApiGen({List<Interceptor> interceptors, bool overrideInterceptors = false, String baseUrl}) {
        _baseRoute = Route(baseUrl ?? basePath).withClient(globalClient ?? IOClient());
        if(interceptors == null) {
            this.interceptors = _defaultInterceptors;
        }
        else if(overrideInterceptors){
            this.interceptors = interceptors;
        }
        else {
            this.interceptors = List.from(_defaultInterceptors)..addAll(interceptors);
        }

        this.interceptors.forEach((interceptor) {
            _baseRoute.before(interceptor.before);
            _baseRoute.after(interceptor.after);
        });
    }

    void setOAuthToken(String name, String token) {
        (_defaultInterceptors[0] as OAuthInterceptor).tokens[name] = token;
    }

    void setBasicAuth(String name, String username, String password) {
        (_defaultInterceptors[1] as BasicAuthInterceptor).authInfo[name] = BasicAuthInfo(username, password);
    }

    void setApiKey(String name, String apiKey) {
        (_defaultInterceptors[2] as ApiKeyAuthInterceptor).apiKeys[name] = apiKey;
    }

    
    /**
     * Get DefaultApi instance, base route and serializer can be overridden by a given but be careful,
     * by doing that all interceptors will not be executed
     */
    DefaultApi getDefaultApi({Route base, SerializerRepo serializers}) {
        if(base == null) {
            base = _baseRoute;
        }
        if(serializers == null) {
            serializers = jsonJaguarRepo;
        }
        return DefaultApi(base: base, serializers: serializers);
    }

    
}