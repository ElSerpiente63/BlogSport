import requests
import json
import hashlib
import couchdb
import config
from config import *
database = couchdb.Database(f"http://{username}:{password}@127.0.0.1:5984/blogsportusers")
password = "pythonmaster63"
json = {"username":"Ayoub", "password":hashlib.md5(str.encode(password)).hexdigest()}
if database.save(json):
    print('Done')
else:
    print('not done')

