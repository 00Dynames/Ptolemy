from app import app, db
from flask import render_template, flash, redirect, url_for
from .models import User, Post

@app.route("/")
@app.route("/index")
def index():

    users = User.query.all()    

    return render_template("index.html", users = users, title = "Index")

@app.route("/user/<username>")
def user(username):

    user = User.query.filter_by(username = username).first()
    posts = user.posts.all() + user.followed_posts().all()
    posts = sorted(posts, key = get_key)
    
    if user == None:
        flash("nah m8")
        return redirect(url_for("index"))

    return render_template("user.html", user = user, posts = posts, title = user.username)

def get_key(post):
    return post.timestamp
