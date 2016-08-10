import requests
import json
import grp
import requests
import sys

class Unix_Groups:
    API_URL = 'http://127.0.0.1:8081/hub/api'

    def tokenAdmin(self, token):
        rUrl = self.API_URL + '/authorizations/token/' + token
        r = requests.get(rUrl,
            headers = {
                'Authorization' : 'token %s' % token,
            }
        )
        userData = r.json()
        print(r.json())
        return userData['admin']
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
        print(r.json())
        return r.json()
    def setUserAdmin(self, user, admin):
        payload = json.dumps({"admin" : admin})
        userData = self.getUserData(user,self.token)

        r = request.patch(self.API_URL + '/users' + user,
            headers = {
                'Authorization' : 'toekn %s' % self.token
            },
            data = payload
        )
        r.raise_for_status()
        return r.json()
    def __init__(self, user, token, groupList):
        self.token = token
        self.groups = groupList
        isAdmin = self.tokenAdmin(token)
        if not isAdmin:
            print("Given user is not an admin. Can not set admins")
        else:
            for group in groups:
                members = grp.getgrnam(group).gr_mem
                for member in members:
                    setUserAdmin(member, True)

    def update(groupList):
        groups = groupList
        diff = list(set(self.groups) - set(groups))
        for group in groups:
            members = grp.getgrnam(group).gr_mem
            for member in members:
                setUserAdmin(member, True)


#testing
token = '95182c3a040b4866aa54d25e2dc265ec'
pay_load = {"admin": False}
parameters = {"name" : 'guest'}
user = '/guest'
groups = ['everyone']
unix = Unix_Groups(user, token, groups)
