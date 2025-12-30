# Mini Problem 1: FizzBuzz (Classic starter)
# Print numbers from 1 to 20, but:

# If the number is divisible by 3, print "Fizz" instead
# If divisible by 5, print "Buzz"
# If divisible by both, print "FizzBuzz"

def fizzBuzz():
    for i in range(1, 21):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i%5 == 0:
            print("Buzz")
        elif i%3 == 0:
            print("Fizz")
        else:
            print(i)

fizzBuzz()

# Mini Problem 2: Reverse a String
# Given a string s, return it reversed.

def reversedStr(s):
    return s[::-1]

example_str = "Hello World"
print(reversedStr(example_str))

# Mini Problem 3: Count Vowels
# Given a string s, return how many vowels (a, e, i, o, u) it has. Case insensitive.

def countVowels(s):
    count = 0
    vowels = "aeiouAEIOU"
    for char in s:
        if char in vowels:
            count +=1
    return count

# Mini Problem 4: Find the Max in a List
# Given a list of numbers nums, return the largest one. Don’t use max() — do it manually.

def maxInList(nums):
    if not nums:
        return None

    maxVal = nums[0]
    for num in nums[1:]:
        if num > maxVal:
            maxVal = num
    return maxVal

exampleNums = [3, 7, 2, 9, 1]
print(maxInList(exampleNums))

