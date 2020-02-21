# taken from:
# https://cloud.google.com/community/tutorials/building-flask-api-with-cloud-firestore-and-deploying-to-cloud-run
import os
from flask import Flask, request, jsonify
from firebase_admin import credentials, firestore, initialize_app
import hashlib
from gps_utils import logger

# Initialize Flask app
app = Flask(__name__)
port = int(os.environ.get('PORT', 8080))

# Initialize Firestore DB
cred = credentials.Certificate('key.json')
default_app = initialize_app(cred)
db = firestore.client()
todo_ref = db.collection('todos')

# secret setup
secret = hashlib.sha1("lucy".encode()).hexdigest()

# Setup consts
AUTH_HEADER = 'Authorization'


@app.before_request
def before_request():
    hash = hashlib.sha1(request.headers.get(AUTH_HEADER, '').encode()).hexdigest()
    if hash != secret:
        logger.warn("attempted create with auth header: ", request.headers.get('auth', ''))
        return jsonify({"error": "Authentication failed. Auth field required"}), 401


@app.route('/add', methods=['POST'])
def create():
    try:
        id = request.json['id']
        todo_ref.document(id).set(request.json.get('data', {}))
        return jsonify({"success": True}), 201

    except Exception as e:
        return f"An Error Occured: {e}"


@app.route('/list', methods=['GET'])
def read():
    try:
        todo_id = request.args.get('id')
        if todo_id:
            todo = todo_ref.document(todo_id).get()
            return jsonify(todo.to_dict()), 200
        else:
            all_todos = [doc.to_dict() for doc in todo_ref.stream()]
            return jsonify(all_todos), 200

    except Exception as e:
        return f"An Error Occured: {e}"


if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=port)
