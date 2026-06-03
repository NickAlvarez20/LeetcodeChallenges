# Intuition: We can use a linked list math package we import the method GCD. We also need a temp variable and awareness of how to detach and nodes another thing is how to create a new node and insert it

# Approach:
# 1. First we import the math package u
# 2. Second we must uncomment the list node so we have a constructor for our list node
# 3. Then we want to declare agcd variable and set it equal to the head value This instantiates the variable so we can update it once we determine the CD of a node and the next node
# 4. we declare cur variable and set it equal to the head for iterating the linked list 
# 5. Then we initialize a while loop and set it equal to cur and curnext to ensure that we are not going beyond the limit
# 6. Within the while loop we declared GCD and set it equal to naf.Gcd method the two parameters are cur val and crew next bow This mathematically determines using the Python math and GCD method the greatest common factor
# 7. We declared new node set it equal to a brand new list node and call this node to create this new node
# 8. We want to update the value within the new node we have created with the value that was determined in the GCD variable
# 9. Next we want to store the next node before we detach it So declare temp inside it equal to curne
# 10. We want to update Kerdot pointer attach the new node
# 11. Then we're going to set the new nodes next pointer equal to temp # 12. Then we want to move curve forward by two so we set Kurt equal to Kerr next next
# 12. Finally we return the head and that will have the correctly updated GCD linked list . 

# Complexity:
# Time: O(n log(max_val))
# the code traverses the linked list exactly once visiting each original node and each newly inserted noded There are in original nodes resulting in N minus 1 new nodes so the number of iterations is proportional to O of. Within the loop the dominate operation is calculating the GCD of two values using math GCD method. The time complexity of the Euclidean algorithm for GCD is typically O log min AB which can be simplified to O log Max val. Where Max val is the largest value in the list. Therefore the total time complexity is the number of iterations multiplied by the complexity of the GCD operation O of N log Maxval 
# Space: O(n)
# The algorithm creates a new list node for each gap between adjacent original nodes since there are N - 1 gaps the amount of additional memory used for these new nodes is proportional to the number of original nodes O of N. The use of a few temporary variables like GCD currently node and temp is constant space. Therefore the overall space complexity is dominated by the newly allocated nodes resulting in O(N) space. 

import math
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        gcd = head.val
        curr = head
        while curr and curr.next:
            gcd = math.gcd(curr.val, curr.next.val)
            new_node = ListNode()
            new_node.val = gcd
            temp = curr.next
            curr.next = new_node
            new_node.next = temp
            curr = curr.next.next
        return head
