# -*- coding: utf-8 -*-
"""
Created on Thu May  6 10:54:17 2021

@author: Victo
"""

from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/get', methods=['GET'])
def get():
    jsonData = {}
    jsonData['carros'] = []
    jsonData['carros'].append({
                'modelo': "Chevrolet Onix",
                'marca': "chevrolet",
                "cor":"laranja",
                "placa":"AFS-4123"
            })
    jsonData['carros'].append({
                'modelo': "Chevrolet Onix",
                'marca': "chevrolet",
                "cor":"laranja",
                "placa":"AFS-4123"
            })
    response = jsonify(message=jsonData)   
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/insert', methods=['Post'])
def insert():
    jsonData = request.data
    response.headers.add("Access-Control-Allow-Origin", "*")
    return jsonData

@app.route('/update', methods=['PUT'])
def update():
    jsonData = request.data
    response.headers.add("Access-Control-Allow-Origin", "*")
    return jsonData


@app.route('/delete', methods=['DELETE'])
def delete():
    jsonData = request.data
    response.headers.add("Access-Control-Allow-Origin", "*")
    return jsonData




if __name__ == '__main__':
    app.run(debug=False)