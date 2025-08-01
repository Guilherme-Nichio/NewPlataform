import sqlite3

def init_db():
    with sqlite3.connect('db.sqlite3') as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        email TEXT UNIQUE NOT NULL,
                        nome TEXT NOT NULL,
                        senha TEXT NOT NULL,
                        telefone TEXT NOT NULL,
                        tipo TEXT DEFAULT 'normal',
                        ativo INTEGER DEFAULT 1,
                        data_expiracao TEXT
                  )''')
        c.execute('''CREATE TABLE IF NOT EXISTS formularios (
                        id TEXT PRIMARY KEY,
                        user_id INTEGER,
                        FOREIGN KEY(user_id) REFERENCES usuarios(id))''')
        
        c.execute('''CREATE TABLE IF NOT EXISTS respostas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            formulario_id TEXT,
            nome TEXT,
            telefone TEXT,
            data_envio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            respostas_json TEXT,
            FOREIGN KEY(formulario_id) REFERENCES formularios(id)
        )''')

