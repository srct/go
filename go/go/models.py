from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class URL( models.Model ):
    owner = models.OneToOneField( User )
    date_created = models.DateTimeField( default=timezone.now() )

    target = models.CharField( max_length = 1000 )
    short = models.CharField( primary_key = True, max_length = 50 )
    clicks = models.IntegerField( default = 0 )
    expires = models.DateTimeField( blank = True, null = True )
