import folium

# Ubicación para centrar tu mapa
location = [45.5236, -122.6750]

# Crear un mapa base
m = folium.Map(location=location, zoom_start=13)

# Ruta o URL del archivo SVG
icon_image = "static/dibujo.svg"

# Crear un icono personalizado
icon = folium.CustomIcon(
    icon_image,
    icon_size=(28, 30)  # Tamaño del icono en píxeles
)

# Crear un marcador con el icono personalizado
folium.Marker(
    location=location,
    icon=icon
).add_to(m)

# Guardar el mapa en un archivo HTML
m.save('mapa_con_svg_personalizado.html')

