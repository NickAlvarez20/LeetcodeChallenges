from collections import Counter


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        freq_dict = Counter(nums)
        for key, value in freq_dict.items():
            if value > len(nums) // 2:
                return key
        return 0


# Time Complexity - O(n)
# Creating the counter numbs object requires a single Passover the input list of size and resulting in O of n time
# The for loop iterates through the unique keys in the dictionary in the worst case if most elements are unique there are up to N keys but the total number of operations remains proportional to N
# Each dictionary look up in comparison within the loop takes O of constant time average

# Space Complexity - O(n)
# So the dictionary is open as we have to build it out so this results in o of n


# The intuition for majority element is to use a frequency dictionary and using mathematical equation we can check if the value is greater than length of noms divided by 2 and it exists in our dictionary as a value then we can return the key

# 1. First we initialize a frequency dictionary using collections importing Counter and declaring frequency dictionary is equal to the frequency dictionary of the noms array that we are currently evaluating
# 2. And then we loop through using four key value and frequency dictionary.items method
# 3. Then we check if the value is greater than the length of the noms array divided by 2
# 4. Then we return the key which will be the value that we are looking for and this will find the majority element
# 5. If not we return zero


# Analysis: This runtime is three milliseconds it beats 84.8% of solutions memory was 21.16 megabytes and it beats 31.77% of solutions based on the graph region it is in the top 20% of all answers combining runtime and memory

# Alternative solutions: The alternative solutions includes sorting We begin by sorting the array in non decreasing order and this rearranges the element such that identical elements are grouped together once the array is sorted the majority element will always be present in the middle of the array This is because the majority element occurs more than N / 2 times in when the array is sorted it will occupy the middle position therefore we can use a mathematical formulae to determine. 
# The other alternative is the one we have already completed using a hash map AKA a frequency map
# The third one is the Moores voting algorithm it's based on the fact that there is a majority element in an array it will always remain in the lead even after encountering other elements so we initialize two variables counting candidates that count to 0 and candidate to an arbitrary value we iterate through the array nums count is zero assign the current element as a new candidate and increment count by 1 So this one's a little bit more advanced and requires knowledge of the moore's voting algorithm. 
