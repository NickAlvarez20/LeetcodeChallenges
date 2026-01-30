class Solution:
    def trap(self, height: List[int]) -> int:
        left = 1
        right = len(height)-2
        rMax = height[right+1]
        lMax = height[left-1]
        totalRainWater = 0
        while left <= right:
            if rMax <= lMax:
                totalRainWater += max(0, rMax-height[right])
                rMax = max(rMax, height[right])
                right -= 1
            else:
                totalRainWater += max(0, lMax-height[left])
                lMax = max(lMax, height[left])
                left += 1
        return totalRainWater

# Intuition:
# In order to pass the trapping Rainwater hard algorithmic intuition you need to see the container rather than just the bars It's also important to note that anything outside of the current bottleneck which is the left and right tallest bars that do not have an outside bar they become run off water So in the initial graph on leak code you see the left doesn't have water and the right one doesn't have water That is confusing if you don't understand the container Most people would assume that the entire graph itself would store water as long as it's within the graph range but the key insight is to see the runoff water that is outside of the container water flows away into the ground if it is not contained within the bars AKA the container Therefore we could a brute force approach but the intuition should tell you any bottleneck Logic in high performance engineering scenarios Will require you to understand the two pointers technique to create a container This will help you identify the spaces within.
#
# Approach:
# 1. So first we assign left to one this is important rather than the traditional left equals 0 we now want to move it up by 1 This will be important
# 2. Next I assign right is equal to the length of the height minus two Once again a different variation rather than one we move it one within this will be important as we keep track of the height of the right and left bar
# 3. Next we assign R Max to the height of right plus one So this will give us the index based on the right pointer position and it will check to the right one index position to the right
# 4. Then we assign left Max this will be the height of the leftmost element based on the Current left index minus one.
# 5. We want to assign total rainwater and assign the value zero
# 6. Initialize a while loop but this time we want the condition to be less than or equal to right This will be important when the two pointers converge in the middle for the final calculation
# 7. Now we check if the right Max is less than or equal to the left Max So if the right building height is less than or equal to the left building height Then we're going to move forward with the calculation because the right building height is currently at a Max As determined by the algorithmic sequence when this condition is true
# 8. We step into the logic we add the Max of either zero or the right building minus the height of the right pointer value This is important to notice the argument is 0 or the subtraction mathematics if we have a negative height when current right Max is less than the bar before it at the right pointer the right pointer will be at a peak therefore there will be no rain water here So we want to remove that from the calculation and default to zero rather than adding a negative height Otherwise we can add the value the tallest bar on the right minus the current value to its left at the right pointer index position value
# 8a. Next thing is to assign right Max set that equal to the Max of the right Max that we already know to be the largest building on the right and we set the other argument as the current value where the right pointer is within the height Will find the new Max like in the previous discussion where you saw that the bar to the left was actually higher than the current right Max so then this would move it to the new Max and establish that as the new right Max
# 8b. Then we decrement right by one
# 9. If this condition is not true then we want to move the left pointer forward until the container finds the left Max
# 9a. So you add the total rainwater using that same mathematical notation with the Max setting as zero and determining if the left Max minus the height equals a peak to the right of the current left Max position which would indicate runoff therefore you would not want to calculate that as it would result in a negative number therefore we can choose between zero or a positive number if it's positive then we can add it to total rainwater
# 9b. Then we want to move left Max if it determines that the Max between the current left Max and the position where the height of the left pointer is currently at is greater if it is we can move the left Max to the next position and then increment left by one until we find the left Max Now for each subsequent pass the lMax stay locked and keep moving til it finds the next highest lMax, and then it reshrinks catches up to the left pointer and then continues until left <= right. This current left Max mathematical calculation for finding the rain water collection and then re shrinking catching up to the left pointer is the classic pattern that allows us to understand the rainwater collection based on peak sizes in between from the left Max to the right Max and this squeezing and sequential calculation for each part magically calculates at each part So if we're going from the left there's not going to be a right wall and it's just going to calculate the difference between the left Max and one position to the right and it's going to keep doing that Keep moving the left pointer forward and then it'll re shrink and update the left Max once it finds a taller bar Same with the right same pattern and then this allows us to understand how to calculate the rain water and anything currently outside of this container is not going to be analyzed because that's run off water
# 10 Then we return the total rainwater which allows us to calculate and understand the exact space collection of rainwater
# Time complexity: O(n)
# We are performing a single pass through the array with the while loop that ensures every element in the height list is visited exactly once whether it has 10 or 10 million elements the time taken grows linearly with the input size of N No nested loops or rescanning and this makes the two pointers approach incredibly amazing and clever for these unique high level problems.
# Space complexity: O(1)
# The space complexity is O-1 and it actually defeats dynamic programming because we don't have to create extra memory. You are only storing five integer variables left right right Max left Max and total rainwater The total amount of memory remains constant because we are not creating any extra lists or data structures which is ideal for memory constrained environments.

