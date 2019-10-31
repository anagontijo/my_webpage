from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = '98e17485c227c59e41d926802c3eb65c'

from flaskblog import routes
