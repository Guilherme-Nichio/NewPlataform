from flask import render_template, request, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
from BancoFunctions import *

def register_auth_routes(app):
    # Rota de logout
    @app.route('/logout')
    def logout():
        session.clear()
        return redirect('/login')


    # Rota de logout
    @app.route('/')
    def Homepage():
        return render_template('homePage.html')
    
    # Rota de login
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            email = request.form['email']
            senha = request.form['senha']
            user = login_auth(email)
            if user and check_password_hash(user[3], senha):
                session['user_id'] = user[0]
                session['email'] = user[1]
                session['tipo'] = user[5]
                session['nome'] = user[2]
                if user[5] == 'admin':
                    return redirect('/admin')
                return redirect('/dashboard')
            return "Login inválido."
        return render_template('login.html')

    # Rota de registro
    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            email = request.form['email']
            senha = generate_password_hash(request.form['senha'])
            try:
                with sqlite3.connect('db.sqlite3') as conn:
                    conn.execute("INSERT INTO usuarios (email, senha) VALUES (?, ?)", (email, senha))
                return redirect('/login')
            except sqlite3.IntegrityError:
                return "Email já cadastrado."
        return render_template('register.html')

    # Rota para trocar senha
    @app.route('/trocar-senha', methods=['GET', 'POST'])
    def trocar_senha():
        if 'user_id' not in session:
            return redirect('/login')

        if request.method == 'POST':
            senha_atual = request.form['senha_atual']
            nova_senha = request.form['nova_senha']

            with sqlite3.connect('db.sqlite3') as conn:
                user = conn.execute("SELECT senha FROM usuarios WHERE id=?", (session['user_id'],)).fetchone()
                if not user or not check_password_hash(user[0], senha_atual):
                    return "Senha atual incorreta!"

                nova_hash = generate_password_hash(nova_senha)
                conn.execute("UPDATE usuarios SET senha=? WHERE id=?", (nova_hash, session['user_id']))
                conn.commit()

            return "Senha atualizada com sucesso!"

        return '''
        <h2>Trocar senha</h2>
        <form method="post">
            Senha atual: <input type="password" name="senha_atual"><br>
            Nova senha: <input type="password" name="nova_senha"><br><br>
            <button type="submit">Atualizar senha</button>
        </form>
        '''
