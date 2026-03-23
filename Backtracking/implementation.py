# Classic example - Generate all permutations of a list in numbers
# Common use cases
# Explore multiple possibilities to solve a problem, like searching for path in maze of solving puzzles like Sudoku
# Think of trial and error method for finding solutions. It explores one path until it hits a dead end or constraint, then backtracks to the last valid step to try a different path.


#Pseudocode

# function backtracking(state):
#     if state is a solution:
#         return state
    
#     for choice in all possible choices:
#         if choice is valid:
#             make choice
#             result = backtracking(state with choice)
#             if result is not failure:
#                 return result
#             undo choice
#     return failure

# Finding subsets: For an input like [1,2], the goal is to find every possible combination: [], [1], [2], and [1,2]

def find_subsets(nums):
    result = []

    def backtrack(index, current_subset):
        # 1. Base Case: Add a copy of the current path to our results
        result.append(list(current_subset))

        # 2. Recursive Step: Explore all remaining elements
        for i in range(index, len(nums)):
            # Make a choice
            current_subset.append(nums[i])

            # Move forward - Recursive call to the next index
            backtrack(i+1, current_subset)

            # Backtrack - Undo the choice to try the next option
            current_subset.pop()

    backtrack(0, [])
    return result
    
# Example usage:
print(find_subsets([1,2]))



