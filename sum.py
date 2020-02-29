import time
import threading

def sum_square(n):
    total=0
    for i in range(n+1):
        total += (i*i)
    return (total)
    
t1 = time.time() 
tasks = [10000000,5000000,6000000,84444000]
threads = []

for task in tasks:
    sum_square(task)

# for task in tasks:
#     th=threading.Thread(target=sum_square,args=[tasks])
#     th.start()
#     threads.append(th)
#     print(sum_square(task))

for thread in threads:
    thread.join()

t2 = time.time()
print(t2-t1)
