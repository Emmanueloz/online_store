from flask import Blueprint, render_template
from app.features.auth.form import LoginForm, RegisterForm

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

    if form.validate_on_submit():
        print(form.data)

        return 'Registrado'
    else:
        print(form.errors)
        return 'Error'
