import json
import pandas as pd 

class Model :
    f = open ('config.json', "r")
    path = json.load(f)            # print(data)
    f.close()
    def get_authors(self , number):  
        
        try:
            # print(data)
            path_descreption = self.path["authors"]
            print(path_descreption)
            g = open (path_descreption, "r")
            data = json.load(g)
            print(data)
            g.close()
            
            df_nested_list = pd.json_normalize(data, record_path =['quoteIds'] , meta=['id' , 'author'])
            df_nested_list.rename(columns = { 0 : "quoteId"}, inplace=True)
            #print(data)
            return df_nested_list[df_nested_list.quoteId == number].author.values[0]
        except:
            return []
    
    def get_qoutes(self , number):  
        try:
            # print(data)
            path_descreption = self.path["quotes"]
            print(path_descreption)
            g = open (path_descreption, "r")
            data = json.load(g)
            #print(data)
            g.close()
        #  print(data[number])
        
            return data[number]
        except:
            return []


