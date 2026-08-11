# Travel profile has necessary details of the traveller
travel_profile = {
    "passport": True,
    "visa": {"required": True, "available": False},
    "tickets": True,
}

# TODO: Implement nested if statements to check if all required documents for travel are available
# Use the pattern: if <condition>: ... else: ...
# Inside the first if block, add another if statement to check visa requirements

if travel_profile["passport"] and travel_profile["tickets"]:
    if travel_profile["visa"]["required"] and not travel_profile["visa"]["available"]:
        print("You need to apply for a visa")
    else:
        print("You have all the required documents")
else:
    print("You do not have all the required documents.")
