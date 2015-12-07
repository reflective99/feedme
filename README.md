### Feed Me

A site that easily finds you a place to eat!

#### To import data

Clone the repo and cd into the first directory.

```
cd feedme/feedme
python yelp.py --location="Durham, NC" > ../feeder/yelp_data_durham.json
python yelp.py --location="Durham, NC" --term="breakfast" > ../feeder/yelp_data_durham_breakfast.json
python yelp.py --location="Durham, NC" --term="lunch" > ../feeder/yelp_data_durham_lunch.json
python yelp.py --location="Durham, NC" --term="bars" > ../feeder/yelp_data_durham_bars.json
python yelp.py --location="Durham, NC" --term="barbeque" > ../feeder/yelp_data_durham_bbq.json
python yelp.py --location="Durham, NC" --term="sushi" > ../feeder/yelp_data_durham_sushi.json
python yelp.py --location="Durham, NC" --term="italian" > ../feeder/yelp_data_durham_italian.json
python yelp.py --location="Durham, NC" --term="mexican" > ../feeder/yelp_data_durham_mex.json
python yelp.py --location="Chapel Hill, NC" > ../feeder/yelp_data_ch.json
python yelp.py --location="Chapel Hill, NC" --term="breakfast" > ../feeder/yelp_data_ch_breakfast.json
python yelp.py --location="Chapel Hill, NC" --term="lunch" > ../feeder/yelp_data_ch_lunch.json
python yelp.py --location="Chapel Hill, NC" --term="bars" > ../feeder/yelp_data_ch_bars.json
python yelp.py --location="Chapel Hill, NC" --term="barbeque" > ../feeder/yelp_data_ch_bbq.json
python yelp.py --location="Chapel Hill, NC" --term="sushi" > ../feeder/yelp_data_ch_sushi.json
python yelp.py --location="Chapel Hill, NC" --term="italian" > ../feeder/yelp_data_ch_italian.json
python yelp.py --location="Chapel Hill, NC" --term="mexican" > ../feeder/yelp_data_ch_mex.json
python yelp.py --location="Washington, DC" > ../feeder/yelp_data_dc.json
python yelp.py --location="Washington, DC" --term="breakfast" > ../feeder/yelp_data_dc_breakfast.json
python yelp.py --location="Washington, DC" --term="lunch" > ../feeder/yelp_data_dc_lunch.json
python yelp.py --location="Washington, DC" --term="bars" > ../feeder/yelp_data_dc_bars.json
python yelp.py --location="Washington, DC" --term="barbeque" > ../feeder/yelp_data_dc_bbq.json
python yelp.py --location="Washington, DC" --term="sushi" > ../feeder/yelp_data_dc_sushi.json
python yelp.py --location="Washington, DC" --term="italian" > ../feeder/yelp_data_dc_italian.json
python yelp.py --location="Washington, DC" --term="mexican" > ../feeder/yelp_data_dc_mex.json
python yelp.py --location="New York, NY" > ../feeder/yelp_data_nyc.json
python yelp.py --location="New York, NY" --term="breakfast" > ../feeder/yelp_data_nyc_breakfast.json
python yelp.py --location="New York, NY" --term="lunch" > ../feeder/yelp_data_nyc_lunch.json
python yelp.py --location="New York, NY" --term="bars" > ../feeder/yelp_data_nyc_bars.json
python yelp.py --location="New York, NY" --term="barbeque" > ../feeder/yelp_data_nyc_bbq.json
python yelp.py --location="New York, NY" --term="sushi" > ../feeder/yelp_data_nyc_sushi.json
python yelp.py --location="New York, NY" --term="italian" > ../feeder/yelp_data_nyc_italian.json
python yelp.py --location="New York, NY" --term="mexican" > ../feeder/yelp_data_nyc_mex.json
cd ..
python manage.py shell
```

Inside the shell:
```
from feeder.models import Restaurant
excefile('feeder/import_data.py')
```

After this, the Restaurant table should be populated.# feedme

AIzaSyALN-hUMbwHEiKz3JtcaXmS1w5o5Yob_Io
