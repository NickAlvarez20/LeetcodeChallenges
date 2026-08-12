# Let's create a simple hash table in Python using dictionaries.

# We'll store information about books in a library, where each book has a unique ID (key) and corresponding title (value).

# Initialize an empty dictionary to serve as the hash table
book_library = {}

# Add some books to the dictionary
book_library[1] = "The Catcher in the Rye"
book_library[2] = "To Kill a Mockingbird"
book_library[3] = "1984"

# Print out the hash table/dictionary
print("Initial book library:")
for key, value in book_library.items():
    print(f"Book ID: {key}, Title: {value}")

# Now, let's attempt to add a new book with an ID that's already used
book_library[1] = "Moby-Dick"

# Print out the updated dictionary
print("\nUpdated book library:")
for key, value in book_library.items():
    print(f"Book ID: {key}, Title: {value}")

# Let's remove the book with ID 2 from the dictionary
del book_library[2]

# Print out the dictionary after deletion operation
print("\nBook library after deletion:")
for key, value in book_library.items():
    print(f"Book ID: {key}, Title: {value}")

# The time complexity of adding, accessing, and deleting operations in a Python dictionary is O(1)
