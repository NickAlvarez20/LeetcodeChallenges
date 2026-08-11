age = 23
budget = 900

if age > 18:
    if budget > 1000:
        print("You are eligible for the international travel package.")
    elif budget >= 500:
        print("You are eligible for a special deal on the local travel package.")
    else:
        print("You are eligible for the local travel package.")
else:
    print("You are eligible for the children's travel package.")
