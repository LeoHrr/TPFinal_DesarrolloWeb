from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *

class FormAlta(FlaskForm):
    nombreCliente = StringField("Nombre", validators=[DataRequired()])
    apellidoCliente = StringField("Apellido", validators=[DataRequired()])
    edad = IntegerField("Edad", validators=[DataRequired(), NumberRange(min=18, max=100)])
    email = EmailField("Email", validators=[DataRequired()])
    contrasenia = PasswordField("Contraseña", validators=[DataRequired()])
    contrasenia2 = PasswordField("Repetir Contraseña", validators=[DataRequired(), EqualTo('contrasenia', message="Las contraseñas no coinciden")])
    submit = SubmitField("Aceptar")