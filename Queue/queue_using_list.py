class ImplementQueueUsingList:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        print(self.queue)

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return
        return self.queue.pop(0)

    def peek_front(self):
        if self.is_empty():
            print("Queue is empty")
            return
        return self.queue[0]

    def peek_rear(self):
        if self.is_empty():
            print("Queue is empty")
            return
        return self.queue[-1]


# Usage
q = ImplementQueueUsingList()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()          # [10, 20, 30]
print(q.dequeue())   # 10
q.display()          # [20, 30]
