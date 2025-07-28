from flask import render_template, redirect, session, jsonify, url_for, request
import sqlite3
import uuid

def register_dashboard_routes(app):

    @app.route('/dashboard')
    def dashboard():
        if 'user_id' not in session:
            return redirect('/login')
        with sqlite3.connect('db.sqlite3') as conn:
            formularios = conn.execute("SELECT id FROM formularios WHERE user_id=?", (session['user_id'],)).fetchall()
            respostas = []
            for f in formularios:
                r = conn.execute("SELECT * FROM respostas WHERE formulario_id=?", (f[0],)).fetchall()
                respostas.extend(r)
        return render_template('dashboard.html', respostas=respostas)

    @app.route('/api/gerar-link', methods=['POST'])
    def api_gerar_link():
        form_id = str(uuid.uuid4())
        with sqlite3.connect('db.sqlite3') as conn:
            conn.execute("INSERT INTO formularios (id, user_id) VALUES (?, ?)", (form_id, session['user_id']))
        link = url_for('formulario_etapa1', form_id=form_id, _external=True)
        return jsonify({"link": link})
