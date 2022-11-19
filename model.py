import json
import pandas as pd 

class Model :
    f = open ('config.json', "r")
    path = json.load(f)            
    f.close()
    def get_authors(self , number):  
        
        try:
            path_descreption = self.path["authors"]
            g = open (path_descreption, "r")
            data = json.load(g)
            g.close()
            df_nested_list = pd.json_normalize(data, record_path =['quoteIds'] , meta=['id' , 'author'])
            df_nested_list.rename(columns = { 0 : "quoteId"}, inplace=True)
            return df_nested_list[df_nested_list.quoteId == number].author.values[0]
        except:
            return []
    
    def get_qoutes(self , number):  
        try:
            path_descreption = self.path["quotes"]
            g = open (path_descreption, "r")
            data = json.load(g)
            g.close()
            return data[number]
        except:
            return []


