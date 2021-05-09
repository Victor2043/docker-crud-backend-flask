from flask import Flask, jsonify, request
import json
import crud
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/get', methods=['GET'])
def get():
    jsonData = crud.get()
    response = jsonify(cars=jsonData)   
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response




@app.route('/insert', methods=['POST'])
@cross_origin()
def insert():
    jsonData = json.loads(request.data)
    crud.insert(jsonData)
    response = jsonify(message="Carro inserido") 
    return response

@app.route('/update', methods=['PUT'])
@cross_origin()
def update():
    jsonData = json.loads(request.data)
    crud.update(jsonData)
    response = jsonify(message="Carro atualizado") 
    return response

@app.route('/delete/<id>', methods=['DELETE'])
def delete(id):
    crud.delete(id)
    response = jsonify(message="Carro excluido") 
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == '__main__':
    app.run(debug=False)