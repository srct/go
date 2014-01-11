# Go (URL Shortener)

A project of [GMU SRCT](http://srct.gmu.edu).

Go is a drop-in URL shortening service. It aims to provide an easily
branded service for institutions that wish to widely disseminate
information without unnecessarily outsourcing branding.

## To D0
* qr codes on links view-- need to save the pictures somewhere, render inline as well as in different formats and sizes for download, and be deleted along with the links

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
