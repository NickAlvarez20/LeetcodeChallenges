class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        result = []
        i = 0
        counter = 0

        while len(result) < len(A):
            # create freq dict
            freq_a = Counter(A[: i + 1])
            freq_b = Counter(B[: i + 1])
            counter = 0
            for key, val in freq_a.items():
                if key in freq_b:
                    counter += 1
            result.append(counter)
            i += 1
        return result

        # [1,3] | [3, 1]
        # [1,3,2] | [3,1,2]

        # [0, 2, ]
