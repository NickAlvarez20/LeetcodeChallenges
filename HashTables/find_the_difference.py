from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = ""

        frequencies_1 = Counter(s)
        frequencies_2 = Counter(t)

        for key, val in frequencies_2.items():
            if key not in frequencies_1 or frequencies_2[key] > frequencies_1[key]:
                result += key
        return result


# # Intuition
# <!-- Describe your first thoughts on how to solve this problem. -->
#  The intuition is to use a frequency counter or a dictionary to identify the outlier The important distinction is when we have a count greater in another count but the key is the same Therefore frequencies and dictionaries work best here.

# # Approach
# <!-- Describe your approach to solving the problem. -->
# The approach is to 1. create a result that will store the letter. 2. Then create two frequency dictionaries using Counter. 3. Then loop through keyvalueusing.items. 3. Then we can check if the key is not in frequencies one or if the value within frequency 2 is greater than frequency 1, For example if we have A and AA, We will need to check if the frequency count is greater. 4. Then we can add to the result, Since we are updating a string variable. 5. Then return the final result

# # Complexity
# - Time complexity:
# <!-- Add your time complexity here, e.g. $$O(n)$$ -->
# The time complexity for this is O of M + N. We need to scan through the entire length of frequency too and then compare it against the frequency one dictionary. 

# - Space complexity:
# <!-- Add your space complexity here, e.g. $$O(n)$$ -->
# The space complexity is O of M + N where frequencies one and two counter dictionaries are equivalent to any given length. So worst case situation if we have unique elements. 

#  Note that when a problem states the input only contains lower case English letters the alphabet size is fixed at 26 because 26 number changes the space complexity becomes O-1 and the loop becomes O-1. If the input could contain any infinite unique characters like full unique code slash email he's your OM plus N space analysis is 100 percent correct. 

# # Code
# ```python3 []
# from collections import Counter

# class Solution:
#     def findTheDifference(self, s: str, t: str) -> str:
#         result = ""

#         frequencies_1 = Counter(s)
#         frequencies_2 = Counter(t)

#         for key, val in frequencies_2.items():
#             if key not in frequencies_1 or frequencies_2[key] > frequencies_1[key]:
#                 result += key
#         return result
