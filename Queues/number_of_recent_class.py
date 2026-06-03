from collections import deque


class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)

        start = t - 3000
        while self.queue[0] < start:
            self.calls.popleft()
        return len(self.calls)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

# Intuition:
# So we will use a data structure queue so we can keep the range and remove The data from within the queue that does not fall within the current range that we are evaluating By popping off from the front or dequeueing using collections import DQ and pop left
#
# Approach:
# 1. Initialize A queue within the init
# 2. Add the current timestamp to the queue with append
# 3. Then we can use the formula T - 3000 and set that in a variable
# 4. Now we remove the timestamps from the front of the queue if they are older than the start of the sliding window
# 5. The size of the queue at any time will give the count of timestamps in the required range


# Time complexity: O(n)
# 1. The time complexity is O of N since we have a while loop that determines an iteration sequence all the other operations are O of one. 

# Space complexity: O(n)
# 1. The space complexity is olive in where in is the number of timestamps in the last 3000 seconds We are also building a queue and adding to it and then removing from the queue all of this requires O of N

# Analysis: 
# Total time to solve: Total time to solve was about 20 minutes I was looking at the logic and determining how to process this It was a little bit vague at first because I thought the output was a little bit different but then I looked at the output in example one and determine that I needed to use pop left and a queue. Then putting together the logical sequence from appending building it and the while loop initializing the start variable for the mathematical formula and then determining when to pop and then how to return the length of the queue at each step within the event was actually pretty complex for this situation The language was a little bit different.
# Alternative solutions
# 1. We could brute force with a list the problem requires us to count the number of calls within a sliding window of 3000 milliseconds one straightforward approach is to maintain a list of timestamps and iterate over them to count how many fall within this range each time a new call is added
