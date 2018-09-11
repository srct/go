# Go 2

[![build status](https://git.gmu.edu/srct/go/badges/master/build.svg)](https://git.gmu.edu/srct/go/commits/master) [![coverage report](https://git.gmu.edu/srct/go/badges/master/coverage.svg)](https://git.gmu.edu/srct/go/commits/master) [![python version](https://img.shields.io/badge/python-2.7,3.4+-blue.svg)]() [![Django version](https://img.shields.io/badge/Django-1.11-brightgreen.svg)]() [![SemVer version](https://img.shields.io/badge/SemVer Version-2.2.3-yellowgreen.svg)]()

** Make sure to switch to the [go-three](https://git.gmu.edu/srct/go/tree/go-three) branch for development! **

In the terminal,

```
git checkout -B go-three
git pull origin go-three
``` 

#### A project of [GMU SRCT](https://srct.gmu.edu).

Go is a drop-in URL shortening service. This project aims to provide an easy to use
URL branding service for institutions that wish to widely disseminate information
without unnecessarily outsourcing branding.

Go is currently a `Python 3` (with backwards compatability foor `Python 2.7` until
Django 2.0 in December 2017) project written in the `Django` web framework, with
`MySQL` as our backend database.

# Setup instructions for local development

Go currently supports developers on Linux, macOS and Windows platforms through
both the Docker and Vagrant virtualization platforms. You may use either one
though we have included instructions for manual setup as well. Here's our walk-through
of steps we will take:

1. Install `git` on your system.
2. Clone the Go codebase.
3. Get Go up and running with the method of your choice.

## 1) Install `git` on your system.

`git` is the version control system used for SRCT projects.

### On Linux Based Systems

**with apt:**

Open a terminal and run the following command:

    sudo apt update

This retrieves links to the most up-to-date and secure versions of your packages.

Next, with:

    sudo apt install git

you install `git` onto your system.

### On macOS

We recommend that you use the third party Homebrew package manager for macOS,
which allows you to install packages from your terminal just as easily as you
could on a Linux based system. You could use another package manager (or not
use one at all), but Homebrew is highly reccomended.

To get homebrew, run the following command in a terminal:

    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)

**Note**: You do NOT need to use `sudo` when running any Homebrew commands, and
it likely won't work if you do.

Next, to make sure Homebrew is up to date, run:

    brew update

Finally we can install git with:

    brew install git

### On Windows

We recommend that if you are on Windows 10 AE (Anniversary Edition) or above to make use of the
Windows Subsystem for Linux (WSL). The following link should get you up and running: 

[https://msdn.microsoft.com/en-us/commandline/wsl/install_guide](https://msdn.microsoft.com/en-us/commandline/wsl/install_guide)


#### Contributing with Windows

After that is setup, you should be able to follow the Linux instructions for _manual setup_ to
contribute to the project. 

If you are not on Windows 10 or would rather prefer to not use the WSL you may download Git for
Windows here:

[https://git-scm.com/download/win](https://git-scm.com/download/win)

You'll want to follow the Vagrant setup method as it is designed to run on all platforms 
including Windows. 

I have also successfully ran the project with Docker, though you need
access to Hyper-V which is only available on "Professional" versions of Windows. 

## 2) Clone the Go codebase.

Now, we're going to clone down a copy of the Go codebase from [git.gmu.edu](https://git.gmu.edu/srct/go),
the SRCT code respository with SSH.

**a)** Configure your ssh keys by following the directions at:

[git.gmu.edu/help/ssh/README](https://git.gmu.edu/help/ssh/README).

**b)** Now, on your computer, navigate to the directory in which you want to download the project (ie. perhaps one called `development/SRCT`), and run

    git clone git@git.gmu.edu:srct/go.git

## 3) Get Go up and running with the method of your choice.

Now that we have `git` setup and cloned down the code you can

    cd go/

and get to working on setting up a development environment!

### Docker

Docker is an emerging containerization platform written in Google's Go
language.
Instead of running a full VM that runs Go, we package up all the
various bits that make up Go and run that as a container (two
containers: one for Go and the other for mysql) that act as normal
processes to the OS.   

Check out [docker.com](https://www.docker.com/what-docker) for more details.

Pros:

 - Lightweight
    - Can be run on most machines without needing significant resources.
    - SRCT members report minimal battery impact on laptops.
 - Fast
    - Compared to other methods, Docker is comparatively faster than
    Vagrant or manual setup.
 - Minimal setup
    - You run one command. Really easy to get up and running once you install
    Docker.
 - Good cross platform support
    - Runs smoothly on macOS, Linux, and Windows
    - Great docs to help if you get stuck.
 - Can easily destroy and rebuild the docker images
 - Loads in changes to code on the fly

Cons:

 - Challenging to debug problems
    - Cannot interact with attached images and as a result, you cannot really
    interact with the database.

There are instructions on how to setup/develop with Docker at the [docker-configuration page in the Go project wiki](https://git.gmu.edu/srct/go/wikis/docker-configuration).

### Vagrant + Ansible

Vagrant boots up a full virtual machine (VM) through VirtualBox that then runs Go. A
script written with Ansible will then run on that VM to automate the setup process
for you. It is similar in a way to running Go on a legitimate server.

Pros:

  - Very similar to a production environment
  - Can use `vagrant ssh` to "ssh" into the VM to debug things such as the
    database.
  - Relatively straightforward and easy setup.
    - One Command.
  - Can easily destroy and rebuild the VM.
  - Loads in changes to code on the fly.
  - Fast-ish (Initial provision takes a bit).

Cons:

  - Heavier on resources.
    - It's literally a full VM.
  - Occasional issues/hiccups.
    - Documented fixes are in the wiki.

There are instructions on how to setup with Vagrant at the [vagrant-configuration
page in the Go project wiki](https://git.gmu.edu/srct/go/wikis/vagrant-configuration).

Additionally, there is documentation about developing with Vagrant at
the [vagrant-usage page in the Go project wiki](https://git.gmu.edu/srct/go/wikis/vagrant-usage).

### Manual Setup

Manual setup (or: the old fashioned way) is where you install all dependecies on
your system and run Go as a local server with Django. Granted you are technically
doing that with Vagrant and Docker except those platforms automate the steps that
are laid out in this section.

Pros:
  - Experience setting up a Django project for local development

Cons:
  - Greater potential for things to go wrong
  - Way more steps

Head to:

https://git.gmu.edu/srct/go/wikis/manual-setup


# Some words about contributing to Go.

## Testing

You are _very strongly_ encouraged to write test cases where applicible for
code that you contribute to the repo. This is not a rule at the moment but rather
a strong suggestion. It's good practice for corporate land and will also ensure
your code works. Additionally, there are quite a few example ones to look at in
the repo and on Google.

### Running Unit Tests

Unit tests are run on every commit sent to gitlab though that can be a pain to
rely on. Here's how to run them locally:

#### Docker

Docker is not supported currently for running unit tests. If you're able to get
it set up, open a merge request and I'll merge it in.

#### Vagrant

    vagrant up
    vagrant ssh
    cd /vagrant
    source venv/bin/activate
    cd go
    source sourceme.sh
    python manage.py test

#### Manual Setup

Assuming you are within your virtualenv:

    python manage.py test

## CONTRIBUTING.md

This document goes into detail about how to contribute to the repo, plus some
opinions about using `git`.

## Opening issues

There is a template for issue descriptions located on the new issue page. I will
close issues with poor descriptions or who do not follow the standard.

## Authentication

The authentication service used for Go is CAS. In local development however we
utilize a test server. You can log in with just your CAS username to simulate logging
in. By default, the Django superuser is set to `dhaynes3`.

In order to approve yourself to be an 'approved user' you must navigate to 127.0.0.1:8000/admin and log in.
Once in the admin page go to "registered users", and create a new registered user in the top right. Be sure to
use the same username and Full Name as your main account and select "approved" in the bottom row.

## Coding style

You should adhere to the style of the repo code. Consistancy is key! PEP8 guidelines
are strongly reccomended but not enforced at the time. Please comment your code,
I will not accept commits that contain uncommented code.

## Getting Help

I encourage you to join the [#go channel](https://srct.slack.com/messages/go/details/) in SRCT's [Slack Group](https://srct.slack.com)
if you have any questions on setup or would like to contribute.

# Some words about deploying Go.

Check out our admin guide:

https://git.gmu.edu/srct/go/wikis/administration-guide

In order to expire links, you need to set up a cron job to run the manage.py
expirelinks command regularly. A sample cron script is available in the
repository and is named go-cleanlinks.cron. Drop this in cron.hourly and
change the paths so that they point to the virtualenv activate script and
manage.py.

---
**Note:**

Link by Viktor Vorobyev from the Noun Project.
