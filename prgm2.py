import requests
import json
import sys
e=sys.argv[1]
url= "http://api.weatherapi.com/v1/current.json?key=f0557d5c4f574d178b655021212212&q="
url2="&aqi=no"
req=url + e + url2
x=requests.get(req)
y=x.text
z=json.loads(y)
a=z["location"]
b=a["name"]
cur=z["current"]
temp=cur["temp_c"]
print(b,temp)