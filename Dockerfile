# Build on top of the python image and install any external packages
FROM python:3.6
RUN apt-get update
RUN apt-get install netcat -y

# Set enviornment variables
ENV PYTHONUNBUFFERED 1

# Copy over all project files into /go/
RUN mkdir /go/
WORKDIR /go/
ADD . /go/

# Install pip dependecies
RUN pip install pipenv
RUN pipenv install --system --deploy
