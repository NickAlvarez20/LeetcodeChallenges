# Intuition: strings module for alphabet creation, slicing for reversing, dictionary for mapping key, values and awareness of the enumerate function(with starting index syntax), how to create key, value pairs for the dictionary, and once again using enumerate for access to index, value properties to properly calculate the final total sum

# Approach: First step is to use the strings package to create a lowercase alphabet then create a slice starting from the end with negative to reverse that alphabet Then we create a dictionary to To Dictionary with key value pairs This will make it O-1 instant access and will significantly increase the efficiency of our algorithm so iterate using enumerate to create this dictionary we also want to make sure that we start at one and not zero. Next we're going to create a total sum variable that will be updated as the algorithm processes. Then we're going to iterate once again through the string this time using index value and enumerate also making sure to start at 1 to get rid of the zero index behavior that is default if we see that the value exists in our dictionary alphabet that we have mapped with the reverse order we will add the total sum using The value assigned to that key and the last part is to multiply by the index so we must make sure once again to start our enumeration index at one in order to get the proper multiplication That's two part process in the mathematical component of the algorithm in order to process this efficiently thus yielding the correct result. 

# Complexity:
# Time: O(n)
# The time complexity is linear as we need to enumerate through any given string and we need to create a reversed alphabet with an dictionary The largest part of the process is the iteration resulting in a linear time complexity .
# Space: O(n)
# We are creating a dictionary which is uses O in space based on the size of the dictionary components that we are adding into it a total sum variable and other variables like creating a alphabet using the string library and a slice all this results O of N extra space. 

import string


class Solution:
    def reverseDegree(self, s: str) -> int:
        alphabet = string.ascii_lowercase
        reverse_alpha = alphabet[::-1]
        map_alpha = {}
        for i, char in enumerate(reverse_alpha, start=1):
            map_alpha[char] = i

        total_sum = 0
        for index, value in enumerate(s, start=1):
            if value in map_alpha:
                total_sum += map_alpha[value] * index
        return total_sum
