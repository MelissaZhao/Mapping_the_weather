import folium as folium
from requests import get
import json
import folium
import os
import webbrowser
import html

# here request is used to fetch Json data from DB.
# Json to process Json data.
# Folium is a tool for visualising data on maps in Python.
# OS library is used to discover the Current Working Directory (CWD), therefore the brower knows from where to load the saved map file.

# URL for the API needs to be stored as a string.
url = "https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations"

# fetch the data
stations = get ( url ).json ()
print ( stations["items"][0] )
print ( stations["items"][0]["weather_stn_long"] )
print ( stations["items"][5]["weather_stn_long"] )

lons = [station['weather_stn_long'] for station in stations['items']]
lats = [station['weather_stn_lat'] for station in stations['items']]
wsnames = [html.escape ( station['weather_stn_name'] ) for station in stations['items']]
print ( wsnames )

# create map & plotting stations
# set Lörrach as central point of map
map_ws = folium.Map ( location=[47, 7], zoom_start=6 )

for n in range ( len ( lons ) ):
    folium.Marker ( [lats[n],
                     lons[n]],
                    icon=folium.Icon ( icon="cloud", color="green" ),
                    popup=wsnames[n] ).add_to ( map_ws )

CWD = os.getcwd()
map_ws.save ( "wsmap1.html" )
webbrowser.open_new("file://"+CWD+"/"+"wsmap1.html")

