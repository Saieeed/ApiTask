from fastapi import Depends,FastAPI , Header, HTTPException ,Response,status
from fastapi.security import OAuth2PasswordBearer

#from typing import Union

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="SHEBAK@2022")




async def verify(token: str = Depends( oauth2_scheme ) ):
    if token != "SHEBAK@2022":
        #return "You are not authorized to use this API!"
        return 0 
    return 1
    

@app.get("/quote/random" ,dependencies=[Depends(verify)] , status_code= 200 )  
async def read_items(  response : Response , check : int  = Depends(verify) ):  
    if check == 0:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"Message" :str(check) +" You are not authorized to use this API!" }
    else :
        response.status_code = status.HTTP_200_OK
        return {str(check) +  "will be implemented"}


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

# if __name__ == "__main__":
#     uvicorn.run(app)