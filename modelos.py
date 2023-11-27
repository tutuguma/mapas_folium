from flask_sqlalchemy import SQLAlchemy

#Instanciamos la base de datos
db = SQLAlchemy()

class Marker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    info = db.Column(db.String(250))