# Go (URL Shortener)

A project of [GMU SRCT](http://srct.gmu.edu).

Go is a drop-in URL shortening service. It aims to provide an easily
branded service for institutions that wish to widely disseminate
information without unnecessarily outsourcing branding.

## Local Enviornment Setup

### Prerequisities & Required Packages
First, install python, pip, and git on your system.
* Python is the programming language used for Django, the web framework used by Go.
* 'Pip' is the python package manager.
* Git is the version control system used for SRCT projects.

Open a terminal and run the following command:

`$ sudo apt-get update`

This retrieves links to the most up-to-date and secure versions of your packages.

Next, with:

`$ sudo apt-get install python python-dev python-pip git`

you install python and git.

Now, we're going to clone down a copy of the Go codebase from git.gmu.edu, the SRCT code respository.

Configure your ssh keys by following the directions at git.gmu.edu/help/ssh/README.

Now, on your computer, navigate to the directory in which you want to download the project (perhaps one called development/ or something similar), and run

`$ git clone git@git.gmu.edu:srct/go.git`

Finally, install these packages from the standard repositories:

`$ sudo apt-get install libldap2-dev mysql-server mysql-client libmysqlclient-dev python-mysqldb libsasl2-dev libjpeg-dev `

If prompted to install additional required packages, install those as well.

When prompted to set your mysql password, it's advisable to set it as the same as your normal superuser password.

### The Virtual Enviornment
Virtual environments are used to keep separate project packages from the main computer, so you can use different versions of packages across different projects and ease deployment server setup.

It's often recommended to create a special directory to store all of your virtual environments together (ie. development/virtualenv/), though they can be placed wherever is most convienent.

Run:

`$ sudo pip install virtualenv`

to install virtualenv system-wide.

Then in your virtual environment directory run:

`$ virtualenv go`

to create your virtual environment.

Activate it by typing:

`$ source go/bin/activate`

If you ever need to exit your virtual environment, simply run:

`$ deactivate`

Now, the packages you need to install for Go are in in the top level of the project's directory structure(go/).

Run:

`$ pip install -r requirements.txt`

to install all of the packages needed for the project.

### Database Configuration
Go is configured for use with a mysql database.

Load up the mysql shell by running

`$ mysql -u root -p insert_password_here`

and putting in your mysql password.

Create the database by running:

`> CREATE DATABASE go;`

You can choose a different name for your database if you desire.

Double check your database was created by running:

`> SHOW DATABASES;`

Though you can use an existing user to access this database, here's how to create a new user and give them the necessary permissions to your newly created database:

`> CREATE USER 'god'@'localhost' IDENTIFIED BY 'password';`

For local development, password strength is less important, but use a strong passphrase for deployment. You can choose a different username.

Run:

`> GRANT ALL ON go.* TO 'god'@'localhost';`

This allows your database user to create all the tables it needs on the bookshare database. (Each model in each app's models.py is a separate table, and each attribute a column, and each instance a row.)

Run:

`> GRANT ALL ON test_go.* TO 'god'@'localhost'; FLUSH PRIVILEGES;`

 When running test cases, django creates a test database so your 'real' database doesn't get screwed up. This database is called 'test_' + whatever your normal database is named. Note that for permissions it doesn't matter that this database hasn't yet been created.

The .* is to grant access all tables in the database, and 'flush privileges' reloads privileges to ensure that your user is ready to go.

Exit the mysql shell by typing:

`> exit`

### Additional Setup

Now, to configure your newly created database with the project settings, and set up your project's cryptographic key, copy the secret.py.template in settings/ to secret.py. Follow the comment instructions provided in each file to set your secret key and database info.

Also copy config.py.template to config.py. You will need to set DEBUG mode to True in order to view more details when things go awry.

Change directory into go/go/ and run:

`$ python manage.py makemigrations`

to create the tables and rows and columns for your database. This command generates sql code based on your database models.

Then run:

`$ python manage.py migrate`

to execute that sql code and set up your database. Migrations also track how you've changed your models over the life of your database, which allows you to make changes to your tables without screwing up existing information.

Finally, run:

`$ python manage.py createsuperuser`

to create an admin account, using the same username and email as you'll access through CAS. This means your 'full' email address, for instance gmason@masonlive.gmu.edu. Your password will be handled through CAS, so you can just use 'password' here.

(If you accidentally skip this step, you can run python manage.py shell and edit your user from there. Select your user, and set .is_staff and .is_superuser to True, then save.)

You can now uncomment line 55 from models.py, we have avoided nuclear armageddon.

Be sure to uncomment line 46 from models.py as well in order to allow short urls to be generated. 

Finally, within 'go/go' run:

`$ python manage.py runserver`

to start the site. Open your preferred web browser and navigate to 127.0.0.1:8000/ to see the site!

In order to approve yourself to be an 'approved user' you must navigate to 127.0.0.1:8000/admin and log in. Once in the admin page go to "registered users", and create a new registered user in the top right. Be sure to use the same username and Full Name aas your main account and select "approved" in the bottom row.

## To Do
* qr codes on links view-- need to save the pictures somewhere, render
    inline as well as in different formats and sizes for download, and be
    deleted along with the links
* Update the user authentication system (ie. port it to CAS to play nicely
    with GMU)
* Update the user registration system. Make it more intuitive to first time
    users, also update the connection between registered users and actual
    user auth accounts on the database.
* Set up Piwik to work with Go.
* Update the documentation on Go to include a setup guide
* Update the interface to bootswatch, perhaps? Maybe the same stylesheet as
    is used on SRCTWeb. (ie. complete HTML overhaul)
* Remove all Mason-specific branding.

## Notes for Production

### settings.py

The settings file should already be configured acceptably. You may need to
add a different authentication backend or database engine.

### nginx / Apache

You must configure an outside web server to properly host the static file
required to run this Django app.

### Cron

In order to expire links, you need to set up a cron job to run the manage.py
expirelinks command regularly. A sample cron script is available in the
repository and is named go-cleanlinks.cron. Drop this in cron.hourly and
change the paths so that they point to the virtualenv activate script and
manage.py.


# Troubleshooting

If your CAPTCHA is messing up, try checking that your system has `libfreetype6-dev` installed. If not, install it and remove + reinstall `pillow` in your virtual environment.
