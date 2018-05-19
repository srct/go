#! /bin/bash
export GO_SECRET_KEY
export GO_CREATE_SUPERUSER

GO_SECRET_KEY=$(dd if=/dev/urandom count=100 | tr -dc "A-Za-z0-9" | fold -w 60 | head -n1 2>/dev/null)
GO_CREATE_SUPERUSER="from django.contrib.auth import get_user_model; User = get_user_model(); me = User.objects.get(username='$SUPERUSER'); me.first_name = 'David'; me.last_name = 'Haynes'; me.save(); "

python go/manage.py makemigrations
python go/manage.py makemigrations go
python go/manage.py migrate
python go/manage.py createsuperuser --noinput --username="$SUPERUSER" --email="$SUPERUSER$GO_EMAIL_DOMAIN"
echo "$GO_CREATE_SUPERUSER" | python go/manage.py shell
python go/manage.py runserver 0.0.0.0:8000
