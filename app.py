"""
The main module that creates\
web application.
"""


from pyexpat.errors import messages
from flask import Flask, render_template, request
import main_twitter
import map_creation 


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Function creates main page, where will be input box\
    and button.
    """
    return render_template("index.html")


@app.route("/create", methods=["POST"])
def create():
    """
    Function creates an input box, where user\
    should enter a username, and a map generation\
    button.
    """
    global username
    username = request.form["username"]
    return render_template("index.html")


global username
@app.route("/create/map", methods= ["POST"])
def create_map():
    """
    Function recieves a dictionary from main_twitter\
    module and generates a map using map_creation\
    module.
    """
    try:
        data = main_twitter.collect_locations(username)
        map = map_creation.create(data)
        ip = request.remote_addr
        return render_template("friends_locs.html", user_ip=ip)
    except:
        return "error occured - return to the previous page and follow the instructions"


if __name__ == "__main__":
    app.run(debug = True, host = "10.10.228.226", port = 8080)
    