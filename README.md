# Blog | Let's Learn Django!

> We'll build a Blog application that allows users to create, edit, and delete post. The homepage will list all blog post and there will be a dedicated detail page for each individual post. We'll also introduce CSS for styling.

Initial Set Up

| **Django** | [Python](https://www.python.org/) | [Django](https://www.djangoproject.com/) |

![](https://www.mattlayman.com/img/python-django.png)

How to do it.

[](#features)Initial Set Up
---------------------

*   create a new directory for our code on the Desktop called blog
*   install Django in a new virtual environment
*   create a new app blog
*   perform a migration to set up the database
*   update settings.py

You do this in command line:

    $ cd ~/Desktop
    $ mkdir blog
    $ cd blog
    $ pipenv install django==3.1.6
    $ pipenv shell
    (blog) $ django-admin startporject blog_project .
    (blog) $ python manage.py startapp blog
    (blog) $ python manage.py migrate
    (blog) $ python manage.py runserver
    

if you navigate to http://127.0.0.1:8000/ in your browser you should see the following page.

![](https://i.imgur.com/5jaC2y7.png)

Ok, initial installation complete! 

You get this:

![](https://d2sofvawe08yqg.cloudfront.net/djangoforbeginners/medium2x?1602530290)
    

Create your gitrebo:

### …or create a new repository on the command line

echo "# blog" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M master
git remote add origin https://github.com/your_git_name_here/blog.git
git push -u origin master

### …or push an existing repository from the command line

git remote add origin https://github.com/your_git_name_here/blog.git
git branch -M master
git push -u origin master

### …or import code from another repository

You can initialize this repository with code from a Subversion, Mercurial, or TFS project.

[Import code](chrome-extension://cjedbglnccaioiolemnfhjncicchinao/peteralexandercharles/blog/import)

**ProTip!** Use the URL for this page when adding GitHub as a remote.


[Source](https://github.com/peteralexandercharles/blog)

![](http://www.molecularecologist.com/wp-content/uploads/2013/11/github-logo.jpg)
