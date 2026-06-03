
# Intuition: Split, append, int with bin method, append, and rejoin

# Approach: 

# Complexity:
# Time: O(n)
# Iterating a given length of a list is the major operation, resulting in O(n) 
# Space: O(n)
# Split creates a new list, which we traverse through. Most of the ops use O(1) 


class Solution:
    def convertDateToBinary(self, date: str) -> str:
        date_list = date.split("-")
        ans = []
        for date in date_list:
            binary_form = bin(int(date))[2:]
            ans.append(binary_form)
        return "-".join(ans)
