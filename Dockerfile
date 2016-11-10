FROM python:2.7
ENV PYTHONUNBUFFERED 1
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
ENV host="*"  \
    email_domain="@masonlive.gmu.edu" \
    cas_url="https://nanderson.me/cas/" \
    superuser="dhaynes3" \
    SECRET_KEY="much-secret" \
    DB_NAME="go" \
    DB_USER="go" \
    DB_PASSWORD="go" \
    DB_HOST="" \
    PIWIK_SITE_ID="" \
    PIWIK_URL="" \
    EMAIL_HOST="" \
    EMAIL_PORT="" \
    EMAIL_HOST_USER="" \
    EMAIL_HOST_PASSWORD=""
