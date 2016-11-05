python go/manage.py flush --no-input 
python go/manage.py makemigrations 
python go/manage.py makemigrations go 
python go/manage.py migrate
python go/manage.py createsuperuser --noinput --username=dhaynes3 --email=dhaynes3@masonlive.gmu.edu
# #echo "from django.contrib.auth.models import User; User.objects.create_superuser('dhaynes3', 'admin@example.com', 'pass')" | python manage.py shell
python go/manage.py runserver 0.0.0.0:8000