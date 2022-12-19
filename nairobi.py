import folium
import os
#import os allows us to import the operating system features
import json
#import json allows to import json features

#JSON is an acronmyn for JavaScript Object Notation
#JSON is used for transporting data from servers to web pages

#import is a keyword that is used to borrow/import the package folium
#folium is package in python programmming that is used to visualize geospatial data
kenya=folium.Map(location=[-1.235,36.5674],zoom_start=10)
#nairobi is variable that will contain the data to be visualized and other elements
#folium.Map is a module in the folium package
#location has two elements namely latitude and the longitude
#zoom_start determines the zoom extent

image=folium.features.CustomIcon('pin.jpg',icon_size=(50,50))

image1=folium.features.CustomIcon('elephant.jpg',icon_size=(50,50))

image2=folium.features.CustomIcon('colton.jpg',icon_size=(30,20))

#image is variable
#folium.features.Custom is a module in the folium package that allows use of a customized image


folium.Marker([-1.235,36.5674],popup="Nairobi",
              tooltip="Show location").add_to(kenya)

folium.Marker([-4.0435,39.6682],popup="<strong>Mombasa</strong>",
              #strong is an html tag to make text appear bolder
              tooltip="Show location").add_to(kenya)

folium.Marker([-0.091702,34.767956],popup="<strong>KISUMU</strong>",
              #strong is an html tag to make text appear bolder
              tooltip="Show location").add_to(kenya)


folium.Marker([-0.3689,35.2863],popup="<small>KERICHO</small>",
              #strong is an html tag to make text appear bolder
              tooltip="Show location",
              icon=folium.Icon(icon="leaf")).add_to(kenya)
#icon is a variavle that will contain the icon values

folium.Marker([0.3476,32.5825],popup="<emphasis>KAMPALA</emphasis>",
              #strong is an html tag to make text appear bolder
              tooltip="Show location",
              icon=image).add_to(kenya)

folium.Marker([-2.1833,38.5126],popup="<emphasis>Tsavo National Park</emphasis>",
              #strong is an html tag to make text appear bolder
              tooltip="Show location",
              icon=image1).add_to(kenya)

folium.Marker([20.2802,38.5126],popup="<b>RED SEA</b>",
              #strong is an html tag to make text appear bolder
              tooltip="Show location",
              icon=folium.Icon(icon="cloud", icon_color="blue")).add_to(kenya)


folium.Marker([-1.2199,36.8892],popup="<b><i>THIKA ROAD MALL</b></i>",
              #strong is an html tag to make text appear bolder
              tooltip="Show location",
              icon=folium.Icon(icon_color="red")).add_to(kenya)


folium.Marker([-1.230207,36.89221],popup="<b>KASARANI SPORTS COMPLEX</b>",
              #strong is an html tag to make text appear bolder
              tooltip="Show location",
              icon=folium.Icon(icon="ball" ,icon_color="green")).add_to(kenya)


folium.CircleMarker(location=[-1.22086, 36.89321],
                    radius=30,
                    popup="<b>Regional Centre for Mapping of Resources for Development</b>",
                    color="blue",
                    fill_color="True",
                    ).add_to(kenya)

folium.CircleMarker(location=[-1.140089, 37.257024],
                    radius=40,
                    popup="<b>Ol Donyo Sabuk National Park</b>",
                    color="purple",
                    fill_color="True",
                    ).add_to(kenya)



folium.Marker([4.218,21.4531],popup="<emphasis>DRC Congo</emphasis>",
              #strong is an html tag to make text appear bolder
              tooltip="Show location",
              icon=image2).add_to(kenya)

overlay=os.path.join("overlay.json")

folium.GeoJson(overlay,name="Nairobi Region").add_to(kenya)

#GeoJson is used to encode geographic data using line strings,polylines,polygons

#folium.Marker is a module in the folium package that allows us to use markers to identify locations
kenya.save("nairobi.html")
#nairobi.save saves the map details in an html file
#.html is an extension to save html