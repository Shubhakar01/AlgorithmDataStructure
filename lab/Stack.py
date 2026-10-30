class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head=None

    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def peek(self):
        if self.head:
            return self.head.data

    def pop(self):
        if self.head is None:
            return
        if self.head.next is None:
            popped_element = self.head.data
            self.head = None
            return popped_element
        else:
            popped_element = self.head.data
            self.head = self.head.next
            return popped_element



def main():
    st = Stack()
    while True:
        print("1 for Push 2 for Pop 3 for Peek 0 for Exit")
        case = int(input("Enter your choice: "))
        match case:
            case 1:
                value = input("Enter your value: ")
                st.push(value)
            case 2:
                value = st.pop()
                if value :
                    print(f"Top value {value} removed")
            case 3:
                value = st.peek()
                if value:
                    print(f"Top of Stack is {value}")
            case 0:
                print("Exiting")
                break
            case _:
                print("Invalid choice")
main()
