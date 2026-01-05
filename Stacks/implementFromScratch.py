# Basic operations we can do on a stack
# 1. Push adds a new element on the stack
# 2. pop removes and returns the top element from the stack
# 3. Peak returns the top (last) element on the stack.
# 4. Is empty: Checks if the stack is empty.
# 5. Size: It forms the number of elements in the stack.

# Stacks can be implemented by using arrays or linked lists.
# Stacks can be used to implement undue mechanisms to revert to previous states, to create algorithms for DFS in graphs, or for backtracking.
# Stacks are often mentioned together with cues, which is a similar data structure described on the next page.
# Stacks use elastin first out like a stack of pancakes, removing the first 1 off the top and any that is inserted will be the 1st one to be removed.


# Push: Push is O(1). Adding an element to the top is O of 1. An array based implementation is occasional resizing double S the array size costing of N but amortized over many operations its O of 1.
# Pop: Pop is O(1) and removing a top element is always over one in both array and link list implementations.
# Peek (or top): O(1) accessing the top element without removing it is O(1)
# Is empty: O(1) Usually checks if size is equal to zero if head pointer is null
# Size:  O(1) Most implementations maintain a size counter that is updated on push/pop.

# Implement from scratch.


# Regular array implementation with built-in python methods
stack = []

# Push
stack.append("A")
stack.append("B")
stack.append("C")
print("Stack: ", stack)
# Peek
topElement = stack[-1]
print("Peek: ", topElement)
# Pop
poppedElement = stack.pop()
print("Pop: ", poppedElement)
# Stack after pop
print("Stack after Pop: ", stack)

# isEmpty
isEmpty = not bool(stack)
print("isEmpty: ", isEmpty)

# Size
print("Size:", len(stack))

# Create Stack Class
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, element):
        self.stack.append(element)
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]
    def isEmpty(self):
        return len(self.stack) == 0
    def size(self):
        return len(self.stack)

# Create a stack
myStack = Stack()

myStack.push("A")
myStack.push("B")
myStack.push("C")
print("Created Stack: ", myStack.stack)

poppedElementValue = myStack.pop()
print("Popped element: ", poppedElementValue)

print("Peek: ", myStack.peek())

print("Stack after pop: ", myStack.stack)
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.size())

# Stack using linked list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
    def push(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size += 1
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        popped_node = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_node.value
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.head.value
    def isEmpty(self):
        return self.size == 0
    def stackSize(self):
        return self.size
    def traverseAndPrint(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value, end=" -> ")
            currentNode = currentNode.next
        print()

myStack = Stack()
myStack.push("A")
myStack.push("B")
myStack.push("C")

print("LinkedList: ", end="")
myStack.traverseAndPrint()
print("Peek: ", myStack.peek())
print("Pop: ", myStack.pop())
print("LinkedList after Pop: ", end="")
myStack.traverseAndPrint()
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.stackSize())
