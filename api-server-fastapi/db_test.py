import couchdb
import requests
import json
import string
import random
import importlib.util
module_spec = importlib.util.spec_from_file_location('config', 'C:/Users/33769/Desktop/config/config.py')
module = importlib.util.module_from_spec(module_spec)
module_spec.loader.exec_module(module)


list_char = string.ascii_letters + string.ascii_letters.upper() + string.digits
print(len(list_char))
while True:
    list_ = []
    for i in range(8):
        num = random.randint(1,110)
        list_.append(list_char[num])
    json = {"Title":str(''.join(list_))}
    database = couchdb.Database(f'http://{module.username}:{module.password}@127.0.0.1:5984/blogsportarticles')
    database.save(json)
    print(''.join(list_))