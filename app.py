from flask import Flask, request, jsonify, render_template
import folium
from modelos import db,Marker
app = Flask(__name__)

#CONFIGURACION DEL TIPO DE BASE DE DATOS
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#iNICIALIZACION DE LA BASE DE DATOS 
db.init_app(app)



##RUTAS

# PAGINA PRINCIPAL PARA VISUALIZACION DE MAPAS
@app.route('/')
def index():
    return render_template('index.html')


# PAGINA PARA GUARDAR MARCADORES A LA DB
@app.route('/save_marker', methods=['POST'])
def save_marker():
    data = request.json
    new_marker = Marker(latitude=data['lat'], longitude=data['lng'])
    db.session.add(new_marker)
    db.session.commit()
    return jsonify({'status': 'success', 'id': new_marker.id})

# PAGINA PARA LEER MARCADORES DE LA DB 
@app.route('/get_markers', methods=['GET'])
def get_markers():
    markers = Marker.query.all()
    markers_data = [{"latitude": marker.latitude, "longitude": marker.longitude, "id": marker.id} for marker in markers]
    return jsonify(markers_data)




if __name__ == '__main__':
    app.run(debug=True)