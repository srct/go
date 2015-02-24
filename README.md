# Go (URL Shortener)

A project of [GMU SRCT](http://srct.gmu.edu).

Go is a drop-in URL shortening service. It aims to provide an easily
branded service for institutions that wish to widely disseminate
information without unnecessarily outsourcing branding.

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

## Configuration

### settings.py

The settings file should already be configured acceptably. You may need to
add a different authentication backend or database engine.

### nginx / Apache

You must configure an outside web server to properly host the static file
required to run this Django app.

### Python

To install the required Python modules, simply execute

```
$ pip install -r requirements.txt
```

and you should be good to go.

### Cron

In order to expire links, you need to set up a cron job to run the manage.py
expirelinks command regularly. A sample cron script is available in the
repository and is named go-cleanlinks.cron. Drop this in cron.hourly and
change the paths so that they point to the virtualenv activate script and
manage.py.


# Troubleshooting

If your CAPTCHA is messing up, try checking that your system has `libfreetype6-dev` installed. If not, install it and remove + reinstall `pillow` in your virtuale environment.
