from operator import methodcaller
from flask import Flask 
from flask import render_template
from flask import g, flash
from flask import abort, request, redirect, url_for
from flask_bootstrap import Bootstrap


from app import *

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


from FormBusqueda import FormBusqueda
from FormAlta import FormAlta

app = Flask(__name__) 
app.config['SECRET_KEY'] = 'xxDDF878945f7f8t9gWavp5p' 

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clientes.db'


bootstrap = Bootstrap(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Cliente(db.Model):
    __tablename__ = 'Clientes'
    Padron = db.Column(db.Integer, primary_key=True, unique=True)
    Nombre = db.Column(db.Text, nullable=False)
    Apellido = db.Column(db.Text, nullable=False)
    Contrasenia = db.Column(db.String(20), nullable=False)
    Email = db.Column(db.Text, nullable=False)

    
@app.route('/nuevo', methods=['GET', 'POST'])
def nuevo():
    alta = FormAlta()
    if request.method == 'POST':
        if alta.validate_on_submit():
            nuevoCliente = Cliente(Nombre=alta.nombreCliente.data, Apellido=alta.apellidoCliente.data, Email=alta.email.data, Contrasenia=alta.contrasenia.data)
            db.session.add(nuevoCliente)
            db.session.commit()
            flash(f"Cliente/a {nuevoCliente.Nombre} creado exitosamente. Inicie Sesion.")
            return redirect(url_for('busqueda', padron=nuevoCliente.Padron))
        else:
            flash("Error. Revise los datos del formulario.")
    return render_template('nuevo.html', form=alta)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/cliente/index_cliente.html')
def index_cliente():
    return render_template("index_cliente.html")


@app.route('/busqueda', methods=['GET', 'POST'])
def busqueda():

    busqueda = FormBusqueda()
    if request.method == 'POST':
        
        return redirect(url_for('cliente', email=busqueda.email.data, contrasenia=busqueda.contrasenia.data))

    return render_template('busqueda.html', form=busqueda)


@app.route('/cliente/<email>')
def cliente(email):

    cliente_buscado = Cliente.query.filter_by(Email=email).first_or_404()


    return render_template("cliente.html", cliente_buscado=cliente_buscado)

@app.route('/cliente/Catalogo_cliente.html')
def cat_cliente():
    return render_template("Catalogo_cliente.html")

@app.route('/cliente/Nosotros_cliente.html')
def nos_cliente():
    return render_template('Nosotros_cliente.html')

@app.route('/SobreNosotros.html')
def nosotros():
    return render_template('SobreNosotros.html')

@app.route('/Catalogo.html')
def catalogo():
    return render_template('Catalogo.html')

app.app_context().push()
db.create_all()
if __name__ == '__main__': 
    app.run(debug=True) 
