import requests
import pprint 

#Request with EthGasStation API key.
#You will need to create an account and input key in the string below.
r = requests.get('https://ethgasstation.info/api/ethgasAPI.json?api-key=f8c65ec148a5a195b73f00241810944500a7fe7fa04b073b0c8c118b00ca')

#Capture the json from request.
x = r.json()
#Print average gas from the json obs.
print("Current gas average :" + str(x['average']))

###TODO
###Define criteria for which the script will run in the background
###Every hour? Every 30 minuets? Every 15 minuets?
###This will help determine if this should run as daemon, a job or
###be ran via executable.
###Configure while loop below to accomodate for how this script will be ran.


#This is an infinite loop. It will continuously execute in it's current form
#unless configured otherwise. 
while(1):
    r = requests.get('https://ethgasstation.info/api/ethgasAPI.json?api-key=f8c65ec148a5a195b73f00241810944500a7fe7fa04b073b0c8c118b00ca')
    x = r.json()
    gas = x['average']
    if gas <= 650:
        print("Alert! Curent gas is LOW: " + str(x['average']))

###TODO
###Send alert to window pop-up