A site that easily finds you a place to eat

To import data

Clone the repo and cd into the first directory.

cd feedme/feedme
python yelp.py --location="Durham, NC" > ../feeder/yelp_data_durham.json
python yelp.py --location="Chapel Hill, NC" > ../feeder/yelp_data_ch.json
python yelp.py --location="Washington, DC" > ../feeder/yelp_data_dc.json
python yelp.py --location="New York, NY" > ../feeder/yelp_data_nyc.json
cd ..
python manage.py shell
Inside the shell:

from feeder.models import Restaurant
excefile('feeder/import_data.py')
After this, the Restaurant table should be populated.# feedme

AIzaSyALN-hUMbwHEiKz3JtcaXmS1w5o5Yob_Io
