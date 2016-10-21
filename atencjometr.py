import wykop
import sqlite3

"""
TODO:
- user i token pobierany automatycznie?
- dodac ranking
- monitorowanie sub4sub
- porownac wyniki z tymi w bazie
"""



from ld import username, apkey, secret, accountkey

api = wykop.WykopAPI(apkey, secret, output='clear')
api.authenticate(username, accountkey)
profile = api.get_profile(username)


conn = sqlite3.connect('atencja.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS podsumowanie
(obserwujacy real, obserwujesz real)''')
c.execute('''CREATE TABLE IF NOT EXISTS obserwuja
(followers text UNIQUE)''')
c.execute('''CREATE TABLE IF NOT EXISTS obserwuje
(followed text UNIQUE)''')
c.execute ("INSERT INTO podsumowanie VALUES (?, ?)", [profile["followers"], profile["following"]]) #ilosc subow
for i in range(1, 16):
    for followers_list in api.get_profile_followers(username, page=i):
        c.execute ("INSERT OR IGNORE INTO obserwuja VALUES (?)", [followers_list["login"]]) #obserwuja mnie
for i in range(1,16):
    for followed_list in api.get_profile_followed(username, page=i):
        c.execute ("INSERT OR IGNORE INTO obserwuje VALUES (?)", [followed_list["login"]]) #ja obserwuje

for i in range(1,16):
    for followed_list in api.get_profile_followed(username, page=i):
        for row in c.execute ("SELECT * FROM obserwuje WHERE followed NOT IN (?)", [followed_list["login"]])
        print row

conn.commit()
conn.close()

