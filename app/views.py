from app import app, db, login_manager
from flask import render_template, flash, redirect, url_for, session, request, g
from flask_login import login_user, logout_user, current_user, login_required
from .models import User, Post
from .forms import LoginForm

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
        # write better "not found" page
        flash("nah m8")
        return redirect(url_for("index"))

    return render_template("user.html", user = user, posts = posts, title = user.username)

def get_key(post):
    return post.timestamp

@app.route("/login", methods = ["GET", "POST"])
def login():
    
    form = LoginForm()
    if form.validate_on_submit():
        
        user = User.query.filter_by(username = str(form.username.raw_data[0])).first_or_404()
        
        if form.password.raw_data[0] == user.password:
            login_user(user)
        else:
            flash("incorrect password")

    return render_template("login.html", title = "Login", form = form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.before_request
def before_request():
    g.user = current_user
