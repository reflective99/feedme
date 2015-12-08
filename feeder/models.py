from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=25)
    zip_code = models.IntegerField()
    rating = models.FloatField()
    
    def __unicode__(self):
        return self.name
        
class Likes(models.Model):
    uid = models.ManyToManyField(User)
    rid = models.ManyToManyField(Restaurant)
    
   
class Like(models.Model):
    uid = models.IntegerField()
    rid = models.IntegerField()
    
class Category(models.Model):
    rid = models.IntegerField()
    cat = models.CharField(db_index = True, max_length=100)
    
  
