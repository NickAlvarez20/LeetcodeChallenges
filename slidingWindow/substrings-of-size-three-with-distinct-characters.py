from collections import Counter


class Solution(object):
    def countGoodSubstrings(self, s):
        # setup the tools
        freq_dict = Counter()
        L = 0
        result = 0
        # expand
        for R in range(len(s)):
            freq_dict[s[R]] += 1
            if (R - L + 1) > 3:
                freq_dict[s[L]] -= 1
                if freq_dict[s[L]] == 0:
                    del freq_dict[s[L]]
                L += 1
            if (R - L + 1) and len(freq_dict) == 3:
                result += 1
        return result
