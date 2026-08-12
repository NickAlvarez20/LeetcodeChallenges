# # Intuition
# To rank the elements we need to know their order from smallest to largest by isolating the unique elements and sorting them The sorted index of each number naturally represents its rank offset by one since rank starts at 1. A hash map allows us to store these pre calculated ranks so we can replace the original elements in a single efficient pass

# # Approach
# 1. First we want to copy the array and then we want to sort that copy into a set due to the duplicate values ensuring unique ranks. 2. Then we want to create an output empty array. 3. Then we want to create a dictionary to pre calculate all the index matches so we initialize rankmap as an empty dictionary. 4. Then we for index value in enumerate over the sorted copy and we update the dictionary keys with the index plus one. 5. Then we want to iterate for index value in the original array and we set the rank equal to the Of value by passing in rank a map of value which will identify based on the key that is associated with that key in value derived. 6. Then it's important to output that rank to the output array. 7. Finally we return the output. 

# # Complexity
# - Time complexity:
# <!-- Add your time complexity here, e.g. $$O(n)$$ -->

# - Space complexity:
# <!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        copy = list(arr)
        sorted_copy = sorted(set(copy))
        output = []

        # create dict to precalc all index matches
        rank_map = {}
        for idx, val in enumerate(sorted_copy):
            rank_map[val] = idx + 1

        for index, value in enumerate(arr):
            rank = rank_map[value]
            output.append(rank)

        return output
        



        
        
```