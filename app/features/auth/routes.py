from flask import Blueprint, render_template, redirect, url_for, flash
from app.features.auth.form import LoginForm, RegisterForm
from app.features.auth.model import User
from app.auth.user import UserLogin
from app.auth.roles import Roles
from app.database import db
from flask_login import login_user, logout_user, current_user
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash
auth_bp = Blueprint('auth', __name__, template_folder='templates')


@auth_bp.get('/login/')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home.index'))
    context = {'form': LoginForm()}
    return render_template('login.jinja2', **context)


@auth_bp.post('/login/')
def login_post():
    form: LoginForm = LoginForm()
    context = {'form': form}

    if not form.validate_on_submit():
        return render_template('login.jinja2', **context)

    user: User = User.query.filter_by(username=form.username.data).first()
    if not user or not check_password_hash(user.password, form.password.data):
        flash('Usuario no encontrado', 'error')
        return render_template('login.jinja2', **context)

    login_user(UserLogin(user.id, user.username, user.email, user.password))
    return redirect(url_for('home.index'))


@auth_bp.get('/register/')
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home.index'))
    context = {'form': RegisterForm()}
    return render_template('register.jinja2', **context)


@auth_bp.post('/register/')
def register_post():

    form: RegisterForm = RegisterForm()

    context = {'form': form}

    if not form.validate_on_submit():
        return render_template('register.jinja2', **context)

    try:
        password_hash = generate_password_hash(form.password.data)
        user = User(form.username.data, form.email.data, password_hash,
                    Roles.CLIENTE)
        db.session.add(user)
        db.session.commit()
        login_user(UserLogin(user.id, user.username,
                   user.email, user.password))

        return redirect(url_for('home.index'))
    except IntegrityError:
        flash('Usuario ya registrado', 'error')
        return render_template('register.jinja2', **context)
    except Exception as e:
        return render_template('error.jinja2')


@auth_bp.get('/logout/')
def logout():
    logout_user()
    return redirect(url_for('home.index'))
