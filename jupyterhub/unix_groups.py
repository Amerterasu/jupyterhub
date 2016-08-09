import requests
import json

import requests
api_url = 'http://127.0.0.1:8081/hub/api'
#probably should not upload tokens but the server has no real important data
token = '95182c3a040b4866aa54d25e2dc265ec'
pay_load = {"admin": False}
parameters = {"name" : 'guest'}
user = '/guest'
r = requests.patch(api_url + '/users' + user,
    headers={
        'Authorization': 'token %s' % token,
    },
    data = json.dumps(pay_load)
)
r.raise_for_status()
users = r.json()

print(users)
