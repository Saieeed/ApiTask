from get_response import myResponse 
from fastapi import Depends,FastAPI , Header, HTTPException ,Response,status , Request
from fastapi.responses import JSONResponse
from response_model import QuoteResponse
from savedata import save_request 


class Quote:

  def get_rand_quote():
    r =  myResponse()
    r.getResponse()  
    save_request(r.quoteId)
    if r.quoteId == "" or r.quoteName == "" or r.author ==  "":
        return JSONResponse(content={"Message": "couldn't load data"}, status_code=500)


    return QuoteResponse(quoteId=r.quoteId, quote=r.quoteName, author=r.author)