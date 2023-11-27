from flask import Flask
from modelos import db

#Instanciamos de la clase flask usando el servidor 'app'
app = Flask('app')

#Configuración de base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Inicializamos la base de datos 
db.init_app(app)

#Creamos la base de datos
with app.app_context():
  db.create_all()