# Analysis:
# The analysis is three milliseconds it beats 96.45% of all solutions memory is 2110 MB and it beats 3477% of all solutions this places it within the top 5% although this is the optimal solution so performance varies by computer specs Internet speed and computer language chosen.
# This was a hardly code problem It required many different insights and new expanding of horizons when understanding a two pointers approach while implementing a right Max and a left Max with unique mathematical invariants This was a very clever approach and it required deep insight and understanding of the container versus the bars approach as well as understanding the outside constraints with the runoff water when you're first initially scanning it and you look at the right and the left without water you question it's within the box of the graph so there should be water there and that leads to many different confusions when you shift your perspective and you look at the height of the bars as we previously learned then this allows you to understand the scope. Another unique insight is the ability to converge and calculate without having to consider the right bar position entirely you can actually calculate it for any given range where the next bar is not is not currently calculated but its future consideration of the update when you do find it allowing you to calculate in between peaks and valleys correctly on the fly while merging with the right which is also doing that concurrently on the other side and then when you meet in the middle you can also calculate any edge cases. It provided a deep insight into the various applied techniques of the 2 pointer solution and seeing how the logic of high level systems is necessary to learn because This is actually applied logic that you need to understand when building out software whether it be image processing and computer vision when algorithms need to identify voids or pockets in a 2D scan like detecting a crack in a physical part or a cavity in a medical MRI they use similar logic to find where the surface level diffs significantly between two peaks Open CVS contour analysis often handle shapes using these boundary comparison principles supply chain and logistics It's important because we can think of the bar as heights as inventory levels or processing experience along a conveyor belt if you have a fast machine at the start in a fast machine at the end but slow machines in the middle of the water represents the backlog or buffer that builds up engineers uses to calculate the maximum capacity system can hold before it overflows you also see this in data compression and histogram analysis and databases or signal processing peak finding and valley finding are used to compress data If you have a signal with lots of noise small dips you can use this logic to fill the noise Simply simplify the signal into a smooth trend line which takes up less storage space we also have a resource management cloud computing imagine the bars are CPU usage over time if you want to identify periods where your system had spare capacity values between two high demand peaks you use a variation of this logic to calculate the total available headroom for schedule lower priority background task and then for financial charting and technical analysis of stock markets identifying support and resistance levels often involves looking for these exact valley truck shapes calculating the depth of a price tip between two high points as A standard way to measure market volatility The real software engineering take away isn't the water it's learning how to eliminate unnecessary calculations by defying which side of a problem is the bottleneck.


# Alternative approaches:
# 1. We could do a brute force approach which is O of N ^2 and O of 1 space
# def trap_brute_force(height):
#     total_water = 0
#     n = len(height)

#     # For each bar (excluding edges), find the max height to its left and right
#     for i in range(1, n - 1):
#         left_max = 0
#         for j in range(i + 1):
#             left_max = max(left_max, height[j])

#         right_max = 0
#         for j in range(i, n):
#             right_max = max(right_max, height[j])

#         # Water trapped at current bar is the difference between the minimum of
#         # left_max and right_max, and the current bar's height.
#         total_water += min(left_max, right_max) - height[i]

#     return total_water


# 2. Dynamic programming approaches is O(N) time and O(n) space
# def trap_dp(height):
#     if not height:
#         return 0
#     n = len(height)
#     total_water = 0

#     # Initialize arrays to store maximum heights to the left and right
#     left_max = [0] * n
#     right_max = [0] * n

#     # Calculate and store maximum height to the left for each position
#     left_max[0] = height[0]
#     for i in range(1, n):
#         left_max[i] = max(left_max[i - 1], height[i])

#     # Calculate and store maximum height to the right for each position
#     right_max[n - 1] = height[n - 1]
#     for i in range(n - 2, -1, -1):
#         right_max[i] = max(right_max[i + 1], height[i])

#     # Calculate trapped water using the pre-computed maximums
#     for i in range(n):
#         total_water += min(left_max[i], right_max[i]) - height[i]

#     return total_water


# left = 1
#         right = len(height) - 1

#         # lMax is init to the height of the left more building
#         # we need to keep track of left as we increment based on the conditions
#         # so use left -1
#         # and right + 1
#         # this will determine the height of the left building and right building
#         lMax = height[left - 1]
#         rMax = height[right + 1]

#         result = 0 # for counting rain water
#         while left <= right:
#             # if right buildingHeight is less than or equal to left building height at the current calculation
#             if rMax <= lMax:
#                 result += max(0, rMax - height[right]) #key detail, compare the max of either 0 or rmax-height[right] - if negative then use 0 as bar to left is higher than rMax, therefore it causes it to overflow right

#                 rMax = max(rMax, height[right]) #update rightMax. choose between current rMax, or height[right]

#                 right -= 1 # decrement right by one
#                 # what does this solve? Why? The amount of water at any point is always limited by the shorter of the two tallest walls (left and right)
#                 # You have a "guarantee" that even if there is a much taller wall somewhere far to the left, the water at the current right position cannot rise higher than rMax
#                 # Because rMax is the bottleneck, you can safely calculate the water at height[right] without needing to know exactly how high the tallest wall on the left is. You just need to know that it's at least as high as rMax

#             else:
#                 res += max(0, lMax - height[left])

#                 lMax = max(lMax, height[left])

#                 left += 1
#         return result
