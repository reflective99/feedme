"""
Yelp API v2.0 code sample.
This program demonstrates the capability of the Yelp API version 2.0
by using the Search API to query for businesses by a search term and location,
and the Business API to query additional information about the top result
from the search query.
Please refer to http://www.yelp.com/developers/documentation for the API documentation.
This program requires the Python oauth2 library, which you can install via:
`pip install -r requirements.txt`.
Sample usage of the program:
`python sample.py --term="bars" --location="San Francisco, CA"`
"""
"""
Adapted by Chris Dieckhaus for CS316 from https://github.com/Yelp/yelp-api/tree/master/v2/python
""" 
import argparse
import json
import pprint
import sys
import urllib
import urllib2

import oauth2


API_HOST = 'api.yelp.com'
DEFAULT_TERM = 'dinner'
DEFAULT_LOCATION = 'Durham, NC'
SEARCH_LIMIT = 49
SEARCH_PATH = '/v2/search/'

# OAuth credential placeholders that must be filled in by users.
CONSUMER_KEY = "oio8kbQbFadwmpSPcpq5kQ"
CONSUMER_SECRET = "HQCiaLe_MAs4Sqf9olD1YhoMY0M"
TOKEN = "c8ptpAaC37GVmmH8L44MjSTeqtPhivHs"
TOKEN_SECRET = "xB5FdHyftA1oE-4KZEdeCk1RhAs"


def request(host, path, url_params=None):
    """Prepares OAuth authentication and sends the request to the API.
    Args:
        host (str): The domain host of the API.
        path (str): The path of the API after the domain.
        url_params (dict): An optional set of query parameters in the request.
    Returns:
        dict: The JSON response from the request.
    Raises:
        urllib2.HTTPError: An error occurs from the HTTP request.
    """
    url_params = url_params or {}
    url = 'https://{0}{1}?'.format(host, urllib.quote(path.encode('utf8')))

    consumer = oauth2.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
    oauth_request = oauth2.Request(method="GET", url=url, parameters=url_params)

    oauth_request.update(
        {
            'oauth_nonce': oauth2.generate_nonce(),
            'oauth_timestamp': oauth2.generate_timestamp(),
            'oauth_token': TOKEN,
            'oauth_consumer_key': CONSUMER_KEY
        }
    )
    token = oauth2.Token(TOKEN, TOKEN_SECRET)
    oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
    signed_url = oauth_request.to_url()
    
    #print u'Querying {0} ...'.format(url)

    conn = urllib2.urlopen(signed_url, None)
    try:
        response = json.loads(conn.read())
    finally:
        conn.close()

    return response

def search(term, location):
    url_params = {
        'term': term.replace(' ', '+'),
        'location': location.replace(' ', '+')
    }
    return request(API_HOST, SEARCH_PATH, url_params=url_params)

def query_api(term, location):
    response = search(term, location)
    
    businesses = response.get('businesses')
    restaurant_list = []
    for business in businesses:
      categories = ""
      for cat in business['categories']:
        categories += ("*"+cat[0])
      address = ' '.join(business['location']['address'])
      city = business['location']['city']
      try:
        zip_code = business['location']['postal_code']
      except KeyError:
        zip_code = 00000
      rest_data = {}
      rest_data['name'] = business['name']
      rest_data['address'] = address
      rest_data['city'] = city
      rest_data['zip'] = zip_code
      try:
        rest_data['coords'] = business['location']['coordinate']
      except KeyError:
        rest_data['coords'] = 0000
      rest_data['rating'] = business['rating']
      rest_data['categories'] = categories
      restaurant_list.append(rest_data)
    print json.dumps(restaurant_list)

    
    
    if not businesses:
        print u'No businesses for {0} in {1} found.'.format(term, location)
        return

    #business_id = businesses[0]['id']

    #print u'{0} businesses found, querying business info for the top result "{1}" ...'.format(
        #len(businesses),
        #business_id
    #)

    #response = get_business(business_id)

    #print u'Result for business "{0}" found:'.format(business_id)
    #pprint.pprint(response, indent=2)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-q', '--term', dest='term', default=DEFAULT_TERM, type=str, help='Search term (default: %(default)s)')
    parser.add_argument('-l', '--location', dest='location', default=DEFAULT_LOCATION, type=str, help='Search location (default: %(default)s)')

    input_values = parser.parse_args()

    try:
        query_api(input_values.term, input_values.location)
    except urllib2.HTTPError as error:
        sys.exit('Encountered HTTP error {0}. Abort program.'.format(error.code))


if __name__ == '__main__':
    main()