
import random 

class Stack: 
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        last = len(self.items)-1
        return self.items[last]

    def size(self):
        return len(self.items)

    def create(self):

        length = int(input("Enter length of stack: "))
        for i in range(length):
            self.push(random.randint(0, 120))
        
        print(self.items)
        
        return self.items


    """
    from node import Node
 
class Stack:
  def __init__(self, limit=1000):
    self.top_item = None
    self.size = 0
 
  def push(self, value):
    if self.has_space():
      item = Node(value)
      item.set_next_node(self.top_item)
      self.top_item = item
      self.size += 1
    else:
      print("All out of space!")
 
  def pop(self):
    if self.size > 0:
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()
    else:
      print("This stack is totally empty.")
 
  def peek(self):
    if self.size > 0:
      return self.top_item.get_value()
    else:
      print("Nothing to see here!")
 
 
  def is_empty(self):
    return self.size == 0
    """


if __name__ == "__main__":
    stack = Stack()
    print(f" is stack empty?     {stack.is_empty()}")      # output True 

    for i in range(10):
        temp = random.randint(0, 120)
        print(f" {i+1}. appending to the stack - PUSH:   {temp}")
        stack.push(temp)

    # get size of stack 
    stack_size = stack.size()
    print("Size of stack: ", stack_size)

    #peek 
    last_num = stack.peek()
    print(f"Most recent (peek): {last_num}")

    for i in range(stack_size):
        print(f"deleting from stack (FIFO DS) - POP  {stack.pop()}")
        #stack.pop()
    print("Done")

    #stack = Stack()
    print(f" is stack empty?     {stack.is_empty()}")      # output True 

    answer = input("Generate a new random stack? (Y, y, or Yes to cont.) \n")

    if answer == "Y" or answer == "yes" or answer =="y":
        new_stack = Stack()
        new_stack.create()
        