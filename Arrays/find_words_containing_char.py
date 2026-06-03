class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []
        n = len(words)

        for i in range(n):
            m = len(words[i])
            for j in range(m):
                letters = words[i][j]
                if letters in x:
                    ans.append(i)
                    break
        return ans
