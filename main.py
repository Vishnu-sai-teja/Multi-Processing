import time 


# perf.counter() - function always returns the float value of time in seconds
start = time.perf_counter()

def reference() :
    print('Sleep for 2 seconds ...')
    time.sleep(2)
    print('Done Sleeping ...')

reference()
reference()

finish = time.perf_counter()

print(f'Time to compute the funciton : {finish - start}')
