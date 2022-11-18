import json
from random import randint 
from model import Model 


class  myResponse :
    def generate_rand(self):       
        return randint(0, 100)


    def getResponse(self):
        data =  Model()
        
        rand = self.generate_rand()   
        
        quote = data.get_qoutes(rand ) 
        self.quoteId = quote["id"]
        self.quoteName = quote["quote"]
        self.author = data.get_authors(self.quoteId)
        
    
    
    





    


#print(get_qoutes(1))