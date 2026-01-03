class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        curr = self.head
        for _ in range(0, index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        curr = self.head
        new_node = ListNode(val)
        if index <= 0:
            new_node.next = curr
            self.head = new_node
        else:
            for _ in range(0, index - 1):
                curr = curr.next
            new_node.next = curr.next
            curr.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        curr = self.head
        if index == 0:
            self.head = self.head.next
        else:
            for _ in range(0, index - 1):
                curr = curr.next
            curr.next = curr.next.next
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

# Intuition: Straightforward linked list implementation The ideas to have a class list node with a value and next pointer and then we need to also in our official linked list solution have self dot head initiated to none and a self dot size for incrementing the linkedlist. GET method is straightforward At first we do an edge case Make sure that we're not below or out of bounds if we already return negative 1. Then do a for loop until the range of the index moving the current node forward with the current dot next pointer Then once we reach the index we return the current node's value. We can use a call to add at index and position for get the head and get the tail. then for added index we want to make sure that we're within a valid range starting out. Added index we want to make sure that we are within the correct parameter size of the current linked list if we are larger than with like a index let's just say we give it an index with the self size is only 10 we'll just immediately return 'cause that's impossible to add it Then we initialize two variables cur to hold the head of the list and then new node will be the node value that we are inserting The index is less than or equal to zero we want to update the new nodes next pointer to the current node then we want to update the head to point to the new node We loop through until we are one before the index specified using the current next method to move the pointer forward then we set the new nodes next pointer and that is set equal to the current dot next pointer So it removes the current nodes next pointer and assigns it as the new nodes next pointer thus updating the new nodes next pointer to hold the current node's next pointer thus taking over the current nodes next pointer Then we set the nodes next pointer to point to the new node Finally we update the size by one. For the delete add index if it is less than zero or greater than the size we also want to return early Initialize the current to start at the head of the current linked list that we are checking for If the index is equal to zero we want to update the self head and we want to remove the head by updating the self head to point to the next pointer Else we loop through until we are in one position before the specified index with the current next implementation and move the pointer forward then we use current next and we want to update that pointer to point to the note after and that will successfully decouple the node and update the next pointer to point to the node beyond the index specified so it skips 1NODE Then we decrement the size by one.  