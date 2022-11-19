from pydantic import BaseModel

class QuoteResponse(BaseModel):
  quoteId: int
  quote: str
  author: str
    
  class Config:
    schema_extra = {"example": {
                      "quoteId": 23,
                      "quote": "I am not a product of my circumstances. I am a product of my decisions.",
                      "author": "Stephen Covey"
                    }}

