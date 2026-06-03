# =============================================================================
# RECURSION PRACTICE DRILLS - Base Case Focused
# Implement only the recursive logic after the base case
# =============================================================================


# 1. Strings & Arrays (Empty Check)
# ---------------------------------


def count_vowels(s: str) -> int:
    """Count the number of vowels in a string (a,e,i,o,u)."""
    # Base Case (already given):
    if not s:
        return 0

    # TODO: Write the recursive step here
    # Hint: Check the first character, then recurse on the rest
    pass


def contains_number(arr: list[int], target: int) -> bool:
    """Return True if target exists in the list, False otherwise."""
    # Base Case:
    if not arr:
        return False

    # TODO: Write the recursive step
    # Hint: Check first element, then recurse on the rest of the list
    pass


def reverse_string(s: str) -> str:
    """Return the string reversed."""
    # Base Case:
    if len(s) <= 1:
        return s

    # TODO: Write the recursive step
    # Hint: Take the last character + reverse of the rest
    pass


# 2. Numbers (Identity Check)
# ----------------------------


def factorial(n: int) -> int:
    """Return n! (factorial of n). Assume n >= 0."""
    # Base Case:
    if n == 0:
        return 1

    # TODO: Write the recursive step
    # Hint: n! = n * (n-1)!
    pass


def sum_to_n(n: int) -> int:
    """Return the sum of all numbers from 1 to n. Assume n >= 0."""
    # Base Case:
    if n == 0:
        return 0

    # TODO: Write the recursive step
    # Hint: sum_to_n(n) = n + sum_to_n(n-1)
    pass


def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number (fib(0)=0, fib(1)=1)."""
    # Base Case:
    if n <= 1:
        return n

    # TODO: Write the recursive step
    # Hint: fib(n) = fib(n-1) + fib(n-2)
    pass


# 3. Linked Lists & Trees (End of the Road)
# ------------------------------------------


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def search_linked_list(head: ListNode, target: int) -> bool:
    """Return True if target exists in the linked list."""
    # Base Case:
    if not head:
        return False

    # TODO: Write the recursive step
    # Hint: Check current node, then recurse on head.next
    pass


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: TreeNode) -> int:
    """Return the maximum depth of a binary tree."""
    # Base Case:
    if not root:
        return 0

    # TODO: Write the recursive step
    # Hint: 1 + max of left and right subtree depths
    pass


# 4. Search & Logic (Success / Failure)
# --------------------------------------


def binary_search(arr: list[int], target: int, left: int = 0, right: int = None) -> int:
    """Return the index of target in sorted array, or -1 if not found."""
    if right is None:
        right = len(arr) - 1

    # Base Case 2 (Failure):
    if left > right:
        return -1

    mid = (left + right) // 2

    # Base Case 1 (Success):
    if arr[mid] == target:
        return mid

    # TODO: Write the recursive steps for both sides
    # Hint: Decide which half to search based on comparison
    pass


# Bonus Maze-style problem (simple version)
def can_reach_exit(maze: list[list[str]], row: int, col: int) -> bool:
    """Return True if we can reach 'E' from current position.
    'W' = wall, ' ' = open path, 'E' = exit.
    """
    # You will need two failure base cases and one success base case
    # TODO: Implement all base cases + recursive exploration (up, down, left, right)
    # (This one is harder — try it after the others)
    pass
