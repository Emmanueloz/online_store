from flask import Blueprint, render_template, redirect, url_for, flash
from app.features.auth.form import LoginForm, RegisterForm
from app.features.auth.model import User
from app.auth.user import UserLogin
from app.auth.roles import Roles
from app.database import db
from flask_login import login_user, logout_user
from sqlalchemy.exc import IntegrityError

auth_bp = Blueprint('auth', __name__, template_folder='templates')


@auth_bp.get('/login/')
def login():
    return render_template('login.jinja2')


@auth_bp.get('/register/')
def register():
    context = {'form': RegisterForm()}
    return render_template('register.jinja2', **context)


@auth_bp.post('/register/')
def register_post():

    form: RegisterForm = RegisterForm()

    context = {'form': form}

    if not form.validate_on_submit():
        return render_template('register.jinja2', **context)

    try:
        user = User(form.username.data, form.email.data, form.password.data,
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
