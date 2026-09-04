# Edge cases to remember, incase list is empty and adding at end of list or deleting from list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    # Like constructor in Java, can be used to initialize and
    # runs only once when the object is created
    def __init__(self):
        self.head = None

    def insert_start(self, data):
        # Make the new node point to current head and
        # Make the new node as new head
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"Inserted {data} at the start.")

    def insert_end(self, data):
        new_node = Node(data)
        # This implies that the list is empty and head would be pointing to Null
        if not self.head:
            self.head = new_node
            print(f"Inserted {data} at the end.")
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        print(f"Inserted {data} at the end.")

    def delete_start(self):
        if not self.head:
            print("List is empty! Nothing to delete from the start.")
            return
        
        deleted_data = self.head.data
        self.head = self.head.next
        print(f"Deleted {deleted_data} from the start.")

    def delete_end(self):
        if not self.head:
            print("List is empty! Nothing to delete from the end.")
            return
        
        if not self.head.next:
            deleted_data = self.head.data
            self.head = None
            print(f"Deleted {deleted_data} from the end.")
            return
        
        current = self.head
        while current.next.next:
            current = current.next
            
        deleted_data = current.next.data
        current.next = None
        print(f"Deleted {deleted_data} from the end.")

    def display(self):
        """Displays all the elements in the linked list."""
        if not self.head:
            print("Linked List is empty.")
            return
        
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        
        print(" -> ".join(elements) + " -> None")


if __name__ == "__main__":
    ll = LinkedList()

    print("--- Testing Insertions ---")
    ll.insert_end(10)
    ll.insert_end(20)
    ll.insert_start(5)
    
    print("\nCurrent List:")
    ll.display()

    print("\n--- Testing Deletions ---")
    ll.delete_start()
    ll.delete_end()
    
    print("\nCurrent List:")
    ll.display()