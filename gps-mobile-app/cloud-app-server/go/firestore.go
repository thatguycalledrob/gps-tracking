package swagger

import (
	"context"
	"log"
	"time"

	"cloud.google.com/go/firestore"
	firebase "firebase.google.com/go"
	"google.golang.org/api/option"
	"google.golang.org/genproto/googleapis/type/latlng"
)

var ctx context.Context
var Client *firestore.Client

// this is the structure of what the pi stores in the database.
type coordinateValue struct {
	Altitude   float64        `firestore:"altitude,omitempty"`
	Geostamp   *latlng.LatLng `firestore:"geostamp,omitempty"`
	Satellites float64        `firestore:"satellites,omitempty"`
	Timestamp  time.Time      `firestore:"timestamp,omitempty"`
	TimeTo     time.Time      `firestore:"timestamp_to,omitempty"`
}

func SetupFirestore() *firestore.Client {
	log.Println("Initalizing new firestore client")

	ctx = context.Background()
	sa := option.WithCredentialsFile("/key.json")

	app, err := firebase.NewApp(ctx, nil, sa)
	if err != nil {
		log.Fatal(err)
	}

	Client, err = app.Firestore(ctx)
	if err != nil {
		log.Fatal(err)
	}

	return Client
}

func toCoordinateResponse(c coordinateValue) Coordinate {
	var converted Coordinate
	converted.Alt = float32(c.Altitude)
	converted.Time = c.Timestamp.Unix()
	converted.Lat = float32(c.Geostamp.Latitude)
	converted.Long = float32(c.Geostamp.Longitude)
	converted.Sats = float32(c.Satellites)
	converted.Order = 1
	return converted
}

func GetLatestCoord() Coordinate {
	// get the coords time ordered. newest first
	log.Println("Accessing coordindates records in Firestore")
	orderedCoords := Client.Collection("coordinates").OrderBy("timestamp", firestore.Desc).Documents(ctx)
	coordsRef, err := orderedCoords.Next()
	if err != nil {
		log.Fatal(err)
	}
	log.Printf("latest coord: %+v", coordsRef)

	var cval *coordinateValue
	coordsRef.DataTo(&cval)
	return toCoordinateResponse(*cval)

}
