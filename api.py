import fastapi
import requests
import couchdb
from fastapi import FastAPI
import pydantic
from pydantic import Optional, BaseModel
import requests 

class Articles(BaseModel):
    content: str
    __id__: int
    author: str
    token: str
    password: str
    username: str

class Login(BaseModel):
    username: str
    password: Optional[str]
#vue couchdb à créer, les appels db/vue ne sont pas officiels
@api.post('/login')
async def admin_login(login: Login):
    response = requests.get("http://admin:pass@127.0.0.1:5084/BlogSport/_design/login/_view/loadlogin?key='" + login['username'] + '"')
    print(response)
    doc = response.json()
    database = couchdb.Database('BlogSportSession')
    token = str(uuid.uuid4())
    payload = {
        "username":login['username'],
        "password":login['password'],
        "token":token,
    }
    print(token)
    if login['username'] == doc['rows'][0]['key'] and login['password'] == doc['rows'][0]['value']['password']:
        database.save()
        return {"Passed":"True"}
    else:
        return {"Passed":"False"}

@api.post('/articles')
async def articles_online(articles_info: Articles):
    url = 'http://admin:pass@127.0.0.1:5084/BlogSport/_design'
    response = requests.get(url)