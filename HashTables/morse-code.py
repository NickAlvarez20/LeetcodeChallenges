import string


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:

        morse_list = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
        ]
        morse_code_dict = dict(zip(string.ascii_lowercase, morse_code))

        print(morse_code_dict)
