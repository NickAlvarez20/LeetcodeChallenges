class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        ans = 0
        for i in range(0, len(nums) + 1):
            if i not in nums:
                ans = i
        return ans


# # Time Complexity - O(n^2)
# The time complexity is O of N squared because the algorithm uses a loop that runs in plus one times and inside the loop it performs an O of inserts operation on the input list therefore if we combine these considering the for loop and the inside for if condition that's n*n so that's N ^2

# Space Complexity - O(1)
# Space complexity algorithm only uses a fixed amount of additional memory for simple variables answer and I regardless of how large the input list grows

#  The intuition for the missing number is to loop through and compare the indices and the values in a clever way using a range that exceeds the current range so it becomes exclusive and not inclusive the way a Python for loop usually increments Then we can see if the index does not exist in the nums array so we compare the index value to the list of numbers and their actual values

# 1. So we declare a variable called answer and we set it equal to zero this is the only thing necessary since we're not going into too complicated of logic we just need one variable that will update mean it won't have multiple updates
# 2. Then we loop through for I in range of zero of the length of the numbers plus one this is the key point here to solve this correctly we need to add one to the end of the range
# 3. then we check if the index does not exist in the noms array then we can update
# 4. Then we check if the index does not exist in the noms array then we can update Now we update the initially declared global variable within the function scope (ans)
#3. Then we return the answer and that will be the correct value that does not exist within the range


# Analysis: This naive approach has a 2173 millisecond runtime and beats 5% of solutions and the memory is 25 megabytes and it beats 15.58%. This is a brute force naive approach but it does solve the question

# Alternative solutions: 
# You can use the mathematical formula in * N + 1 / 2 this would be a mathematical formulae approach

# You could do another mathematical approach where you create a result variable you add the index value and you subtract it from the value within the array You do this through the entire length and this will cleverly return a solution where it is the correct value.

# You could also use a vectors approach, a XOR approach, or a clever sort approach Where we check if first element does not equal zero we return zero if the last element does not equal the length of the noms array we return the length of the arr and then another case where we loop from one to the length of the array and if the value does not equal the index then we return the index so that will find any value that does not equal the index and we return the index. 
