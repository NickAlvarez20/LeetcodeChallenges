class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count = 0
        split_str = text.split(" ")
        for word in split_str:
            for letter in word:
                if letter in brokenLetters:
                    count += 1
                    break
        return len(split_str) - count

# Top solution, beats 100% and memory beats 93.97%
