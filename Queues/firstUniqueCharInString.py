from collections import deque

# Solution 1: This one I used the DQ data structure to access the pop left for a queue and optimized data structure Python library So I broke it out into a DQ to have access to the operations of the optimized queue that Python offers and then I use the list method to change the string into a list I declared a frequency dictionary variable and then I loop through the items in the queue and I said if item is there increase the frequency else it's equal to one and then we use index character in enumeration to check the very first instance of the character that is equal to 1 and then we can return its index otherwise we return -1

class Solution:
    def firstUniqChar(self, s: str) -> int:
        queue = deque(list(s))
        frequency_dictionary = {}
        for item in queue:
            if item in frequency_dictionary:
                frequency_dictionary[item] += 1
            else:
                frequency_dictionary[item] = 1
        for index, char in enumerate(s):
            if char in frequency_dictionary and frequency_dictionary[char] == 1:
                return index
        return -1


# Solution 2 : Use a dictionary iterate through the string and tally up the frequency of the current letter by iterating through the frequency dictionary to check if it is in there. Then using index value and enumeration we can check if the value is in frequency dictionary and the frequency dictionary value is equal to 1 on the first pass we will find the first letter that is the target value we can return its index otherwise we return -1
class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq_dict = {}
        for letter in s:
            if letter in freq_dict:
                freq_dict[letter] += 1
            else:
                freq_dict[letter] = 1
        for index, val in enumerate(s):
            if val in freq_dict and freq_dict[val] == 1:
                return index
        return -1

# Solution 3: Queue implementation

class Solution:
    def firstUniqChar(self, s: str) -> int:
        queue = deque()
        freq_dict = {}
        for index, char in enumerate(s):
            freq_dict[char] = freq_dict.get(char, 0) + 1
            queue.append((char, index))
        while queue:
            char, index = queue.popleft()
            if freq_dict[char] == 1:
                return index
        return -1


testString = "leetcode"
test = Solution()
print(test.firstUniqChar(testString))

# Intuition:
# The intuition is to loop through the screen and create a dictionary to understand the frequency count and then we loop through one more time and we want to check each letter and see what its frequency count is within the dictionary and if that equals 1 then we can return its index.
#
# Approach: For queue algorithm
# 1. Declare a variable called Q and set it equal to a deque data structure
# 2. Declare a frequency dictionary and set it equal to an empty curly braces indicating a dictionary
# 3. Using four index value and enumeration we want to loop through the string
# 4. Then we'll use A reference to the frequency dictionary and index bracket access to identify if it exists within it'sdictionarymethod.git char and zero for the value starting off and then add one for each time that it's seen within the dictionary
# 5. After that we append to the queue the index and the value of the current character This will allow us to store the data of the index and value within a tuple that will be crucial in retrieving the correct index value for this problem
# 6. Then while the queue is not empty loop through it
# 7. Then using char index we can set the character and destructure the character and the index from Q popleft which will unpack the tuple and store it in Character in index accordingly
# 8. For each iteration we want to check if the current character count is equal to one so using frequency dictionary reference and bracket notation to reference the key this will allow us to check the value of the key and if the key is equal to 1 then we return the index otherwise return -1


# Time complexity: O(n)
# 1. The time complexity of the largest coefficients to be evaluated would be the four in the while loop Each is one pass through the string and one pass through the queue all operations are O of one therefore time complexity is O of N

# Space complexity: O(n)
# 1. Space complexity requires building a queue structure and that is O(n)

# Analysis: The runtime is 127 milliseconds with the Q data structure it beats 6.42% and the memory is 29.42 megabytes and it beats 5.9% of solutions
# Total time to solve: Total time to solve was about 20 to 30 minutes but due to iterating on the algorithm it was around 40 to 50 minutes This was crucial because I was understanding how to implement the brute force solution of dictionary and frequency matching and then I wanted to understand how to implement the same logic using a queue The Q method was a little bit tougher because I did have to understand the get method and the index value method as well as unpacking the contents into the variable and using key value index bracket notation to access the value of the key and the contextual switching from multiple different languages
# Alternative solutions
# 1. The alternative solution to the queue implementation is simply building a frequency dictionary and looping through with enumeration to check the index value and the index within the dictionary where the count is equal to 1

# The standard way most engineers would prefer the dictionary only approach to passes over the string because it uses O of one additional space for the character set whereas the queue approaches uses O bin space for the queue itself the queue approach is actually better for streaming data if the string was an infinite stream of characters and you needed to find the first unique character at any given moment your Q solution is superior because it avoids rescanning the entire string from the start. 