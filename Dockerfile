FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install netcat -y

RUN mkdir /go
WORKDIR /go
ADD /requirements/ /go/
RUN pip install -r base.txt
ADD . /go/
