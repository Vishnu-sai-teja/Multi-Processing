# Python 3.2 - Process pull executer - use multiple threads instead of processes whenever needed

import concurrent.futures
import time


def reference(seconds) :
    print(f'Sleeping for {seconds}...')
    time.sleep(seconds)
    return f'Done Sleeping... {seconds}'
 
if __name__ == '__main__' :

    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        '''
            If function once at a time , submit() method , schedules a function to be executed and returns a future object
            future object - execution of the function and allows to check on it once it is schedules ,
                            running or done , check the result
        '''

        # Way - 1  for smaller number of processes

        # f1 = executor.submit(reference , 1)
        # f2 = executor.submit(reference , 1.5)

        # print(f1.result())
        # print(f2.result())

        # Way 2 with mutliple processes

        secs = [5,4,3,2,1]
        results = [executor.submit(reference , secs) for secs in secs]

        '''
            In order to get these results we get as_completed , 
            iterator to yield results as the processes are completed
        '''
        for f in concurrent.futures.as_completed(results) :
            print(f.result())


        finish = time.perf_counter()

        print(f'Total time time for execution : {finish - start}')
