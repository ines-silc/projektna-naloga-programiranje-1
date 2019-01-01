import pandas as pd
import matplotlib.pyplot as plt
import folium
import os

regional = pd.read_csv('podatki/regional.csv', encoding = 'cp1252')
regional['town'], regional['state'] = regional['location'].str.split(',', 1).str

a = regional.groupby(['state'])[['show']].count()
a.to_csv('podatki/zemljevid.csv', sep=',')


b = pd.read_csv('podatki/zemljevid.csv')
b['state'] = b['state'].str.strip()

state_geo = os.path.join('/Users/Ines Šilc/Documents/projektna-naloga-programiranje-1', 'podatki/us-states.json')
state_data = os.path.join('/Users/Ines Šilc/Documents/projektna-naloga-programiranje-1', 'podatki/poskus.csv')

### Initialize the map:
m = folium.Map(location=[38, -96], zoom_start = 4)
## 
### Add the color for the chloropleth:
m.choropleth(
 geo_data=state_geo,
 name='choropleth',
 data=b,
 columns=['state', 'show'],
 key_on='feature.id',
 fill_color='YlGn',
 fill_opacity=0.6,
 line_opacity=0.3,
 legend_name='Število predstav'
)
folium.LayerControl().add_to(m)

m.save('zemljevid.html')
