# FRIENDS' LOCATIONS MAP  
There is one main module - app.py, four auxiliary modules - oauth.py, twurl.py, main_twitter.py and map_creation.py, one template - index.html and two examples of the work of the program - friends_locs.html and twitter.json.

App.py creates three web pages - '/', '/create' and '/create/map' using Flask library. The first page is main, the second one contains an input box, where the user should enter a Twitter username, twitter's logo, some instructions and the button for map creation. This module uses index.html template.

Main_twitter.py receives a username and, using Twitter API, collects the user's info and writes it to a JSON file. Then it opens a file, parses it and then creates a dictionary. The user's name is a key, and a tuple is a value. The first element of a tuple is another tuple with two coordinates - latitude and longitude which qre further going to help locate markers on a map. The second value is a location from a Twitter account.

Map_creation.py accepts data (dictionary) from the main_twitter.py module and generates a map using folium library.

To run the module user should enter the following commands:

$export FLASK_APP=app.py <br />
$flask run --host=0.0.0.0 --port=8080

and copy the link that appears right after entering these commands (for instance, http://10.10.247.27:8080/).

Then the main page will appear - with the twitters logo, some text, instructions, input box and 'create a map' button.

![screen1](https://user-images.githubusercontent.com/91615687/154692677-97db1c3f-5874-4f98-b913-a46e1d680ec3.jpg)

It is important to follow these steps: writing down (existing) username, PRESSING ENTER and clicking the button after that. Otherwise, the page with the notification about the problem will appear.

After following all these steps, you should wait from 10 to 30 seconds and the map will be created.

![screen2](https://user-images.githubusercontent.com/91615687/154692715-fe078b32-5810-4e59-bbb5-b9f74061df59.jpg)
![screen3](https://user-images.githubusercontent.com/91615687/154692742-58f3c1eb-d85c-4363-8da2-c4a2fe5e647f.jpg)
