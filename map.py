## Web API you haven’t used before that requires API key or HTTP Basic authorization 
## 4 points
## MAPBOX : show the restaurant map in city

import plotly.graph_objects as locate

access_tokens = 'pk.eyJ1Ijoiam9jZWx5bjAwIiwiYSI6ImNsZ2E5eWY5NjBmM2QzZXFpMnVvZWg3d2cifQ.ywfvBv6WcSzE8iWYKhUScA'

def city_map(tree):
    text_list = []
    lat_list = []
    lon_list = []
    rating_list = []

    # Iterate through each restaurant in the info_tree and append the relevant values to their respective lists
    for rest in tree:
        text_list.append("{} ({}) price: {}, rating: {}".format(rest["name"], rest["attributes"]['category'],  rest["attributes"]['price'], rest["attributes"]['rating']))
        lat_list.append(rest["attributes"]['latitude'])
        lon_list.append(rest["attributes"]['longitude'])
        rating_list.append(rest["attributes"]['rating'])
        
    # Create a scattermapbox figure using the latitudes and longitudes of the restaurants as the markers
    # The size of the markers is set to 10, and their color and opacity are determined by the restaurant ratings
    # The text attribute is set to show the name, category, price, and rating of each restaurant when the user hovers over the marker
    map = locate.Figure(
        locate.Scattermapbox(lat=lat_list, lon=lon_list, mode='markers',
            marker=locate.scattermapbox.Marker(size=10, color=rating_list, opacity=0.5, colorbar=dict(title="ratings of resturants")),
            text=text_list))

    # Set the layout of the map, including the center, zoom level, paper background color, and size
    # The center of the map is set to the average latitude and longitude of all the restaurants in the info_tree
    layout = dict(autosize=True, hovermode='closest',
        mapbox=locate.layout.Mapbox(accesstoken=access_tokens, bearing=0, center=locate.layout.mapbox.Center(lat=(sum(lat_list) / len(lat_list)), lon=(sum(lon_list) / len(lon_list))), pitch=0, zoom=11),
        paper_bgcolor="white", width=1500, height=800)
    
    # Update the layout of the map
    map.update_layout(layout)
    
    # Write the map to an HTML file and open it in a web browser
    map.write_html("map.html", auto_open=True)
    
    # Return the map object
    return map