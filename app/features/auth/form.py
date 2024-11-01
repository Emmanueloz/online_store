from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo


class AuthForm(FlaskForm):
    username = StringField('Usuario', validators=[
                           DataRequired(message='El campo Usuario es requerido')])
    password = PasswordField('Contraseña', validators=[
                             DataRequired(message='El campo Contraseña es requerido')])


class LoginForm(AuthForm):
    pass


class RegisterForm(AuthForm):
    email = StringField(
        'Correo',
        validators=[
            DataRequired(message="El campo correo es requerido"),
            Email(message='Correo inválido')
        ])

    confirm_password = PasswordField(
        'Confirmar Contraseña',
        validators=[
            DataRequired(),
            EqualTo('password', message='Las contraseñas no coinciden')
        ])
