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
poppedElement = queue.pop(0) #removes from left - FIFO
print("Popped: ", poppedElement)

print("After dequeue: ", queue)

# isEmpty 
isEmpty = not bool(queue)
print("isEmpty: ", isEmpty)

# Size
print("Size: ", len(queue))