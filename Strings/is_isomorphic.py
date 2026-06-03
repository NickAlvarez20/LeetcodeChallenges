from collections import Counter


class Solution(object):
    def isIsomorphic(self, s, t):
        # Create two dictionaries
        mapST = {}
        mapTS = {}

        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]

            # Check if char_s is already mapped to something else
            if char_s in mapST and mapST[char_s] != char_t:
                return False

            # Check if char_t is already mapped to something else
            if char_t in mapTS and mapTS[char_t] != char_s:
                return False

            # Establish the mapping
            mapST[char_s] = char_t
            mapTS[char_t] = char_s

        return True
