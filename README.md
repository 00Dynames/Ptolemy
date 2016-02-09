# Ptolemy

    - Flask fun website
        - based off this tutorial: http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
    - refer to log file for details
    
#Log file 

- 22/01/2016
  - app init started
    - run.py, views and __init__ added
  - Config:
    - only variables with upeercase chars in a config file are used by app.config.from_object()
    - naming is weird, not explicit as to the specifics of what it does. would replace with "load_config" /10

- 26/01/2016
  - db migrate/upgrade/downgrade/create introduced
    - I'm not really clear on what/how these scripts do but ok
  - DB IS WORKING !!! YASSSS

- 09/02/2016
  - added templates and view functions to facilitate user profiles
  - currently working on migrating dataset-large users/posts into db
  - added large-dataset users into db
  - database populated with users and posts
  - fiure out how to get posts in reversed order from query
    - I can use all() to get a lins of the posts which are in order then reverse them but....
    - user.html is showing posts in reverse chronological