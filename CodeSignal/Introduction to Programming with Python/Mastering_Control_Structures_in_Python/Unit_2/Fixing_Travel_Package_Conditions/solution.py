# Check age and assign a travel package accordingly
age = 20  # Example age

if age < 18:
    print("You are eligible for the children's travel package.")
elif age <= 59 and age >= 18:
    print("You are eligible for the adult's travel package.")
else:
    print("You are eligible for the senior citizen's travel package.")
