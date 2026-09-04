class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.head = -1
        self.tail = -1

    def is_empty(self):
        return self.head == -1

    def is_full(self):
        return (self.tail + 1) % self.capacity == self.head

    def enqueue(self, data):
        if self.is_full():
            return False
        if self.is_empty():
            self.head = 0
        self.tail = (self.tail + 1) % self.capacity
        self.queue[self.tail] = data
        return True

    def dequeue(self):
        if self.is_empty():
            return None
        data = self.queue[self.head]
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
        else:
            self.head = (self.head + 1) % self.capacity
        return data

    def display(self):
        if self.is_empty():
            print("Empty Queue")
            return
        i = self.head
        while True:
            print(self.queue[i])
            if i == self.tail:
                break
            i = (i + 1) % self.capacity

if __name__ == "__main__":
    cq = CircularQueue(3)
    cq.enqueue(10)
    cq.enqueue(20)
    cq.enqueue(30)
    cq.dequeue()
    cq.enqueue(40)
    cq.display()