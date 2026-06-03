class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = {}
        total_pairs = 0

        for num in nums:
            prev_seen = counts.get(num, 0)

            total_pairs += prev_seen

            counts[num] = prev_seen + 1
        return total_pairs

        # Brute Force Solution
        # def numIdenticalPairs(self, nums: list[int]) -> int:
        # count = 0
        # # Start i from 0 to the second-to-last element
        # for i in range(len(nums)):
        #     # Start j specifically from i + 1 to avoid i == j and duplicates
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             count += 1
        # return count

# Intuition:
# So the intuition is to count the number of occurrences of numbers that are matching within the array.
#
# Approach: Hash map
# 1. The hash map approach involves creating a counts variable as a dictionary
# 2. Then we create a total pairs variable and set that equal to zero This will store the total pairs that we have seen based on the frequency within the dictionary
# 3. Next thing we do is loop through the entire nums array
# 4. Then we create a variable called previously seen and it equals the dictionary.get method and we use NUM as the key and set the initial value to 0
# 5. After that we increment total pairs plus equals previously seen. 
# 6. Then we update the key value pair with counts with the key of the current NUM and then equals previously seen plus one
# 7. we loop through the entire array and then we return the total pairs. 



# Time complexity: O(n)
# 1. Your time complexity is linear where N is the number of elements in the input list Algorithm iterates through the list exactly once Use this constant operations inside the loop hash maca operations like git look U and update a key insertion take O of 1 constant time on average. The hash map allows for optimal time complexity because it gets rid of the double nested for loops.
# Space complexity: O(n)
# 1. Space complexity is linear because the memory use grows relative to the size of the input Worst case if every number in the list is unique the hash map will store N distinct keys. In many coding problems the range of numbers is small between one and 100 if unique elements are limited by a fixed constant the space could technically be considered O of one constant space because the map will never grow beyond that fixed limit

# Analysis: The solution is zero milliseconds and it beats 100% of the solutions the memory is 19.3 megabytes and it beats 16.12 percent of all solutions on leak code This places the problem in the upper 1% of all total solutions. 
# Alternative solutions
# 1. The alternative solution to the hash map would be a brute force approach using a double nested for loop

# What I learned from this problem was that it's good to go through the brute force solution and then to recognize the creation using brackets with a Python dictionary and the git method so in order to be proficient with a hash map you must be familiar with all the dictionary methods including git and how they're syntactically invoked using key and the current value in order to be able to optimize the solution as well as being familiar with key value pairs looping through them updating them just the normal syntax of the data structure with the bracket notation It's a constant pattern that's recognized.
