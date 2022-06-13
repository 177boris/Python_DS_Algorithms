from pip import main

class Recursion():

    def __init__(self) -> None:
        super().__init__()

    def my_factorial(self, num):
        
        call_stack = []
        if num == 1:
            print('base case reached! Num is 1.')
            return 1
        else:
            call_stack.append({'input': num})
            print('call stack: ', call_stack)
        return (num * self.my_factorial(num - 1)) 
        


if __name__ == '__main__':

    rec = Recursion()
    val = int(input("Enter number:  \n"))
    rec.my_factorial(val)