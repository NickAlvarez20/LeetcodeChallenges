class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        total_count = 0

        for i in range(len(hours)):
            for j in range(len(hours)):
                if i < j and (hours[i] + hours[j]) % 24 == 0:
                    total_count += 1

        return total_count
