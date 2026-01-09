# Python list as queue

queue = []

# Enqueue
queue.append("A")
queue.append("B")
queue.append("C")
print("Queue: ", queue)

# Peek - view first pos (FIFO)
frontElement = queue[0]
print("Peek: ", frontElement)

# Dequeue - pop from front - use 0 - store in var
poppedElement = queue.pop(0)  # removes from left - FIFO
print("Popped: ", poppedElement)

print("After dequeue: ", queue)

# isEmpty
isEmpty = not bool(queue)
print("isEmpty: ", isEmpty)

# Size
print("Size: ", len(queue))


# Implement a queue class
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue[0]

    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


# Create a queue
queueOne = Queue()
queueOne.enqueue("A")
queueOne.enqueue("B")
queueOne.enqueue("C")
print("Enqueue:", queueOne.queue)

# Peek the top element
print("Peek: ", queueOne.peek())

# Dequeue an element
queueOne.dequeue()
print("After dequeue: ", queueOne.queue)

# Check if empty
print("Is Empty?: ", queueOne.isEmpty())
# Check size
print("Size: ", queueOne.size())
