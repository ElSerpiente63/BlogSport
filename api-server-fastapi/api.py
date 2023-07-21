import fastapi
import requests
import couchdb
from fastapi import FastAPI
import pydantic
from pydantic import BaseModel
import hashlib
from hashlib import md5 
import uvicorn
from uvicorn import *
import regex as re
import validate_email
from validate_email import validate_email


class Articles(BaseModel):
    content: str
    author: str
    token: str
    password: str
    username: str

class Register(BaseModel):
    username: str
    password: str

class Login(BaseModel):
    username: str
    password: str

class Content(BaseModel):
    id: str
    title: str


import importlib.util
module_spec = importlib.util.spec_from_file_location('config', 'C:/Users/33769/Desktop/config/config.py')
module = importlib.util.module_from_spec(module_spec)
module_spec.loader.exec_module(module)

api = FastAPI()
#vue couchdb à créer, les appels db/vue ne sont pas officiels
@api.post('/login')
async def admin_login(login: Login):
    response = requests.get(f"http://{module.username}:{module.password}@127.0.0.1:5984/blogsportusers/_design/login/_view/loadlogin?key='" + login['username'] + '"')
    print(response)
    doc = response.json()
    database = couchdb.Database(f'http://{module.username}:{module.password}@127.0.0.1:5984/blogsportsession')
    token = str(uuid.uuid4())
    hashed_token = hashlib.md5(str.encode(token)).hexdigest()
    payload = {
        "username":login['username'],
        "password":login['password'],
        "token":hashed_token,
    }
    print(token)
    if login['username'] == doc['rows'][0]['key'] and hashlib.md5(str.encode(login['password'])).hexdigest() == doc['rows'][0]['value']['password']:
        database.save(payload)
        return {"Passed":"True"}
    else:
        return {"Passed":"False"}

@api.post('/register')    
async def register(reg: Register):
    url = f"http://{module.username}:{module.password}@127.0.0.1:5984/blogsportusers/_design/Users/_view/Register?key='" + reg['username'] + '"'
    response = requests.get(url)
    doc = response.text
    database = couchdb.Database(f'http:{module.username}:{module.password}@127.0.0.1:5984/blogsportusers')
    payload = {
        "username": reg["username"],
        "password":hashlib.md5(str.encode(reg['password'])).hexdigest()
    } 
    if len(reg['username']) != 0 and len(reg['password']) > 8 and reg['username'] not in doc and validate_email(reg['username']) :
        database.save(payload)
        return {"Registered":"True"}
    else:
        return {"Error while registering"}


@api.post('/post_articles')
async def post_articles(articles: Articles)->dict:
    random_id = str(uuid.uuid4())
    articles['__id__'] = random_id
    token_hash = hashlib.md5(str.encode(articles['token'])).hexdigest()
    url = f"http://{module.username}:{module.password}@127.0.0.1:5984/blogsportsession/_design/Sessions/_view/connection?key='{token_hash}"
    database = couchdb.Database(url)
    response = requests.get(url)
    doc = response.json()
    #pas sur pour cette condition faut que j'analyse la réponse que me donne la db
    if str(token_hash) == doc['rows'][0]['key']:
        database.save(articles)
    else:
        return {"Status":"Not done"}


@api.get("/articles")
async def get_articles()->dict:
    response = requests.get(f"http://{module.username}:{module.password}@127.0.0.1:5984/blogsportarticles/_design/title/_view/title")
    print(len(response.json()['rows']))
    __list__ = []
    for i in range(len(response.json()['rows'])):
        __list__.append({"title":response.json()['rows'][i]['key'], "id":response.json()['rows'][i]['value']})
    return __list__
 
@api.get("/content")
async def return_content(content: Content):
    url = f"http://{module.username}:{module.password}@127.0.0.1:5984/blogsport"
    response = requests.get()
 
if __name__ == '__main__':
    uvicorn.run(api, host='127.0.0.1', port=4001)