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
        for row in csv.reader(csvfile, delimiter=',', quotechar='"'):
            courses[int(row[0])-1].append([])
            for elem in range(4):
                courses[int(row[0])-1][-1].append(row[elem+1])
    return courses

def get_ext_courses():
    ext_courses = []
    with open(os.getcwd()+"/flaskblog/static/docs/ext_courses.csv") as csvfile:
        for row in csv.reader(csvfile, delimiter=',', quotechar='"'):
            ext_courses.append([])
            parts = row[5].split("/")
            topics = []
            for part in parts:
                topics.append(part.split(":"))
            for elem in range(5):
                ext_courses[-1].append(row[elem])
            ext_courses[-1].append(topics)
            ext_courses[-1].append(row[6])
    return ext_courses

def get_jobs():
    internships = []
    jobs = []
    with open(os.getcwd()+"/flaskblog/static/docs/jobs.csv") as csvfile:
        for row in csv.reader(csvfile, delimiter=',', quotechar='"'):
            if int(row[0]) == 0:
                internships.append([])
                for elem in range(7):
                    internships[-1].append(row[elem+1])
            else:
                jobs.append([])
                for elem in range(7):
                    jobs[-1].append(row[elem+1])
    return internships, jobs

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
    courses = get_courses()
    return render_template("about.html", title='Sobre mim',
                           image_file = image_file,
                           logo_files = logo_files)

@app.route("/studies")
def studies():
    logo_files, image_file = get_files()
    courses = get_courses()
    return render_template("studies.html", title='Graduação',
                           image_file = image_file,
                           logo_files = logo_files,
                           courses = courses)

@app.route("/external-courses")
def ext_courses():
    logo_files, image_file = get_files()
    ext_courses = get_ext_courses()
    return render_template("external_courses.html", title='Cursos externos',
                           logo_files = logo_files,
                           image_file = image_file,
                           ext_courses = ext_courses)

@app.route("/jobs")
def jobs():
    logo_files, image_file = get_files()
    internships, jobs = get_jobs()
    return render_template("jobs.html", title='Experiência',
                           logo_files = logo_files,
                           image_file = image_file,
                           internships = internships,
                           jobs = jobs)
