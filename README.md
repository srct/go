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
