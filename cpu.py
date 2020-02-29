import time
import threading
import multiprocessing

def sum_square(n):
    total=0
    for i in range(n+1):
        total += (i*i)
    return (total)
    
t1 = time.time() 
tasks = [10000000,5000000,600000,84444000]
processes = []

# for task in tasks:
#     sum_square(task)

for task in tasks:
    process = multiprocessing.Process(target=sum_square,args=[task])
    process.start()
    processes.append(process)
#     th.start()
#     threads.append(th)
#     print(sum_square(task))

for pr in processes:
    pr.join()

t2 = time.time()
print(t2-t1)
