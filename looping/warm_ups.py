fruits = ['apple', 'banana', 'cherry', 'kiwi']
fruits_in_salad = ""

index = 0

while index < len(fruits):
    if index == len(fruits) - 1:
        fruits_in_salad += fruits[index]
        index += 1
    else:
        fruits_in_salad += fruits[index] + " "
        index += 1

print(fruits_in_salad)