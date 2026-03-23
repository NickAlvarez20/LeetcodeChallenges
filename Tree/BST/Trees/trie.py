class Trie:
    def __init__(self):
        # Each node is a dictionary: {char: next_node}
        self.root = {}
        self.end_symbol = "*"  # Marks the end of a complete word

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current:
                current[char] = {}
            current = current[char]
        current[self.end_symbol] = True

    def search(self, word):
        current = self.root
        for char in word:
            if char not in current:
                return False
            current = current[char]
        return self.end_symbol in current

    def starts_with(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current:
                return False
            current = current[char]
        return True
# Example:
t = Trie()
t.insert("apple")
print(t.search("apple"))  # True
print(t.search("app"))  # False (it's only a prefix)
print(t.starts_with("app"))  # True
