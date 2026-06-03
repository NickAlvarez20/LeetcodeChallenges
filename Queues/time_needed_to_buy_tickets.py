from collections import deque


class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        queue = deque([val, i] for i, val in enumerate(tickets))
        seconds = 0
        while deque:
            count, index = queue.popleft()
            count -= 1
            seconds += 1
            if count == 0 and index == k:
                return seconds
            if count > 0:
                queue.append((count, index))
        return seconds


# Intuition:
# The main part of this algorithm challenge is to keep track of the KTH element within the tickets we need to use a stack in order to remove the first element of the person buying at the front of the line decrementing their ticket count and then moving them to the back of the line If that person has no tickets left we also remove them from the queue So this not adding them back if their tickets are less than 0 So if the tickets are greater we append to the end otherwise we don't append them. The next most important thing is to somehow keep track of the KTH person in the line so 1 way to do that is with a tuple using value index formatting to identify the value associated with that current tuple we are evaluating at the front of the line if its index is the KTH element then we can correctly determine when to return the seconds This is the whole part of the challenge is learning how to implement this data structure whether through a queue or manual updates.
#
# Approach:
# 1. We want to use the DQ data structure because it allows us to use Popalft which in Python is a lot more efficient than popping from zero because popping from zero requires O of N time complexity because we have to move and shift the whole array therefore we utilize dequeue
# 2. So we create AQ variable and we then initiate the DQ data structure
# 3. Within the DQ data structure we want to use the generator expression of brackets val I to create a tuple data on the fly rather than building a whole new list in memory first it swaps the order to eval, I so that when you pop an item the 1st thing you see is how many tickets they need which is indicated by val and the 2nd thing is their original ID
# 4. Then we use 4 val in enumerate tickets enumerate allows us to get the index and the value and combined with the generator expression we can now set up the queue properly with the tuple like structure for keeping track of the KTH element
# 5. Next we create a seconds and we initialize it to zero
# 6. While D which means while the queue is not empty
# 7. We use destructuring of count, index equals Q popleft This D structures the count and the index when we pop it from the left and it stores it in a variable in a destructed structured variable
# 8. We then decrement the count by one within the D structured variable and we increment our seconds counter
# 9. We check if count equals zero and index equals K we can return the seconds
# 10. If count is greater than zero then we will append the count and the index to the end of the queue otherwise we leave it popped off
# 11. Then we return the seconds.


# Time complexity: O(n)
# 1. The largest coefficient is the while loop and this results in O of in time complexity for any given Q length

# Space complexity: O(n)
# 1. The space complexity is also O of N since we are building a queue at first and utilizing the tuple variable storage All the other variables are O of one therefore the largest coefficient is O of N for any given Q length

# Analysis: The runtime is 10 milliseconds it beats 36.95% of solutions and the memory is 1934 MB and it beats 1153 of solutions it is within the top 75%
# Total time to solve: Total time to solve was about an hour maybe an hour and a half because of trying to figure out how to update the KTH variable this one was a little bit trickier and I had to learn enumerate as well as generator expressions
# Alternative solutions
# 1. The one pass solution is you can calculate how many tickets each person buys before person K finishes so we check the person or people at the index before the K position and then we check the people after K they will buy atmos tickets minus one of the K position because the process stops at the moment person K gets their final ticket. So what we do is we get total seconds set it to zero then we set target_tickets = tickets[k]. For loop is initiated for index count and enumerate tickets we check if index is less than or equal to K Then we say total seconds plus equals the minimum count, target tickets else total seconds plus equals min count, target tickets minus one
# 2. You can do simulation with a cyclic index you can simulate the process without a DQ by using a simple while loop in an index variable that wraps around the array length using the medulla operator this keeps the space complexity at zero1 but the time complexity remains slower It's less common than others because it is slower than the mathematical approach and more complex to implement than the DQ simulation

