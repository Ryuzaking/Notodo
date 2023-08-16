from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from bson.json_util import dumps
import json

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})  # Especifica el origen permitido para /api/*

# Conexión a MongoDB Atlas
atlas_username = 'va1234'
atlas_password = 'hope123'
cluster_name = 'cluster0.dauozg0.mongodb.net/terra'
atlas_client = MongoClient(f'mongodb+srv://{atlas_username}:{atlas_password}@{cluster_name}?retryWrites=true&w=majority')

db = atlas_client.terra  # Reemplaza 'terra' con el nombre de tu base de datos
collection = db.datos

@app.route('/api/data', methods=['GET'])
def get_data():
    # Ordena por _id en orden descendente (último documento) y limita a 1 resultado
    data = collection.find().sort([("_id", -1)]).limit(4)
    data_json = dumps(data)
    # Load the JSON string into a Python list of dictionaries
    data_list = json.loads(data_json)
    # Return the formatted JSON response
    return jsonify(data_list)  # Return the JSON-formatted data

if __name__ == '__main__':
    app.run(debug=True)
