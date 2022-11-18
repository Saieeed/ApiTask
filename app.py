from fastapi import Depends,FastAPI , Header, HTTPException ,Response,status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
from dependincies import get_query_token
from get_response import myResponse 
import uvicorn 
import json
#from typing import Union

app = FastAPI()


    

@app.get("/quote/random" )  
async def read_items(  response : Response , check : int  = Depends(get_query_token) ):  
    if check == False:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"Message" :" You are not authorized to use this API!" }
    else :
        r = await myResponse()
        r.getResponse()
        if r.quoteId == "" or r.quoteName == "" or r.author ==  "":
            return JSONResponse(content={"Message": "couldn't load data"}, status_code=500)
        else:
            return JSONResponse(content={"quoteId":str(r.quoteId)  , "quote":str(r.quoteName) , "author":r.author} , status_code=200)


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