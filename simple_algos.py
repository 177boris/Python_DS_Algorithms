from itertools import count
import random
from stacks import Stack
from queues import Queue 

import pygorithm


class Simple_Algos():

    def __init__(self, data) -> None:
        self.data = data 


    def fizz_buzz(self):
        for i in self.data:
            if i % 3 == 0 and i % 5 ==0:
                print("FizzBuzz")
            elif i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")
            else:
                print(i)


    def sequential_search(self):
        found = False 
        target = self.data[random.randint(0, len(self.data))]
        print (f"Searching for:  {target}")

        for i in self.data: 
            if i == target:
                found = True 
                print(f"found {target} in {i}")
                break
        return found 


    def count_occurences(self):

        txt = input("Enter a word:  \n")
        
        count_dict = {}
        for c in txt:
            if c in count_dict:
                count_dict[c] += 1 
            else: 
                count_dict[c] = 1 
        print(count_dict)


        def linked_list(self):
            head = None

            temp = self.head
            while (temp):
                print(temp.data)
                temp = temp.next  
    

if __name__ == "__main__":
    print("Simple Algos.")

    queue = Queue()
    #stack = Stack()

    test_set1 = queue.create()
    #test_set2 = stack.create()

    a = Simple_Algos(test_set1)

    print(" ")
    a.fizz_buzz()
    
    print(" ")
    a.sequential_search()

    print(" ")
    a.count_occurences()
    print(" ")

