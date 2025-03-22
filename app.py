from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!!!!!!'

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