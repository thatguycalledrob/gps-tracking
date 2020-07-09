import 'package:flutter/material.dart';
import 'package:flutter_map/flutter_map.dart';
import 'package:latlong/latlong.dart';
import 'package:flutter/widgets.dart';
import 'package:flutter_map/plugin_api.dart';

import '../widgets/drawer.dart';
import '../logic/get_current_location.dart';

class VanCurrentLocation extends StatefulWidget {
  static const String route = 'map_controller_animated';
  @override
  VanCurrentLocationState createState() {
    return VanCurrentLocationState();
  }
}

class VanCurrentLocationState extends State<VanCurrentLocation>
    with TickerProviderStateMixin {

  LatLng _vanLocation = LatLng(0, 0);
  MapController mapController;

  @override
  void initState() {
    super.initState();
    mapController = MapController();
    getLatestLocation();
  }

  void getLatestLocation() async {
    final v = await fetchVanLocation();
    setState(() {
      _vanLocation = v;
    });
  }

  void _animatedMapMove(LatLng destLocation, double destZoom) async {
    await mapController.onReady;
    // Create some tweens. These serve to split up the transition from one location to another.
    // In our case, we want to split the transition be<tween> our current map center and the destination.
    final _latTween = Tween<double>(
        begin: mapController.center.latitude, end: destLocation.latitude);
    final _lngTween = Tween<double>(
        begin: mapController.center.longitude, end: destLocation.longitude);
    final _zoomTween = Tween<double>(begin: mapController.zoom, end: destZoom);

    // Create a animation controller that has a duration and a TickerProvider.
    var controller = AnimationController(
        duration: const Duration(milliseconds: 500), vsync: this);
    // The animation determines what path the animation will take. You can try different Curves values, although I found
    // fastOutSlowIn to be my favorite.
    Animation<double> animation =
    CurvedAnimation(parent: controller, curve: Curves.fastOutSlowIn);

    controller.addListener(() {
      mapController.move(
          LatLng(_latTween.evaluate(animation), _lngTween.evaluate(animation)),
          _zoomTween.evaluate(animation));
    });

    animation.addStatusListener((status) {
      if (status == AnimationStatus.completed) {
        controller.dispose();
      } else if (status == AnimationStatus.dismissed) {
        controller.dispose();
      }
    });

    controller.forward();
  }

  @override
  Widget build(BuildContext context) {
    var markers = <Marker>[
      Marker(
        width: 80.0,
        height: 80.0,
        point: _vanLocation,
        builder: (ctx) => Container(
            child: Image.asset('assets/images/transit.png')
        ),
      )
    ];

    return Scaffold(
      appBar: AppBar(title: Text('Van Current location')),
      drawer: buildDrawer(context, VanCurrentLocation.route),
      body: Column(
        children: [
          Padding(
            padding: EdgeInsets.only(top: 0.5, bottom: 0.5),
            child: Row(
                children: <Widget>[
                  MaterialButton(
                    child: Text('Jump to Van'),
                    onPressed: () {
                      print(_vanLocation);
                      print("");
                      print(mapController);
                      _animatedMapMove(_vanLocation, 15);
                    },
                  ),
                  MaterialButton(
                    child: Text('Reload Van Location'),
                    onPressed: () {
                      print(_vanLocation);
                      getLatestLocation();
                      print(_vanLocation);
                    },
                  ),
                ],
            )
          ),
          Flexible(
            child: FlutterMap(
              mapController: mapController,
              options: MapOptions(
                  center: _vanLocation,
                  zoom: 13.0,
                  maxZoom: 19.0,
                  minZoom: 3.0),
              layers: [
                TileLayerOptions(
                    urlTemplate:
                    //'https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}',
                    'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
                    subdomains: ['a', 'b', 'c']),
                MarkerLayerOptions(markers: markers)
              ],
            ),
          ),
        ],
      ),
    );
  }
}
