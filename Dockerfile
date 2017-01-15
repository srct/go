FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install libsasl2-dev -y
RUN apt-get install libldap2-dev -y
RUN apt-get install netcat -y

RUN mkdir /go
WORKDIR /go
ADD requirements.txt /go/
RUN pip install -r requirements.txt
ADD . /go/
