# Build on top of the python image and install any external packages
FROM python:3.7
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


RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get install -y nodejs
RUN apt-get install -y build-essential
RUN npm install -g yarn