import requests
import time

url = "https://bit.ly/32DA0Ra"
t1 = time.time()
requests.get(url)
t2 = time.time()

#print(t1/60/60/7/30/12/365)

print(t2-t1)