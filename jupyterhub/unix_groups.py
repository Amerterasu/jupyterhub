import requests

import requests
api_url = 'http://127.0.0.1:8081/hub/api'
token = "79dddaf639aa4b97b5975f5b9ca32c8a"
pay_load = {"admin" : False}
parameters = {"name" : 'khoa le'}
user = '/khoa le'
r = requests.patch(api_url + '/users' + user,
    headers={
        'Authorization': 'token %s' % token,
    },
    params = parameters,
    data = pay_load
)
r.raise_for_status()
users = r.json()

print(users)
