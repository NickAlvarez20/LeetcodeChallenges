# Intuition: To decode the message first we need to build a substitution table based on the first appearance of each unique character in the key therefore we will use a dictionary data structure to handle the substitution We map these unique characters to the standard English alphabet in order ABC etcetera using the strings package from Python Once the mapping is established we translate the message character by character ensuring spaces remain unchanged. The main intuition for this is recognizing the dictionary as well as the need to keep track of an alphabet index this is a one off where we must account for the alphabet index in order to iterate and update the key value pairs for the new mapping Therefore intuition to be focused on dictionary introducing one off variables that can increment as we remap the dictionary This also requires building a string so knowledge of strings string building dictionary key value pairs in finding likeness amongst values

# Approach:
# 1. Initialize a dictionary new map to store character mappings in an alphabet index to track our progress through the standard alphabet
# 2. filter the key by removing spaces and iterating through its characters
# 3. Map each character to the next available lettered in standard alphabet only if it hasn't been seen before
# 4. Preserve any space characters found in message without attempting to decode them
# 5. Translate the message by looking up each character in new map
# 6. Return the final hidden message stream 
# Complexity:
# Time: O(n+m)
# Reiterate through the key (N) To build the map and the message (M) To decode it
#
# Space: O(1)
# While we use a dictionary it will never store more than 26 key value pairs the size of the alphabet


import string


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alphabet_index = 0  # key concept
        alphabet = string.ascii_lowercase
        new_map = {}
        hidden_message = ""
        # 1
        for char in key.replace(" ", ""):
            if char not in new_map:
                new_map[char] = alphabet[alphabet_index]
                alphabet_index += 1
        # 2
        for char in message:
            if char == " ":
                hidden_message += " "
            if char in new_map:
                hidden_message += new_map[char]

        return hidden_message
