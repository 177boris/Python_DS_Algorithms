import random
from stacks import Stack

class B_Search():

    def __init__(self, data):
        self.data = data

        self.target = self.data[4]
        print(f"Target ===> {self.target}")
        
        self.sorted_list = self.sort(self.data)

        print("SORTED")
        print(self.sorted_list)

        self.rec_binarySearch(self.target, self.sorted_list, self.sorted_list[0], self.sorted_list[len(self.sorted_list) -1] )        
        # search for number 


    def sort(self, data):
        return sorted(data)
    

    # recursive binary search 
    def rec_binarySearch(self, target, sequence, first, last):

        #first = sequence[0]
        #last = sequence[len(sequence)-1]

        if first > last:
            return False
        else:
            mid = (last + first) // 2
            if sequence[mid] == target:
                return True
            elif target < sequence[mid]:
                return self.rec_binarySearch(target, sequence, first, mid-1)
            else:
                return self.rec_binarySearch(target, sequence, mid + 1, last)


"""
Recursion is a very powerful tool for programming and problem-solving.
It can be used to solve and implement a wide range of algorithms to solve basic iterative 
problems to advanced backtracking problems. 
"""

if __name__ == "__main__":

    ds = Stack()

    for i in range(10):
        temp = random.randint(0,8)
        print(f"Pushing: {temp}")
        ds.push(temp)
    
    # convert to list so it can be sorted 
    temp_list = []
    for x in range(ds.size()):
        temp_list.append(ds.pop())

    search = B_Search(temp_list)
