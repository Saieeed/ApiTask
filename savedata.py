import json
import pandas as pd
from datetime import datetime

def save_request(key):
    def create (key) :
        f = open ('config.json', 'r' )
        config = json.load ( f )
        counter = config["counter"]
        csvName = config["csvName"]   
        request_count = {}

        f.close()
        try:     
            f = open ('request_count.json', "r")
            request_count = json.load ( f )
            f.close()

        except:
            f= open ("request_count.json", "w")
            json.dump (request_count, f )
            f.close()

        
        if str(key) in request_count:
            request_count[str(key)] = request_count[str(key)]+1
        else:
            request_count[str(key)] = 1
        print(sum(request_count.values()))
        today = datetime.now()

        today  = today.strftime("%Y_%m_%d_%H_%M_%S")

        #print("Today's date:", today)
        if sum(request_count.values()) == 100 :
            df = pd.DataFrame.from_dict(request_count.items())
            df.columns = ["Quote ID", "Count"]
            print(df)
            df.to_csv(csvName+today+'.xlsx', encoding='utf-8'  ,index=False ,header=True )
            request_count={}

        f= open ("request_count.json", "w")
        json.dump (request_count, f )
        f.close ()
        return True
        
    return create(key)

#save_request(6)