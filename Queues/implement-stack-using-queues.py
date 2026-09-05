# # Intuition
# A stack uses last in first out, so it behaves similarly to a deque. From collections, we can import the deque and utilize this to implement two stacks with all the operational abilities of a deque.

# # Approach
# 1. First, we want to go into collections and import DQ.
# 2. Next we want to self set up the constructor method init. So we're going to say self.q1 equals an emptyDQ as well as self.q2 equals an emptyDQ.
# 3. Next, we want to define our push method so in order to do this, we're going to first append to q2 the x that is given within the push call.
# 3a. Next we're going to initialize a while loop and make sure that it runs as long as Q1 is currently full or has elements existing.
# 3b. Within the while loop, we'll set a temp variable to store the pop left from Q1, and then we can use that temp variable to append it to Q2.
# 3c. Then we want to make sure that Q1 overtakes Q2, so we set Q1 is now equal to self.Q2, which allows us to extract the data and make Q1 work properly.
# 3d. Then we want to clear out the Q2. So we set Q2 equal to an empty DQ.
# 4. We are only going to be removing so this one's relatively simple. We create a variable called removedElement, set it equal to the pop() of q1, and then return that removedElement.
# 5. In order to peak from the top, we're going to create a variable called peaking set equal to the zero position index within Q1 and then return that variable.
# 6. For the empty method, we want to return a boolean, so all we do is return the length of self.q1 if it's equal to 0. This will return True if true, else False.


# # Complexity
# - Time complexity: O(N)
# The time complexity is based on each part of the class. So we have methods push, pop, top, and empty. And within these methods, the process is pretty straightforward. Most of them are constant. The only one is push, which we need to consider for this current implementation. That would be the while loop that iterates until the length of Q1 is empty while updating Q1. So it would be O of n for any given length of Q1.

# - Space complexity: O(N+M)
# The space complexity revolves around setting up a Q1 and a Q2. So, allocating memory for the Qs and temporary variables. Overall, the time complexity is O(N * N). Alternatively, it is O(N + M), where N is the length of Q1 and M is the length of Q2. The majority of the space will come from Q1.

# Code

from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        

    def push(self, x: int) -> None:
        self.q2.append(x)
        while self.q1:
            temp = self.q1.popleft()
            self.q2.append(temp)
        self.q1 = self.q2
        self.q2 = deque()
        

    def pop(self) -> int: # removing
        removed_element = self.q1.popleft()
        return removed_element
        

    def top(self) -> int: # peeking
        peeking = self.q1[0]
        return peeking
        

    def empty(self) -> bool: # return len
        return len(self.q1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
