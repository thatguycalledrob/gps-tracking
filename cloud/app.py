import json
import os
import hashlib
import uuid
from typing import Tuple, Union

from flask import Flask, request, jsonify
from firebase_admin import credentials, firestore, initialize_app

from gps_utils import logger # custom logger

# Initialize Flask app
app = Flask(__name__)
port = int(os.environ.get('PORT', 8080))

# Initialize Firestore DB
cred = credentials.Certificate('key.json')
default_app = initialize_app(cred)
db = firestore.client()
todo_ref = db.collection('todos')

# secret setup - read from file
with open(os.path.abspath(os.path.join(__file__, '..', 'secret.txt'))) as f:
    secret = hashlib.sha1(f.read().strip().encode()).hexdigest()

# Setup consts
AUTH_HEADER = 'Authorization'


def server_error(e: Exception):
    # todo: log the error instead of sending back to client.
    # todo: Maybe switch on e and return proper error code?
    return f"An Error Occurred. Stacktrace: {e}", 500


@app.before_request
def before_request() -> Union[Tuple[str, int], None]:
    h = request.headers.get(AUTH_HEADER, '')
    if not h:
        return jsonify({"error": "Authentication failed. Auth header not found"}), 401
    hashed = hashlib.sha1(h.encode()).hexdigest()
    if hashed != secret:
        logger.warn("attempted create with auth header: ", h)
        return jsonify({"error": "Authentication failed. secret mismatch"}), 401
    else:
        logger.info("successful authenticated required made")


@app.route('/position', methods=['POST'])
def create() -> Tuple[str, int]:
    try:
        id = str(uuid.uuid1().hex)  # basic uuid
        if not isinstance(request.json, dict):
            logger.warn("Written new document.", id=id, data=request.json)
            return jsonify({"malformed request": "request body is not in json format"}), 400
        todo_ref.document(id).set(request.json)
        logger.debug("Written new document.", id=id, data=request.json)
        return jsonify({"id": id}), 201
    except Exception as e:
        return server_error(e)


@app.route('/positions', methods=['GET'])
def readall() -> Tuple[str, int]:
    try:
        all_todos = [doc.to_dict() for doc in todo_ref.stream()]
        return jsonify(all_todos), 200
    except Exception as e:
        return server_error(e)


@app.route('/positions/<position_id>', methods=['GET'])
def readone(position_id: str) -> Tuple[str, int]:
    try:
        todo = todo_ref.document(position_id).get()
        return jsonify(todo.to_dict()), 200
    except Exception as e:
        return server_error(e)


if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=port)
