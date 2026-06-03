# Intuition: This problem can be solved using a brute force approach the string package dictionaries and string concatenation enumeration is important and understanding of the different indentation levels this approach is not optimal but it's good for a start.

# Approach:
# 1. First thing we want to import the string package
# 2. then create an alphabet with the string sie lower syntax and a reversed alphabet using slice to reverse 
# 3. we also want to create two dictionaries one for mapping the reversed alphabet and the other four mapping the weighted alphabet the weighted alphabet needs to have a dictionary to assign the correct key value pairs for the weights that are assigned to each individual waited list If you look at the problem you'll see there's always 26 characters so you need to map the values for each weighted list in order to map it correctly 
# 4. We then create a for loop to map and create the dictionary for the reverse alphabet and then we do the same with the weighted alphabet using al key value for the key and weighted alphabet and assign it to the value
# 5. Next we're going to want to sum each word in order to process the algorithm efficiently so we initialize A result word modulo and a final result variable which be utilized later on when we are calcul the sum mod 26 and for creating the final result 
# 6. then we use a 4 in loop to go and find each individual word in the words list and then we set up per word to store each words total sum per word so we character by character adding them up and at the end of that logic every time we wanna update the vari and reset per word sum for each iteration after we get the correct sum
# 7. We use a double nested loop to go 4 character in the word and then we check conditionally if character is in weighted alphabet We're going to use per word sum plus equals the weighted alphabet character This will assign it with the correct number based on the Weight so key value pairs key is assigned to the letter and then when we use the syntax weighted alphabet bracket character we are finding the actual weighted value assigned to that character in our weighted character alphabet
# 8. After this accumulates all of the sum we want to make sure we store that for each iteration for every word so we use result word badulo and we take the sum and mod it by 26 this is important because this ultimately what's going to decide the output so we store that in result word modulo 
# 9. After we store that we wanna do another for loop for index character since dictionary key is the index in the character is the value in our key value We use enumerate and we say if result word modulo is equal to the index then add the character to the final result
# 10. Finally we return the final result
# Complexity:
# Time: O(N * (L+A))
# Dictionary setup is OA you loop through the 26 letters of the alphabet twice to build mapping and weighted alphabet 
# Word processing is N * L you iterate through every word and every character in those words to calculate the sum
# Medullo lookup is N times a for each word you run a loop for index char and enumerate mapping that checks up to 26 letters
# Total since A is small 26 this is often implied to ONL but technically the lookup adds an extra O of a per word. 
# Reiterate through the key (N) To build the map and the message (M) To decode it
#
# Space: O(NxA)
# Dictionaries O(A)- You store two dictionaries each with 26 entries
# Final Result: O(N) - You build a string that contains one character for every word in the input list
# Constants: Since a is a fixed number 26 the space is dominated by the size of your input output effectively O of N. 
# Performance TIP instead of looping through mapping to find the character we can just use a list reverse list equals list reversed alphabet and then we say final result plus equals reverse list racket result word modulo look up OV one
# rev_list = list(reversed_alphabet)
# final_result += rev_list[result_word_modulo]

import string

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        alphabet = string.ascii_lowercase
        reversed_alphabet = string.ascii_lowercase[::-1]
        mapping = dict()
        weighted_alphabet = dict()
        for i in range(len(reversed_alphabet)):
            mapping[reversed_alphabet[i]] = i
        for i in range(len(weights)):
            weighted_alphabet[alphabet[i]] = weights[i]
        # sum each word
        result_word_modulo = 0
        final_result = ""
        for word in words:
            per_word_sum = 0
            for char in word:
                if char in weighted_alphabet:
                    per_word_sum += weighted_alphabet[char]
            result_word_modulo = per_word_sum % 26
            for index, char in enumerate(mapping):
                if result_word_modulo == index:
                    final_result += char
        return final_result
