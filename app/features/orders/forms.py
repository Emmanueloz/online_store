from flask_wtf import FlaskForm
from wtforms import DateField, SelectField
from wtforms.validators import DataRequired
from datetime import date


class OrderForm(FlaskForm):
    state = SelectField('Estado', choices=[
                       ('pending', 'Pendiente'), ('sent', 'Enviado'), ('delivered', 'Entregado')])
    delivery_date = DateField('Fecha de entrega',
                              validators=[DataRequired()], render_kw={"min": date.today().isoformat()})
