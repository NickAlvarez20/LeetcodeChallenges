from collections import Counter


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq_list = Counter(nums)
        result = []

        freq_list = list(freq_list.items())
        freq_list.sort(key=lambda x: (x[1], -x[0]))

        for index, _ in enumerate(freq_list):
            keys = freq_list[index][0]
            values = freq_list[index][1]
            counter = values
            while counter > 0:
                result.append(keys)
                counter -= 1
        return result
