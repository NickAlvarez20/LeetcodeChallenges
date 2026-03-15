# Intuition: When dealing with strings data structure we can use the replace method to simply replace any matches within a given string

# Approach: Using a sequence of chain replace methods we can look for all matches of a given order pattern and replace all of them with the updated pattern 

# Complexity:
# Time: O(n)
# The replace method must scan the entire string once fine and replace matches Since we are chaining three replacements the interpreter performs three separate passes over the string Total work is O of three N which simplifies to O of N 
# Space: O(n)
# Since strings are immutable every time you call replace Python creates a brand new string in memory the first replace creates a new string the 2nd creates another and so on the resulting string also occupies space proportional to the input size leading to O of N total space

class Solution:
    def interpret(self, command: str) -> str:
        return command.replace("G", "G").replace("()", "o").replace("(al)", "al")
