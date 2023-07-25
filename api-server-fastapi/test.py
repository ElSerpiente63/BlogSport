import couchdb
import json
import requests
import uuid
import importlib.util
import string
module_spec = importlib.util.spec_from_file_location('config', 'C:/Users/33769/Desktop/config/config.py')
module = importlib.util.module_from_spec(module_spec)
module_spec.loader.exec_module(module)
response = requests.get(f'http://{module.username}:{module.password}@127.0.0.1:5984/blogsportarticles/_design/title/_view/title')
database = couchdb.Database(f"http://{module.username}:{module.password}@127.0.0.1:5984/blogsportarticles")

print(response.json())
__list__ = []
for i in range(len(response.json()['rows'])):
    __list__.append(response.json()['rows'][i]['id'])

for i in range(len(__list__)):
    id_doc = __list__[i]
    new_key = 'content'
    new_value = str(uuid.uuid4())
    doc = database[id_doc]
    doc[new_key] = new_value
    database[id_doc] = doc
print('Done')
