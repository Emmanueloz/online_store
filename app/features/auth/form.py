from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TelField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo


class AuthForm(FlaskForm):
    username = StringField('Usuario', validators=[
                           DataRequired(message='El campo Usuario es requerido')])
    password = PasswordField('Contraseña', validators=[
                             DataRequired(message='El campo Contraseña es requerido')])


class LoginForm(AuthForm):
    pass


class UserForm(AuthForm):
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


class DirectionForm(FlaskForm):
    street = StringField('Calle', validators=[DataRequired()])
    number = StringField('Número', default='s/n')
    city = StringField('Ciudad', validators=[DataRequired()])
    state = StringField('Estado', validators=[DataRequired()])
    zip_code = StringField('Código Postal', validators=[DataRequired()])
    neighborhood = StringField('Barrio', validators=[DataRequired()])
    phone = TelField('Teléfono', validators=[DataRequired()])
    country = SelectField('País', validators=[DataRequired()], choices=[
        ('mx', 'México'),
        ('us', 'Estados Unidos'),
        ('ca', 'Canadá'),
        ('ar', 'Argentina'),
        ('cl', 'Chile'),
        ('co', 'Colombia'),
        ('pe', 'Perú'),
        ('uy', 'Uruguay'),
        ('ve', 'Venezuela'),
        ('do', 'Dominicana'),
        ('cr', 'Costa Rica'),
        ('pa', 'Panamá'),
        ('bo', 'Bolivia'),
        ('br', 'Brasil'),
        ('ec', 'Ecuador'),
        ('gy', 'Guyana'),
        ('py', 'Paraguay'),
        ('sr', 'Surinam'),
        ('uy', 'Uruguay'),
        ('ve', 'Venezuela'),
    ])


class RegisterForm(UserForm, DirectionForm):
    pass
