# Controlling travel according to age and budget
age = 27
budget = 800

if age > 18:
    if budget > 1000:
        print("You are eligible for the international travel package.")
    elif budget >= 500:  # Add the correct condition here
        print("You are eligible for a special deal on the local travel package.")
    else:
        print("You are eligible for the local travel package.")
else:
    print("You are eligible for the children's travel package.")
