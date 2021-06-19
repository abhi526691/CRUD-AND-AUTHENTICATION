
# Introduction

This is a simple website made in django. To kickstart your journey in django you can go for this project in your learning phase of django. This project contains CRUD operation as well as Authentication System made in django which is must in any framework you are learning

![Default Home View](screenshots/Index1.png "Title")

### Main features

* Register, Login and Logout

* Profile Page 

* Profile Updation Page

* Futute Enchancement: Email Alert System



### Existing virtualenv

If your project is already in an existing python3 virtualenv first install django by running

    $ pip install django
    
And then run the `django-admin.py` command to start the new project:

    $ django-admin.py startproject \
      --template=https://github.com/abhi526691/CRUD-AND-AUTHENTICATION \
      --extension=py,md \
      <ScheduleMaker>
      
### No virtualenv

Installing inside virtualenv is recommended, however you can start your project without virtualenv too.

If you don't have django installed for python 3 then run:

    $ pip3 install django
    
And then:

    $ python3 -m django startproject \
      --template=https://github.com/abhi526691/CRUD-AND-AUTHENTICATION \
      --extension=py,md \
      <CRUD-AND-AUTHENTICATION>
      
      
After that just install the local dependencies, run migrations, and start the server.

{% endif %}

# CRUD-AND-AUTHENTICATION

# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@https://github.com/abhi526691/CRUD-AND-AUTHENTICATION{{ CRUD-AND-AUTHENTICATION }}.git
    $ cd {{ ScheduleMaker }}
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements.txt
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver
    
    
    
<!-- CONTACT -->
## Contact

Abhishek Pandey - [linkedin](https://www.linkedin.com/in/abhishek-pandey-1515aa171/) - sauravpandey597@gmail.com

Project Link: [https://github.com/abhi526691/CRUD-AND-AUTHENTICATION](https://github.com/abhi526691/CRUD-AND-AUTHENTICATION)
