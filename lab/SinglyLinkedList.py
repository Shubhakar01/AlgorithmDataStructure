class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def insert_rear(self,data):
        if self.head is None:
            self.head = Node(data)
            return
        cur = self.head
        while(cur.next is not None):
            cur = cur.next
        cur.next = Node(data)

    def insert_after(self,pos,value):
        if self.head is None:
            return
        newNode = Node(value)
        cur = self.head
        while(cur is not None):
            if(cur.data ==pos):
                newNode.next = cur.next
                cur.next = newNode
                return
            cur = cur.next

    def delete_after(self,pos):
        if self.head is None:
            return
        cur = self.head
        while(cur is not None):
            if(cur.data == pos):
                cur.next = cur.next.next
            cur = cur.next
    def display(self):
        if self.head is None:
            return
        cur = self.head
        print("\n")
        while(cur is not None):
            print(cur.data)
            cur = cur.next

sll = SLL()
sll.insert_rear(12)
sll.insert_rear(23)
sll.insert_rear(45)
sll.insert_rear(67)
sll.display()
sll.insert_after(23,34)
sll.display()
sll.delete_after(23)
sll.display()
