import 'package:flutter/material.dart';
import 'package:flutter_map/flutter_map.dart';
import 'package:latlong/latlong.dart';

import '../widgets/drawer.dart';

class VanHistory extends StatelessWidget {
  static const String route = 'polyline';

  @override
  Widget build(BuildContext context) {
    var points = <LatLng>[ // todo: load from API
      LatLng(51.5, -0.09),
      LatLng(53.3498, -6.2603),
      LatLng(48.8566, 2.3522),
    ];
    return Scaffold(
      appBar: AppBar(title: Text('Van history')),
      drawer: buildDrawer(context, VanHistory.route),
      body: Column(
      children: [
        Padding(
          padding: EdgeInsets.only(top: 1.0, bottom: 1.0),
          child: Text('Todo: selection of history here'),
        ),
        Flexible(
          child: FlutterMap(
            options: MapOptions(
              maxZoom: 17.0,
              center: LatLng(51.5, -0.09),
              zoom: 10.0,
            ),
            layers: [
              TileLayerOptions(
                  urlTemplate:
                      'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
                  subdomains: ['a', 'b', 'c']),
              PolylineLayerOptions(
                polylines: [
                  Polyline(
                      points: points,
                      strokeWidth: 4.0,
                      color: Colors.purple),
                ],
              )
            ],
          ),
        ),
      ],
      ),
    );
  }
}
