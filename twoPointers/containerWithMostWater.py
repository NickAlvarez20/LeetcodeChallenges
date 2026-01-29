class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            # current area calculated by width right index - left index (positive num) * current values at left and right pointer
            current_area = (right - left) * min(height[left], height[right])
            # need max_area to evaluate the max_area of any given combination
            max_area = max(max_area, current_area)
            # this will identify the tallest bar and increment left until it finds the tallest bar on the left, this increase in size creates a larger area. However, if the bar on the left is currently taller, then increment right until a taller bar is found on the right.
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


# Intuition:
# We use two pointers to grab the width with the index subtraction of right minus left And min and Max methods We pair this with a comparison of the left bar height and the right bar height these will be the conditions to increment left or decrement right.
#
# Approach:
# 1.So we assign left and right pointers to zero and the last position in the index of the length of the array of the length of the array
# 2. Then we assign Max area to zero This will assign a value in order for us to properly update and have the global scope assigned.
# 3. Then we initialize a while loop for left less than right for the two pointers pattern
# 4. Then we assign current area as the right index minus the current left index for every iteration times the minimum of the current value at the left pointer and the current value at the right so this equates to comparing the left bar with the right bar and that allows us to identify the minimum Is a key point to notice because the difference in these values will determine the water level for that range as the minimum of those two values will be what the water goes up to. 
# 5. Then we need to assign Max area To the maximum of comparing the previous Max area with the current area
# 6. Next thing we do we check if the current value at the left pointer is less than the current value at the right pointer If it is we move left forward The reason behind this is because we want the left bar to be greater than the right bar If you look at a left skewed distribution graph you can see that to accurately calculate the area you would need to keep incrementing the left value until it's graded in This would identify a bar in any given array that would change the Max area.
# 7. Otherwise we want to move the right pointer by decrementing it in this position the left bar is greater than the current right bar so we want to keep moving the right pointer until the condition of the left bar being greater than the right bar is met otherwise we can just keep moving the pointer and those values will be the Max area.
# 8. Finally we return the Max area
# Time complexity: O(n)
# The time complexity of this algorithm requires one while loop which is the largest coefficient in constant operations and conditional checks therefore the time complexity is O(n)
# Space complexity: O(1)
# The space complexity of this only assigns constant variables as containers for storage Thus we are not building a new list or structure which results in O of one constant space. 

# Analysis:
# The runtime is 59 milliseconds it beats 76.64% of all solutions and the memory is 29.53 megabytes and it beats 36.38 percent of all solutions this place is the combined metrics at top 50% of all solutions.
# This algorithm was quite intense for an easy challenge It required min and Max approach with two pointers which is outside of the initial scope and understanding which requires a creative solution utilizing a min container and a Max container although the math itself is easy visualization of the algorithm as well as knowing when to move the left and right pointer in calculating the Max at each pass is the difficult part in understanding how to implement that in code form with minimal clean solution using min and Max containers. 

# Alternative approaches:
# You could use a brute force approach involves checking the area for every possible pair of lines and keeping track of the maximum area found you initialize a variable Max area to 0 using a nested loop to iterate through every possible pair of indices where I is the left line and J is the right line for each pair calculate the current area using the formula min of height brackets I,, height brackets J * J - I similar to the min formula and you label it within the current area variable and then you update Max area equals Max area you consider Max area with the current area and then you return Max area so very similar solution but we are not using the 2 pointers convenience and this would be an oath in square time complexity and a space complexity of O of 1 therefore the optimal time complexity is a 2 point or solution and the two pointer solution is significantly more efficient for large inputs because it eliminates many non optimal combinations in a single patch making it the preferred approach the brute force method guarantees the correct result but it's less performant. 