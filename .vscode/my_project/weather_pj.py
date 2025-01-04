import json
import requests
from datetime import datetime

url ='https://api.openweathermap.org/data/2.5/weather?appid=ab927d7076cae28312326f9a3a9d060f&q='

user_input = input("Please enter your city name  ")

data_time = datetime.utcnow()

new_url = url+user_input

data = requests.get(new_url).json()

#Print both keys and values using zip


#file_name = str(user_input)

city_name = user_input+".txt"

with open(city_name,"a+") as data_file:
  
  try :
    
    if data_file:
     print("hello")
     data_file.write( "  --{0}--  \n".format(data_time))
     p_data = json.loads(data)
     data_file.write(p_data)
    
    
    else:
     print("Something wrong!")

  except Exception as err:
  
    print(err)