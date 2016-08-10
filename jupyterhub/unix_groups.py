import requests
import json
import grp
import requests
import sys

class Unix_Groups:
    API_URL = 'http://127.0.0.1:8081/hub/api'
    def getUserData(self, user, token):
        #args:
        # user - the targeted user info
        # token - token of user trying to query the API. Careful if token of non Admin user
        r = requests.get(self.API_URL + '/users' + user,
            headers = {
                'Authorization' : 'token %s' % token,
            }
        )
        r.raise_for_status()
        return r.json()
    def __init__(self, user, token, groupList):
        self.token = token
        self.groups = groupList
        userData = self.getUserData(user, token)
        if not userData['admin']:
            print("Given user is not an admin. Some API calls will be unavailable such as changing other users' data")
        else:
            for group in groups:
                members = grp.getgrnam(group).gr_mem
                print(members)
    def update(groupList):
        groups = groupList
        diff = list(set(self.groups) - set(groups))
        for group in groups:
            members = grp.getgrnam(group).gr_mem
            for member in members:
                user = self.getUserData(member, )


token = '95182c3a040b4866aa54d25e2dc265ec'
pay_load = {"admin": False}
parameters = {"name" : 'guest'}
user = '/khoa le'
groups = ['everyone']
unix = Unix_Groups(user, token, groups)
