import time
import threading

start = time.perf_counter()

def func1(num : int) :
    for i in range(num) :
        time.sleep(0.1)
        print('From func1 : ' , i )

def func2(num : int) :
   for i in range(num) :
        time.sleep(0.1)
        print('From func2 : ' , i/10 )


if __name__ == '__main__' :
    num = 5

    # func1(num)
    # func2(num)

    # Lets optimize this using the multi threading 

    t1 = threading.Thread(target = func1,args = (num,))
    t2 =threading.Thread(target= func2,args = (num,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    final = time.perf_counter()

    print('Total time taken : ' , final - start)


