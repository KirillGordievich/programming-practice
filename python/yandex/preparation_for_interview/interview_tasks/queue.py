class Queue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if len(self.queue) == 0:
            return None
        removed = self.queue.pop(0)
        return removed


queue = Queue()

queue.push(1)
queue.push(2)
queue.push(50)

print(queue.pop())
print(queue.pop())
print(queue.pop())