class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if(self.head is None):
            print("Empty Queue")
            return True

    def enqueue(self,data):
        new_node = Node(data)
        if(self.head is None):
            self.head = new_node
        else:
            curr=self.head
            while(curr.next is not None):
                curr=curr.next
            curr.next=new_node
    def dequeue(self):
        if(not self.isEmpty()):
            self.head = self.head.next
            return self.head

    def display(self):
        if(not self.isEmpty()):
            curr=self.head
            while(curr is not None):
                print(curr.data)
                curr=curr.next

    def length(self):
        if(not self.isEmpty()):
            curr=self.head
            count =0
            while(curr is not None):
                count+=1
                curr=curr.next
            return count

if __name__ == "__main__":
    q1 = Queue()
    q1.enqueue(5)
    q1.enqueue(7)
    q1.dequeue()
    q1.enqueue(9)
    q1.display()
    print(q1.length())

        