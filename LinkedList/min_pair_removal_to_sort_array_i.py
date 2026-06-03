import heapq

class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
        self.deleted = False

class Solution:
    def minimumPairRemoval(self, nums: list[int]) -> int:
        if not nums: return 0
        
        # 1. Build Doubly Linked List
        head = Node(nums[0])
        curr = head
        for i in range(1, len(nums)):
            new_node = Node(nums[i])
            curr.next = new_node
            new_node.prev = curr
            curr = new_node
            
        # 2. Initial Heap: (sum, left_node_id, left_node)
        # We use id(node) to handle ties in the heap
        pq = []
        curr = head
        while curr.next:
            heapq.heappush(pq, (curr.val + curr.next.val, id(curr), curr))
            curr = curr.next

        def is_sorted(node):
            temp = node
            while temp and temp.next:
                if temp.val > temp.next.val:
                    return False
                temp = temp.next
            return True

        operations = 0
        while not is_sorted(head):
            # 3. Get the smallest pair
            while pq:
                s, _, left = heapq.heappop(pq)
                # Check if the pair is still valid/adjacent
                if not left.deleted and left.next and not left.next.deleted:
                    right = left.next
                    
                    # Perform "Removal": Update left, delete right
                    left.val = s
                    right.deleted = True
                    left.next = right.next
                    if right.next:
                        right.next.prev = left
                    
                    # Push new potential pairs into heap
                    if left.prev:
                        heapq.heappush(pq, (left.prev.val + left.val, id(left.prev), left.prev))
                    if left.next:
                        heapq.heappush(pq, (left.val + left.next.val, id(left), left))
                    
                    operations += 1
                    break
                    
        return operations
    

# Bruce force approach
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def is_sorted(arr):
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    return False
            return True

        operations = 0
        while not is_sorted(nums):
            min_sum = float('inf')
            best_i = -1
            for i in range(len(nums) - 1):
                current_sum = nums[i] + nums[i + 1]
                if current_sum < min_sum:
                    min_sum = current_sum
                    best_i = i
            nums[best_i] = min_sum
            nums.pop(best_i + 1)
            operations += 1
        return operations
           


        