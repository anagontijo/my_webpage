import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from flaskblog import app
import csv

class GlobalStore:
    language = "pt"

def get_files():
    logos = ["br","uk","document" ,"linkedin", "github", "trello", "gmail", "telegram","UFMG"]
    logo_files = {}
    for logo in logos:
        logo_files[logo] = url_for('static', filename='logos/'+logo+'.png')
    image_file = url_for('static', filename='fotos/foto_padrao.jpeg')
    return logo_files, image_file

def get_courses():
    courses = []
    for sem in range(8):
        courses.append([])
    if variables.language == "pt":
        path = "/flaskblog/static/docs/course_pt.csv"
    else:
        path = "/flaskblog/static/docs/course_en.csv"
    with open(os.getcwd()+path) as csvfile:
        for row in csv.reader(csvfile, delimiter=',', quotechar='"'):
            courses[int(row[0])-1].append([])
            for elem in range(4):
                courses[int(row[0])-1][-1].append(row[elem+1])
    return courses

def get_ext_courses():
    ext_courses = []
    if variables.language == "pt":
        path = "/flaskblog/static/docs/ext_courses_pt.csv"
    else:
        path = "/flaskblog/static/docs/ext_courses_en.csv"
    with open(os.getcwd()+path) as csvfile:
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

variables = GlobalStore()

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

def get_projects():
    projects = []
    with open(os.getcwd()+"/flaskblog/static/docs/projects.csv") as csvfile:
        for row in csv.reader(csvfile, delimiter=',', quotechar='"'):
            projects.append({})
            projects[-1]["images"] = []
            for file in row[0].split("/"):
                projects[-1]["images"].append(url_for('static',
                                                  filename='fotos/'+file))
            projects[-1]["main_image"] = projects[-1]["images"][0]
            projects[-1]["images"] = projects[-1]["images"][1:]
            projects[-1]["github"] = row[2]
            projects[-1]["name"] = row[1]
            projects[-1]["description"] = row[3]
            projects[-1]["poster"] = url_for('static', filename='docs/'+row[4])
            projects[-1]["poster_type"] = row[5]

    return projects

def get_stylesheet():
    stylesheet = url_for('static', filename="webpage.css")
    return stylesheet

def get_cv_paths():
    cv_path_en = url_for('static', filename="docs/anagracaresume2019_en.pdf")
    cv_path_pt = url_for('static', filename="docs/anagracaresume2019_pt.pdf")
    return cv_path_en, cv_path_pt

# Rota para a página home do sistema
@app.route("/", methods=["POST","GET"])
@app.route("/home", methods=["POST","GET"])
def home():
    if "english.x" in request.form:
        variables.language = "en"
    elif "portuguese.x" in request.form:
        variables.language = "pt"

    logo_files, image_file = get_files()
    return render_template("home.html", image_file = image_file,
                           logo_files = logo_files,
                           stylesheet = get_stylesheet(),
                           language = variables.language,
                           self_url = url_for("home"))

# Rota para a página about do sistema
@app.route("/about", methods=["POST","GET"])
def about():
    if "english.x" in request.form:
        variables.language = "en"
    elif "portuguese.x" in request.form:
        variables.language = "pt"

    logo_files, image_file = get_files()
    courses = get_courses()
    cv_path_en, cv_path_pt = get_cv_paths()

    return render_template("about.html", title={"pt":"Sobre mim", "en":"About"},
                           image_file = image_file,
                           logo_files = logo_files,
                           stylesheet = get_stylesheet(),
                           cv_path_en = cv_path_en,
                           cv_path_pt = cv_path_pt,
                           language = variables.language,
                           self_url = url_for("about"))

@app.route("/studies", methods=["POST","GET"])
def studies():
    if "english.x" in request.form:
        variables.language = "en"
    elif "portuguese.x" in request.form:
        variables.language = "pt"

    logo_files, image_file = get_files()
    courses = get_courses()
    return render_template("studies.html", title={"pt":"Graduação","en":"Studies"},
                           image_file = image_file,
                           logo_files = logo_files,
                           courses = courses,
                           stylesheet = get_stylesheet(),
                           language = variables.language,
                           self_url = url_for("studies"))

@app.route("/external-courses", methods=["POST","GET"])
def ext_courses():
    if "english.x" in request.form:
        variables.language = "en"
    elif "portuguese.x" in request.form:
        variables.language = "pt"

    logo_files, image_file = get_files()
    extern_courses = get_ext_courses()
    return render_template("external_courses.html", title={"pt":"Cursos Externos","en":"External Courses"},
                           logo_files = logo_files,
                           image_file = image_file,
                           ext_courses = extern_courses,
                           stylesheet = get_stylesheet(),
                           language = variables.language,
                           self_url = url_for("ext_courses"))

@app.route("/jobs", methods=["POST","GET"])
def jobs():
    if "english.x" in request.form:
        variables.language = "en"
    elif "portuguese.x" in request.form:
        variables.language = "pt"

    logo_files, image_file = get_files()
    internships, jobs = get_jobs()
    return render_template("jobs.html", title={"pt":"Experiência","en":"Work Experience"},
                           logo_files = logo_files,
                           image_file = image_file,
                           internships = internships,
                           jobs = jobs,
                           stylesheet = get_stylesheet(),
                           language = variables.language,
                           self_url = url_for("jobs"))

@app.route("/projects", methods=["POST","GET"])
def projects():
    if "english.x" in request.form:
        variables.language = "en"
    elif "portuguese.x" in request.form:
        variables.language = "pt"

    logo_files, image_file = get_files()
    projects = get_projects()
    return render_template("projects.html", title={"pt":"Projetos","en":"Projects"},
                           logo_files = logo_files,
                           image_file = image_file,
                           projects = projects,
                           stylesheet = get_stylesheet(),
                           language = variables.language,
                           self_url = url_for("projects"))
