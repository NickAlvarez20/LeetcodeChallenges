class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)

testString = "abbaca" # Output should equal ca
testStringTwo = "azxxzy"  # Output should equal ay
solution = Solution()
testResult = solution.removeDuplicates(testString)
testResultTwo = solution.removeDuplicates(testStringTwo)
print(testResult, testResultTwo) # prints valid results

# Intuition:
# So we loop through the entire string and make a comparison after each char in the string if the char after the current string matches then we remove it Add all the strings that do not have a positive match There are two ways to do this One is with a stack the other is with two pointers and the third is brute force We could also do fast and slow pointers for this one since I'm learning stacks we'll do a stack
#
# Approach:
# 1. create an empty stack using array
# 2. loop through string
# 3. at each step, Check if the stack is not empty and the top of the stack matches the current character
# 4. If it does match then we pop that current value, Remove the pair
# 5. Else we append to the stack
# 6. Finally we'll have a stack with all the remove duplicates and then we just perform a simple join to get the proper output string

# Time complexity: O(n)
# 1. Time complexity is O(n) Since the largest coefficient is the for loop so for any gaping stack size and string size will just pass one time

# Space complexity: O(1)
# 1. Space complexity is O(1) since we are building a stack

# Analysis: The runtime is 23 milliseconds that beats 44.1% of all solutions and the memory is 18.23 megabytes and it beats 82.12 percent of all solutions it is within the top 25%. 
# Total time to solve: Had the revisit stacks and check out how to build one and understand the difference between array and linked list The simplification of a stack using an array versus the ability to add on easier if the stack becomes very large then we would use a linked list this is important to know with larger systems Because we do not have to reallocate memory whereas we would within an array So linked list dynamic although it does cost a little bit more memory because we are using pointers and storing pointer therefore it's a little bit costlier.

# Alternative solutions
# 1. An alternative solution that I'm considering is two pointers one that keeps track of the current index value and the other that keeps track of the next index value, Then we compare the current with the next and if they match then we could basically not add them into the list or string we are building.
# 2. The next one would be fast and slow pointers although in this situation now that I think of it it would only retrieve the middle value and we need to iterate through the entire so in this situation fast and slow pointers do not work
#. 3 The 3rd solution would be brute forcing with a double for loop but this is time complexity of ON squared which is not going to be the best solution especially as the system goes larger but it can be performed similar to two pointers.
