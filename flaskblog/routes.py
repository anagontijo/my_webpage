import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from flaskblog import app
import datetime

# Rota para a página home do sistema
@app.route("/", methods=['GET'])
@app.route("/home", methods=['GET'])
def home():
    image_file = url_for('static', filename='fotos/foto_padrao.jpeg');
    return render_template("home.html", image_file = image_file)

# Rota para a página about do sistema
@app.route("/about")
def about():
    return render_template("about.html", title='Sobre mim')

@app.route('/getmsg/', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    name = request.args.get("name", None)

    # For debugging
    print(f"got name {name}")

    response = {}

    # Check if user sent a name at all
    if not name:
        response["ERROR"] = "no name found, please send a name."
    # Check if the user entered a number not a name
    elif str(name).isdigit():
        response["ERROR"] = "name can't be numeric."
    # Now the user entered a valid name
    else:
        response["MESSAGE"] = f"Welcome {name} to our awesome platform!!"

    # Return the response in json format
    return jsonify(response)
