import json
import os
import hashlib
import uuid
from typing import Tuple, Union

from flask import Flask, request, jsonify
from firebase_admin import credentials, firestore, initialize_app

# Initialize Firestore DB
cred = credentials.Certificate('key.json')
default_app = initialize_app(cred)
db = firestore.client()
coords_ref = db.collection('coordinates')