import time
import multiprocessing

# Using shared memory

# Data share between the process is imporssible , so we have to use some 
# Ways to shift data between process and threads

# result = []

def calc_square(numbers,result,value) :
    for idx,n in enumerate(numbers) :
        result[idx] = n**2

    value = 12
    print('Inside the process : ' ,str(result[:]),value)

if __name__ == '__main__' :
    numbers = [2,3,5]

    # p1 = multiprocessing.Process(target = calc_square,args = (numbers,))
    # p1.start()
    # p1.join()

    ''' 
    So we use the shared memory , the memory lives outside the process and we can acess it from both the process
    There are two ways of using shared memory
       * Array

            Shared memory variable array - multiproicessing.Array(data type ,size)
            Acess the array using the [:] , to acess all teh values in the shared memory varaible array

        * Value 
            Shared memory variable value = multiprocessing.Value(data type,assign value)
            Acess the value using : value.value , to acess the value
    '''

    result = multiprocessing.Array('i',3)
    value = multiprocessing.Value('d',0.0)
    p = multiprocessing.Process(target=calc_square,args = (numbers,result,value))

    p.start()
    p.join()

    print('Result outside the process : ', result[:],value.value)



