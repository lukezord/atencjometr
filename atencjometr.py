import wykop, io, json
#import mysql.connector

"""
TODO:
- user i token pobierany automatycznie?
- dodac ranking
- uporzadkowac otrzymane info (sam login i avatar) - JSON?!
- zliczenie subow
- monitorowanie sub4sub
- zrzut do sqla
- nie wiem
"""
#MYSQL - logowanie do bazy - na pozniej

"""config = {

    'user': '',
    'password': '',
    'host': '',
    'database': '',
    'raise_on_warnings': True,
    'use_pure': False,
}

cnx = mysql.connector.connect(**config)
cnx.close()
"""
from ld import user, apkey, secret, accountkey

api = wykop.WykopAPI(apkey, secret, output='clear')
api.authenticate(user, accountkey)
profile = api.get_profile(user)

profile["followers"]
print "Obserwujacy:", profile.followers #liczymy suby

profile["following"]
print "Obserwujesz:", profile.following #liczymy zasubowanych
"""
subnames = api.get_profile_followers(user)
subnames["login"]
print "Obserwujacy:", subnames.login #nie dziala ;_;

"""




