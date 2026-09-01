# # Intuition
# Intuitively this problem for flipping the square sub-matrix vertically requires a two pointers approach. One where we're keeping track of the top and bottom column. And basically that is how we design it. One pointer points at the top column, one keeps track of the bottom column. That way we can flip them dynamically.

# # Approach
# 1. First, mentally identify what the X, Y, and K stand for and set up an equation where you can fundamentally understand it by using a whiteboard as well as understanding how they work within each part of the process.
# 2. Now we're going to set up a while loop for the top and bottom to make sure once they meet in the middle the loop exits.
# 3. Then we have to check for each element within the range. So for column offset and range of K, which suggests that I'm looking at the column only within the range of that matrix. This allows me to identify the sub matrix.
# 4. Setup a variable current column set that equals y plus the column offset. This will initialize the correct index position and allow us to start from the y position within each subarray within the matrix that we are currently evaluating.
# 5. Now I can simply swap the values within the positions from the top row and the bottom row.
# 6. and then I can increment top row +1 and bottom row -1 which effectively moves the top row and bottom row until the conditions in the parameters given for X and K meet the while loop exit condition
# 7. Then I can return the grid and that will have effectively in place using the two pointers swapped the values that we needed to update in memory within the matrix, etc. submatrix.

# # Complexity
# - Time complexity: The time complexity is O(K^2). The time complexity depends entirely on the size of the submatrix, which is defined by K, not the entire grid.
# The while loop runs exactly K divided by 2 times moving the top row and bottom row toward the center.
# Inside the while loop, the for loop runs exactly k times visiting every column in that row.
# Total operations is k divided by 2 times k, which equals k squared divided by 2.
# Then we can simplify it to O(n*m) since K2 is the largest factor for the algorithm. You can also express it in terms of the total grid size, n times m. The worst case scenario where the submatrix spans the entire grid would be O(n*m).

# - Space complexity:
# The space complexity is constant. We're using top row, bottom row, and updating a current column and just swapping so everything remains consistent as it's done in place with the two pointers variable making this algorithm O of 1, constant auxiliary space.

# Code

class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        top_row = x
        bottom_row = x + k -1

        while top_row < bottom_row:
            for column_offset in range(k):
                curr_col = y + column_offset
                grid[top_row][curr_col], grid[bottom_row][curr_col] = grid[bottom_row][curr_col], grid[top_row][curr_col]

            top_row += 1
            bottom_row -= 1

        return grid
