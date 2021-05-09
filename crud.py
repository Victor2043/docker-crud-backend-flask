import sqlite3
import json

def cursor_DB():
    conn = sqlite3.connect('carros.db')
    cursor = conn.cursor()
    return cursor

def get():
    conn = sqlite3.connect('carros.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM carros""")
    data = cursor.fetchall()
    jsonData = {}
    jsonData['carros'] = []
    for i in range(0, len(data)):
        jsonData['carros'].append({
            'id': data[i][0],
            'modelo': data[i][1],
            'marca': data[i][2],
            'cor': data[i][3],
            'placa': data[i][4]
            })
    #data = json.dumps(data)

    conn.commit()
    conn.close()
    return jsonData

def insert(jsonData):
    conn = sqlite3.connect('carros.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO carros (modelo, marca, cor, placa) VALUES (? , ?, ?, ?)",
    (jsonData['modelo'], jsonData['marca'], jsonData['cor'], jsonData['placa']))
    conn.commit()
    conn.close()

def update(jsonData):
    conn = sqlite3.connect('carros.db')
    cursor = conn.cursor()
    cursor.execute("""UPDATE carros SET modelo = ? ,
     marca = ? , cor = ?,  placa = ?  WHERE id = """ + jsonData['id'],
    (jsonData['modelo'], jsonData['marca'], jsonData['cor'], jsonData['placa']))
    conn.commit()
    conn.close()

def delete(id):
    conn = sqlite3.connect('carros.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM carros where id = " + id)
    conn.commit()
    conn.close()