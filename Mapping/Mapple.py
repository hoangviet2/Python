import folium
from folium.map import Icon
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
long = list(data["LON"])
name = list(data["NAME"])
el = list(data["ELEV"])

map = folium.Map(location=[14.389859277267677, 108.86193785529044], zoom_start=6, title =  "Stamen Terrain")
featuresgroup = folium.FeatureGroup(name="Volcanoes")
for lt,lg,els in zip(lat,long,el):
    featuresgroup.add_child(folium.Marker(location=[lt, lg],popup=str(els)+" m",icon= folium.Icon(color = 'green')))

map.add_child(featuresgroup)
map.save("testedMap.html")