
from werkzeug.security import generate_password_hash
import sqlite3
from datetime import datetime, timedelta
from openpyxl import load_workbook

def admin():
     with sqlite3.connect('db.sqlite3') as conn:
            formularios = conn.execute("SELECT id FROM formularios").fetchall()
            respostas = []
            for f in formularios:
                r = conn.execute("SELECT * FROM respostas WHERE formulario_id=?", (f[0],)).fetchall()
                respostas.extend(r)
            return respostas