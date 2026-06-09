from flask import Blueprint,flash,render_template,redirect,url_for,session,request
from app.models import Note
from app import db

notes_bp = Blueprint('notes',__name__)

@notes_bp.route('/create',methods = ['GET','POST'])
def create_note():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        new_note = Note(title = title,content = content,user_id = session['user_id'])
        db.session.add(new_note)
        db.session.commit()
        flash('Notes created Successfully')
        return redirect(url_for('notes.view_notes'))
    return render_template('create_notes.html')

@notes_bp.route('/view_notes')
def view_notes():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    notes = Note.query.filter_by(user_id = session['user_id']).all()
    return render_template('view_notes.html',notes = notes)
