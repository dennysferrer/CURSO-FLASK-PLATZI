import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

DB_FILE_PATH = os.path.join(
    os.path.dirname(__name__),
    "notes.sqlite"
)

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_FILE_PATH}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    #created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    def __repr__(self):
        return f'<Note {self.id}: {self.title}>'

with app.app_context():
    db.create_all() 

@app.route('/')
def home():
    #role = "admin"
    notas = Note.query.all()
    return render_template('home.html', notas=notas)

@app.route('/about')
def about():
    return 'Esto es una app de rutas'

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return "Formulario enviado",201
    return "Pagina de contacto"

@app.route('/api/info')
def api_info():
    data = {
        "name": "Notes App",
        "version": "1.0.0",
        "author": "Dennys Ferrer"
    }
    return jsonify(data),200

@app.route('/confirmacion')
def confirmation():
    nota = request.args.get('nota')
    return render_template('confirmation.html', nota=nota)

@app.route('/crear', methods=['GET', 'POST'])
def create_note():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        nota = Note(title=title, content=content)
        db.session.add(nota)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('note_form.html')

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def edit_note(id):
    nota = Note.query.get_or_404(id)
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        nota.title = title
        nota.content = content
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit_form.html', nota = nota)

    
    
    
