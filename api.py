import requests 

r = requests.get("https://www.youtube.com/")
x = r.text
# print(type(x))
print(x)
