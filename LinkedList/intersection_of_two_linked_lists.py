# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        currPointerA = headA
        currPointerB = headB
        while currPointerA != currPointerB:
            currPointerA = headB if currPointerA is None else currPointerA.next
            currPointerB = headA if currPointerB is None else currPointerB.next
        return currPointerA

        # currListOne = headA
        # currListTwo = headB
        # while currListOne is not None:
        #     currListTwo = headB
        #     while currListTwo is not None:
        #         if currListOne == currListTwo:
        #             return currListTwo
        #         currListTwo = currListTwo.next
        #     currListOne = currListOne.next
        # return None



# Intuition: Intuition is to traverse through a link list with the next pointers and compare them and see if they are of equal value If they are of equal value we can return either or head.value or head B.value. In this situation we aren't given an exact explicit value so we can just compare the nodes. At first brute force approach is just to loop through with a double nested while loop and compare making sure that while the next pointer is not None we essentially loop through and then compare the values If we find a match then we can return either one or two value really doesn't matter Then we have to update the pointers and then reset the head of B This essentially allows us to go through list A iterate through the entire length of list B comparing the values This is not the optimal approach this is a double nested loop which is O(n^2). The optimal approach involves creating two variables to store head A and head B and while they do not match we're going to loop through concurrently at the same time and compare the pointers So if current pointer of a is None which means we've reached the end of the list and we switched to B and while these pointer values are not true we do the same thing for list B we loop through the entire thing and while the pointers do not match we then flip it to the other track which would be list A It is a very elegant solution and it is tough to understand at first but ultimately finds the matching position and if there is no matching pointer then it will automatically return none.
# Approach
# 1. Create two variables to store the current pointer of A and B
# 2. Create a while loop to check While current pointer A is not equal to current pointer B
# 3. Create two variables one for current pointer A and one for current pointer B
# 4. Concurrently loop through the list while the condition is true.
# 5. They looped through each starting list if a is starting it loops through the entire length of list a until the next node is None and then it switches tracks to compare it to list B and vice versa.
# 6. If we don't find a match then we increment the pointers
# 7. If we do find a match then we can either return current pointer A or current pointer B doesn't really matter
# 8. And then it will implicitly return None if this condition does not exist. 

# Time complexity: O(n+m)
# 1. The while loop is a simple condition that loops through N + M where in is the length of list one and M is the length of list 2, Since it is a while loop and there are in no further nested loops the largest coefficients are O of N + M.


# Space complexity: O(1)
# 1. The optimal solution is O of one since we are comparing in place for space complexity

# Analysis: This current working solution has a runtime of 118 milliseconds and it beats 39.07% of answers The memory is 32.21 MB and it beats 46.7 percent. 
# Total time to solve: This one involved a heavy assessment took about 30 to 40 minutes I had to understand the first brute force solution where I was using a double nested while loop and having to deal with nested indentation errors and updating the variable pointers in the correct outer loop and inner loop. Then I refined my answer by understanding the wow the condition does not exist compare and contrast as well as iterate concurrently through the list.

# Alternative solutions
# 1. The alternative solution which is not optimal was O of N ^2 in time complexity which resulted in a timeout air therefore this answer was not appropriate especially considering larger systems this would cause performance issues and all sorts of other problems.


# Understandings of Elegant Solution
# so while that does not equal the same, since we're going sequentially, we'll have to iterate through the entire length of the list at the same time. So although it exists in A and we found it, it still is currently not existent until the position of current current pointer B walks in at that millionth step, if that makes sense. Because current pointer B is going through the list and it's saying, hey, we haven't found it because it doesn't exist. It exists in A. So, when we finally reach the end, that's when we find it. It's really weird on the brain to see that, but because you are not on the same sequential step, you have to wait until you get to that five plus. Because it doesn't exist. The value that you're looking for is that the next pointer equals pointer A. Therefore, you walk through the entire list of B. The current pointer B does not exist because you have to go to A where A is found. Same thing for current pointer A. You iterate through the entire sequential sequence of A, and you find the pointer. You find the pointer. Right. But it's not going to be equal until the length is fully traversed at one million five. That is really strange.
