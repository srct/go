# Go (URL Shortener)

A project of [GMU SRCT](http://srct.gmu.edu).

Go is a drop-in URL shortening service. It aims to provide an easily
branded service for institutions that wish to widely disseminate
information without unnecessarily outsourcing branding.

## Configuration

### GoConfig

See `/wsgi/goconfig.py.template` for configuration variables. Relocate this
to `/wsgi/goconfig.py` when configured properly.

### Apache

The host or virtualhost being used for Go must have certain WSGIScriptAlias
directives.

```
WSGIScriptAlias /rd /srv/http/go/wsgi/redir.py
WSGIScriptAlias /index.html /srv/http/go/wsgi/index.py
WSGIScriptAlias /mylinks /srv/http/go/wsgi/mylinks.py
WSGIScriptAlias /login /srv/http/go/wsgi/login.py
WSGIScriptAlias /logout /srv/http/go/wsgi/logout.py
WSGIScriptAlias /signup /srv/http/go/wsgi/signup.py
WSGIScriptAlias /about /srv/http/go/wsgi/about.py
```

### Piwik

Piwik analytics are optionally enabled. See `/wsgi/goconfig.py.template`
for relevant configuration values. In order to use Piwik with this service,
you will need the
[Piwik Python API](https://github.com/piwik/piwik-python-api) installed.
Use one of the following for easy setup:

```
pip install piwikapi
pip2 install piwikapi
```
