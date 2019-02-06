#! /bin/bash
export GO_SECRET_KEY

until nc -z db 3306; do
    echo "waiting for database to start..."
    sleep 1
done

GO_SECRET_KEY=$(dd if=/dev/urandom count=100 | tr -dc "A-Za-z0-9" | fold -w 60 | head -n1 2>/dev/null)

yarn build

python go/manage.py makemigrations
python go/manage.py makemigrations go_back
python go/manage.py makemigrations go_ahead
python go/manage.py migrate
python go/manage.py runserver 0.0.0.0:8000
