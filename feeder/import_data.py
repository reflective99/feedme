import json
from django.core.files import File

print "starting data import"

#execfile('feeder/import_data.py')

with open('feeder/yelp_data_durham.json') as data_file:    
    data = json.load(data_file)
    for rst in data:
      r = Restaurant(name=rst["name"], address=rst["address"], city=rst["city"], zip_code=rst["zip"], rating=rst["rating"], categories=rst["categories"])
      r.save()

with open('feeder/yelp_data_ch.json') as data_file:    
    data = json.load(data_file)
    for rst in data:
      r = Restaurant(name=rst["name"], address=rst["address"], city=rst["city"], zip_code=rst["zip"], rating=rst["rating"], categories=rst["categories"])
      r.save()
      
with open('feeder/yelp_data_dc.json') as data_file:    
    data = json.load(data_file)
    for rst in data:
      r = Restaurant(name=rst["name"], address=rst["address"], city=rst["city"], zip_code=rst["zip"], rating=rst["rating"], categories=rst["categories"])
      r.save()
      
with open('feeder/yelp_data_nyc.json') as data_file:    
    data = json.load(data_file)
    for rst in data:
      r = Restaurant(name=rst["name"], address=rst["address"], city=rst["city"], zip_code=rst["zip"], rating=rst["rating"], categories=rst["categories"])
      r.save()