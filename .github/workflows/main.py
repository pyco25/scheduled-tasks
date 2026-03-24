import requests                                                                            
from twilio.rest import Client                                                             
import os                                                                                  
                                                                                           
                                                                                           
OWM_Endpoint = "OWM_ENDPOINT"                          
api_key = "API_KEY"                                               
account_sid = "ACC_SID"                                         
auth_token = "AUTH_TOKEN"                                            
client = Client(account_sid, auth_token)                                                   
                                                                                           
                                                                                           
weather_params = {                                                                         
    "lat": 39.933365,                                                                      
    "lon": 32.859741,                                                                      
    "appid": api_key,                                                                      
    "cnt": 4,                                                                              
                                                                                           
}                                                                                          
                                                                                           
response = requests.get(OWM_Endpoint, params=weather_params)                               
response.raise_for_status()                                                                
weather_data = response.json()                                                             
                                                                                           
                                                                                           
will_rain = False                                                                          
for data in weather_data["list"]:                                                          
    if data["weather"][0]["id"] < 700:                                                     
        will_rain = True                                                                   
                                                                                           
if will_rain:                                                                              
    message = client.messages.create(                                                      
        from_="FROM_WHATSAPP",                                                     
        body="It's going to rain today. Remember to bring an umbrella",                    
        to="TO_WHATSAPP"                                                        
    )                                                                                      
                                                                                           
    print(message.sid)                                                                     
