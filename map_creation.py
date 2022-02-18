"""
Module creates a map, using data from\
dictionary.
"""

import folium

def create(data):
    """
    Function accepts dictionary, and creates\
    a map using its data and folium library.\
    Then saves it as a 'friends_locs.html'.
    """
    html = """<h4>{}</h4>
    location: {}
    """
    map = folium.Map()
    fg_locations = folium.FeatureGroup(name=f"friends' locations")
    for key in data.keys():
            iframe = folium.IFrame(html=html.format(key, data[key][1]),
                                width=250,
                                height=80)
            fg_locations.add_child(folium.Marker(location=data[key][0],
                                    popup=folium.Popup(iframe),
                                    icon=folium.Icon(color='lightblue')))
    map.add_child(fg_locations)
    map.add_child(folium.LayerControl())
    map.save("/home/oleksandra/Desktop/programming-ucu/labworks-2sem/lab2/task3/templates/friends_locs.html")




