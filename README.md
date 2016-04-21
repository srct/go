# Go (URL Shortener)

A project of [GMU SRCT](http://srct.gmu.edu).

Go is a drop-in URL shortening service. It aims to provide an easily
branded service for institutions that wish to widely disseminate
information without unnecessarily outsourcing branding.

## Package Installation

### Prerequisities & Required Packages
First, install python, pip, and git on your system.
* Python is the programming language used for Django, the web framework used by Go.
* Git is the version control system used for SRCT projects.

Open a terminal and run the following command:

`$ sudo apt-get update`

This retrieves links to the most up-to-date and secure versions of your packages.

Next, with:

`$ sudo apt-get install python git`

you install python and git.

Now, we're going to clone down a copy of the Go codebase from git.gmu.edu, the SRCT code respository.

Configure your ssh keys by following the directions at git.gmu.edu/help/ssh/README.

Now, on your computer, navigate to the directory in which you want to download the project (perhaps one called development/ or something similar), and run

`$ git clone git@git.gmu.edu:srct/go.git`

Finally, install these packages from the standard repositories:
 - VirtualBox
 - Vagrant
 - Ansible
 - 


## On Deployemnt
### Cron

In order to expire links, you need to set up a cron job to run the manage.py
expirelinks command regularly. A sample cron script is available in the
repository and is named go-cleanlinks.cron. Drop this in cron.hourly and
change the paths so that they point to the virtualenv activate script and
manage.py.
