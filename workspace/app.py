from flask import Flask, render_template
from flask_login import LoginManager
from workspace.config import Config
from workspace.forms import LoginForm

app = Flask(__name__)
app.config.from_object(Config)

login = LoginManager(app)


@app.route("/")
def index():
    return render_template("home.html")


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
