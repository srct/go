FROM python:3.6.9
ENV PYTHONUNBUFFERED 1
RUN apt-get update
RUN apt-get install netcat python3-dev default-libmysqlclient-dev -y

# downgrade openssl security for login.gmu.edu compatibility
RUN sed -i -e 's/DEFAULT@SECLEVEL=2/DEFAULT@SECLEVEL=1/g' /etc/ssl/openssl.cnf

RUN mkdir /go
WORKDIR /go
ADD /requirements/ /go/
RUN pip install -r base.txt
ADD . /go/
