import sqlite3

conn = sqlite3.connect('carros.db')

cursor = conn.cursor()

cursor.execute("""
INSERT INTO carros (modelo, marca, cor, placa)
VALUES ('Lancer', Mitsubishi, 'preto', 'FPS-1512)
""")

cursor.execute("""
INSERT INTO carros (modelo, marca, cor, placa)
VALUES ('Tracker', Chevrolet, 'branco', 'COD-3412)
""")

cursor.execute("""
INSERT INTO carros (modelo, marca, cor, placa)
VALUES ('Kicks', Nissan , 'vermelho', 'GOW-6632)
""")

conn.commit()

print('Dados inseridos com sucesso.')


conn.close()