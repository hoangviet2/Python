import folium
from folium.map import Icon
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
long = list(data["LON"])
name = list(data["NAME"])
el = list(data["ELEV"])

def coolorDectertor(elevation):
    if elevation<1000:
        return 'green'
    elif elevation<3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[14.389859277267677, 108.86193785529044], zoom_start=6, title =  "Stamen Terrain")
featuresgroupVol = folium.FeatureGroup(name="Volcanoes")
for lt,lg,els,nms in zip(lat,long,el,name):
    #featuresgroup.add_child(folium.Marker(location=[lt, lg],popup=str(els)+" m",icon= folium.Icon(color = coolorDectertor(els))))
    featuresgroupVol.add_child(folium.CircleMarker(location=[lt,lg],popup=str(els)+" m",radius=6,tooltip=nms,color='grey',fill_color =coolorDectertor(els),fill_opacity = 0.7 ))

featuresgroup = folium.FeatureGroup(name="Population")
featuresgroup.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(),
style_function= lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'red' if x['properties']['POP2005']>20000000  else 'orange' }))

map.add_child(featuresgroup)
map.add_child(featuresgroupVol)
map.add_child(folium.LayerControl())

map.save("testedMap.html")