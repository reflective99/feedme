from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=15)
    zip_code = models.IntegerField()
    rating = models.IntegerField()
    categories = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.name
    
