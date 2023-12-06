"""auth blueprint"""
from functools import wraps
from flask import (
    Blueprint, redirect, render_template, request, session
)
from wtforms import Form, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

from . import db

class LoginForm(Form):
    """login form"""
    username = StringField('Username', validators=[DataRequired(), Length(min=1, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=1, max=20)])
    submit = SubmitField('Login')

bp = Blueprint('auth', __name__)



def login_required(func):
    """check if user login"""
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if 'username' in session:
            print('username is', session['username'])
            return func(*args, **kwargs)
        return redirect('/login')
    return decorated_function

@bp.route("/")
@bp.route("/home")
@login_required
def hello_world():
    """home page"""
    return render_template('index.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    """user login"""
    if request.method == 'GET':
        return render_template('login.html')

    form = LoginForm(request.form)
    if not form.validate():
        return render_template('login.html', err_msg="Invalid input.", form=form)
    
    if request.method == 'POST':
        username = form.username.data
        password = form.password.data

        acc = db.find_user_by_password(username, password)
        if acc is None:
            return render_template('login.html', err_msg="Username or password wrong.")

        session['username'] = username
        session['accid'] = 123  #acc.id
        return redirect('/home')


@bp.route("/logout")
def logout():
    """user logout"""
    if 'username' in session:
        session.pop('username')
    return redirect('/home')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    """user register"""
    if request.method == 'GET':
        return render_template('register.html')

    username = request.form['username']
    password = request.form['password']
    password2 = request.form['confirm_password']
    if username == '' or password == '' or password2 == '':
        return render_template('register.html', err_msg="Required field can not be empty.")
    if password != password2:
        return render_template('register.html', err_msg="Confirm password is not same as password.")

    acc = db.find_by_name(username)
    if acc is not None:
        return render_template('register.html', err_msg="Username already exists.")

    db.save_user({'username': username, 'password': password})

    return render_template('register.html', success_msg="Register successfylly.")
