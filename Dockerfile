FROM python:2.7
ENV PYTHONUNBUFFERED 1
# currently this doesnt do anything 

RUN mkdir /go
WORKDIR /go
ADD requirements.txt /go/
# 
RUN apt-get update
RUN apt-get install git-all -y
RUN apt-get install python2.7-dev -y
RUN apt-get install libsasl2-dev -y
RUN apt-get install libldap2-dev -y
RUN apt-get install 
RUN pip install -r requirements.txt
ADD . /go/

