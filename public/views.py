from . import app
from flask import render_template


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/auth")
def auth():
    return render_template("auth.html")


@app.route("/registr")
def registr():
    return render_template("registr.html")


@app.route("/message")
def blog():
    return render_template("blog.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")
