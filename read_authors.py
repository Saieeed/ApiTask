import json
import pandas as pd 

def get_authors(number):  
    try:
        f = open ('authors.json', "r")
        data = json.load(f)
         
        df_nested_list = pd.json_normalize(data, record_path =['quoteIds'] , meta=['id' , 'author'])
        df_nested_list.rename(columns = { 0 : "quoteId"}, inplace=True)
        #print(data)
        f.close()
        return df_nested_list[df_nested_list.quoteId == number]
    except:
        return []
    
    
#print(get_authors(68))