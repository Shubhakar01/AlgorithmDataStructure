# self.head is the first node
# self.tail is the last node
# So each time an element is added or deleted then these values need to be updated and their pointers as well

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_front(self,data):
        new_node = Node(data)
        if(self.head == None):
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_end(self,data):
        new_node = Node(data)
        if(self.head == None):
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def delete_front(self):
        if self.head is None:
            print("Empty List")
        else:
            self.head=self.head.next
            self.head.prev=None

    def display(self):
        if self.head is None:
            print("Empty List")
        else:
            curr=self.head
            while(curr):
                print(curr.data)
                curr=curr.next

if __name__ == "__main__":
    n1 = DoubleLinkedList()
    n1.insert_front(16)
    n1.insert_front(26)
    n1.insert_end(36)
    n1.display()
    n1.delete_front()
    n1.display()

                
