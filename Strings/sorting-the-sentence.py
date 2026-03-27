class Solution:
    def sortSentence(self, s: str) -> str:
        split_str = s.split(" ")  # split string for iterating
        sorted_dict = {}  # create new dictionary for key, value pairs
        result = []  # final result arr/list
        for word in split_str:
            sorted_dict[int(word[-1])] = word[:-1]  # parse nTOi and slice
        correct_order = sorted(sorted_dict)  # sort the keys in asc
        # iterate proper order of sentence
        for num in correct_order:
            result.append(
                sorted_dict[num]
            )  # use num to iden key match within dict and append corresponding word
        return " ".join(result)  # join results
