#!flask/bin/python

import os, glob, re, datetime
from app import db, models

def main():
    add_followers()

def add_followers():
    user_list = sorted(glob.glob("dataset-large/users/*"))

    for user_dir in user_list:
        username = re.sub("dataset-large/users/", "", user_dir)
        user = models.User.query.filter_by(username = username).first()
        following = open(os.path.join(user_dir, "details.txt"))
        following = following.readlines()

        has_following = False

        for line in following:
            if re.search("^listens: ", line):
                following = re.sub("^listens: |\n", "", line)
                following = following.split(" ")
                has_following = True
        
        assert (type(following) == list)
        
        if has_following == False:
            continue
        
        #print user.username

        for followed in following:
            new = models.User.query.filter_by(username = followed).first()
            user.follow(new)
            #print new.username, 
        
        db.session.add(user)
        db.session.commit()
        #print user.followed.all()

        
       







def link_tags():
    posts = models.Post.query.all()

    for post in posts:
        post_ = post.body
        #print type(post)
        post_ = post_.split(" ")
        
        skip_next = False

        for word in range(len(post_)):
            #print word, post[word]
            if skip_next :
                continue
            if re.match("^@\w", post_[word]):
                user = re.sub("@", "", post_[word])
                post_.insert(word, "<a href=\"/user/%s\">" % user)
                post_.insert(word + 2, "</a>")
                skip_next = True
                #print "yes", word
    
        post_ = " ".join(post_)
        post.body = post_
        print post
        print
        db.session.add(post)
        db.session.commit()


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
            elif re.search("^username: ", line):
                username = re.sub("^username: |\n", "", line)
                user_id = models.User.query.filter_by(username = username).first().id
                post.user_id = user_id

        db.session.add(post)
        db.session.commit()

main()

#print models.Post.query.all()
