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

@app.route('/insert', methods=['Post'])
def insert():
    jsonData = request.data
    
    response = jsonify(cars=jsonData) 
    #data = crud.insert(response) 
    response.headers.add("Access-Control-Allow-Origin", "*")
    dataJson = json.dumps(response)
    return str(dataJson)

@app.route('/update', methods=['PUT'])
def update():
    jsonData = request.data
    data = crud.insert(jsonData)
    response = jsonify(cars=data)  
    response.headers.add("Access-Control-Allow-Origin", "*")
    return jsonData


@app.route('/delete', methods=['DELETE'])
def delete():
    jsonData = request.data
    response.headers.add("Access-Control-Allow-Origin", "*")
    return data



if __name__ == '__main__':
    app.run(debug=False)