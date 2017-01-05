# Go

[![build status](https://git.gmu.edu/srct/go/badges/master/build.svg)](https://git.gmu.edu/srct/go/commits/master)
[![coverage report](https://git.gmu.edu/srct/go/badges/master/coverage.svg)](https://git.gmu.edu/srct/go/commits/master)
![python version](https://img.shields.io/badge/python-2.7-blue.svg)
![Django version](https://img.shields.io/badge/Django-1.10-brightgreen.svg)

#### A project of [GMU SRCT](http://srct.gmu.edu).

Go is a drop-in URL shortening service. This project aims to provide an easy to use
URL branding service for institutions that wish to widely disseminate information
without unnecessarily outsourcing branding.

Go is currently a `Python 2.7` project written in the `Django` web framework, with
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

Open a terminal and run the following command:

    $ sudo apt-get update

This retrieves links to the most up-to-date and secure versions of your packages.

Next, with:

    $ sudo apt-get install git

you install `git` onto your system.

### On macOS

We recommend that you use the third party Homebrew package manager for macOS,
which allows you to install packages from your terminal just as easily as you
could on a Linux based system. You could use another package manager (or not
use one at all), but Homebrew is highly reccomended.

To get homebrew, run the following command in a terminal:

    $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)

**Note**: You do NOT need to use `sudo` when running any Homebrew commands, and
it likely won't work if you do.

Next, to make sure Homebrew is up to date, run:

    $ brew update

Finally we can install git with `brew install git`

### On Windows
---

Instruction on how to setup git on Windows goes here.

## 2) Clone the Go codebase.

Now, we're going to clone down a copy of the Go codebase from [git.gmu.edu](http://git.gmu.edu/srct/go),
the SRCT code respository.

Configure your ssh keys by following the directions at [git.gmu.edu/help/ssh/README](http://git.gmu.edu/help/ssh/README).

Now, on your computer, navigate to the directory in which you want to download the project (perhaps one called development/ or something similar), and run

`$ git clone git@git.gmu.edu:srct/go.git`

## 3) Get Go up and running with the method of your choice.

### Docker

[docker configuration on the wiki](https://git.gmu.edu/srct/go/wikis/docker-configuration)

### Vagrant

[config](https://git.gmu.edu/srct/go/wikis/vagrant-configuration)

[usage](https://git.gmu.edu/srct/go/wikis/vagrant-usage)

### Manual Setup

# On Contributing


I encourage you to join the [#go channel](https://srct.slack.com/messages/go/details/) in SRCT's [Slack Group](https://srct.slack.com)
if you have any questions on setup or would like to contribute.


# Deployment

In order to expire links, you need to set up a cron job to run the manage.py
expirelinks command regularly. A sample cron script is available in the
repository and is named go-cleanlinks.cron. Drop this in cron.hourly and
change the paths so that they point to the virtualenv activate script and
manage.py.

---
**Note:**

Link by Viktor Vorobyev from the Noun Project.
