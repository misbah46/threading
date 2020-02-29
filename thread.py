import threading
import requests
import time

urls =['https://bit.ly/2vqkYSu','https://bit.ly/3aqlYoH']

result = []

def download_save(url):
    response = requests.get(url)
    result.append(response.status_code)

t1 = time.time()
threads = []

for url in urls:
    th = threading.Thread(target=download_save,args=[url])   #syntax of thread
    th.start()
    #th.join()
    threads.append(th)
    #download_save(url)

for thread in threads:
     thread.join()

t2 = time.time()        

print(t2-t1) 
print(result)
