import json
from django.core.files import File

print "starting data import"

#execfile('feeder/import_data.py')

files = ['feeder/yelp_data_durham.json',
        'feeder/yelp_data_durham_breakfast.json',
        'feeder/yelp_data_durham_lunch.json' ,
        'feeder/yelp_data_durham_bars.json',
        'feeder/yelp_data_durham_bbq.json',
        'feeder/yelp_data_durham_sushi.json',
        'feeder/yelp_data_durham_italian.json',
        'feeder/yelp_data_durham_mex.json',
        'feeder/yelp_data_durham_korean.json',
        'feeder/yelp_data_durham_sw.json',
        'feeder/yelp_data_durham_pizza.json',
        'feeder/yelp_data_durham_cheap.json',
        'feeder/yelp_data_ch.json',
        'feeder/yelp_data_ch_breakfast.json',
        'feeder/yelp_data_ch_lunch.json',
        'feeder/yelp_data_ch_bars.json',
        'feeder/yelp_data_ch_bbq.json',
        'feeder/yelp_data_ch_sushi.json',
        'feeder/yelp_data_ch_italian.json',
        'feeder/yelp_data_ch_mex.json',
        'feeder/yelp_data_ch_korean.json',
        'feeder/yelp_data_ch_sw.json',
        'feeder/yelp_data_ch_cheap.json',
        'feeder/yelp_data_dc.json',
        'feeder/yelp_data_dc_breakfast.json',
        'feeder/yelp_data_dc_lunch.json',
        'feeder/yelp_data_dc_bars.json',
        'feeder/yelp_data_dc_sushi.json',
        'feeder/yelp_data_dc_italian.json',
        'feeder/yelp_data_dc_mex.json',
        'feeder/yelp_data_dc_korean.json',
        'feeder/yelp_data_dc_sw.json',
        'feeder/yelp_data_dc_cheap.json',
        'feeder/yelp_data_nyc.json',
        'feeder/yelp_data_nyc_breakfast.json',
        'feeder/yelp_data_nyc_lunch.json',
        'feeder/yelp_data_nyc_bars.json',
        'feeder/yelp_data_nyc_bbq.json',
        'feeder/yelp_data_nyc_sushi.json',
        'feeder/yelp_data_nyc_italian.json',
        'feeder/yelp_data_nyc_mex.json',
        'feeder/yelp_data_nyc_korean.json',
        'feeder/yelp_data_nyc_sw.json',
        'feeder/yelp_data_nyc_cheap.json'
        ]

count = 0

for f in files:
  with open(f) as data_file:
    print f
    data = json.load(data_file)
    for rst in data:
      count += 1
      print "Name: " + rst["name"]
      print "City : " +rst["city"]
      if Restaurant.objects.filter(name = rst["name"]).exists() == False:
        print "This restaurant is not in the database. Adding to db..."
        r = Restaurant(name=rst["name"], address=rst["address"], city=rst["city"], zip_code=rst["zip"], rating=rst["rating"])
        r.save()
      else:
        print "Restaurant already exists in database"
        r = Restaurant.objects.get(name = rst["name"])
      print r.id
      for c in rst["categories"].split('*')[1:]:
        if Category.objects.filter(rid=r.id, cat=c).exists() == False:
          cgy = Category(rid=r.id, cat=c)
          print cgy.rid
          print cgy.cat
          cgy.save()
print count
