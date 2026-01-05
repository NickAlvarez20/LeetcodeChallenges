class Solution:
    def isValid(self, s: str) -> bool:
        stack = []


        # Intuition: So for valid parentheses we can use a stack and compare the item on the top of the stack that we had just appended as well as any other parentheses that's contained