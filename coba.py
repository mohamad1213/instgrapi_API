from instagrapi import Client
from time import sleep
ACCOUNT_USERNAME = 'koisugara'
ACCOUNT_PASSWORD = 'katakanlah123'
cl = Client()
cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)
# for u in user_id:
#     print(u.username)
for i in range(60):
    user_id = cl.search_users(query="hatami.io")
    print (str(i) + ' --> ' + str(len(list(user_id))))
    sleep(5)