# WELCOME

This is the Go (Python) repository! Welcome!

A project of [GMU SRCT](http://srct.gmu.edu).

See [wsgi/goconfig.py.template] for configuration variables. Relocate this to `/wsgi/goconfig.py` when configured properly.

## Apache Configuration

The host or virtualhost being used for Go must have certain WSGIScriptAlias directives.

```
WSGIScriptAlias /rd /srv/http/go/wsgi/redir.py
WSGIScriptAlias /index.html /srv/http/go/wsgi/index.py
WSGIScriptAlias /login /srv/http/go/wsgi/login.py
WSGIScriptAlias /logout /srv/http/go/wsgi/logout.py
WSGIScriptAlias /signup /srv/http/go/wsgi/signup.py
WSGIScriptAlias /about /srv/http/go/wsgi/about.py
```
