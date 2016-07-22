# Go (URL Shortener)

A project of [GMU SRCT](http://srct.gmu.edu)

Go is a drop-in URL shortening service. It aims to provide an easily
branded service for institutions that wish to widely disseminate
information without unnecessarily outsourcing branding.

I encourage you to join the #go channel in SRCT's [Slack Group](http://srct.slack.com) if you have any questions on setup or would like to contribute.

## Package Installation
<legend></legend>
### Prerequisities
First, install python and git on your system.
* Python is the programming language used for Django, the web framework used by Go.
* Git is the version control system used for SRCT projects.

Open a terminal and run the following command:

`$ sudo apt-get update`

This retrieves links to the most up-to-date and secure versions of your packages.

Next, with:

`$ sudo apt-get install python git`

you install python and git.

### Cloning the Go Codebase
Now, we're going to clone down a copy of the Go codebase from [git.gmu.edu](http://git.gmu.edu/srct/go), the SRCT code respository.

Configure your ssh keys by following the directions at [git.gmu.edu/help/ssh/README](http://git.gmu.edu/help/ssh/README).

Now, on your computer, navigate to the directory in which you want to download the project (perhaps one called development/ or something similar), and run

`$ git clone git@git.gmu.edu:srct/go.git`


### Required Packages
Finally, install these packages from the standard repositories:
 - VirtualBox

    `$ sudo apt-get install virtualbox`
 - Vagrant

    `$ sudo apt-get install vagrant`
 - Ansible

    `$ sudo easy_install pip && sudo pip install ansible`

## Developing with Vagrant
<legend></legend>
Vagrant allows for the virtualization of your development enviornment and automates the setup process for Go.

### Vagrant Setup
Navigate to go/ and run:

`$ vagrant up`

This will setup a vm to run Go on your computer and will setup a database, install packages, etc. The first time you run `vagrant up` it may take a few minutes to setup, specifically when installing Go packages. Don't worry as progressive times it will speed up.

And that's it! Navigate to [localhost](http://127.0.0.1:8000) in your web browser to view the website.

### Additional Notes

The authentication service used for Go is CAS. In local development however we utilize a test server. You can log in using your CAS username for both the username and password fields.

 The default superuser is _dhaynes3_ though this can be changed in _vagrantfile_ if you wish. You can run `$ vagrant provision` to apply this change. Be sure not to include that change in your commits.

For a currently undetermined reason at some points if you try to navigate to [localhost](http://127.0.0.1:8000) and you see an error like: "Conenction has been reset" then:
1. `vagrant ssh`
2. `sudo /etc/init.d/networking restart` and then `exit`
3. `vagrant provision` (may need to do twice)

This is the only temporary fix that we know exists.

If you make any changes to _models.py_ you will need to re-provision the vm's database:

`$ vagrant provision`

Please note that this will refresh the database (as in delete everything in it).

It is also good practice to shutdown your vm when you are done:

`$ vagrant halt`

and to restart with:

`$ vagrant up`

## On Deployment
<legend></legend>
### Deploying with Vagrant
TODO

### Cron

In order to expire links, you need to set up a cron job to run the manage.py
expirelinks command regularly. A sample cron script is available in the
repository and is named go-cleanlinks.cron. Drop this in cron.hourly and
change the paths so that they point to the virtualenv activate script and
manage.py.


### Note
Link by Viktor Vorobyev from the Noun Project.