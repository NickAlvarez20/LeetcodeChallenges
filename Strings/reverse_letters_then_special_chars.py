# Intuition
# So the intuition is to use a stack or two pointers Intuitively the first one that stands out is using the 2 pointers approach but this becomes quickly complex Therefore the most convenient and optimal solution is using a stack and simple alpha checks or special character checks Since we are not specifying explicitly special characters all we're doing is checking if it's an alpha because of their parameters of the given context for the constraints

# Approach
# First step is to create letters and special list and initialize them as empty then we want to loop through gather all the characters for character in the string we want to check if it's an alpha if it is alpha we're going to append it to our empty letters list else we're going to append it to our special characters list. Next thing we're going to want to do is initialize an empty result list and we're going to loop through the characters in string now we're going to check conditionally if character is alpha we need pop it from the stack of our letters stack and a pin that pop to the result Otherwise we're going to pop from the specials list stack and pin that to result doing these operations in this process will give us conditional check for each character and will help us to reverse them correctly based on the stack order.

# Complexity
# - Time complexity: O(N)
# We iterate through the string of length N twice: once to populate the stacks and once to reconstruct the result. Each insertion and pop operation takes O(1) constant time. Since there are no nested loops, the overall time complexity is strictly linear.


# - Space complexity: O(N)
#  We allocate members for the letters and special stack as well as the result stack so it scales linearly with the input size of the string, Therefore the auxiliary space is O of N


class Solution:
    def reverseByType(self, s: str) -> str:
        # Separate letters and special chars into their own pools
        letters = []
        specials = []

        for char in s:
            if char.isalpha():
                letters.append(char)
            else:
                specials.append(char)

            # Reconstruct the string using stack
            # If the original slot was a letter, pop from the letter pool (gives reversed order)
            # If it was special, pop from the special pool (gives reversed order)
        result = []
        for char in s:
            if char.isalpha():
                result.append(letters.pop())
            else:
                result.append(specials.pop())
        return "".join(result)
    

        #  Wrong because strings are immutable, therefore cannot swap in place 
        # index1 = 0
        # index2 = len(s) - 1
        # # two pointers approach
        # left = s[index1]
        # right = s[index2]

        # while index1 != index2 and len(s):
        #     if (
        #         isinstance(s[index1], str)
        #         and s[index1].isalpha()
        #         and s[index1].islower()
        #         and isinstance(s[index2], str)
        #         and s[index2].isalpha()
        #         and s[index2].islower()
        #     ):
        #         s[index1], s[index2] = s[index2], s[index1]
        #     else:
        #         continue

        # while index1 != index2 and len(s):
        #     if (
        #         isinstance(s[index1], str)
        #         and isinstance(s[index2], str)
        #         and s[index1].isalnum()
        #         and s[index1].isspace()
        #         and s[index2].isalnum()
        #         and s[index2].isspace()
        #     ):
        #         s[index1], s[index2] = s[index2], s[index1]
        # return s
