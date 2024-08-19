import time
import multiprocessing

# Queue is also a part of shared memory - same as queue DS
# .put() method to insert into the queue here
# .empty() methods lets you know if the queue is emtpy
# .get() to get the elements in the queue , by FIFO way

def calc_square(numbers,q) :
    for n in numbers :
        q.put(n**2)

if __name__ == '__main__' :
    numbers = [2,3,4]

    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=calc_square,args = (numbers,q))
    p.start()
    p.join()

    while q.empty() is False :
        print(q.get(),end = ' ')

