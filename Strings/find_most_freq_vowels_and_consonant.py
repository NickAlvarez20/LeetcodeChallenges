from collections import Counter


class Solution:
    def maxFreqSum(self, s: str) -> int:
        max_freq_consonant = 0
        max_freq_vowel = 0
        vowels = ["a", "e", "i", "o", "u"]
        freq_dict = Counter(s)
        for key, value in freq_dict.items():
            if key in vowels:
                temp = value
                max_freq_vowel = max(max_freq_vowel, temp)
            elif key not in vowels:
                temp2 = value
                max_freq_consonant = max(max_freq_consonant, temp2)
        return max_freq_vowel + max_freq_consonant
