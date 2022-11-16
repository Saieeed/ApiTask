import json
from random import randint 

def get_qoutes(number):  
    try:
        f = open ('quotes.json', "r")
        data = json.load(f)
      #  print(data[number])
        f.close()
        return data[number]
    except:
        return []


def generate_rand():
    
    return randint(0, 101)


#print(get_qoutes(1))