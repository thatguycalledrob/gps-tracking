package logic

import (
	"context"
	"fmt"
	"log"
	"net/http"
	"time"

	"cloud.google.com/go/firestore"
	"google.golang.org/api/iterator"
	"google.golang.org/genproto/googleapis/type/latlng"

	"github.com/tidwall/geojson"
	"github.com/tidwall/geojson/geometry"
)

// the GPS has some jitter. In general, lets discount readings if we have moved below this amounr
const PRECISION float64 = 50.0

// this is the structure of what the pi stores in the database.
type coordinateValue struct {
	Altitude   float64        `firestore:"altitude,omitempty"`
	Geostamp   *latlng.LatLng `firestore:"geostamp,omitempty"`
	Satellites float64        `firestore:"satellites,omitempty"`
	Timestamp  time.Time      `firestore:"timestamp,omitempty"`
	TimeTo     time.Time      `firestore:"timestamp_to,omitempty"`
}

// this is the working geoJSON with timestamp
type pointWithTime struct {
	p          *geojson.Point
	Satellites float64
	t_from     time.Time
	t_to       time.Time
}

func (pt *pointWithTime) separation(p2 *pointWithTime) float64 {
	return pt.p.DistancePoint(p2.p.Base())
}

// stringer func to enable debugging
func (pt *pointWithTime) String() string {
	return fmt.Sprintf(
		"{x: %v y: %v z: %v from_time: %v to_time: %v}",
		pt.p.Base().X, pt.p.Base().Y, pt.p.Z(), pt.t_from, pt.t_to,
	)
}

func convertToGeoJson(cv *coordinateValue) *pointWithTime {
	x := cv.Geostamp.Longitude
	y := cv.Geostamp.Latitude
	z := cv.Altitude

	return &pointWithTime{
		p:          geojson.NewPointZ(geometry.Point{X: x, Y: y}, z),
		Satellites: cv.Satellites,
		t_from:     cv.Timestamp,
		t_to:       cv.Timestamp,
	}
}

func convertToFirestoreFormat(pt *pointWithTime) *coordinateValue {
	return &coordinateValue{
		Altitude: pt.p.Z(),
		Geostamp: &latlng.LatLng{
			Latitude:  pt.p.Base().X,
			Longitude: pt.p.Base().Y,
		},
		Satellites: pt.Satellites,
		Timestamp:  pt.t_from,
		TimeTo:     pt.t_to,
	}
}

func listToFirestoreFormat(lpt []*pointWithTime) []*coordinateValue {
	r := make([]*coordinateValue, len(lpt))
	for i, pt := range lpt {
		r[i] = convertToFirestoreFormat(pt)
	}
	return r
}

func readCoords(client *firestore.Client, ctx context.Context) []*pointWithTime {
	// get the coords time ordered. Oldest first
	log.Println("Accessing coordindates records in Firestore")
	orderedCoords := client.Collection("coordinates").OrderBy("timestamp", firestore.Asc).Documents(ctx)
	coordsRef, err := orderedCoords.GetAll()
	if err != nil {
		log.Fatal(err)
	}

	log.Printf("Accessing %v records", len(coordsRef))
	var coords []*pointWithTime
	for _, c := range coordsRef {
		// cast to known struct
		var cval *coordinateValue
		c.DataTo(&cval)

		// convert to geo package
		point := convertToGeoJson(cval)

		if len(coords) > 0 && point.separation(coords[len(coords)-1]) < PRECISION {
			// basically, we want to ignore periods where the van is sat doing nothing
			// e.g. on the driveway, or in a carpark
			coords[len(coords)-1].t_to = point.t_from
			continue
		}

		coords = append(coords, point)
	}
	log.Printf("processing complete, coords left: %v", len(coords))
	return coords
}

func writeNewRecord(c []*pointWithTime, client *firestore.Client, ctx context.Context) {

	write := make(map[string]interface{})
	write["formatted"] = listToFirestoreFormat(c)

	today := fmt.Sprintf("%v", time.Now().Unix())
	log.Printf("Creating new record with ID: %v", today)
	_, err := client.Collection("daily-updates").Doc(today).Set(ctx, write)
	if err != nil {
		log.Fatal(err)
	}
	log.Printf("New record written")
}

func deleteCollection(ctx context.Context, client *firestore.Client,
	ref *firestore.CollectionRef, batchSize int) error {
	for {
		iter := ref.Limit(batchSize).Documents(ctx)
		numDeleted := 0
		batch := client.Batch()
		for {
			doc, err := iter.Next()
			if err == iterator.Done {
				break
			}
			if err != nil {
				return err
			}

			batch.Delete(doc.Ref)
			numDeleted++
		}
		if numDeleted == 0 {
			return nil
		}
		_, err := batch.Commit(ctx)
		if err != nil {
			return err
		}
	}
}

func removeOutdatedCoords(client *firestore.Client, ctx context.Context) {
	log.Println("Removing outdated coordindates records in Firestore")
	coords := client.Collection("coordinates")
	err := deleteCollection(ctx, client, coords, 100)
	if err != nil {
		log.Fatal(err)
	}
	return
}

func ProcessCoords(w http.ResponseWriter, r *http.Request, client *firestore.Client, ctx context.Context) {
	coords := readCoords(client, ctx)
	writeNewRecord(coords, client, ctx)
	removeOutdatedCoords(client, ctx)
}
