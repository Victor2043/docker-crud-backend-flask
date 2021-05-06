from flask import Flask, jsonify, request
import json
import crud

app = Flask(__name__)

@app.route('/get', methods=['GET'])
def get():
    jsonData = crud.get()
    response = jsonify(message=jsonData)   
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/insert', methods=['Post'])
def insert():
    jsonData = request.data
    crud.insert(jsonData)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return jsonData

@app.route('/update', methods=['PUT'])
def update():
    jsonData = request.data
    crud.update(jsonData)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return jsonData


@app.route('/delete', methods=['DELETE'])
def delete():
    jsonData = request.data
    response.headers.add("Access-Control-Allow-Origin", "*")
    return jsonData



if __name__ == '__main__':
    app.run(debug=False)