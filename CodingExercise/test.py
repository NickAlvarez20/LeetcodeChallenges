import random

random_list = [random.randint(-50, 50) for _ in range(10)]


for i in range(len(random_list)):
    if random_list[i] > 0:
        print(random_list[i])
    else:
        break

print(random_list)


digit = 56
print(digit % 10)