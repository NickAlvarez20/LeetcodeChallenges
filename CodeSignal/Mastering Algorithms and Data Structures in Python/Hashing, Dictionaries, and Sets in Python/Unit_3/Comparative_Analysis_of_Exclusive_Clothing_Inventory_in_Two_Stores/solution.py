def exclusive_products(inventory1, inventory2):
    # convert to uppercase
    format_uppercase_1 = [word.upper() for word in inventory1]
    format_uppercase_2 = [word.upper() for word in inventory2]

    # create two sets
    set1 = set(format_uppercase_1)
    set2 = set(format_uppercase_2)

    # perform difference operation (-)

    unique_to_one = sorted(list(set1 - set2))
    unique_to_two = sorted(list(set2 - set1))

    # convert back into sorted lists and return as tuple

    return (unique_to_one, unique_to_two)


inventory1 = ["Shirt", "Jeans", "Hat"]
inventory2 = ["jeans", "Belt", "Boots"]
print(exclusive_products(inventory1, inventory2))
# Expected output: (['HAT', 'SHIRT'], ['BELT', 'BOOTS'])

inventory1 = ["T-Shirt", "hoodie", "Backpack"]
inventory2 = ["Backpack", "Hoodie", "t-shirt"]
print(exclusive_products(inventory1, inventory2))
# Expected output: ([], [])

inventory1 = []
inventory2 = ["Dress", "Skirt", "Coat"]
print(exclusive_products(inventory1, inventory2))
# Expected output: ([], ['COAT', 'DRESS', 'SKIRT'])
