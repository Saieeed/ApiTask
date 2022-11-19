from fastapi import Depends,FastAPI , Header, HTTPException ,Response,status
from fastapi.security import OAuth2PasswordBearer
import uvicorn 
import json



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="")

async def get_query_token(token: str = Depends( oauth2_scheme ) ):
    f = open ('config.json', "r")
    data = json.load(f)
   # print(data)
    key = data["token"]
    f.close()
    if token != key:
        return False 
    return True

def get_token():
    f = open ('config.json', "r")
    data = json.load(f)
    return data["token"]