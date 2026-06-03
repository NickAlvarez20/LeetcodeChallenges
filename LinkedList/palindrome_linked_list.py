import math


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # declare slow, fast pointers and set curr as None to hold middle pos
        slow = head
        fast = head
        curr = None
        # two pointers to find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        curr = slow  # set curr to slow(middle)
        prev = None  # init prev for reversing second half

        # reverse second half of linked list starting from middle
        while curr is not None:
            next = curr.next  # store next in temp var
            curr.next = prev  # reverse pointer to point at prev node
            prev = curr  # move prev forward first
            curr = next  # then move curr forward

        # final piece: set left as head and right as head of reversed second half, when return prev we have reversed second half
        left = head
        right = prev
        # start from the reversedLinkedList starting val, and compare vals, if not equal return false else then move pointers forward each step and return true if all match
        while right is not None:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True


# First solution logic flow:
# divide by two and ceil the results then do a reverse comparison
# middle = 0
# curr = head
# oddMiddle = None
# oddFirstHalf = None
# oddSecondHalf = None
# evenFirstHalf = None
# evenSecondHalf = None

# if len(self) % 2 == 1:
#     middle = math.ceil(len(self) / 2)
#     for _ in range(0, middle):
#         curr = curr.next
#     oddMiddle = curr.val
#     oddFirstHalf = self.slice[0:oddMiddle]
#     oddSecondHalf = self.slice[oddMiddle : len(self)]
#     if oddFirstHalf != oddSecondHalf.reverse():
#         return False
# elif len(self) % 2 == 0:
#     evenFirstHalf = self.slice[0 : (len(self) / 2)]
#     evenSecondHalf = self.slice[len(self) / 2 : len(self)]
#     if evenFirstHalf != evenSecondHalf.reverse():
#         return False
# else:
#     return True


# Intuition: Usually to check if a valid palindrome exists we would use two pointers one on the left and one at the end since this is a linked list we cannot use the traditional array logic to check for valid palindrome. Therefore we need to use slow and fast pointers and two pointers in combination First slow and fast pointers help us to find the middle value Then we reverse the linked list from the middle value and then finally we used two pointers left and right to compare the values with the left while traversing the right in order This will allow us to compare the values while only using the next pointers that are given in this problem.
# Approach
# 1. Declare slow fast pointers and set curr as None to hold middle position
# 2. Utilize two pointers to find the middle and a while loop Slow pointer points to the next and fast two positions ahead using the traditional slow fast pointer algorithms
# 3. At the end we can set cur to equal slow which is the middle value and then we initialize a pre value and set it equal to None This will be utilized for reversing the second half
# 4. We reversed the second half of the linked list starting from the middle We have to create a next variable that stores the next node Then we reverse the pointer to point to the previous node move the previous forward by setting it equal to cur and then updating current traversing it forward by setting it equal to the next that holds the next node that was previously a temp variable
# 5. Final piece is to set left as head and right as head of reversed second half So left equals head right equals previous When we return pre from the previous loop we have the reverse second half this will be useful in this final piece of the puzzle
# 6. Now we start from the reversed linked list starting valve and compare the values with a conditional check So we start from the reverse link list we are comparing this to first half of the traditionally in order list that we have not reversed while right is not None we checked the condition if the left value does not equal the right value then we return false immediately this is not a palindrome Otherwise we traverse the left by setting it to next and right setting it to next and continue this check throughout the entire linked list if all of this passes and at the end we can exit the loop and return true


# Time complexity: O(n)
# 1. Time complexity is O The fast and slow pointer loop traverses the list once visits about N / 2 nodes
# 2. Reversing the second half traverses about north / 2 or log in nodes since we are iterating through half the list
# 3. Final comparison loop traverses the second half again about in divided by 2 nodes roughly 1.5 passes over the list is around O(n) time


# Space complexity: O(1)
# 1. Space complexity is O of one because you can use a constant number of pointers slow fast curve pre next left right
# 2. No recursion no extra data structures like array or stacks
# 3. All operations are in place reversing the second half modifies pointers directly so constant extra space equals O of one space

# Analysis: The runtime on this current pass is 32MILLISECONDS it beats approximately 59.77% solutions the memory is at 34.32 megabytes and it beats approximately 87.94% of solutions This is the optimal solution for this leet code challenge
# Total time to solve: Total time to solve was pretty extensive I had to probably study for about an hour to an hour and 1/2 because first I had created a non working solution walking through the logic understanding the flow because it was a non traditional method to access the end of the linked list and there is no way to step back using a previous node so it required an out of the box solution which required refactoring the logic into something more robust and having to understand the new pattern of fast and slow pointers reversing a linked list review and then implementing two pointers it is medium level challenge but it is listed as easy It was great for learning and understanding different approaches with in place sorting and two pointers and slow pointers and good review for reversing a linked list So it was a three in one challenge it's listed as easy I would probably reclassify it as medium or hard leaning slightly towards hard I would say about 80% more weight because of the dynamic implementation of three different algorithms At first it seems challenging but if you understand these from prior practice it is probably around a medium if not it is definitely hard.

# Alternative solutions
# 1. There are various alternative solutions we can use a stack reverse second half explicitly traverse the list once push all nodes or just values onto a stack traverse again pop from stack and compare with current node or find middle with fast slow push 2nd half on the stack and then compare it with first half uses over in extra space
# 2. We can convert to a list/array it's over in time and of in space It's extremely simple and readable but it's all of an extra space and not in place
# 3. We can do a recursive comparison elegant but risky oven time over in space due to recursion stack use recursion to reach the end that compare values while unwinding the stack moving a pointer from the front forward It's clean no explicit reversal but it is ovine stack space can cause stack overflow for a very long list
# 4. Brute force reversed the entire list and compare its ove in time and O of one space if you reverse in place and restore or over in if you make a copy how we do it is to reverse the whole list compare with the original need to keep original or restore not recommended more work than necessary. 
