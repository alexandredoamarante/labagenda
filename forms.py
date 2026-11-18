# Validação de formulários com Flask-WTF
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField
from wtforms.validators import DataRequired

class ReservaForm(FlaskForm):
    turma = StringField('Turma', validators=[DataRequired()])
    data = DateField('Data da Reserva', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Agendar Horário')
