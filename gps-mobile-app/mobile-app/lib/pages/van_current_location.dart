import 'package:flutter/material.dart';
import 'package:flutter_map/flutter_map.dart';
import 'package:latlong/latlong.dart';

import '../widgets/drawer.dart';

class VanCurrentLocation extends StatefulWidget {
  static const String route = 'map_controller_animated';

  @override
  VanCurrentLocationState createState() {
    return VanCurrentLocationState();
  }
}

class VanCurrentLocationState extends State<VanCurrentLocation>
    with TickerProviderStateMixin {
  // Note the addition of the TickerProviderStateMixin here. If you are getting an error like
  // 'The class 'TickerProviderStateMixin' can't be used as a mixin because it extends a class other than Object.'
  // in your IDE, you can probably fix it by adding an analysis_options.yaml file to your project
  // with the following content:
  //  analyzer:
  //    language:
  //      enableSuperMixins: true
  // See https://github.com/flutter/flutter/issues/14317#issuecomment-361085869
  // This project didn't require that change, so YMMV.

  static LatLng london = LatLng(51.5, -0.09);

  MapController mapController;

  @override
  void initState() {
    super.initState();
    mapController = MapController();
  }

  void _animatedMapMove(LatLng destLocation, double destZoom) {
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
        point: london,
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
              padding: EdgeInsets.only(top: 1.0, bottom: 1.0),
              child:                   MaterialButton(
                child: Text('Jump to Bounds'),
                onPressed: () {
                  var bounds = LatLngBounds();
                  bounds.extend(london);
                  mapController.fitBounds(
                    bounds,
                    options: FitBoundsOptions(
                      padding: EdgeInsets.only(left: 15.0, right: 15.0),
                    ),
                  );
                },
              ),
            ),
            Flexible(
              child: FlutterMap(
                mapController: mapController,
                options: MapOptions(
                    center: LatLng(51.5, -0.09), //todo: grab via API
                    zoom: 13.0,
                    maxZoom: 19.0,
                    minZoom: 3.0),
                layers: [
                  TileLayerOptions(
                      urlTemplate:
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
