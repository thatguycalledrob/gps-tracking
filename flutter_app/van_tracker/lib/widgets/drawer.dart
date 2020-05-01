import 'package:flutter/material.dart';

import '../pages/van_current_location.dart';
import '../pages/esri.dart';
import '../pages/van_history.dart';

Drawer buildDrawer(BuildContext context, String currentRoute) {
  return Drawer(
    child: ListView(
      children: <Widget>[
        ListTile(
          title: const Text('Esri'),
          selected: currentRoute == EsriMapStyle.route,
          onTap: () {
            Navigator.pushReplacementNamed(context, EsriMapStyle.route);
          },
        ),
        ListTile(
          title: const Text('Van History'),
          selected: currentRoute == VanHistory.route,
          onTap: () {
            Navigator.pushReplacementNamed(context, VanHistory.route);
          },
        ),
        ListTile(
          title: const Text('Van Current Location'),
          selected: currentRoute == VanCurrentLocation.route,
          onTap: () {
            Navigator.pushReplacementNamed(
                context, VanCurrentLocation.route);
          },
        ),
      ],
    ),
  );
}
