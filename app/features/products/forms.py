from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, TextAreaField, SelectField
from wtforms.validators import DataRequired


class FormProduct(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired()])
    description = TextAreaField('Descripción', validators=[DataRequired()])
    price = FloatField('Precio', validators=[DataRequired()])
    amount = IntegerField('Cantidad', validators=[DataRequired()])
    category = SelectField('Categoría',
                           validators=[DataRequired()],
                           choices=[('electrónicos', 'Electrónicos'),
                                    ('ropa', 'Ropa'),
                                    ('comida', 'Comida'),
                                    ('juguetes', 'Juguetes'),
                                    ('deportes', 'Deportes'),
                                    ('libros', 'Libros'),
                                    ('música', 'Música'),
                                    ('computadoras', 'Computadoras'),
                                    ('videojuego', 'Videojuego'),
                                    ('otros', 'Otros'),
                                    ]
                           )
