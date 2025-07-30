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

            S1Q1 CHAR,
            S1Q2 CHAR,
            S1Q3 CHAR,
            S1Q4 CHAR,
            S1Q5 CHAR,

            S2Q1 CHAR,
            S2Q2 CHAR,
            S2Q3 CHAR,
            S2Q4 CHAR,

            S3Q1 CHAR,
            S3Q2 CHAR,
            S3Q3 CHAR,
            S3Q4 CHAR,

            S4Q1 CHAR,
            S4Q2 CHAR,
            S4Q3 CHAR,
            S4Q4 CHAR,
            S4Q5 CHAR,
            S4Q6 CHAR,

            S5Q1 CHAR,
            S5Q2 CHAR,
            S5Q3 CHAR,
            O_D INTEGER,
            S_R INTEGER,
            P_N INTEGER,
            W_T INTEGER,

            FOREIGN KEY(formulario_id) REFERENCES formularios(id)
        )''')
