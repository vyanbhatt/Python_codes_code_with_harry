import requests #this helps to get things from net
import json #this helps to convert string into dictionary
city = input("Enter the name of the city\n")

url = f"http://api.weatherapi.com/v1/current.json?key=b7df91ea474e4da498c173942231307&q={city}"

r = requests.get(url)

#print(r.text)
print(type(r.text))

'''above will work fine but we don't want 
to print all the data but only the temp
hence we are converting r.text(string type)
into dictionary type in order to get only the temp
and to do this we have a built in library
called json'''

wdic = json.loads(r.text)
#loads will convert string to dictionary

print(wdic["location"]["name"])
print(wdic["location"]["region"])
print(wdic["location"]["country"])
print(wdic["location"]["localtime"])

print("Following is the temperature ")
print(wdic["current"]["temp_c"])


