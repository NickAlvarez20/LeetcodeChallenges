def special_order(inputString):
    # create result var for updating string 
    result = ''
    # create length for easier readability
    length = len(inputString)

    # iterate through and build string starting from back of loop
    for i in range(length // 2 + length % 2):
        result += inputString[length-1-i]
    for i in range(length // 2 + length % 2):
        if length - 1 - i != i: # checks for odd indices, so if i doesn't equal the index like 4 then add it, this prevents duplicates
            result += inputString[i]
    return result


test = special_order("abcdefghijklmnopqrstuvwxyz" * 4 + "abcd")

print(test)
