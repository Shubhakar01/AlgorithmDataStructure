#push, pop, peek, display

class Stack:
    def __init__(self):
        self.stack_list = []

    def push(self,data):
        self.stack_list.append(data)

    def pop(self):
        return self.stack_list.pop()

    def peek(self):
        return(self.stack_list[-1])

    def display(self):
        new_list=  self.stack_list[::-1]
        for element in new_list:
            print(element)

    def length(self):
        return len(self.stack_list)

if __name__ == "__main__":
    s1 = Stack()
    s1.push(3)
    s1.push(4)
    s1.push(5)
    s1.pop()
    s1.push(6)
    s1.display()
    print(s1.length())
    