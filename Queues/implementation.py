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


# Queue implementation using linked list


# init Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# init Queue class
class QueueLL:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def enqueue(self, element):
        new_node = Node(element)  # init new node
        if self.rear is None:
            self.front = self.rear = new_node
            self.length += 1
            return
        self.rear.next = new_node
        self.rear = new_node
        self.length += 1

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        temp = self.front
        self.front = temp.next
        self.length -= 1
        if self.front is None:
            self.rear = None
        return temp.data

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.front.data

    def isEmpty(self):
        return self.length == 0

    def size(self):
        return self.length

    def printQueue(self):
        temp = self.front
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print()


# Create a queue
myQueue = QueueLL()

myQueue.enqueue("A")
myQueue.enqueue("B")
myQueue.enqueue("C")

print("Queue: ", end="")
myQueue.printQueue()
print("Peek: ", myQueue.peek())
print("Dequeue: ", myQueue.dequeue())
print("Queue after Dequeue: ", end="")
myQueue.printQueue()
print("isEmpty: ", myQueue.isEmpty())
print("Size: ", myQueue.size())
