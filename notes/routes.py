from flask import request, render_template, redirect, url_for, blueprints, flash
from models import Note, db

notes_bp = blueprints.Blueprint('notes', __name__)

@notes_bp.route('/')
def home():
    #role = "admin"
    notas = Note.query.all()
    return render_template('home.html', notas=notas)

@notes_bp.route('/crear', methods=['GET', 'POST'])
def create_note():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        nota = Note(title=title, content=content)
        db.session.add(nota)
        db.session.commit()
        flash('Nota creada con éxito', 'success')
        return redirect(url_for('notes.home'))
    return render_template('note_form.html')

@notes_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def edit_note(id):
    nota = Note.query.get_or_404(id)
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        nota.title = title
        nota.content = content
        db.session.commit()
        return redirect(url_for('notes.home'))
    return render_template('edit_form.html', nota = nota)


@notes_bp.route('/eliminar/<int:id>', methods=['POST'])
def delete_note(id):
    nota = Note.query.get_or_404(id)
    db.session.delete(nota)
    db.session.commit()
    return redirect(url_for('notes.home'))
    
