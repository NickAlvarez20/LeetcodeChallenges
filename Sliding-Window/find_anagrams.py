from collections import Counter


class Solution(object):
    def findAnagrams(self, s, p):
        # Declare length for s and p
        s_len = len(s)
        p_len = len(p)
        # Edge case for initial smaller s than p
        if p_len > s_len:
            return []

        # Declare three vars, result and target/window counts for freq dictionary
        result = []
        target_counts = Counter(p)
        window_counts = Counter(s[:p_len])

        # Loop through the entire s string using sliding window
        for i in range(s_len - p_len + 1):
            # Check if frequencies match
            if target_counts == window_counts:
                result.append(i)
            char_to_remove = s[i]  # Easier to read
            window_counts[char_to_remove] -= 1
            if window_counts[char_to_remove] == 0:
                del window_counts[char_to_remove]
            right = i + p_len  # Easier to read
            if right < s_len:
                window_counts[s[right]] += 1
        return result

# Intuition:
# Identifying the pattern within is to see that we are given two inputs 1 is given string and the other is window Therefore we will use sliding window to solve this problem.
#
# Approach:
# 1. The first step is to declare two variables for SMP to determine their length so we can utilize this for the algorithm
# 2. The next situation is to set up an edge case if initial string length is smaller than the given P
# 3. After that we have to declare 3 variables. One is to hold the that will be returned at the end as determined by the problem constraints. Next we want to use a frequency dictionary for the algorithm so we will declare target counts set it equal to the counter which turns P into a frequency dictionary holding its current values. Next we want to declare another variable called window counts using a frequency dictionary for S and within S we do a slice up to P length This is important when comparing the anagram
# 4. Then we want to loop through the entire S string using the sliding window syntax so a for loop and add since indexes start at 0
# 5. For the first part of the logic we wanna check if the frequencies match within our target counts and compare this to window counts If we find a match we are going to append the current I value to result
# 6. Then we create a chart to remove and set it equal to s[i] This will allow us to access the current character within the S string and it makes it easier to read
# 7. Then decrement the character that we are removing from the window by since it no longer exists within that frequency dictionary as we move forward we decrement the count
# 8. We want to check if the window and the character that we removed equals zero Because if it does we should remove that from the current frequency dictionary window in order to properly assess the anagram. If it does equal zero we remove that from the window counts window.
# 9. We declare a variable called write and set it equal to I plus P length This will make it easier to read
# 10. We check if right is less than S length to make sure that we are not outside of the given primary array of S linked if it were larger than as length we would be outside and we would get an index out of bounds
# 11. If the last in condition is true then we can proceed with the logic and increment the count of the character that is now being introduced with the sliding window algorithm and increase the frequency by 1 This will find the exact letter in that frequency dictionary of window counts and increment its count by one So if a becomes introduced then we will increase the value of that current frequency dictionary of a plus one
# 12. Then we return the result and this will give us the correct output with the correct indices also we will find all of the start indices of PS anagrams in S


# Time complexity: O(n+m) - (Where N is the length of string S and M is the length of string P)
# Building the initial frequency map for P takes O of M time
# Reiterate through string S exactly once for each of the N characters we perform constant O of one operations updating two values in a hash map comparing two hash maps of a fixed size at most 26 characters
# Since we only visit each character once the total time complexity is linear or O More specifically O of N + M

# Space complexity: O(k)
# K is the size of character set slash alphabet in this case 26
# Frequency maps we maintain two hash maps or arrays to store character counts
# Because the input is restricted to lowercase English letters these maps will never exceed 26 entries regardless of how large the input strings in or in become
# Since the extra space used does not grow with the input size and the space complexity is O-1 constant space. More precisely this would be O of K where K = 26 for the letters in the alphabet all lower case. 

# Analysis:
# The runtime is 123 milliseconds it beats 84.49% of all solutions The memory is 13.59 megabytes and it beats 56.34% of all solutions
# It requires some expertise with frequency dictionaries and understanding when it's important to delete them How to check and compare frequency dictionaries How to initialize the frequency dictionaries with the proper slice and how to access the proper character using bracket notation We also have edge cases where we want to analyze if the window is out of bounds which is important to know for a common edge case situation testing it's also important to know how to update the logic properly after we append I we actually want to step out into the outer scope in order to properly assess and update the character count of the left that is being removed and increase the character count of the right side of the window that is being incremented. Overall it's a medium level problem It's very good for understanding this type of pattern where we need a sliding window to analyze and update the algorithm to pull out various data for analysis or checks. This is important to know because creates a resource optimization laws for proper scalability memory efficiency and real time processing For example real time processing You don't need the whole data set to start you can process data as it slides into your system memory efficiency instead of storing every possible subsegment of Theta you only store the current state of the window saving massive amounts of RAM As the data set becomes larger this algorithm takes it from hours to run comparing it to seconds. 

# Alternative solutions
# Instead of a hash map dictionary we could use a frequency array of size 26 to store character counts In Python this is often faster because list indexing team is more efficient than hashing dictionary keys
# We could use a sliding window with a match counter Instead of comparing in higher frequency maps at every step maintain a single integer called matches Matches tracks how many of the 26 possible characters have the exact same count in both the window and the target
# To pointer approach with a flexible window is an alternative This is a more generalized version of the sliding window that is useful for other substring problems where the window size might not be fixed
