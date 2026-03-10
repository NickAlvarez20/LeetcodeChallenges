class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        str = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            if str[left] not in vowels and str[right] in vowels:
                left += 1
            elif str[left] in vowels and str[right] not in vowels:
                right -= 1
            elif str[left] in vowels and str[right] in vowels:
                str[left], str[right] = str[right], str[left]
                left += 1
                right -= 1
            else:
                left += 1
                right -= 1
        return "".join(str)

# Intuition:
# We can use a two pointer approach for reversing the matching valves within the string so we'll use a left and a right pointer and conditional checks.
#
# Approach:
# 1. Create a string of vowels to check with for each iteration
# 2. Turn the string into a list by assigning it to string variable and using method list
# 3. Assign left and right pointers to the zero index and the last index within the length of the string
# 4. Declare While left is less than right loop for two pointers technique
# 5. We check if The left pointer value not in valves and the string right in vowels we need to increment the left pointer by 1
# 6. Else if the left pointer value invals and the right pointer value not in vowels then we decrement the right pointer
# 7. Else if both are in vowels Then we will swap increment left pointer by one and decrement right pointer by one
# 8. Otherwise we're just going to move the pointers because it's two consonants


# Time complexity: O(n)
# Time complexity is oven since we are using a while loop and conditional basis to check each position within the list
# Space complexity: O(n)
# For this solution it is O of N since we are creating a list called string that allows us to evaluate with the Python language to iterate through the string and then join it back once we have updated using an index based position strategy. This is also good to know that strings are immutable to swap characters by index you must convert the string into a list which creates a new data structure of size in additionally the final join method creates another new string of size N thus the extra space scales line eerily with input

# Analysis:
# The runtime is 7 milliseconds it beats 89.8% of solutions and the memory is 20.70 megabytes and it beats 23.26% of solutions
# This was a great easy exercise for understanding how to move pointers and implementing the two pointers technique for a variety of conditions. 
# We can optimize the lookup speed for vows by instead of using a string which is O of K where K is the number of vowels we could optimize it by using a set that is O of one on average.
