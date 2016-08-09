import requests
import json

import requests
api_url = 'http://127.0.0.1:8081/hub/api'
#probably should not upload tokens but the server has no real important data
token = "79dd505f425d411bb994d4cbc09aec83"
pay_load = {"admin": True}
parameters = {"name" : 'khoa le'}
user = '/khoa le'
r = requests.patch(api_url + '/users' + user,
    headers={
        'Authorization': 'token %s' % token,
    },
    data = json.dumps(pay_load)
)
r.raise_for_status()
users = r.json()

print(users)
