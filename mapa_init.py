import folium
m= folium.Map().add_child(
    folium.ClickForMarker("<b>Lat:</b> ${lat}<br /><b>Lon:</b> ${lng}")
)
m.save("index.html")