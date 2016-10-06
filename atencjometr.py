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

# zapisujemy dane do pliku

with io.open('followers.txt', 'w', encoding='utf-8') as f:
    f.write(unicode(json.dumps(api.get_profile_followers(user), ensure_ascii=False)))

with io.open('followed.txt', 'w', encoding='utf-8') as f:
    f.write(unicode(json.dumps(api.get_profile_followed(user), ensure_ascii=False)))






