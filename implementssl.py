class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while(current.next):
            current = current.next
        current.next = new_node

    def delete_end(self):
        if not self.head:
            print("Empty list")
            return
        current = self.head
        while(current.next):
            previous = current
            current = current.next
        previous.next = None

    def delete_front(self):
        if not self.head:
            print("Empty list")
            return
        self.head = self.head.next

    def display_elements(self):
        if not self.head:
            print("Empty list")
            return
        current = self.head
        display_list = []
        while current:
            display_list.append(current.data)
            current = current.next
        print(display_list)

if __name__ == "__main__":
    linked_list = SinglyLinkedList()
    # linked_list.display_elements()
    linked_list.insert_front(55)
    # linked_list.display_elements()
    linked_list.insert_front(11)
    linked_list.insert_end(99)
    linked_list.display_elements()
    linked_list.delete_end()
    linked_list.display_elements()
    linked_list.delete_front()
    linked_list.display_elements()
