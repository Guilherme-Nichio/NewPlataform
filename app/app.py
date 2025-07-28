from flask import Flask
from models import init_db

app = Flask(__name__)
app.secret_key = 'sua_chave_super_secreta_aqui'  
from routes.auth import register_auth_routes
from routes.admin import register_admin_routes , criar_admin
from routes.dashboard import register_dashboard_routes
from routes.formulario import register_formulario_routes

register_auth_routes(app)
register_admin_routes(app)
register_dashboard_routes(app)
register_formulario_routes(app)

if __name__ == '__main__':
    criar_admin()
    app.run(debug=True)
