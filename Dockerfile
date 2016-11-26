FROM python:2.7
ENV PYTHONUNBUFFERED 1
# HEALTHCHECK CMD curl --fail http://localhost:8000/ || exit 1
RUN mkdir /go
WORKDIR /go
ADD requirements.txt /go/

RUN apt-get update
RUN apt-get install git-all -y
RUN apt-get install python2.7-dev -y
RUN apt-get install libsasl2-dev -y
RUN apt-get install libldap2-dev -y
RUN apt-get install netcat -y

RUN apt-get install 
RUN pip install -r requirements.txt
ADD . /go/

RUN mv go/settings/settings.docker.py.template go/settings/settings.py 
RUN mv go/settings/secret.docker.py.template go/settings/secret.py

