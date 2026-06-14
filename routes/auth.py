from flask import Blueprint,flash,render_template,redirect,url_for,session,request
from app.forms import registerForm,LoginForm
from app.models import User
from werkzeug.security import generate_password_hash,check_password_hash
from app import db

auth_bp = Blueprint('auth',__name__)

@auth_bp.route('/register',methods=['GET','POST'])
def register():
    form = registerForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        hashed_password = generate_password_hash(password)
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already registered')
            return render_template('register.html',form=form)
        new_user = User(username=username,email=email,password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration Successful','success')
        return redirect(url_for('auth.login'))
    return render_template('register.html',form=form)

@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print("Validation Passed")
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password,password):
            session['user_id'] = user.id
            flash('Login Successful','success')
            return redirect(url_for('notes.view_notes'))
        flash('Invalid username or password')
    return render_template('login.html',form=form)

@auth_bp.route('/user')
def user():
    user = User.query.all()
    return render_template('user.html',user=user)


