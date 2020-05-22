import 'package:flutter/material.dart';
import 'package:flutter_map/flutter_map.dart';
import 'package:latlong/latlong.dart';

import '../widgets/drawer.dart';

class EsriMapStyle extends StatelessWidget {
  static const String route = 'esri';

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Esri')),
      drawer: buildDrawer(context, route),
      body: Flexible(
        child: FlutterMap(
          options: MapOptions(
            center: LatLng(45.5231, -122.6765),
            zoom: 13.0,
          ),
          layers: [
            TileLayerOptions(
              urlTemplate:
                  'https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}',
            ),
          ],
        ),
      ),
    );
  }
}
