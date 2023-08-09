import couchdb
import json
import requests
import uuid
import importlib.util
import string
import random as rand 
module_spec = importlib.util.spec_from_file_location('config', 'C:/Users/33769/Desktop/config/config.py')
module = importlib.util.module_from_spec(module_spec)
module_spec.loader.exec_module(module)
response = requests.get(f'http://{module.username}:{module.password}@127.0.0.1:5984/blogsportarticles/_design/title/_view/title')
database = couchdb.Database(f"http://{module.username}:{module.password}@127.0.0.1:5984/blogsportarticles")
char = list(string.ascii_letters) + list(string.ascii_letters.upper())
print(char)
print(response.json())
__list__ = []
for i in range(len(response.json()['rows'])):
    __list__.append(response.json()['rows'][i]['id'])

for i in range(len(__list__)):
    id_doc = __list__[i]
    key = 'content'
    document = database[id_doc]
    _text_ = []
    for i in range(800):
        _text_.append(char[rand.randint(0, len(char)-1)])
    document[key] = "".join(_text_)
    database[id_doc] = document
for i in range(len(__list__)):
    id_doc = __list__[i]
    key = 'ide'
    document = database[id_doc]
    document[key] = str(uuid.uuid4()) 
    database[id_doc] = document 
res = requests.get(f"http://{module.username}:{module.password}@127.0.0.1:5984/blogsportarticles/_design/title/_view/title")
print(res.json())
print('Done')
