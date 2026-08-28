# Intuition
#  So for word pattern we're checking and looking for mapping exactly one unique word and mapping exactly one letter so ultimately there's the pattern that I see is we need to iterate through both the pattern and the string variable for any given parameter and concurrently check and map. The dictionary is the key intuition that would solve this problem. 

# Approach
# 1. So first we need to split the words in order to create something that is feasible for mapping due to the white space characters within the string. 
# 2. Then we need to allocate space in a variable for the dictionary zip. We need to add the word clause and immediately check if the length of the pattern does not equal the length of the split words. 
# 3. This is not going to map correctly so we can immediately return false. 
# 4. For the main part of the iteration we can now check if the length of the pattern is equal to the length of the split words. Then we're going to go into the next objectives. 
# 5. We can now use forElement and element2 using the zip method to check the first element within pattern as well as iterating through the second element within split words concurrently. 
# 6. We can check if the element is within dictzip, which is shorthand for saying if the key exists in dictionary. 
# 7. Now we can do a nested check. If the key for the current element is equal to the assigned value that we're currently reading at element 2, we can pass by and say this is a good match. Else, if it doesn't match, we can return false immediately. 
# 8. On the outer else if the element key does not exist, so in other words, if the key for any given element that we are currently iterating through does not exist. 
# 9. Then we can do another conditional check to see if element2 is already established as a value within any of the assigned values. If the value is already assigned to a key, we can return false as this will lead to an overwrite issue. 
# 10. Else we can assign the key value pair and correctly update the dictionary. 
# 11. If everything is good and we pass all of these conditions we can finally return true. And the pattern and string follow the same pattern with a matching key value pair for the assigned key value pair within the dictionary that maps to the correct positions. 

# Complexity
# - Time complexity: O(N^2)
# While the main for loop runs in an amount of times where n is the number of characters and words, there is a costly operation currently within this algorithm. If element2 in dictionary zip.values, which essentially says calling .values on a dictionary creates a view of all values, and using the in operator forces Python to scan through them one by one. It is O(n) time, and since it runs inside an O(n) loop, the overall time complexity becomes O(n squared). 

# - Space complexity: O(N)
# SplitWord stores n elements taking O(n) space. dict_zip stores at most n unique key value pairs taking O(n) space. Therefore, the overall space complexity is O(n) allocated space. 

# Code

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        split_words = s.split(" ")
        dict_zip = {}

        if len(pattern) != len(split_words):
            return False

        if len(pattern) == len(split_words):
            for ele, ele2 in zip(pattern, split_words):
                if ele in dict_zip:
                    if dict_zip[ele] == ele2:
                        pass
                    else:
                        return False
                else:
                    if ele2 in dict_zip.values(): #if value already assigned to key
                        return False
                    else:
                        dict_zip[ele] = ele2 #assign key-val pair
        return True
        


                


