# go_back | The django API

If you have taken CS 112, you should be somewhat familiar with the fundamentals of Python. This is nice for building simple applications, but in the real world we utilize larger scale frameworks to help us with the heavy lifting for tasks such as building websites.

[Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.](https://www.djangoproject.com/) They designed the framework for to allow for rapid iteration, be secure by default, and scale outwards with ease.

It is necessary you become familiar with the concepts of the Django framework:

1. The [Django Overview](https://docs.djangoproject.com/en/2.1/intro/overview/) does a good job at highlighting specific components.
1. The [Django Rest Framework tutorial](https://www.django-rest-framework.org/tutorial/1-serialization/) walks through how to utilize Django components in building an API.

## The gist

1. Store data in models.

1. Extract data from models with serializers.

1. Present data with views.

1. Navigate to views with urls.

## Dev work

You will need to install the latest version of python 3.

```
pip install pipenv
pipenv install
pipenv shell
```

With docker-compose running the app, you can open a code editor to work on the API. All errors are printed to the docker console stdout.
