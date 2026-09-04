class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_front(self, data):
        new_node = Node(data)
        if not self.head: 
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        print(f"Inserted {data} at the front.")

    def insert_end(self, data):
        new_node = Node(data)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        print(f"Inserted {data} at the end.")

    def delete_front(self):
        """Deletes the first node from the list."""
        if not self.head:
            print("List is empty! Nothing to delete from the front.")
            return

        deleted_data = self.head.data
        if self.head == self.tail: 
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        print(f"Deleted {deleted_data} from the front.")

    def delete_end(self):
        """Deletes the last node from the list."""
        if not self.tail:
            print("List is empty! Nothing to delete from the end.")
            return

        deleted_data = self.tail.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        print(f"Deleted {deleted_data} from the end.")

    def display(self):
        """Displays elements of the list from front to back."""
        if not self.head:
            print("List is empty.")
            return

        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        
        print(" <-> ".join(elements) + " <-> None")


if __name__ == "__main__":
    dll = DoublyLinkedList()

    print("--- Testing Insertions ---")
    dll.insert_end(10)
    dll.insert_end(20)
    dll.insert_front(5)

    print("\nCurrent List:")
    dll.display()

    print("\n--- Testing Deletions ---")
    dll.delete_front() 
    dll.delete_end() 

    print("\nCurrent List:")
    dll.display()