from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        frequency_dict_ransom = Counter(ransomNote)
        frequency_dict_magazine = Counter(magazine)
        for key, value in frequency_dict_ransom.items():
            if frequency_dict_ransom[key] > frequency_dict_magazine[key]:
                return False
        return True

    # Intuition:
    # So the intuition is to use hash map and determine the key value pairs Essentially what we want to do is understand that if the ransom note frequency value associated with the key for example let's just say we're looking at a we see that it has a 2 if that is greater than Within magazine then we do not have enough letters in magazine.
    #
    # Approach: Hash map
    # 1. We create a frequency dictionary variable for the ransom using Counter class from collections module which is part of the Python standard library.
    # 2. Then we create a frequency dictionary variable for magazine using the Counter class from collections module which is part of the Python standard library
    # 3. Loop through using for key, value in frequency_dict_ransom.items(): Which allows us to gain access to the key value tuple using the dot items method
    # 4. next we do a conditional check: We check if the value in the ransom using variable name with bracket notation that accesses the key in the current iteration, Thus looking at the frequency value within the counter hash map. We check if it is greater than the same value that is indicated in the hash map magazine frequency dictionary. This allows us to essentially look at the key value pair and identify the value of each dictionary if the ransom value is higher than The magazine value then it is theoretically impossible to reconstruct.
    # 5. We return false if we find that the frequency value for each associated character within our frequency dictionary of ransom is greater than its counterpart within the frequency dictionary of the magazine.
    # 6. Otherwise we return true this means that there is greater than or equal to letters which allows us to reconstruct properly.

    # Time complexity: O(m+n)
    # 1. Time complexity is O of m+n
    # Create encounter magazine frequency dictionary takes O(m) time and counter random note takes O(n) time
    # The for loop runs K times where K is the number of unique characters in the ransom note since there are at most 26 lowercase English letters this part is typically O(1) or O(k)
    # Dictionary access is O(1) on average
    # Space complexity: O(1)
    # 1. The problem constraints usually specify that the input consists of lowercase English letters therefore dictionaries will never store more than 26 keys regardless of how long the strings are since 26 is a constant the space is O(1)
    #If the character set was infinite then it would be O(k) where K is the number of unique characters

    # Analysis: This current solution that I built is 7 millisecond runtime beats 94.5% of all answers and the memory is 19.74 megabyte and it beats 13.76%. This leads me to question the memory usage of the counter frequency dictionary as it could be optimized it looks like the lower end of the threshold is 17.1 megabytes. The solution stands within the top 10% of all answers combining runtime and memory usage.




    # Alternative solutions
    # 1. Pythonic Counter Subtraction: The collections.counterclass supports multi set subtraction if you subtract the magazine from the ransom note and the result is empty it means the magazine had enough characters So it's a simple one line return not counter(ransomNote) - counter(magazine)
    # python
    # from collections import Counter

    # class Solution:
    #     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    #         # Subtracting Counters removes keys with non-positive counts
    #         # If (ransomNote - magazine) has no elements, the result is an empty Counter
    #         return not Counter(ransomNote) - Counter(magazine)



    # 2. Single Counter Optimization (Better Memory) - Instead of creating two full frequency dictionaries you can create one for the magazine and then decrement counts as you iterate through the ransom note this is more efficient because it can return false as soon as the shortage is found. This involves creating a account variable setting it equal to the counter of the magazine so we get a frequency dictionary for the magazine then we loop through four character in ransom note if the key of the magazine is less than or equal to zero then we can return false otherwise we decrement the value of the key within the counts frequency dictionary by -1 If this passes then we return true
    # class Solution:
    #     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    #         counts = Counter(magazine)
    #         for char in ransomNote:
    #             if counts[char] <= 0:
    #                 return False
    #             counts[char] -= 1
    #         return True



    # 3. Array-based Solution (Best Performance): Since the problem typically involves lowercase English letters using a fixed size array size 26 is faster than a hash map dictionary and uses less memory.
    # class Solution:
    # def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    #     # Array for 26 lowercase English letters
    #     counts = [0] * 26

    #     for char in magazine:
    #         counts[ord(char) - ord("a")] += 1

    #     for char in ransomNote:
    #         index = ord(char) - ord("a")
    #         if counts[index] == 0:
    #             return False
    #         counts[index] -= 1

    #     return True


# 4. Using str.count(): For can slice solution without imports you can iterate through the unique characters in the ransom note while this can be O of N times N in some languages Python count is highly optimized in C.
# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         # Check count of each unique character in ransomNote
#         for char in set(ransomNote):
#             if ransomNote.count(char) > magazine.count(char):
#                 return False
#         return True

# Comparing solutions: 
# Solution 1 is the most readable and "Pythonic."
# Solution 3 is generally the fastest for large inputs because it avoids the overhead of hash map collisions and object creation in the Counter class.
# Solution 2 is a great middle-ground for interviews, showing you understand how to optimize by returning early.
