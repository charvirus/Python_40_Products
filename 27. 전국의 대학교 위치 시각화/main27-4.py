import folium
map = folium.Map(location=[32,127],zoom_start=7)

marker = folium.Marker([37.341435483,126.733026596], popup='한국공학대학교',icon=folium.Icon(color='blue'))

marker.add_to(map)

map.save(r'uni_map.html')