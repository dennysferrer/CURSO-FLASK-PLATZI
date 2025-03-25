from flask import Flask, request
from models import db
from config import Config
from notes.routes import notes_bp

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(notes_bp)
db.init_app(app)
with app.app_context():
    db.create_all()

@app.route('/about')
def about():
    return 'Esto es una app de rutas'

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return "Formulario enviado",201
    return "Pagina de contacto"



