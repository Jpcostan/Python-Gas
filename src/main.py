import requests
import pprint
import json 

r = requests.get('https://ethgasstation.info/api/ethgasAPI.json?api-key=f8c65ec148a5a195b73f00241810944500a7fe7fa04b073b0c8c118b00ca')
#print(r.json())
#pprint.pprint(r.json())
#need to parse the json to only print 'average' key and val

#capture the json from request
x = r.json()
#print average gas from the json obj
print("Current gas average :" + str(x['average']))
