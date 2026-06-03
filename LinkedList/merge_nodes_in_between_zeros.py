# Intuition: The intuition behind the solution is to treat the zero nodes as the limiters that mark the boundaries of different segments since you need to transform the list in place you need to use 2 pointers to perform a read and overwrite operation. 
# The reader: This pointer acts like a scanner that traverses the entire original list that accumulates the values of non zero nodes into a running sum until it hits another 0
# The writer: This pointer keeps track of where the next merge some should be stored instead of creating a new list you simply overwrite the value of an existing node with the accumulated running sum
# Segment linking: Every time the reader hits a zero the writing phase occurs. The writer updates its value to the current sum and then jumps its next pointer to the node immediately following that 0, Effectively skipping the zero node and connecting directly to the next segment. 
# By the end of the traversal you have effectively crushed the segments of numbers into single nodes and bypassed all the zeros leaving a clean merged list. In conclusion this requires you to be aware two pointers fast and slow pointers and the ability to keep track of read and write operations Spatial reasoning and the ability to update pointers and the while keeping track of a current sum and initializing the two starting variables to the note right after the start. 

# Approach:
# 1. Declare a writer and set it equal to head next this represents the node right after the starting 0
# 2. Declare a reader variable and also set it to head next 
# 3. declare a running sum and set it equal to zero 
# 4. Initialize a while lo the first argument is wowreader.next is not None this will ensure that we traverse the entire linked list up until the point that the reader next pointer is not None 
# 5. recheckifreader.value does not equal zero as a first conditional part of the algorithm we want to ensure the value is not 0 being added Within this we update the running sum with the current reader value 
# 6. We want to move reader forward so we set reader to reader dot next to traverse the linked list
# 7. If reader that value does equal zero we want to do some logic because this is a condition we are explicitly checking for
# 8. So if we determine that the read value is zero we want to 
# 9. update the current node writer.value with the running sum up until this point 
# 10. we want to move writer dot next ointer and setitequaltoreader.net our reader will currently be on 0 and we move the writer dot next pointer to the node right after this zero valued node
# 11. Then last thing we want to do is make sure that we also move the pencil that is responsible for overriding the current node value which in this case is the rider variable We want to update that rider.next
# 12. Then we will set the running sum equal to 0 at the end of the algorithm to make sure that our sum for that segment is reset to zero 
# 13. At the end we will return head dot next instead of head since we are avoiding the initial 0 in the modified linked list

# Complexity:
# Time: O(n)
# The algorithm uses a single pass through the linked list. The reader pointer visits each node exactly once wherein is the total number of nodes in the list. All operations inside the loop (Additions and pointer reassignments) are O(1)
# Space: O(1)
# The solution performs the merge in place. It modifies the existing node values and pointers rather than creating a new list or using auxiliary data structures (Like an array of recursion stack) That scale with input size. Only a few constant space pointers (writer, read, and running_sum) are used.
# Shout out to Donald Knuth, Allen Newell, Cliff Shaw, Herbert Simon, and Harold Lawson. 
# 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        writer = head.next
        reader = head.next
        running_sum = 0
        while reader.next is not None:
            if reader.val != 0:
                running_sum += reader.val
            reader = reader.next
            if reader.val == 0:
                writer.val = running_sum
                writer.next = (
                    reader.next
                )  # sets this equal to the node after, which is the one after the 0
                writer = writer.next  # move the "pencil" for writing new running_sum
                running_sum = 0
        return head.next
