
import 'package:flutter/material.dart';

import 'pages/van_current_location.dart';
import 'pages/esri.dart';
import 'pages/van_history.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Van Tracking Map',
      theme: ThemeData(
        primarySwatch: mapBoxBlue,
      ),
      home: VanCurrentLocation(),
      routes: <String, WidgetBuilder>{

        EsriMapStyle.route: (context) => EsriMapStyle(),
        VanHistory.route: (context) => VanHistory(),
        VanCurrentLocation.route: (context) => VanCurrentLocation(),
      },
    );
  }
}

// Generated using Material Design Palette/Theme Generator
// http://mcg.mbitson.com/
// https://github.com/mbitson/mcg
const int _bluePrimary = 0xFF395afa;
const MaterialColor mapBoxBlue = const MaterialColor(
  _bluePrimary,
  const <int, Color>{
    50: const Color(0xFFE7EBFE),
    100: const Color(0xFFC4CEFE),
    200: const Color(0xFF9CADFD),
    300: const Color(0xFF748CFC),
    400: const Color(0xFF5773FB),
    500: const Color(_bluePrimary),
    600: const Color(0xFF3352F9),
    700: const Color(0xFF2C48F9),
    800: const Color(0xFF243FF8),
    900: const Color(0xFF172EF6),
  },
);