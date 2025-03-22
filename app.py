from flask import Flask, request, jsonify, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    role = "admin"
    notas = ["Nota 1", "Nota 2", "Nota 3"]
    return render_template('home.html', role=role, notas=notas)

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
    return "Prueba"

@app.route('/crear', methods=['GET', 'POST'])
def create_note():
    if request.method == 'POST':
        nota = request.form.get('nota')
        return redirect(url_for('confirmation', nota=nota))
    return render_template('note_form.html')
    
    
    
