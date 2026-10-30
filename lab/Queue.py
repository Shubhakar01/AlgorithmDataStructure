class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = 0
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.capacity

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full")
            return
        rear = (self.front + self.count) % self.capacity   # wrap around
        self.items[rear] = item
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        item = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % self.capacity     # wrap around
        self.count -= 1
        return item

    def peek(self):
        return None if self.is_empty() else self.items[self.front]

    def display(self):
        print([self.items[(self.front + i) % self.capacity] for i in range(self.count)])


q = CircularQueue(4)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)      # Queue is full
print(q.dequeue()) # 10
q.enqueue(50)      # reuses the freed slot at index 0
q.display()        # [20, 30, 40, 50]