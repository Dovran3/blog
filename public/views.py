from . import app
from .models import *
from flask import render_template, request, redirect, flash
from flask_login import UserMixin, login_user, logout_user, login_required


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/auth", methods=["GET", "POST"])
def auth():
    logout_user()
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
        user = cursor.fetchall()
        if user and user[0][2] == password:
            user = UserMixin()
            user.id = username
            login_user(user, remember=True)
            try:
                return redirect(request.args.get("next"), code=301)
            except:
                return redirect("/", code=301)
        else:
            return redirect("/auth", code=301)
    return render_template("auth.html")


@app.route("/registr", methods=["GET", "POST"])
def registr():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        con_password = request.form.get("con_password")

        if password != con_password:
            flash("Incorrect confirm password!")
            return redirect("/registr", code=301)

        cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
        user = cursor.fetchall()

        print(user)
        if not user:
            cursor.execute(f"INSERT INTO users (username, password) \
                             VALUES ('{username}', '{password}')")
            db.commit()
            flash("Account's been successfuly created!")
            return redirect("/auth", code=301)
        else:
            flash("This user's already been in")
            return redirect("/registr", code=301)
    return render_template("registr.html")


@app.route("/message")
@login_required
def blog():
    return render_template("blog.html")


@app.route("/profile")
@login_required
def profile():
    return render_template("profile.html")
