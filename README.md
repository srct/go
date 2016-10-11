# Go (URL Shortener) [![build status](https://git.gmu.edu/srct/go/badges/master/build.svg)](https://git.gmu.edu/srct/go/commits/master) [![coverage report](https://git.gmu.edu/srct/go/badges/master/coverage.svg)](https://git.gmu.edu/srct/go/commits/master)



A project of [GMU SRCT](http://srct.gmu.edu).

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

`$ sudo apt-get install python python-dev python-pip git`

you install python and git.

**MacOS**

Open terminal and run the following command:

If you have Homebrew installed skip the following command

`/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

This installs Homebrew on your Mac

Next run the command:

`brew update`

This updates Homebrew

Next we install python and git with:

`brew install python git`

### Cloning the Go Codebase
Now, we're going to clone down a copy of the Go codebase from [git.gmu.edu](http://git.gmu.edu/srct/go), the SRCT code respository.

Configure your ssh keys by following the directions at [git.gmu.edu/help/ssh/README](http://git.gmu.edu/help/ssh/README).

Now, on your computer, navigate to the directory in which you want to download the project (perhaps one called development/ or something similar), and run

`$ git clone git@git.gmu.edu:srct/go.git`


### Required Packages
Finally, install these packages from the standard repositories:
 - VirtualBox

    `$ sudo apt-get install virtualbox`


    You should be installing the latest virtualbox version which as of time of writing is `5.0.24_Ubuntur108355`. You can verify the version number by running `vboxmanage --version`.
 - Vagrant

    `$ sudo apt-get install vagrant`

    You should be installing the latest vagrant version which as of time of writing is `Vagrant 1.8.1`. You can verify the version number by running `vagrant -v`.
 - Ansible

    `$ sudo pip install ansible`

    You should be installing the latest ansible version which as of time of writing is `ansible 2.1.1.0`. You can verify the version number by running `ansible --version`.

  **MacOS**

  Install virtual box at:  
  [VirtualBox.org](https://www.virtualbox.org/wiki/Downloads)

  Then install Vagrant and Ansible with Homebrew with the following command:

  `brew install Caskroom/cask/vagrant Ansible`

## Developing with Vagrant
<legend></legend>
Vagrant allows for the virtualization of your development enviornment and automates the setup process for Go.

### Vagrant Setup
Navigate to go/ and run:

`$ vagrant up`

This will setup a vm to run Go on your computer and will setup a database, install packages, etc. The first time you run `vagrant up` it may take a few minutes to setup, specifically when installing Go packages. Don't worry as progressive times it will speed up.

And that's it! Navigate to [localhost:8000](http://127.0.0.1:8000) in your web browser to view the website.

### Additional Notes & Troubleshooting

The authentication service used for Go is CAS. In local development however we utilize a test server. You can log in using your CAS username for both the username and password fields.

 The default superuser is _dhaynes3_ though this can be changed in _vagrantfile_ if you wish. You can run `$ vagrant provision` to apply this change. Be sure not to include that change in your commits.

*Note:* For a currently undetermined reason at some points if you try to navigate to [localhost](http://127.0.0.1:8000) and you see an error like: "Conenction has been reset" then:
1. `vagrant ssh`
2. `sudo /etc/init.d/networking restart` and then `exit`
3. `vagrant provision` (may need to do twice)

This is the only temporary fix that we know exists.

If you make any changes to _models.py_ you will need to re-provision the vm's database:

`$ vagrant provision`

Please note that this will refresh the database (as in delete everything in it).


### Cron

In order to expire links, you need to set up a cron job to run the manage.py
expirelinks command regularly. A sample cron script is available in the
repository and is named go-cleanlinks.cron. Drop this in cron.hourly and
change the paths so that they point to the virtualenv activate script and
manage.py.


### Note
Link by Viktor Vorobyev from the Noun Project.
