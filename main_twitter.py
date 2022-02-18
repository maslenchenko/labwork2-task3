"""
This module creates JSON file with\
users' info using Twitter API, then\
using data from this file creates a dictionary\
with users' names and locations.
"""


import urllib.request, urllib.parse, urllib.error
import twurl
import ssl
import sys
import json
from geopy.geocoders import Nominatim, ArcGIS


def get_friends(username):
    """
    (str)
    Function uses Twitter API to create JSON file\
    with information about friends of given account.
    """
    TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    if (len(username) < 1):
        return 
    else:
        try:
            url = twurl.augment(TWITTER_URL,
                                {'screen_name': username, 'count': '100'})
            connection = urllib.request.urlopen(url, context=ctx)
            data = connection.read().decode()
            js = json.loads(data)
            with open("twitter.json", "w") as file:
                json.dump(js,file, ensure_ascii=False, indent=4)
        except:
            return f"{sys.exc_info()[0]} occured\nplease try again"


def read_json(name):
    """
    (str) -> (dict)
    Function reads a JSON file and converts\
    it to a dictionary.
    >>> print(len(read_json("twitter.json")))
    6
    """
    try:
        with open(name) as file:
            data = json.load(file)
        return data
    except:
        return f"{sys.exc_info()[0]} occured\nplease try again"


def geocode(address):
    """
    (str) -> (tuple)
    Function returns two coordinates of given\
    location - latitude and lontitude.
    >>> print(geocode("Werder,Brandenburg,Germany"))
    (52.37695000000008, 12.933300000000031)
    """
    i = 0
    try:
        location = geocoders[i].geocode(address)
        if location != None:
            return location.latitude, location.longitude
        i += 1
        location = geocoders[i].geocode(address)
        if location != None:
            return location.latitude, location.longitude
    except:
        return None
arcgis = ArcGIS(timeout=10)
nominatim = Nominatim(timeout=10, user_agent="location")
geocoders = [arcgis, nominatim]


def collect_locations(user):
    """
    (str) -> (dict)
    Function transorms data from "twitter.json" into\
    a dictionary with name as a key and tuple as a value\
    with coordinates (latitude and longtitude) as the first element\
    and name of location as the second one.
    >>> print(list((collect_locations("maaaslenchenko").items()))[0])
    ('nstbhn', [(42.833330000000046, 12.833330000000046), 'Italia'])
    """
    try:
        friends_locs = dict()
        get_friends(user)
        data =  read_json("twitter.json")
        for index in range(len(data.get("users"))):
            for key in data["users"][index].keys():
                if key == "name":
                    name = data["users"][index]["name"]
                if key == "location":
                    location = data["users"][index]["location"]
                    info = [geocode(location), location]
            friends_locs[name] = info
            if info[1] == None or info[0] == None:
                del friends_locs[name]
        return friends_locs
    except:
        return f"{sys.exc_info()[0]} occured\nplease try again"
