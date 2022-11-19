from fastapi import Depends,FastAPI  ,Response,status ,Request
from fastapi.responses import JSONResponse , HTMLResponse
from dependincies import get_query_token ,get_token
from savedata import save_request
from quote import Quote 
from response_model import QuoteResponse
import uvicorn 
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# @app.middleware("http")
# def before_request(request: Request, call_next):
#   token = request.headers.get("authorization")
#   # saved token continans a valid token
#   saved_token = get_token()
#   print(token)
#   if token != "Bearer "+saved_token:
#       return JSONResponse(content={"Message": "You are not authorized to use this API!"}, status_code=401)
#   else :
#         return call_next(request)

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get ("/",response_class=HTMLResponse)
async def home (request: Request):
    return templates.TemplateResponse("index.html" ,{"request": request})

@app.get(
    "/quote/random",
    summary="Get random quote",
    tags=["Quotes"],
    #response_model=QuoteResponse,
    status_code=status.HTTP_200_OK
)

def get_random_quote(response : Response, check : int  = Depends(get_query_token)) -> QuoteResponse:
    if check == False:
      return JSONResponse(content={"Message": "You are not authorized to use this API!"}, status_code=401)
    return Quote.get_rand_quote()


## @app.get("/quote/random" )  
## async def read_items(  response : Response , check : int  = Depends(get_query_token) ):  
#     if check == False:
#         response.status_code = status.HTTP_401_UNAUTHORIZED
#         return {"Message" :" You are not authorized to use this API!" }
#     else :
#         r =  myResponse()
#         r.getResponse()
#         if r.quoteId == "" or r.quoteName == "" or r.author ==  "":
#             return JSONResponse(content={"Message": "couldn't load data"}, status_code=500)
#         else:
#             save_request(r.quoteId)
#             return JSONResponse(content={"quoteId":str(r.quoteId)  , "quote":str(r.quoteName) , "author":r.author} , status_code=200)



if __name__ == "__main__":
    uvicorn.run(app)