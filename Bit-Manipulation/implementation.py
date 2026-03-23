# Operator	Name	Effect	Python Example
# &	AND	1 only if both bits are 1	5 & 3 (0101 & 0011 = 0001) → 1
# |	OR	1 if at least one bit is 1	5 | 3 (0101 | 0011 = 0111) → 7
# ^	XOR	1 if bits are different	5 ^ 3 (0101 ^ 0011 = 0110) → 6
# ~	NOT	Flips all bits (0→1, 1→0)	~5 → -6 (due to Two's Complement)
# <<	Left Shift	Moves bits left (Multiplies by 2)	5 << 1 (0101 becomes 1010) → 10
# >>	Right Shift	Moves bits right (Divides by 2)	5 >> 1 (0101 becomes 0010) → 2


def is_even(n):
    return (n & 1) == 0


print(is_even(4))  # True


# Check if a number is a Power of 2
# Powers of 2 (2, 4, 8, 16) only have one 1 in binary (e.g., 8 is 1000). If you subtract 1, you get all 1s (e.g., 7 is 0111).
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0


print(is_power_of_two(16))  # True


# C. The XOR Swap Trick
# You can swap two numbers without using a third "temp" variable.
a, b = 5, 10
a = a ^ b
b = a ^ b
a = a ^ b
print(a, b)  # 10, 5


# 3. The "Single Number" Problem (Classic Interview Question)
# Problem: You have a list where every number appears twice except for one. Find the single one.
# Solution: XORing a number with itself results in 0 (x ^ x = 0). If you XOR everything in the list, the pairs cancel out, leaving only the unique number.
def find_single(arr):
    res = 0
    for x in arr:
        res ^= x
    return res


data = [4, 1, 2, 1, 2]
print(f"The unique number is: {find_single(data)}")  # 4


# Why use this?
# Speed: Bitwise operations are executed directly by the CPU in a single cycle.
# Space: You can store multiple "True/False" flags in a single integer (called a Bitmask).