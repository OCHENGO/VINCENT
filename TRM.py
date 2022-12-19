import folium
Roysambu=folium.Map(location=[-1.219818,36.888994],zoom_start=18)
folium.Marker([-1.219818,36.888994],popup="TRM Drive",
              icon=folium.Icon(icon_color="blue")).add_to(Roysambu)
Roysambu.save("TRM.html")