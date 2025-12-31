class Solution:
    def reverseWords(self, s: str) -> str:
        wordList = s.split()
        reversedWords = wordList[::-1]
        return " ".join(reversedWords)


# Intuition: Use a variable to keep the string that we will split into a list and then use a slice to return that list in reverse order finally using the join method and a separator of space indicated we can rejoin list into a string.

# Approach
# 1. First we want to split the original string into a list using the split method and store that in a word list variable
# 2. Next we want to reverse the list using a slice and store that in a variable called reversed words
# 3. Finally we want to join by a space separator the reversed words variable back into a string

# Time complexity: O(n)
# 1. Split method is O(n) for any given string length
# 2. Slice is O(n) for any given list (creates a new list)
# 3. Join is O(n)for any given list
# 4. Therefore total time complexity for the maximum coefficient is O(n) where n is the length of the string
# Space complexity: O(n)
# 1. Storing the results of the split string in Word list is O(n)
# 2. Storing the slice of word list that reverses the list is O(n)
# 3. Returning the final sorted word into a string using the join method is also O(n)
# 4. Therefore the maximum coefficient for the space complexity is O of N for any given string
# Alternative methods.
# 1. An alternative solution is to reverse in place with two pointers to use O of one space excluding output but it's more complex and not worth it in Python for this problem. This would be the most official elite code solution since it uses the 2 pointer method and that pattern is something we need to work on.

# Analysis: Overall analysis the runtime is zero milliseconds and it beats 100% of official leetcode solutions the memory is 17.44 megabytes and it beats 91.39% of solutions. 
# Total time to solve: Total time to solve was relatively quickly I would have put it at about maybe 10 to 15 minutes for this medium level string challenge This is because I am currently rusty at Python but this was actually a very easy problem to solve. 
