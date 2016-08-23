import requests
import json
import grp
import requests
import sys, getopt

class Unix_Groups:
    API_URL = 'http://127.0.0.1:8081/hub/api'

    def createNewUser(self, users):
        payload = json.dumps({"usernames": users ,"admin" : True})
        r = requests.post(self.API_URL + '/users',
            headers = {
                'Authorization' : 'token %s' % self.token,
            },
            data = payload
        )
    def tokenAdmin(self, token):
        rUrl = self.API_URL + '/authorizations/token/' + token
        r = requests.get(rUrl,
            headers = {
                'Authorization' : 'token %s' % token,
            }
        )
        userData = r.json()
        return userData['admin']
    def getUserData(self, user, token):
        #args:
        # user - the targeted user info
        # token - token of user trying to query the API. Careful if token of non Admin user
        r = requests.get(self.API_URL + '/users/' + user,
            headers = {
                'Authorization' : 'token %s' % token,
            }
        )
        if r.status_code == 404:
            return r.status_code
        else:
            return r.json()
        return r.json()
    def setUserAdmin(self, user, admin):
        payload = json.dumps({"admin" : admin})
        #userData = self.getUserData(user,self.token)

        r = requests.patch(self.API_URL + '/users/' + user,
            headers = {
                'Authorization' : 'token %s' % self.token
            },
            data = payload
        )

        return r.json()
    def __init__(self, user, token, groupList):
        self.token = token
        self.groups = groupList
        self.newuser = user
        createUserList = []
        isAdmin = self.tokenAdmin(token)
        if not isAdmin:
            print("Given user is not an admin. Can not set admins")
        else:
            for group in self.groups:
                members = grp.getgrnam(group).gr_mem
                for member in members:
                    userdata = self.getUserData(member, self.token)
                    if userdata == 404:
                        createUserList.append(member)
                    else:
                        self.setUserAdmin(member, True)
        #empty creatuser list afterwards
            if createUserList and self.newuser:
                self.createNewUser(createUserList)
                del createUserList[:]
            elif createUserList and not self.newuser:
                print("The following users were not created: ")
                print(createUserList)
    # def update(groupList):
    #     groups = groupList
    #     diff = list(set(self.groups) - set(groups))
    #     for group in groups:
    #         members = grp.getgrnam(group).gr_mem
    #         for member in members:
    #             setUserAdmin(member, True)

def main(argv):
    newuser = True
    token = '336e608c4ede4329bf9347e999a81b99'
    groups = ['philliple']
    try:
      opts, args = getopt.getopt(argv,"a:ug:t:")
    except getopt.GetoptError:
      print("Invalid Argument")
      sys.exit(2)
    for opt, arg in opts:
      if opt == '-g':
        groups.append(arg)
        print("using group options")
      elif opt == '-u':
        print("Toggle new user creation off")
        newuser = False
      elif opt == '-t':
        print("Set Token (use admin token)")
        token = arg
      elif opt == '-a':
          print("Set API URL")
          api_url = arg
    unix = Unix_Groups(newuser, token, groups)


if __name__ == "__main__":
    main(sys.argv[1:])
#testing
# token = '336e608c4ede4329bf9347e999a81b99'
# user = '/test'
# groups = ['philliple']
# for group in groups:
#     print(grp.getgrnam(group).gr_mem)
# unix = Unix_Groups(user, token, groups)
