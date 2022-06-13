import queue
import random 

class Queue():
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def create(self):

        length = int(input("Enter length of queue: "))
        for i in range(length):
            self.enqueue(random.randint(0, 120))
        
        print(self.items)
    
        return self.items    



    """
    class Queue:
 def __init__(self):
   self.head = None
   self.tail = None
   self.size = 0
 
 def enqueue(self, value):
   if self.has_space():
     item_to_add = Node(value)
     print("Adding " + str(item_to_add.get_value()) + " to the queue!")
     if self.is_empty():
       self.head = item_to_add
       self.tail = item_to_add
     else:
       self.tail.set_next_node(item_to_add)
       self.tail = item_to_add
     self.size += 1
   else:
     print("Sorry, no more room!")
 
 def dequeue(self):
   if self.get_size() > 0:
     item_to_remove = self.head
     print(str(item_to_remove.get_value()) + " is served!")
     if self.get_size() == 1:
       self.head = None
       self.tail = None
     else:
       self.head = self.head.get_next_node()
     self.size -= 1
     return item_to_remove.get_value()
   else:
     print("The queue is totally empty!")
  def peek(self):
   if self.size > 0:
     return self.head.get_value()
   else:
     print("No orders waiting!")
  def get_size(self):
        return self.size
    def is_empty(self):
    return self.size == 0
    """


if __name__ == "__main__":

    # initialise a queue instance 
    a_queue =  Queue()
    print(f"Is queue empty?     {a_queue.is_empty()}")


    #add items to queue 
    for i in range(10):
        temp = random.randint(0,120)
        print(f"{i+1}.      enqueuing       {temp}")
        a_queue.enqueue(temp)


    # get size of queue
    queue_size = a_queue.size()
    print("Size of queue: ", queue_size)

    # empty the queue 
    for i in range(10):
        print(f"{i+1}.      dequeueing       {a_queue.dequeue()}")

    print("Done")

    print(f"is the queue empty?         {a_queue.is_empty()}")  # output True 

    answer = input("Generate a new random queue? (Y, y, or Yes to cont.) \n")

    if answer == "Y" or answer == "yes" or answer =="y":
        new_queue = Queue()
        new_queue.create()
