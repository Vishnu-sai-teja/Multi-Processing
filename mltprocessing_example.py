import time
import os
import concurrent.futures
from PIL import Image


images = []

dir = os.path.join(os.getcwd(),images)

def reference(imagePath) :
    return image

start = time.perf_counter()

if __name__ == '__main__' :

    with concurrent.futures.ProcessPoolExecutor as executor :

        imagepath = [os.path.join(dir,image) for image in images]
        
        results = executor.map(reference,imagepaths)


    finish = time.perf_counter()

    print(f'Total time for execution : {finish - start}')

