from flask import Flask, render_template, request, redirect
import sqlite3
import os
from datetime import datetime


app = Flask(__name__)
#DATABASE = 'database.db'

DATABASE = os.environ.get('DB_PATH', 'data/database.db')
LOGFILE_PATH = os.environ.get('LOGFILE_PATH', 'data/registro.log')
APP_ENV = os.environ.get('APP_ENV', 'development')

def init_db():
    os.makedirs(os.path.dirname(DATABASE), exist_ok=True)

    with sqlite3.connect(DATABASE) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS registros (
                rtc TEXT NOT NULL,
                nombre TEXT NOT NULL,
                fechaini DATE NOT NULL,
                fechafin DATE NOT NULL,
                scrum TEXT NOT NULL,
                estado TEXT NOT NULL
            );
        ''')
        print("Base de datos verificada o creada.")



#    if not os.path.exists(DATABASE):
#        with sqlite3.connect(DATABASE) as conn:
#            conn.execute('''
#                CREATE TABLE registros (
#                    rtc TEXT NOT NULL,
#                    nombre TEXT NOT NULL,
#                    fechaini DATE NOT NULL,
#                    fechafin DATE NOT NULL,
#                    scrum TEXT NOT NULL,
#                    estado TEXT NOT NULL
#                );
#            ''')
#            print("Base de datos creada.")


@app.route('/')
def index():
    conn = sqlite3.connect(DATABASE)
    registros = conn.execute("SELECT * FROM registros").fetchall()
    conn.close()
    return render_template('index.html', registros=registros)

@app.route('/agregar', methods=['POST'])
def agregar():
    rtc = request.form['rtc']
    nombre = request.form['nombre']
    fechaini = request.form['fechaini']
    fechafin = request.form['fechafin']
    scrum = request.form['scrum']
    estado = request.form['estado']


    conn = sqlite3.connect(DATABASE)
    conn.execute("INSERT INTO registros (rtc, nombre, fechaini, fechafin, scrum, estado) VALUES (?, ?, ?, ?, ?, ?)", (rtc, nombre, fechaini, fechafin, scrum, estado))
    conn.commit()
    conn.close()


    with open(LOGFILE_PATH, 'a') as f:
        f.write(f"[{datetime.now()}] Nuevo registro: {rtc} - {nombre} - {fechaini} - {fechafin} - {scrum} - {estado}\n")

    return redirect('/')

if __name__ == '__main__':
    print(f"Entorno de aplicación: {APP_ENV}")
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)
