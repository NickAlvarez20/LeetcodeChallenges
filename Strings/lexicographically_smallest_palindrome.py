# Intuition
# A two pointer approach with a convergent to a list and ordinal checks.

# Approach
# 1. First we initialize the left and right pointers and a convert to string where we convert an immutable string to a list
# 2. Next we initialize a while loop while left is less than the right pointer .
# 3. Then we do a conditional check if the current letter at the left pointer does not equal the right pointer
# 3a. Then we need to check the ordinal conversion between the left and right value If the one on the left is greater than we want to swap out the value on the left with the smaller ordinal value on the right and vice versa. 
# 4. Then we update the left and right we decrement
# 5. We must convert the list back into a string so we use the join method.
# 6. Then we return the join string

# Complexity
# - Time complexity: O(N)
# The time complexity is old in where in is the length of the string S. First converting the string into a list of characters takes O(N) time. Men are two pointer while loop processes the string from both ends meeting in the middle. Since the pointers move closer by one step each iteration the loop runs exactly in divided by two times. Inside the loop all character comparisons ordinal checks via Ord and assignments are O of one constant time operations so the loop takes O of N time. Finally joining the list back into a string takes another O of in time. Combining these steps in plus in/ 2 + N overall time complexity scales in the nearly which simplifies to O of N. 

# - Space complexity: O(N)
# The space complexity is open wherein is the length of the string S. Python strings are immutable sort of modify characters in place we must convert the string into immutable list of characters the list takes oven auxiliary space. Our 2 pointer variables left and right only require of one auxiliary space. At the end generating the final join string requires another OV in space for the return value. Therefore the total auxiliary memory used scales linearly with the input size giving us a space complexity above N. 

# Offer optimzation: If we want to optimize the auxiliary space complexity to O(1) in a real-world scenario, we could use a language like C++ or Java (with a char[] array modified in-place) where strings can be mutated directly without allocating extra structures, or ask if modifying the input in-place is allowed. However, due to Python's immutability, O(N) space is the optimal constraint here.

# Code
```python3 []
class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        conv_to_str = list(s)
        
        while left < right:
            if conv_to_str[left] != conv_to_str[right]:
                if ord(conv_to_str[left]) > ord(conv_to_str[right]):
                    conv_to_str[left] = conv_to_str[right]
                elif ord(conv_to_str[right]) > ord(conv_to_str[left]):
                    conv_to_str[right] = conv_to_str[left]
            left += 1
            right -= 1
                    
        joined_str = ''.join(conv_to_str)
        return joined_str



        # print(largest_ascii_val, min_ascii_val)


        # # Find largest ASCII value 

        # largest_ascii_val = 0
        # min_ascii_val = float('-inf')
        
        # for char in s:
        #     largest_ascii_val = ord(char)
        #     if ord(char) > largest_ascii_val:
        #         largest_ascii_val = ord(char)
        # for char in s:
        #     min_ascii_val = ord(char)
        #     if ord(char) < min_ascii_val:
        #         min_ascii_val = ord(char)

        

```