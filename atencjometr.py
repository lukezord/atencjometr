import wykop
#import mysql.connector

"""
TODO:
- user i token pobierany automatycznie?
- dodac ranking
- monitorowanie sub4sub
- zrzut do sqla
- pobiera 25 pozycji z obserwujacych - REST next page? - nie wiem jak ale sie dowiem :| na chwile obecna jest rak XD
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
from ld import username, apkey, secret, accountkey

api = wykop.WykopAPI(apkey, secret, output='clear')
api.authenticate(username, accountkey)
profile = api.get_profile(username)

profile["followers"]
print "Obserwujacy:", profile.followers #liczymy suby

profile["following"]
print "Obserwujesz:", profile.following #liczymy zasubowanych

            
for followers_list in api.get_profile_followers(username, page=1):
   file = open('followers.txt', 'a')
   file.write(str(followers_list['login'] + "\n"))
   file.close()

for followers_list in api.get_profile_followers(username, page=2):
   file = open('followers.txt', 'a')
   file.write(str(followers_list['login'] + "\n"))
   file.close()

for followers_list in api.get_profile_followers(username, page=3):
   file = open('followers.txt', 'a')
   file.write(str(followers_list['login'] + "\n"))
   file.close()
   
for followers_list in api.get_profile_followers(username, page=4):
   file = open('followers.txt', 'a')
   file.write(str(followers_list['login'] + "\n"))
   file.close()
   
for followers_list in api.get_profile_followers(username, page=5):
   file = open('followers.txt', 'a')
   file.write(str(followers_list['login'] + "\n"))
   file.close()