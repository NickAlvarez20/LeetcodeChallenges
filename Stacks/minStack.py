class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        min = self.stack[0]
        for num in range(self.stack):
            if num < min:
                min, num = num, min
        return min


class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        min = self.stack[0]
        if self.stack.append(val) < min:
            min = val
        self.stack.append(val, min)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.pop(min)

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(val)
            min = self.val
        else:
            min = self.stack[0]
            if self.val < min:
                min = val
            self.stack.append((val, min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# Intuition:
# Straightforward implementation of a stack. The only thing that needs to be changed is the get min. Need to loop through the entire array and find the minimum. This straightforward approach solves it, but there is an optimized approach. The clever solution that's OVON uses a tracking of the last pop. Storing that in a variable and then comparing that to min and updating the min.
#
# Approach:
# 1. Implement self stack for the initialization of the first data structure.
# 2. Use stack data pinned to push a new value toward the end of the array that we are using.
# 3. Use self stack pop to remove the last element.
# 4. Use soft. Stack with -1 index access to retrieve the stack at the end of array.
# 5. Create a minimum that stores the first initial Number within the array
# 6. Compare that minimum of the first value of the array with every number in the array and update it if the current number is less than the min.
# 7. Thin swap the. Minimum width The current value if the current is less than.
# 8. Finally, return the min.

# Time complexity: O(1)/O(n)
# 1. Time complexity for most of it is O(1) for push, pop and top.
# 2. For getMin, it is O(n) wherein is the length of the array or in this situation, stack.

# Space complexity: O(1)
# 1. Space complexity for all methods are O(1)

# Analysis: Current runtime is 627 MILLISECONDS. It beats only 5% of the other solutions. The time complexity is 22.47 megabytes and it only beats 12.51% of solutions.
# Total time to solve: This is a medium level solution and despite it being medium I solved it in 5 minutes. Everything was straightforward from push, pop top and then implementing a simple for loop to update the min.
# Alternative solutions
# 1. The optimal alternative solution is. Pop and as we pop we store the value in min and then compare the last pop value with the next pop value and if one of them is lower then we can swap the minimum and return it, therefore keeping track of the state and updating without having to loop through each time. Therefore by the time the stack is empty we have the minimum value without needing the check again.
# 2. We could also do a linked list implementation with similar logic, although we would have to update the pointers for. Some of these situations which is a little bit more complex and memory intensive for this solution it would not be optimal.
# 3. There are further alternative solutions, but for the sake of argument will only stick to these two for now.
