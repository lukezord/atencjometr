import wykop

"""
TODO:
- user i token pobierany automatycznie?
- dodac ranking
- uporzadkowac otrzymane info (sam login i avatar) - JSON?!
- zliczenie subow
- monitorowanie sub4sub
- nie wiem
"""

user = "" #login
apkey = "" #klucz api
secret = "" #secret
accountkey = "" #token

api = wykop.WykopAPI(apkey, secret, output='clear')
api.authenticate(user, accountkey)

#ranking = api.get_rank?
followers = api.get_profile_followers(user)
followed = api.get_profile_followed(user)

#print("miejsce w rankingu:", ranking)
print("obserwujacy:", followers)
print("obserwujesz:", followed)


