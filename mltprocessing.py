import multiprocessing
import concurrent.futures
import time

start = time.perf_counter()

def reference() :
    print('Starting a 2 second delay ...')
    time.sleep(2)
    print('Done Sleeping ...')

def reference_sleep(seconds) :
    print(f'Starting a {seconds} second delay ...')
    time.sleep(seconds)
    print('Done Sleeping ...')

# Python 3.2 - Process pull executer - use multiple threads instead of processes whenever needed


if __name__ == '__main__':

    # Way -1 

    '''Instead of running the two processing one after the other we do the 
        following for multi processing - make them into process'''
    # p1 = multiprocessing.Process(target = reference)
    # p2 = multiprocessing.Process(target = reference)

    ''' So we have created the processes above ,
      but now we have to run the processes (by  .start ) '''
    # p1.start()
    # p2.start()

    '''While the scripts were sleeping , it has just started to print the finish before the processes were started
    To wsolve this - join helps us to wait till the process will wait till the end '''

    # p1.join()
    # p2.join()

    ''' Wait till the process will be completed and proceed for further -'''
    
    # Way - 2  

    ''' 
        multiprocesses for any number of processes but doesnt take input arguments, 
        Now try to implement it with a loop for faster compute , Run multiple processes paralelly , 
        and saved a lot of time 
    '''
    
    # processes = []
    
    # for p in range(18) :
    #     p = multiprocessing.Process(target = reference)
    #     p.start()
    #     processes.append(p)

    # for process in processes :
    #     process.join()


    # Way - 3

    ''' Multi processesing that takes the arguments as input and able to take it as input
    
    Arguments to multiprocess : Arguments should be serialized , convert python to format x , 
    x - can be deconstructed and reconstructed in python script '''

    processes = []

    for p in range(10) :
        p = multiprocessing.Process(target = reference_sleep,args = [1.5])
        p.start()
        processes.append(p)

    for process in processes :
        process.join()


    finish = time.perf_counter()

    print(f'Time to compute the funciton : {finish - start}')