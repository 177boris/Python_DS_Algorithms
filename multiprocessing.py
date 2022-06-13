import math, time
import multiprocess as mp 


def fun(numbers):
    c = []
    for x in numbers: 
        c.append(math.sqrt(x ** 5))


if __name__ == "__main__":

    numlist = list(range(5000000))

    p1 = mp.Process(target=fun, args = (numlist, ))
    p2 = mp.Process(target=fun, args = (numlist, ))
    p3 = mp.Process(target=fun, args = (numlist, ))
    
    start = time.time()
    p1.start()
    p2.start()
    p3.start()
    end = time.time()
    print(f"With multiprocessing: -  {round(end - start, 2) } seconds")


    start = time.time()
    fun(numlist)
    fun(numlist)
    fun(numlist)
    end = time.time()
    print(f"Without multiprocessing: - {round(end - start, 2) } seconds")
