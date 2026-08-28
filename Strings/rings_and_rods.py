# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
from collections import Counter

class Solution:
    def countPoints(self, rings: str) -> int:
        res = []
        frequencies = {}

        for i in range(0, len(rings), 2):
            res.append(rings[i:i+2])

        
        # need to make a key, value dictionary where key is rod and value is colors
        for ele in res:
            color = ele[0] # 'B'
            rod = ele[1] # '0'
            if rod not in frequencies: 
                frequencies[rod] = color # '0' = 'B'
            elif color not in frequencies[rod]: # if color not in key
                frequencies[rod] += color  # add new color 

        print(frequencies)


        count = 0


        key = sorted('BGR')

        for rod, val in frequencies.items():
            if sorted(val) == key:
                count += 1
        return count
        
      
        

        
```