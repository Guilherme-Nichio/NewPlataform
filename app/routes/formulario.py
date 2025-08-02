from flask import render_template, request, redirect, session, url_for, jsonify
import sqlite3
import json

def register_formulario_routes(app):

    @app.route('/formulario/<form_id>', methods=['GET', 'POST'])
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
                return redirect(f'/formulario/{form_id}/Skin')
        # Aqui você pode substituir pelo render_template do seu formulário etapa1
        return '''
            <h2>Identifique-se</h2>
            <form method="post">
                Nome: <input name="nome"><br>
                Telefone: <input name="telefone"><br>
                <button type="submit">Próxima etapa</button>
            </form>
        '''

    @app.route('/formulario/<form_id>/Skin', methods=['GET','POST'])
    def quiz_skin(form_id):
        if request.method == 'POST':
            dados = request.get_json()
            # Filtra só chaves numéricas (respostas)
            respostas_filtradas = {k: v for k, v in dados.items() if k.isdigit()}

            # Garante lista ordenada e só letras válidas ('a' a 'd')
            respostas = []
            for i in range(1, 23):
                r = respostas_filtradas.get(str(i), 'a')  # padrão 'a' para evitar erro
                if isinstance(r, str) and len(r) == 1 and r.lower() in ['a','b','c','d']:
                    respostas.append(r.lower())
                else:
                    respostas.append('a')  # default

            def calcular_tipo_pele(respostas):
                pontuacoes = [ord(r) - ord('a') + 1 for r in respostas]

                O_D = sum(pontuacoes[0:5])
                S_R = sum(pontuacoes[5:9])
                P_N = sum(pontuacoes[9:13])
                W_T = sum(pontuacoes[13:19])
                hidratacao = pontuacoes[19:22]

                tipo_OD = "Oleosa (O)" if O_D >= 13 else "Seca (D)"
                tipo_SR = "Sensível (S)" if S_R >= 9 else "Resistente (R)"
                tipo_PN = "Pigmentada (P)" if P_N >= 11 else "Não-pigmentada (N)"
                tipo_WT = "Enrugada (W)" if W_T >= 15 else "Firme (T)"

                tipo_OD2 = "O" if O_D >= 13 else "D"
                tipo_SR2 = "S" if S_R >= 9 else "R"
                tipo_PN2 = "P" if P_N >= 11 else "N"
                tipo_WT2 = "W" if W_T >= 15 else "T"

                combined_string = f"{tipo_OD2} {tipo_SR2} {tipo_PN2} {tipo_WT2}"

                qtd_a = hidratacao.count(1)
                qtd_b = hidratacao.count(2)
                tipo_hidratacao = "Desidratada" if qtd_a > qtd_b else "Equilibrada"

                return {
                    'O x D': tipo_OD,
                    'S x R': tipo_SR,
                    'P x N': tipo_PN,
                    'W x T': tipo_WT,
                    'Hidratação': tipo_hidratacao,
                    'Tipo_de_pele': combined_string,
                    'tipo_OD2': tipo_OD2,
                    'tipo_SR2': tipo_SR2,
                    'tipo_PN2': tipo_PN2,
                    'tipo_WT2': tipo_WT2
                }

            resultado = calcular_tipo_pele(respostas)

            nome = session.get('nome')
            telefone = session.get('telefone')   

            with sqlite3.connect('db.sqlite3') as conn:
                c = conn.cursor()
                c.execute('''INSERT INTO respostas (formulario_id, nome, telefone, respostas_json)
                            VALUES (?, ?, ?, ?)''',
                        (form_id, nome, telefone, json.dumps(respostas_filtradas)))
                conn.commit()
            return jsonify({"mensagem": "Respostas enviadas com sucesso!", 'resultado': resultado})

        return render_template('formulario.html', form_id=form_id)

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
