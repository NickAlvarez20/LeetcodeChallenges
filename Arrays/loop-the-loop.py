# List of fruits to include in a fruit salad
fruits = ["apple", "banana", "orange", "kiwi", "melon"]

index = 0

while index < len(fruits):
    print(fruits[index])
    index += 1

    # This code will create a simplified fruit salad with the provided fruits
fruits = ["apple", "banana", "cherry", "date"]
fruits_in_salad = ""

index = 0
# TODO: Create a while loop that assembles a string of fruit names separated by spaces, without adding a space after the last fruit
# Hint: Consider using a conditional to determine when to add a space

while index < len(fruits):
    if fruits[index] == fruits[-1]:
        fruits_in_salad += fruits[-1] + ""
        index += 1
    else:
        fruits_in_salad += fruits[index] + " "
        index += 1

print(fruits_in_salad)  # Output the fruits in the salad
