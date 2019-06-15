'''retrieves a list of links to all nyc 311 services and a brief description of each service'''

import requests
import os
import json

# Set environment variables

app_id = os.environ.get('app_id')
app_key = os.environ.get('app_key')

# Create Session

url_base = 'https://api.cityofnewyork.us/311/v1/'
querystring = {"app_id":app_id,"app_key":app_key}
s = requests.Session()
r = s.get(url_base +'services' + '/' + 'all.json?', params=querystring, verify=False)

# Save results as text to working dir

with open("all_services", "w") as f:
    f.write(r.text)
