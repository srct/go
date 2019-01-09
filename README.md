# Go 3.0 - Go Forward 🚀

Go is at its core a URL shortening service built for the GMU community. It was
the first big SRCT project that was taken from development to production by the
founders. Originally a PHP app, it was translated into Django as a 1.0 release
and sat unmaintained for a period of time. Development on 2.0 started in 2016
with the intention of modernizing the application as well as designing for long
term maintenance. Additionally, since the core of the project is fairly simple,
2.0 functioned as a good introduction to open source development for new
members.

Go 3.0 is currently in production with the goal of modernizing the project with new functionality.

A project of [GMU SRCT](https://srct.gmu.edu).

## Architecture of the project

### `go_ahead` | The react app

`go_ahead` is the react.js frontend of the project. It is built with the React
JavaScript framework to allow for rapid development and experimentation. There
is also a lot of interactivty that the framework allows that we can leverage
for a smooth user experience.

### `go_back` | The django API

`go_back` is the API backend of the project. It is built with the Django REST
Framework (python). It supports all CRUD (Create, Read, Update, Delete)
operations on Go links as well as account management.

## How to get up and running

As always, the first step is to get the project running on your local machine.

Consult the [docker documentation](https://docs.docker.com/install/) for instructions on how to install Docker CE and the [docker-compose documentation](https://docs.docker.com/compose/install/) on how to install Docker Compose.

Run:

```sh
docker-compose build
docker-compose up
```

Navigate to [127.0.0.1:8000](http://127.0.0.1:8000) after the compose process has finished running to access the app.

## How to contribute to the project

1. Go to [the issues page](https://git.gmu.edu/srct/go/issues) and look at what needs to be done, and have a cursory choice of something.
1. Review [CONTRIBUTING.md](https://git.gmu.edu/srct/go/blob/go-three/CONTRIBUTING.md)
1. Review the documentation for individual components:
   1. [`go_ahead` documentation](https://git.gmu.edu/srct/go/blob/go-three/go/go_ahead/README.md)
   1. [`go_back` documentation](https://git.gmu.edu/srct/go/blob/go-three/go/go_back/README.md)
1. Get to the #go channel in SRCT Slack and ask for assistance.

## Other

- Make sure to ask any questions you have in the #go channel in SRCT Slack
- Go 3 logo was created by <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ">Andres Villogas</a>
- Don't worry if nothing makes sense, we all start there.
- This project was made possible through the collective contributions of multiple Mason SRCT members:

  <a href="https://git.gmu.edu/srct/go/milestones/3">Go 2.2</a>:
  <br />
  <a href="https://github.com/dhaynespls">David Haynes</a>,
  <a href="https://github.com/ocelotsloth">Mark Stenglein</a>,
  <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ">
  Andres Villogas
  </a>
  ,<a href="https://github.com/IAmEyad">Eyad Hasan</a>,
  <a href="https://github.com/zosman1">Zach Osman</a>,
  <a href="">Leo Grandinetti</a>,
  <a href="https://mason.gmu.edu/~gmoran/">Grady Moran</a>,
  <a href="https://github.com/zmknox">Zach Knox</a>,
  <a href="https://github.com/mike-bailey">Michael Bailey</a>,
  <a href="https://github.com/jrouly">Michel Rouly</a>,
  <a href="https://github.com/nanderson94">Nicholas Anderson</a>,
  <a href="">Kevin Mckigney</a>, and
  <a href="https://github.com/dwbond">Daniel Bond</a>.<br />

  <a href="https://git.gmu.edu/srct/go/milestones/2">Go 2.1</a>:
  <br />
  <a href="https://github.com/dhaynespls">David Haynes</a>,
  <a href="https://github.com/zosman1">Zach Osman</a>,
  <a href="https://github.com/roberthitt">Robert Hitt</a>,
  <a href="https://github.com/nanderson94">Nicholas Anderson</a>,
  <a href="https://github.com/zmknox">Zach Knox</a>,
  <a href="https://github.com/mike-bailey">Michael Bailey</a>,
  <a href="https://github.com/mdsecurity">Mattias Duffy</a>,
  <a href="https://github.com/IAmEyad">Eyad Hasan</a>, and
  <a href="https://github.com/danielkim1">Danny Kim</a>.<br />

  <a href="https://git.gmu.edu/srct/go/milestones/1">Go 2.0</a>:
  <br />
  <a href="https://github.com/dhaynespls">David Haynes</a>,
  <a href="">Matthew Rodgers</a>,
  <a href="https://github.com/nanderson94">Nicholas Anderson</a>, and
  <a href="https://github.com/dwbond">Daniel Bond</a>.<br />

  Go 1.0:
  <br />
  <a href="https://github.com/jrouly">Michel Rouly</a>,
  <a href="https://github.com/creffett">Chris Reffett</a>,
  <a href="https://github.com/nanderson94">Nicholas Anderson</a>, and
  <a href="https://github.com/akshaykarthik">Akshay Karthik</a>.
  <br />
