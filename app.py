from fastapi import Depends,FastAPI , Header, HTTPException ,Response,status
from fastapi.security import OAuth2PasswordBearer
import uvicorn 
import json


#from typing import Union

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="")




async def verify(token: str = Depends( oauth2_scheme ) ):
    f = open ('config.json', "r")
    data = json.load(f)
    print(data)
    key = data["token"]
    if token != key:
        #return "You are not authorized to use this API!"
        return False 
    return True
    

@app.get("/quote/random" ,dependencies=[Depends(verify)] , status_code= 200 )  
async def read_items(  response : Response , check : int  = Depends(verify) ):  
    if check == False:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"Message" :" You are not authorized to use this API!" }
    else :
        response.status_code = status.HTTP_200_OK
        return { "will be implemented"}


# import random
# import uvicorn
# from fastapi import FastAPI
# from fastapi.responses import JSONResponse

# app = FastAPI()

# def divide(a, b):
#     print(f"Dividing {a} / {b} ...")
#     result = a / b
#     print(f"Result is {result}")

# @app.get("/")
# def read_root():
#     print("Request started")
#     a = 100
#     b = random.randint(0, 1)

#     try:
#         return {"success": True, "result": divide(a, b)}

#     except Exception as ex:
#         print(f"Request failed: {ex}")
#         return JSONResponse(content={"success": False}, status_code=500)

#     finally:
#         print("Request ended")
if __name__ == "__main__":
    uvicorn.run(app)