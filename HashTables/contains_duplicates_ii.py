class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        dictionary = {}
        for current_index, value in enumerate(nums):
            # checks key,values pairs in dictionary, dictionary stores {value, index} pairs
            if value in dictionary and current_index - dictionary[value] <= k:
                return True
            # if key doesn't exist in dictionary, then add it and set its value as the current index
            dictionary[value] = current_index
        return False


# Brute Force solution
# class Solution:
#     def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
#         correctRange = 0
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] == nums[j] and abs(i - j) <= k:
#                     return True
#         return False


# Intuition:
# So we want to loop through the array and we want to consider the current index that we're on and compare it to the sequential indexes see if they're equal and then if they do and the absolute value of I - J which is the index minus the J index is less than or equal to K then we can return true otherwise we'll return false which means that the nearby duplicate does not exist within the correct range. 
#
# Approach: Hash map
# Note. First I want to say first and foremost we can go with a brute force solution but due to the time complexity it times out for the official solution therefore it needs to be optimized in order to get a pass from the leet code servers
# 1. So first we initialize an empty dictionary
# 2. Then we're going to loop through using index value in enumerate of the numbers array
# 3. We want to check key value pairs in dictionary in the dictionary stores value index pairs with the value as the key and the index as the value It's a little bit of reverse but this allows constant time access
# 4. For this loop we're going to check if the value in dictionary So what that means explicitly is that if the key exists in the dictionary then we can check further logic but first we want to check to make sure that the key exists in the dictionary and if we find a valid key match then we can do the rest of the logic. It's important to know that if we wanted to access the values this would be O linear time complexity because we would have to use for value in dictionary.values in order to make the comparison using the method dot values with the in syntax allows us to gain access to the value that is corresponding to the key. 

#  The next part of this sequence is to say if the key exists in the dictionary matches the current value that we are iterating through in the nums array and this is the most important part right here and the current index minus the value that corresponds to the dictionary value key So we check if the current index let's just say we're on the 3rd element within the array so we're going to take index 3 subtract it from the dictionary and we set the key as the value so the 3rd element let's just say its index is 2 so this is going to look up the corresponding key that has two assigned this will give us value from the key axis which will basically say in our dictionary we have key value or value key pairs and when we use dictionary bracket value we are gaining access to the index value so we're subtracting the current index which would be 3 - whatever the previously seen associated indexes was to say it's zero if we saw another at the beginning so this would be 3 - 0 we want to check if that is less than or equal to K so if the key exists in the dictionary and the current index minus the index value of the dictionary is less than or equal to K then we return true.
# 5. Otherwise if the key doesn't exist in the dictionary then add it and set its value as the current index
# 6. We continue this process until we iterate through the entire noms array and this will properly allow us to assess the correct logic and if none of this works we return false



# Time complexity: O(n)
# 1. This is linear time complexity ON since we are using index value and enumeration in Python to loop through the entire nums array and then we use constant access by accessing the key value pairs in the dictionary and assessing with constant time access to the value that's stored there resulting in O-1 operations constant operations and total time complexity of linear O of N
# Space complexity: O(n)
# 1. Space complexity is O of N since we are building a dictionary for each instance that is not seen and this is the main key point.
# Analysis: The solution is 27 milliseconds and it beats a 79.99% of all solutions it has 36.8 megabytes of memory and beats 18.6% of solutions On the graph it shows it is in the top 25% of all solutions
# 1. An alternative solution would be a brute force approach where we iterate I and J incrementing and we compare the abstract value of the index I-J
# 2. Another approach would be sliding window with a hash set. 

# This problem gave great insight into creatively Designing key value pairs in order to properly assess with a constant time access with a dictionary in order to update the key and the value of the dictionary we are checking we have to reverse the order of the assignment that we are given from the first four loop iteration. 
