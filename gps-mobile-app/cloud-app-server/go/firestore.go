package swagger

import (
	"context"
	"fmt"
	"log"
	"net/http"
	"os"

	"cloud.google.com/go/firestore"
	firebase "firebase.google.com/go"
	"google.golang.org/api/option"

	"github.com/gorilla/mux"
	"github.com/thatguycalledrob/gps-tracking/cloud-processing/process-gps-points/logic"
)


func setupFirestore() *firestore.Client {
	log.Println("Initalizing new firestore client")

	ctx = context.Background()
	sa := option.WithCredentialsFile("/key.json")

	app, err := firebase.NewApp(ctx, nil, sa); if err != nil {
		log.Fatal(err)
	}

	c, err := app.Firestore(ctx); if err != nil {
		log.Fatal(err)
	}

	return c
}
