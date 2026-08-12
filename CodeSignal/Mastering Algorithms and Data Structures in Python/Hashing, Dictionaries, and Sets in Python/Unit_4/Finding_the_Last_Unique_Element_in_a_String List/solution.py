def find_unique_string(words):
    # create two sets
    seen, duplicates = set(), set()

    # iterate through words and add to sets and duplicates
    for word in words:
        if word in seen:
            duplicates.add(word)
        seen.add(word)

    # next iterate words again and check if in duplicates
    unique_string = []
    for word in words:
        if word not in duplicates:
            unique_string.append(word)

    if unique_string:
        return unique_string[-1]
    return ""


print(
    find_unique_string(["apple", "banana", "apple", "mango", "banana"])
)  # It should print: 'mango'
print(find_unique_string(["hello", "world", "hello"]))  # It should print: 'world'
print(find_unique_string(["hello", "world", "hello", "world"]))  # It should print: ''
print(find_unique_string([]))  # It should print: ''
