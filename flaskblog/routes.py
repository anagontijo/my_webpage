import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from flaskblog import app
import datetime

# Rota para a página home do sistema
@app.route("/")
@app.route("/home")
def home():
    image_file = url_for('static', filename='fotos/foto_padrao.jpeg');
    return render_template("home.html", image_file = image_file)

# Rota para a página about do sistema
@app.route("/about")
def about():
    return render_template("about.html", title='Sobre mim')
