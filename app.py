import sqlite3
from datetime import datetime

def create_table():
    conn = sqlite3.connect('imc.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS pacientes
                      (id INTEGER PRIMARY KEY,
                       nome TEXT,
                       altura REAL,
                       peso REAL,
                       imc REAL,
                       data TEXT)''')
    conn.commit()
    conn.close()

create_table()

def calcular_imc(nome, altura, peso):
    imc = peso / (altura ** 2)
    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect('imc.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO pacientes (nome, altura, peso, imc, data) VALUES (?, ?, ?, ?, ?)', 
                   (nome, altura, peso, imc, data))
    conn.commit()
    conn.close()
    return imc

nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura em metros (ex: 1.75): "))
peso = float(input("Digite seu peso em kg (ex: 70): "))

imc = calcular_imc(nome, altura, peso)
print(f"{nome}, seu IMC é {imc:.2f}")

def consultar_dados():
    conn = sqlite3.connect('imc.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM pacientes')
    rows = cursor.fetchall()
    conn.close()
    for row in rows:
        print(row)

consultar_dados()
