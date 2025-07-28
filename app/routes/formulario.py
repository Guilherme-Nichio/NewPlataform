from flask import render_template, request, redirect, session, url_for
import sqlite3

def register_formulario_routes(app):

    @app.route('/formulario/<form_id>/etapa1', methods=['GET', 'POST'])
    def formulario_etapa1(form_id):
        if request.method == 'POST':
            nome = request.form['nome']
            telefone = request.form['telefone']

            session['form_id'] = form_id
            session['nome'] = nome
            session['telefone'] = telefone

            with sqlite3.connect('db.sqlite3') as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT id FROM respostas
                    WHERE formulario_id=? AND nome=? AND telefone=?
                """, (form_id, nome, telefone))
                resposta = cursor.fetchone()

            if resposta:
                return redirect(f'/formulario/{form_id}/confirmar-substituicao')
            else:
                return redirect(f'/formulario/{form_id}/Session1')
        # Aqui você pode substituir pelo render_template do seu formulário etapa1
        return '''
            <h2>Identifique-se</h2>
            <form method="post">
                Nome: <input name="nome"><br>
                Telefone: <input name="telefone"><br>
                <button type="submit">Próxima etapa</button>
            </form>
        '''

    @app.route('/formulario/<form_id>/confirmar-substituicao', methods=['GET', 'POST'])
    def confirmar_substituicao(form_id):
        if request.method == 'POST':
            acao = request.form.get('acao')
            if acao == 'sim':
                return redirect(f'/formulario/{form_id}/Session1')
            else:
                session.clear()
                return "Resposta não foi alterada."
        # Pode trocar por template real de confirmação
        return '''
            <h2>Você já respondeu este formulário</h2>
            <p>Deseja responder novamente e substituir a resposta anterior?</p>
            <form method="post">
                <button type="submit" name="acao" value="sim">Sim, quero atualizar</button>
                <button type="submit" name="acao" value="nao">Não</button>
            </form>
        '''

    @app.route('/formulario/<form_id>/etapa2', methods=['GET', 'POST'])
    def formulario_etapa2(form_id):
        if request.method == 'POST':
            nome = session.get('nome')
            telefone = session.get('telefone')
            r1 = request.form['r1']
            r2 = request.form['r2']
            r3 = request.form['r3']
            r4 = request.form['r4']
            r5 = request.form['r5']

            with sqlite3.connect('db.sqlite3') as conn:
                c = conn.cursor()
                c.execute("""
                    DELETE FROM respostas
                    WHERE formulario_id=? AND nome=? AND telefone=?
                """, (form_id, nome, telefone))
                c.execute("""
                    INSERT INTO respostas (formulario_id, nome, telefone, r1, r2, r3, r4, r5)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (form_id, nome, telefone, r1, r2, r3, r4, r5))
                conn.commit()

            session.clear()
            return "<h3>Resposta atualizada com sucesso!</h3>"
        return render_template('form.html')

    # Sessões 1 a 5 seguem mesma lógica, só salvando na sessão e renderizando o template correspondente
    @app.route('/formulario/<form_id>/Session1', methods=['GET', 'POST'])
    def formulario_SessionOne(form_id):
        if not session.get('nome'):
            return redirect(f'/formulario/{form_id}/etapa1')
        if request.method == 'POST':
            session['r1'] = request.form['S1R1']
            session['r2'] = request.form['S1R2']
            session['r3'] = request.form['S1R3']
            session['r4'] = request.form['S1R4']
            session['r5'] = request.form['S1R5']
            return redirect(f'/formulario/{form_id}/Session2')
        return render_template('sectionOne.html')

    @app.route('/formulario/<form_id>/Session2', methods=['GET', 'POST'])
    def formulario_SessionTwo(form_id):
        if not session.get('nome'):
            return redirect(f'/formulario/{form_id}/etapa1')
        if request.method == 'POST':
            session['r6'] = request.form['S2R1']
            session['r7'] = request.form['S2R2']
            session['r8'] = request.form['S2R3']
            session['r9'] = request.form['S2R4']
            return redirect(f'/formulario/{form_id}/Session3')
        return render_template('sectionTwo.html')

    @app.route('/formulario/<form_id>/Session3', methods=['GET', 'POST'])
    def formulario_SessionThree(form_id):
        if not session.get('nome'):
            return redirect(f'/formulario/{form_id}/etapa1')
        if request.method == 'POST':
            session['r10'] = request.form['S3R1']
            session['r11'] = request.form['S3R2']
            session['r12'] = request.form['S3R3']
            session['r13'] = request.form['S3R4']
            return redirect(f'/formulario/{form_id}/Session4')
        return render_template('sectionThree.html')

    @app.route('/formulario/<form_id>/Session4', methods=['GET', 'POST'])
    def formulario_SessionFour(form_id):
        if not session.get('nome'):
            return redirect(f'/formulario/{form_id}/etapa1')
        if request.method == 'POST':
            session['r14'] = request.form['S4R1']
            session['r15'] = request.form['S4R2']
            session['r16'] = request.form['S4R3']
            session['r17'] = request.form['S4R4']
            session['r18'] = request.form['S4R5']
            session['r19'] = request.form['S4R6']
            return redirect(f'/formulario/{form_id}/Session5')
        return render_template('sectionFour.html')

    @app.route('/formulario/<form_id>/Session5', methods=['GET', 'POST'])
    def formulario_SessionFive(form_id):
        if request.method == 'POST':
            session['r20'] = request.form['S5R1']
            session['r21'] = request.form['S5R2']
            session['r22'] = request.form['S5R3']

            respostas = [session.get(f"r{i}") for i in range(1, 23)]
            if None in respostas:
                return redirect(f'/formulario/{form_id}/Session1')

            resultado = calcular_tipo_pele(respostas)

            nome = session.get('nome')
            telefone = session.get('telefone')

            conn = sqlite3.connect('db.sqlite3')
            c = conn.cursor()

            c.execute('''
                INSERT INTO respostas (
                    formulario_id, nome, telefone,
                    S1Q1, S1Q2, S1Q3, S1Q4, S1Q5,
                    S2Q1, S2Q2, S2Q3, S2Q4,
                    S3Q1, S3Q2, S3Q3, S3Q4,
                    S4Q1, S4Q2, S4Q3, S4Q4, S4Q5, S4Q6,
                    S5Q1, S5Q2, S5Q3,
                    O_D, S_R, P_N, W_T
                ) VALUES (?, ?, ?,
                          ?, ?, ?, ?, ?,
                          ?, ?, ?, ?,
                          ?, ?, ?, ?,
                          ?, ?, ?, ?, ?, ?,
                          ?, ?, ?,
                          ?, ?, ?, ?)
            ''', (
                form_id, nome, telefone,
                *respostas,
                resultado_valor(resultado['O x D']),
                resultado_valor(resultado['S x R']),
                resultado_valor(resultado['P x N']),
                resultado_valor(resultado['W x T'])
            ))

            conn.commit()
            conn.close()

            return render_template('result.html', resultado=resultado)

        return render_template('sectionFive.html')

    def resultado_valor(resultado_str):
        if "Oleosa" in resultado_str or "O" in resultado_str:
            return 1
        if "Seca" in resultado_str or "D" in resultado_str:
            return 2
        if "Sensível" in resultado_str or "S" in resultado_str:
            return 1
        if "Resistente" in resultado_str or "R" in resultado_str:
            return 2
        if "Pigmentada" in resultado_str or "P" in resultado_str:
            return 1
        if "Não-pigmentada" in resultado_str or "N" in resultado_str:
            return 2
        if "Enrugada" in resultado_str or "W" in resultado_str:
            return 1
        if "Firme" in resultado_str or "T" in resultado_str:
            return 2
        return None

    def calcular_tipo_pele(respostas):
        pontuacoes = [ord(r.lower()) - ord('a') + 1 for r in respostas]

        O_D = sum(pontuacoes[0:5])
        S_R = sum(pontuacoes[5:9])
        P_N = sum(pontuacoes[9:13])
        W_T = sum(pontuacoes[13:19])
        hidratacao = pontuacoes[19:22]

        tipo_OD = "Oleosa (O)" if O_D >= 13 else "Seca (D)"
        tipo_SR = "Sensível (S)" if S_R >= 9 else "Resistente (R)"
        tipo_PN = "Pigmentada (P)" if P_N >= 11 else "Não-pigmentada (N)"
        tipo_WT = "Enrugada (W)" if W_T >= 15 else "Firme (T)"

        qtd_a = hidratacao.count(1)
        qtd_b = hidratacao.count(2)
        tipo_hidratacao = "Desidratada" if qtd_a > qtd_b else "Equilibrada"

        return {
            'O x D': tipo_OD,
            'S x R': tipo_SR,
            'P x N': tipo_PN,
            'W x T': tipo_WT,
            'Hidratação': tipo_hidratacao
        }
