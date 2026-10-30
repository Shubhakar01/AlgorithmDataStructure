class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_rear(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def insert_after(self, pos, value):
        """Insert value after the first node containing pos. Returns True if done."""
        cur = self.head
        while cur is not None:
            if cur.data == pos:
                new_node = Node(value)
                new_node.prev = cur
                new_node.next = cur.next
                if cur.next is not None:
                    cur.next.prev = new_node
                else:
                    self.tail = new_node
                cur.next = new_node
                return True
            cur = cur.next
        return False

    def delete_front(self):
        if self.head is None:
            return None
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        return data

    def delete_rear(self):
        if self.tail is None:
            return None
        data = self.tail.data
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None
        return data

    def delete_value(self, key):
        """Delete the first node containing key. Returns True if deleted."""
        cur = self.head
        while cur is not None:
            if cur.data == key:
                if cur.prev is not None:
                    cur.prev.next = cur.next
                else:
                    self.head = cur.next
                if cur.next is not None:
                    cur.next.prev = cur.prev
                else:
                    self.tail = cur.prev
                return True
            cur = cur.next
        return False

    def search(self, key):
        cur = self.head
        while cur is not None:
            if cur.data == key:
                return True
            cur = cur.next
        return False

    def display_forward(self):
        cur = self.head
        items = []
        while cur is not None:
            items.append(str(cur.data))
            cur = cur.next
        print(" <-> ".join(items) if items else "List is empty")

    def display_backward(self):
        cur = self.tail
        items = []
        while cur is not None:
            items.append(str(cur.data))
            cur = cur.prev
        print(" <-> ".join(items) if items else "List is empty")


def main():
    dll = DLL()
    dll.insert_rear(10)
    dll.insert_rear(20)
    dll.insert_front(5)
    dll.insert_after(10, 15)
    dll.display_forward()    # 5 <-> 10 <-> 15 <-> 20
    dll.display_backward()   # 20 <-> 15 <-> 10 <-> 5
    dll.delete_value(15)
    dll.delete_front()
    dll.delete_rear()
    dll.display_forward()    # 10


if __name__ == "__main__":
    main()
