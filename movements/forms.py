from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired, Length

monedas=('EUR', 'ETH', 'LTC', 'BNB', 'EOS', 'XLM', 'TRX', 'BTC', 'XRP', 'BCH', 'USDT', 'BSV', 'ADA')

class FormMovimientos(FlaskForm):
    monedafrom = SelectField('From', validators=[DataRequired()])
    cantidadfrom = FloatField('Cantidad', validators=[DataRequired()])
    monedato = SelectField('To', validators=[DataRequired()], choices=monedas)
    cantidadto = FloatField('CantidadTO', validators=[DataRequired()])
    
    submit = SubmitField('Aceptar')
    calc =SubmitField('Calcular')