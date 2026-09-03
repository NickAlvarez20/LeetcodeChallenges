# # Intuition
# So based on the circular nature of the game as well as removing at one instant and iterating through a certain sequence of events we can ideally use a queue or a stack while a deque works best for this situation rather than using the stack and having to implement a naive solution. Python's deque is optimized for this so we'll use a deque for this type of pattern.

# # Approach
# 1. Starting out from collections, import Deque.
# 2. Then we want to set up the DQ, so we name a variable called Q and set it equal to an empty DQ.
# 3. Next, you have to populate the queue. So, I initialize a for loop for i in the range from 1 to 4, making sure to start at the 1-based count position as well as in plus 1 since it is inclusive and it will exclude the next number we need. So, 1 to 4 but we need 1 to 5, therefore we have to set up these condition parameters correctly. The queue by appending i for that range.
# 4. If n equals 1, this is a guard clause that is done up front for one of the test cases, we can return 1 immediately.
# 5. So now I want to implement a queue and while the queue is not empty we can perform this while loop.
# 6. Now for i in range of k-1 we want to perform operations for this range using k as the argument or parameter minus 1, because we don't want to go to k position, we want to go to k minus the 1 position.
# 7. Now during this for loop we want to store the current pop left within a winner variable and then after that we want to append whatever value to the right end of the queue using q.append with the value that we stored within winner.
# 8. Now after we've reached the end of the K position, our current position will be what we need to remove. So we will just Q.popLeft after we get out of this initial for loop, thus removing the loser of that round.
# 9. After this loop completes, we want to check at any time if the length of the queue is equal to one. If so, we can return the value within that queue using element access at the first index of the queue, and that will return the winner of the game.

# # Complexity
# - Time complexity: O(N*K)
# 1. So the time complexity is equal to the length of the queue as well as the sub-for loop within the queue, which runs k times. So we'll need to perform operations within the queue, therefore it's O of n times k.
# 2. The first one to consider is populating the Q. So for any given n, we will have to run O operations for the length of n, from 1 to n plus 1 position. Therefore, that operation is O(n) for any given n.
# 3. Next, we have a while queue is not empty. So this condition will run until the queue is completely empty, which is equal to n minus 1 for any given length of the queue that we give it. We're going to run the entire while loop until the last length is equal to 1. Therefore, it's O of n minus 1 operations that this entire queue will run for.
# 4. Then there's the inner mini for loop for i in range of K-1 which is equivalent to running this condition and performing the operations within to the length of K-1. Therefore that total loop in itself is O of K.
# 5. Then q.popLeft is a constant operation. It pops from the start of the deque. Optimize for Python. And then a final length check is also constant once it is equal to 1.

# - Space complexity: O(N)
# So we are allocating a new DQ and then we are populating the Q. So for any given N, the auxiliary space we need to allocate is O of N for the entire range from 1 to N plus 1.
# The operations within that queue are removing and making it smaller, and we are simply removing and updating in place, so there is no extra memory being allocated within the while and for loops within the while loop. Therefore, the overall space complexity is O(N) for building the entire deque.

# Code

from collections import deque

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # set up the deque
        queue = deque()
        # populate the queue
        for i in range(1, n+1):
            queue.append(i)
        
        if n == 1:
            return 1
        
        while queue:
            for i in range(k-1):
                winner = queue.popleft()
                queue.append(winner)
            queue.popleft()
            if len(queue) == 1:
                return queue[0]
