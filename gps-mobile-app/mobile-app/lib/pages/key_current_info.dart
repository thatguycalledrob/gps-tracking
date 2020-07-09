import 'package:flutter/material.dart';
import 'package:latlong/latlong.dart';
import 'package:flutter/widgets.dart';

import '../widgets/drawer.dart';
import '../logic/get_current_location.dart';

class VanInfoPage extends StatefulWidget {
  static const String route = 'van_info_page';
  @override
  VanInfoPageState createState() {
    return VanInfoPageState();
  }
}

class VanInfoPageState extends State<VanInfoPage>
    with TickerProviderStateMixin {

  LatLng _vanLocation = LatLng(0, 0);

  @override
  void initState() {
    super.initState();
    getLatestLocation();
  }

  void getLatestLocation() async {
    final v = await fetchVanLocation();
    setState(() {
      _vanLocation = v;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Van Current location')),
      drawer: buildDrawer(context, VanInfoPage.route),
      body: Column(
        children: [
          MaterialButton(
            child: Text('Jump to Van'),
            onPressed: () {
              print("hello world");
            },
          ),
          MaterialButton(
            child: Text('Reload Van Location'),
            onPressed: () {
              getLatestLocation();
            },
          ),
        ],
      )
    );
  }
}
