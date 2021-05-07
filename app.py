from flask import Flask, jsonify, request
import json
import crud

app = Flask(__name__)

@app.route('/get', methods=['GET'])
def get():
    jsonData = crud.get()
    response = jsonify(cars=jsonData)   
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/insert', methods=['POST'])
def insert():
    jsonData = json.loads(request.data)
    crud.insert(jsonData)
    response = jsonify(message="carro inserico.") 
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/update', methods=['PUT'])
def update():
    jsonData = json.loads(request.data)
    crud.update(jsonData)
    response = jsonify(message="carro atualizado.") 
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/delete', methods=['DELETE'])
def delete():
    carId = json.loads(request.data)
    crud.delete(carId)
    response = jsonify(message=carId) 
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == '__main__':
    app.run(debug=False)