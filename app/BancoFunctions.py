import sqlite3
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash
from itertools import product
from collections import Counter


#FUNCAO DE ANCO DE DADOS DO ADM
def criar_adm():
    with sqlite3.connect('db.sqlite3') as conn:
        c = conn.cursor()
        admin = c.execute("SELECT * FROM usuarios WHERE tipo='admin'").fetchone()
        if not admin:
            senha_hash = generate_password_hash("admin123")  # senha padrão
            c.execute(
                    "INSERT INTO usuarios (email,nome, senha, telefone, tipo) VALUES (?, ?, ?, ?, ?)",
                    ("admin@admin.com","admin", senha_hash, "00000000", "admin")
            )
            conn.commit()    

def contarTipos_graph():
    with sqlite3.connect('db.sqlite3') as conn:
        rows = conn.execute("SELECT OxD, SxR, PxN, WxT FROM respostas").fetchall()
    
    tipos_respostas = [''.join(r) for r in rows]
    contagem = Counter(tipos_respostas)

    # Todos os 16 tipos possíveis
    oxd = ['O','D']
    sxr = ['S','R']
    pxn = ['P','N']
    wxt = ['W','T']
    todos_tipos = [''.join(p) for p in product(oxd, sxr, pxn, wxt)]
        # Garantir que todos os 16 tipos apareçam
    resultado = {t: contagem.get(t,0) for t in todos_tipos}
    return resultado

#ROTA DE AUTENTICAÇÃO - FUNCOES
def login_auth(email):
    with sqlite3.connect('db.sqlite3') as conn:
        user = conn.execute("SELECT * FROM usuarios WHERE email=?", (email,)).fetchone()
        return user