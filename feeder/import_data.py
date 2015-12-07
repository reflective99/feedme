import json
from django.core.files import File

print "starting data import"

#execfile('feeder/import_data.py')

with open('feeder/yelp_data_durham.json') as data_file:    
    data = json.load(data_file)
    for rst in data:
      print rst["rating"]
      if Restaurant.objects.filter(name = rst["name"]).exists() == False:  
          print "This doesn't exist"
          r = Restaurant(name=rst["name"], address=rst["address"], city=rst["city"], zip_code=rst["zip"], rating=rst["rating"], categories=rst["categories"])
          print r.categories
          r.save()
      else:
          print "Restaurant already exists in database"
          r = Restaurant.objects.get(name = rst["name"])
      print r.id
      for c in r.categories.split('*')[1:]:
        cgy = Category(rid=r.id, cat=c)
        print cgy.rid
        print cgy.cat
        cgy.save()

with open('feeder/yelp_data_ch.json') as data_file:    
    data = json.load(data_file)
    for rst in data:

      if Restaurant.objects.filter(name = rst["name"]).exists() == False:  
          print "This doesn't exist"
          r = Restaurant(name=rst["name"], address=rst["address"], city=rst["city"], zip_code=rst["zip"], rating=rst["rating"], categories=rst["categories"])
          print r.categories
          r.save()
      else:
          print "Restaurant already exists in database"
          r = Restaurant.objects.get(name = rst["name"])
      print r.id
      for c in r.categories.split('*')[1:]:
        cgy = Category(rid=r.id, cat=c)
        print cgy.rid
        print cgy.cat
        cgy.save()
      
with open('feeder/yelp_data_dc.json') as data_file:    
    data = json.load(data_file)
    for rst in data:

      if Restaurant.objects.filter(name = rst["name"]).exists() == False:  
          print "This doesn't exist"
          r = Restaurant(name=rst["name"], address=rst["address"], city=rst["city"], zip_code=rst["zip"], rating=rst["rating"], categories=rst["categories"])
          print r.categories
          r.save()
      else:
          print "Restaurant already exists in database"
          r = Restaurant.objects.get(name = rst["name"])
      print r.id
      for c in r.categories.split('*')[1:]:
        cgy = Category(rid=r.id, cat=c)
        print cgy.rid
        print cgy.cat
        cgy.save()
      
with open('feeder/yelp_data_nyc.json') as data_file:    
    data = json.load(data_file)
    for rst in data:

      if Restaurant.objects.filter(name = rst["name"]).exists() == False:  
          print "This doesn't exist"
          r = Restaurant(name=rst["name"], address=rst["address"], city=rst["city"], zip_code=rst["zip"], rating=rst["rating"], categories=rst["categories"])
          print r.categories
          r.save()
      else:
          print "Restaurant already exists in database"
          r = Restaurant.objects.get(name = rst["name"])
      print r.id
      for c in r.categories.split('*')[1:]:
        cgy = Category(rid=r.id, cat=c)
        print cgy.rid
        print cgy.cat
        cgy.save()