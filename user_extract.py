#!flask/bin/python

import os, glob, re, datetime
from app import db, models

def main():
    extract_posts()

def extract_users():  
    user_list = sorted(glob.glob("dataset-large/users/*"))

    for user_dir in user_list:
        details = open(os.path.join(user_dir, "details.txt"))
        details = details.readlines()

        user = models.User()

        for line in details:
            if re.search("^username", line):
                user.username = re.sub("username: |\n", "", line)
            elif re.search("^email", line):
                user.email = re.sub("email: |\n", "", line) 
            elif re.search("^password: ", line):
                user.password = re.sub("password: |\n", "", line)
            elif re.search("^full_name: ", line):
                user.full_name = re.sub("full_name: |\n", "", line)

        db.session.add(user)
        db.session.commit()
        #print user.username

def extract_posts():
    post_list = sorted(glob.glob("dataset-large/bleats/*"))

    for post_dir in post_list:
        post_details = open(post_dir)
        post_details = post_details.readlines()

        post = models.Post()

        for line in post_details:
            if re.search("^bleat: ", line):
                post.body = re.sub("^bleat: |\n", "", line)
            elif re.search("^time: ", line):
                time = float(re.sub("^time: |\n", "", line))
                post.timestamp = datetime.datetime.fromtimestamp(time)
                #print datetime.datetime.fromtimestamp(time)
            elif re.search("^username: ", line):
                username = re.sub("^username: |\n", "", line)
                user_id = models.User.query.filter_by(username = username).first().id
                post.user_id = user_id
                #print re.sub("^username: |\n", "", line)

        #print post
        #print

        db.session.add(post)
        db.session.commit()

main()


#print models.User.query.all() #filter_by(username = "john").first().id
print models.Post.query.all()
