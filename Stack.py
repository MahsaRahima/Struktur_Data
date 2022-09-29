class stack:

    def __init__(self):
        self.stack = []
        self.top = -1

    def push(self,value):
        if self.top == 2 :
            print("Sorry stack is full")
        self.top +=1
        self.stack.append(value)

    def pop(self):
        if self.top == -1 :
            print("Sorry stack is empty")
        self.top -=1
        self.stack.pop()

    def print_stack(self):
        for i in range(self.top,-1,-1):
            if i == self.top:
                print(self.stack[i], "<--- Top")
            else: 
                print(self.stack[i])
            print(" ")
s = stack()
s.push(50)
s.push(67)
s.push(2)
s.push(10)


s.print_stack()