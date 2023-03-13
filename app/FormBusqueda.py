from flask_wtf import FlaskForm
from wtforms import EmailField, SubmitField, PasswordField, StringField
from wtforms.validators import DataRequired

class FormBusqueda(FlaskForm):
    email = EmailField("Email", validators=[DataRequired()])
    contrasenia = PasswordField("Contraseña", validators=[DataRequired()])
    submit = SubmitField("Ingresar")