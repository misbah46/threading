import requests
import time
t1 = time.time()

s = requests.session()

url =['https://bit.ly/2vqkYSu','https://bit.ly/3aqlYoH','https://bit.ly/32DA0Ra']

name = 1
for i in url:
    #print(url)
    response=s.get(i)
    response_byte = response.content
    fo =open(str(name)+".pdf",'wb')
    fo.write(response_byte)
    fo.close()
    name = name +1
    
"""    t1 = time.time()
    requests.get(i)
    t2 = time.time()    
    print(t2-t1)"""

"""r = "https://bit.ly/32DA0Ra"
t1 = time.time()
requests.get(r)
t2 = time.time()    
print(t2-t1)"""
t2 = time.time()    

print(t2-t1)