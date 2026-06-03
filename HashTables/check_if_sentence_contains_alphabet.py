from collections import Counter


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = string.ascii_lowercase
        count_alph = Counter(alphabet)
        count_sentence = Counter(sentence)
        return len(count_alph) == len(count_sentence)
