from fastapi import Depends,FastAPI , Header, HTTPException ,Response,status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
from dependincies import get_query_token
from get_response import myResponse 
from savedata import save_request
import uvicorn 
import json

app = FastAPI()


    

@app.get("/quote/random" )  
async def read_items(  response : Response , check : int  = Depends(get_query_token) ):  
    if check == False:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"Message" :" You are not authorized to use this API!" }
    else :
        r =  myResponse()
        r.getResponse()
        if r.quoteId == "" or r.quoteName == "" or r.author ==  "":
            return JSONResponse(content={"Message": "couldn't load data"}, status_code=500)
        else:
            save_request(r.quoteId)
            return JSONResponse(content={"quoteId":str(r.quoteId)  , "quote":str(r.quoteName) , "author":r.author} , status_code=200)



if __name__ == "__main__":
    uvicorn.run(app)