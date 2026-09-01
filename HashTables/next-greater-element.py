# # Intuition
# So the intuition is that you can utilize slicing, .index(), and iteration to check for the subarray within it. So either a sliding window, two pointers, or a subset. But ideally it aligns with a subset using a slice or a monotonic stack. 

# # Approach
# 1. So first, we declare the result array and set it equal to an empty list. 
# 2. Then we create the first for loop for index value using enumerate to check within nums, 1. 
# 3. Next I want to check if the value exists within nums2. 
# 4. And then I want to set a variable called currentIndex and look at nums2 using the index method and plug in the value if it matches within the current enumeration to find the index within nums2. 
# 5. Then I want to create a slice num2, set it equal to reach within nums2 and take a slice from that current index that we just found until the end of the nums2 array based on the index position. 
# 6. Now that I have these two variables, I can start another for loop to iterate within the range of length minus one. So up until the very last element. Otherwise, we'll have an index out of range. 
# 7. Now within this iteration I want to conditional check if the value is less than the next value past the current index, so index plus one. And as long as this continues we're looking for the next greatest element whether it exists at the next position or within any of the next positions within the entire slice. This is the main point that we are looking for. The next greater element, whether it exists in the next position or any other position within that slice after the current value. 
# 8. If we find that the value is less than any of the numbers within that slice, we can append to the result. Then we can immediately break out because we're just looking for the next greatest, it doesn't have to be the max. 
# 9. At the end of this, if we do not find a greater element, we can just append -1, if that value is the greatest for its current position within nums2 and its value is greater than all the other elements to its right. 
# 10. Finally, we can return the result. 

# # Complexity
# - Time complexity: O(M*N)
# The code iterates through each element in nums1 of length m. For each element, it searches for the index in nums2 of length n, and then scans the subsequent elements in nums2. Finding val in nums2 takes O(n) time. The inner loop scans up to O(n) elements. Since this happens for every element in nums1, the total time is O(m * n). This is significantly slower than the optimal O(m + n) approach using a monotonic stack and hash map. 

# - Space complexity: O(m)
# The primary additional space used is the resultList, which stores one integer for each element in nums1. The resultList grows to size m. Temporary variables, such as currentIndex and sliceNum2, use O or O auxiliary space depending on the implementation details. Slicing creates a copy, but the dominant factor for the output is O(m)


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []

        for index, val in enumerate(nums1):
            if val in nums2:
                curr_index = nums2.index(val)
                slice_num2 = nums2[curr_index:]
                for i in range(len(slice_num2)-1):
                    if val < slice_num2[i+1]:
                        result.append(slice_num2[i+1])
                        break
                else:
                    result.append(-1)
        return result
                    
        
