class Solution:
    def countKeyChanges(self, s: str) -> int:
        # look at the letters in the string, compare the current val with the next val, if not the same, update count
        count = 0
        lowercase_str = s.lower()
        curr_val = lowercase_str[:1]
        # iterate thorugh lowercase str
        for char in range(1, len(lowercase_str)):
            if curr_val != lowercase_str[char]:
                count += 1
            curr_val = lowercase_str[char]
        return count