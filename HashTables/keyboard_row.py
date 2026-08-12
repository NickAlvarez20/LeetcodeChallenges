# # Intuition
# So we want to use a dictionary and an array to store the final results Ideally we have to create key value pairs that map the rows with the letters both lower case and uppercase to correctly initialize the dictionary

# # Approach
# 1. first we initialize an output and set it equal to an empty array. 2. And then we create a dictionary and create key value pairs that match the word to the row of the keyboard . 3. Then we iterate for the word in the words list that we are initially given 4. Then we want to set a boolean flag is valid and set it equal to true. 5. Then we loop through for each character within the word. 6. So we need to check if the value of the character does not equal the value of the first letter of the given word we are currently iterating through If this is a mismatch then we set is valid to false and we break. 7. Then if we get through this entire loop and is valid has not been set to false then we can append the word indicating that all the letters within that word match the given row. 8. Finally we return the output and this will contain the correct words for any given keyboard row that match

# # Complexity
# - Time complexity: O(N x M)
# 1. Let N be the number of words in the input list. 
# 2. Let M be the maximum length of a word. 
# 3. You loop through inwards for each word you look at most in characters
# 4.  Dictionary lookups are of one on average
# 5. This results in an overall time complexity of ON times M or O of L where L is the total number of characters across all words.

# - Space complexity: O(1) auxillary space
# Keyboard hashmap has a fixed size of 52 keys constant size. 2. Fixed size structures take all of one space because they do not grow with the input size. 3. The output list takes all in space to store the results but the extra memory used by the algorithm itself is constant. 

# Code
```python3 []
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        output = []
        keyboard_map = {
            "q": 1,
            "w": 1,
            "e": 1,
            "r": 1,
            "t": 1,
            "y": 1,
            "u": 1,
            "i": 1,
            "o": 1,
            "p": 1,
            "Q": 1,
            "W": 1,
            "E": 1,
            "R": 1,
            "T": 1,
            "Y": 1,
            "U": 1,
            "I": 1,
            "O": 1,
            "P": 1,
            "a": 2,
            "s": 2,
            "d": 2,
            "f": 2,
            "g": 2,
            "h": 2,
            "j": 2,
            "k": 2,
            "l": 2,
            "A": 2,
            "S": 2,
            "D": 2,
            "F": 2,
            "G": 2,
            "H": 2,
            "J": 2,
            "K": 2,
            "L": 2,
            "z": 3,
            "x": 3,
            "c": 3,
            "v": 3,
            "b": 3,
            "n": 3,
            "m": 3,
            "Z": 3,
            "X": 3,
            "C": 3,
            "V": 3,
            "B": 3,
            "N": 3,
            "M": 3,
        }

        for word in words:
            is_valid = True
            for char in word:
                if keyboard_map[char] != keyboard_map[word[0]]:
                    is_valid = False
                    break
            if is_valid:
                output.append(word)
        return output
```