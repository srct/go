until nc -z db 3306; do
    echo "waiting for database to start..."
    sleep 1
done

python go/manage.py flush --no-input 
python go/manage.py makemigrations 
python go/manage.py makemigrations go 
python go/manage.py migrate
python go/manage.py createsuperuser --noinput --username=$superuser --email=$superuser$email_domain
python go/manage.py runserver 0.0.0.0:8000