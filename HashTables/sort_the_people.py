class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        height_names = {}
        result = []
        # Create a list of height: name pairs for dictionary
        for index, val in enumerate(heights):
            height_names[val] = names[index]
        # sort the heights list
        sorted_heights = sorted(heights, reverse=True)
        # iterate the sorted list and check where it matches key
        for height in sorted_heights:
            result.append(height_names[height])
        return result
