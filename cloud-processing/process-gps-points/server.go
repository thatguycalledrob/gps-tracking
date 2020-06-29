package main

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

var ctx context.Context
var client *firestore.Client


func handleProcessCoords(w http.ResponseWriter, r *http.Request) {
	logic.ProcessCoords(w, r, client, ctx)
	
}

func getPort() string {
	p := os.Getenv("PORT")
	if p == "" {
		p = "8080"
	}
	return p
}

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

func setupServer() {
	r := mux.NewRouter().StrictSlash(true)
	r.HandleFunc("/", handleProcessCoords).Methods("POST")

	port := getPort()	
	log.Printf("Server listening on port %s", port)
	log.Fatal(http.ListenAndServe(fmt.Sprintf(":%s", port), r))
}

func main() {
	client = setupFirestore()
	defer client.Close()

	setupServer()
}
