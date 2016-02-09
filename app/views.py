from app import app, db
from flask import render_template, flash, redirect, url_for
from .models import User

@app.route("/")
def index():
    
    return render_template("index.html")

@app.route("/user/<username>")
def user(username):

    user = User.query.filter_by(username = username).first()

    if user == None:
        flash("nah m8")
        return redirect(url_for("index"))

    return render_template("user.html", user = user)
