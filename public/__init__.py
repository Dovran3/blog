from flask import Flask


app = Flask(__name__)
app.config["SECRET_KEY"] = "some secret key"

from . import views
