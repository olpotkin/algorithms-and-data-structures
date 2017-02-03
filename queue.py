
class Queue(object):
    # Constructor
    def __init__(self):
        self.queue = []                         # Queue is empty list in the beginning

    # Is queue empty or not
    def isEmpty(self):
        return self.queue == []

    # Insert element in queue
    def enqueue(self, data):
        self.queue.insert(0, data)

    # Remove element from queue
    def dequeue(self):
        return self.queue.pop()

    def queue_size(self):
        return len(self.queue)

# Testing
q = Queue()

q.enqueue("Word")
q.enqueue(12)
q.enqueue(10.5)

print(q.dequeue())
print(q.dequeue())
print(q.queue_size())
print(q.dequeue())
print(q.queue_size())
