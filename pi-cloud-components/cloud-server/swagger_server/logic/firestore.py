from datetime import datetime

import uuid0
from typing import List, Dict, Union

from firebase_admin import credentials, firestore, initialize_app
from google.cloud.firestore import Client, CollectionReference

# Initialize Firestore DB
from swagger_server.logic.stackdriver_logger import slogger
from swagger_server.models import Coordinate

cred = credentials.Certificate('key.json')
default_app = initialize_app(cred)
db: Client = firestore.client()
coords_ref: CollectionReference = db.collection('coordinates')


# next up: https://firebase.google.com/docs/firestore/query-data/queries#python
# maybe we want a "processed" field?
def getEntry(c: Coordinate) -> Dict[str, Union[float, firestore.firestore.GeoPoint, datetime]]:
    return {
        'timestamp': datetime.fromtimestamp(c.time),
        'geostamp': firestore.firestore.GeoPoint(latitude=c.lat, longitude=c.long),
        'altitude': c.alt,
        'satellites': c.sats
    }


def add_coordinates(cc: List[Coordinate]) -> None:
    slogger.info(f"Received Coordinates. number: {len(cc)}")
    for coord in cc:
        add_coordinate(coord)


def add_coordinate(c: Coordinate) -> None:
    try:

        uid = str(uuid0.generate())  # basic uuid0, provides time ordered ids, over uuid's random
        entry = getEntry(c)

        coords_ref.document(document_id=uid).set(entry)
        slogger.debug("Written new coordinate to firestore.", id=id, data=entry)

    except Exception as e:

        slogger.error(f"Exception while writing new coordinate", error=e)
        pass  # error to the logs is good enough for now
