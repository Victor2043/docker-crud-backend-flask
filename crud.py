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
    conn.commit()
    conn.close()
    return data

def insert(jsonData):
    conn = sqlite3.connect('carros.db')
    cursor = conn.cursor()
    return jsonData
    # cursor.execute("INSERT INTO carros (modelo, marca, cor, placa) VALUES (? , ?, ?, ?)",
    # (jsonData['modelo'], jsonData['marca'], jsonData['cor'], jsonData['placa']))

def update(jsonData):
    cursor = cursor_DB()
    return jsonData["modelo"]
    # cursor.execute("""
    # UPDATE carros (modelo, marca, cor, placa)
    # SET modelo='?', 'Mitsubishi', 'preto', 'FPS-1512')
    # """)

def delete():
    cursor = cursor_DB()
    # cursor.execute("""
    # DELETE FROM carros (modelo, marca, cor, placa)
    # WHERE ('Lancer', 'Mitsubishi', 'preto', 'FPS-1512')
    # """)



