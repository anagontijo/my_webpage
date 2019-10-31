import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from flaskblog import app
import csv

def get_files():
    logos = ["linkedin", "github", "trello", "gmail", "telegram","UFMG"]
    logo_files = {}
    for logo in logos:
        logo_files[logo] = url_for('static', filename='logos/'+logo+'.png')
    image_file = url_for('static', filename='fotos/foto_padrao.jpeg')
    return logo_files, image_file

def get_courses():
    courses = []
    for sem in range(8):
        courses.append([])
    with open(os.getcwd()+"/flaskblog/static/docs/course.csv") as csvfile:
        for row in csv.reader(csvfile, delimiter=',', quotechar='|'):
            courses[int(row[0])-1].append([])
            for elem in range(4):
                courses[int(row[0])-1][-1].append(row[elem+1])
    return courses

# Rota para a página home do sistema
@app.route("/")
@app.route("/home")
def home():
    logo_files, image_file = get_files()
    return render_template("home.html", image_file = image_file,
                           logo_files = logo_files)

# Rota para a página about do sistema
@app.route("/about")
def about():
    logo_files, image_file = get_files()
    return render_template("about.html", title='Sobre mim',
                           image_file = image_file,
                           logo_files = logo_files)

@app.route("/studies")
def studies():
    courses = get_courses()
    print(courses)
    logo_files, image_file = get_files()
    return render_template("studies.html", title='Grad',
                           image_file = image_file,
                           logo_files = logo_files,
                           courses=courses)
