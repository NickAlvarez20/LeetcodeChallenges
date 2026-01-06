class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if char != "*":
                stack.append(char)
            elif stack:
                stack.pop()
        return "".join(stack)

# Intuition:
# Build a stack and check each letter within the string if the string does not equal a star we can append this to the stack Then anytime it is a star and we encounter it then we're going to pop This will remove the * and we'll remove the character that was previously pushed thus resulting in both the star and the character to the left being removed.
#
# Approach:
# 1. Create an empty stack
# 2. Loop through the string
# 3. If the string does not equal a star then append the current character to the stack
# 4. Else if it is a star then we're going to pop from the stack resulting in the star not being appended and the character to the left of the star being removed with the pop operation
# 5. Finally we will do a join to return the fully formed string as requested


# Time complexity: O(n)
# 1. The largest coefficient is O(N) for any given string
# 2. So we loop through the string in one pass we're building the stack and then appending from the stack all of one operations and then a join at the end which is also of one Thus the total time complexity is O(n)

# Space complexity: O(n)
# 1. Space complexity we are building a stack therefore it is ON and this is the largest given space factor

# Analysis: The runtime is 77 milliseconds and it beats 99.37% of solutions The memory is 20.66 megabytes and it beats 5% of solutions This lands within the top 20% of all solutions
# Total time to solve: Total time to solve was about 45 minutes I had to go through the initial brute force solution and where I was doing too many conditional checks and over complicating the logic I was building two new stacks and then looping through them and then comparing the current pop value and removing the previous value Pretty straightforward brute force approach but not optimal since the complexity was getting very large and could result in a lot of buggy code After figuring out the simple solution was just to build the stack and then pop off the most recent Total time to solve was about 45 minutes.
# Alternative solutions
# 1. We could use a string as stack where we create a result stack we loop through the string if the character in the string is equal to a star as long as the stack is not empty then we will pop the value before it else we append and then join
# 2. We could do it recursively We check with the base case if the string exists and then we check the last end of the string and check it if it's equal to a star then we skip the star and also skip the char before it if exists By doing return self dot removes stars calling the function and using S bracket: -2 if length of S is greater than or equal to 2 else empty string Health conditions says returned self that removes stars parentheses S bracket: -1 so a slice from the beginning up until the end plus the last character of the string
# 3. Then we could also do the two pointer wizardry we turn the character into a list set a right index equal to zero and then for read index and range of the length of the list we have made if the characters of the read index are currently a star if the right index is greater than 0 then delete previous by moving pointer back one else char's right index equals charge read index so move the pointer forward and then increment right index plus or equal to one and then we can return with and a slice all the way up until the right index Right pointer only moved forward when keeping char moves back when deleting superficial and fancy for interviews
