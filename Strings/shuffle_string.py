class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        zipped = dict(zip(indices, s))
        return "".join(zipped[i] for i in range(len(s)))
