# Go 3.0 - Go Forward 🚀

Go is at its core a URL shortening service built for the GMU community. It was
the first big SRCT project that was taken from development to production by the
founders. Originally a PHP app, it was translated into Django as a 1.0 release
and sat unmaintained for a period of time. Development on 2.0 started in 2016
with the intention of modernizing the application as well as designing for long
term maintenance. Additionally, since the core of the project is fairly simple,
2.0 functioned as a good introduction to open source development for new
members.

A project of [GMU SRCT](https://srct.gmu.edu).

## Architecture of the project

### `go_back`

`go_back` is the API backend of the project. It is built with the Django REST
Framework (python). It supports all CRUD (Create, Read, Update, Delete)
operations on Go links as well as RegisteredUser account management.

### `go_ahead`

## Getting started with contributing

There's a workflow involved with getting started contributing but once you do
it once or twice it'll seem a lot less daunting.

1. React / Webpack


    ```sh
    yarn
    yarn dev
    ```

2.  Docker

    In another terminal tab:
    ```sh
    docker-compose up
    ```

3.  Actually coding

    All JS changes will require a refresh (Webpack rebuilds the app in the background).

    All Python changes will require a refresh. 


4.  Deployment of changes

    See me.