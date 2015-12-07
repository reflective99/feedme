import json
from django.core.files import File

print "starting data import"

#execfile('feeder/import_data.py')

files = ['feeder/yelp_data_durham.json', 'feeder/yelp_data_durham_breakfast.json', 'feeder/yelp_data_durham_lunch.json', 'feeder/yelp_data_ch.json', 'feeder/yelp_data_ch_breakfast.json', 'feeder/yelp_data_ch_lunch.json', 'feeder/yelp_data_dc.json', 'feeder/yelp_data_dc_breakfast.json', 'feeder/yelp_data_dc_lunch.json', 'feeder/yelp_data_nyc.json', 'feeder/yelp_data_nyc_breakfast.json', 'feeder/yelp_data_nyc_lunch.json']

count = 0

for f in files:
  with open(f) as data_file:   
    print f 
    data = json.load(data_file)
    for rst in data:
      count += 1
      print rst["name"]
      print rst["rating"]
      if Restaurant.objects.filter(name = rst["name"]).exists() == False:  
        print "This restaurant is not in the database. Adding to db..."
        r = Restaurant(name=rst["name"], address=rst["address"], city=rst["city"], zip_code=rst["zip"], rating=rst["rating"], categories=rst["categories"])
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
print count
