class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        from collections import Counter

        morse_dict = {
            "a": ".-",
            "b": "-...",
            "c": "-.-.",
            "d": "-..",
            "e": ".",
            "f": "..-.",
            "g": "--.",
            "h": "....",
            "i": "..",
            "j": ".---",
            "k": "-.-",
            "l": ".-..",
            "m": "--",
            "n": "-.",
            "o": "---",
            "p": ".--.",
            "q": "--.-",
            "r": ".-.",
            "s": "...",
            "t": "-",
            "u": "..-",
            "v": "...-",
            "w": ".--",
            "x": "-..-",
            "y": "-.--",
            "z": "--..",
        }

        built_word = ""
        morse_words = []

        # iterate through and update based on code val
        for word in words:
            built_word = ""
            for char in word:
                built_word += morse_dict[char]
            morse_words.append(built_word)

        total_unique_words = set(morse_words)

        return len(total_unique_words)
