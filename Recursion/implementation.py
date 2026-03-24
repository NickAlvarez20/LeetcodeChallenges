
# EVERY LEETCODE PROBLEM FOLLOWS THIS STRUCTURAL FLOW

def recursive_function(params):
    # 1. BASE CASE: When do we stop? (The tiniest version of the problem)
    if condition_to_stop:
        return base_value
    
    # 2. RECURSIVE CASE: break the problem down
    # Trust that this call works for a smaller input
    result_from_smaller_part = recursive_function(smaller_input)

    # 3 COMBINE: Use the sub-result to solve the current level
    return current_work + result_from_smaller_part

# 2. The exercise: print down return up

# helps memorize LIFO nature of the stack

def warm_up(n):
    # -- GOING DOWN THE STACK --
    print(f"Entering level {n}")

    # 1. Base case: The smallest possible n
    if n == 1:
        print("reached Base Case: 1. Now returning...")
        return 1
    
    # 2. Recursive call: move toward the base case (n-1)
    sub_sum = warm_up(n-1)

    # -- COMING BACK UP THE STACK --
    total = n + sub_sum
    print(f"Returning to level {n}: Added {n} to sub-sum {sub_sum} = {total}")
    return total

# Run it
final_result = warm_up(3)
print(f"Final Answer: {final_result}")


def solve(input):
    # 1. Base Case: The smallest possible input
    if input_is_tiny:
        return simplest_answer
    
    # 2. Relation: My piece + friend's work on the rest
    friend_result = solve(smaller_input)
    return my_piece + friend_result

#```python
# =============================================================================
# Base Cases Cheat Sheet - Essential Patterns for Recursion & Edge Handling
# =============================================================================

# 1. Strings & Arrays (The "Empty" Check)
# If you are processing a collection, the most "pathetic" version is having nothing to process.

# Problem: Count vowels in a string.
# Base Case: if not string: return 0          # An empty string has 0 vowels

# Problem: Check if a list contains a specific number.
# Base Case: if not arr: return False         # You can't find a number in an empty list

# Problem: Reverse a string.
# Base Case: if len(s) <= 1: return s         # A single letter or empty string is already "reversed"


# 2. Numbers (The "Identity" Check)
# If you are doing math, the base case is usually the identity element
# (the number that doesn't change the result of the operation).

# Problem: Factorial
# Base Case: if n == 0: return 1              # By definition, 0! = 1

# Problem: Sum of numbers from 1 to n
# Base Case: if n == 0: return 0              # The sum of nothing is 0

# Problem: Fibonacci sequence
# Base Case: if n <= 1: return n              # The 0th Fibonacci is 0, the 1st is 1


# 3. Linked Lists & Trees (The "End of the Road")
# In data structures with pointers, the base case is hitting a dead end (None).

# Problem: Find the maximum depth of a Binary Tree.
# Base Case: if not node: return 0            # A non-existent tree has 0 height

# Problem: Search for a value in a Linked List.
# Base Case: if not head: return False        # If you hit the end without finding it, it's not there


# 4. Search & Logic (The "Success/Failure" Check)
# In these problems, you usually have two base cases: one for winning and one for losing.

# Problem: Binary Search
# Base Case 1 (Success): if arr[mid] == target: return mid
# Base Case 2 (Failure): if left > right: return -1   # The search area vanished

# Problem: Pathfinding in a maze
# Base Case 1 (Success): if current_pos == exit: return True
# Base Case 2 (Failure): if wall_hit or out_of_bounds: return False


