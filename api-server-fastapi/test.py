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

for i in range(len(response.json()['rows'])):
    database.delete(database[str(response.json()['rows'][i]['id'])])
    print(f"document number {i} is deleted")

def generate_string()->list:
    import random
    letters_low = string.ascii_letters
    letters_up = string.ascii_letters.upper()
    digits = string.digits
    __list__ = []
    for i in range(8):
        __list__.append(list(digits)[random.randint(1,9)])
        __list__.append(list(letters_low + letters_up)[random.randint(1,50)])
    return __list__ 


n = 0
for i in range(30):
    json = {"ide":str(uuid.uuid4()), "title":""}
    json["title"] = "".join(generate_string())
    database.save(json)
    n = n + 1
    print(n)
    print(f'document {n} saved')

