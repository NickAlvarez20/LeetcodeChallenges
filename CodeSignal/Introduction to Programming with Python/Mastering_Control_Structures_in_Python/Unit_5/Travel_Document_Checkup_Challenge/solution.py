# Travel profile has necessary details of the traveller
travel_profile = {
    "passport": True,
    "visa": {"required": True, "available": False},
    "tickets": True,
}

# Check if all required documents for travel are available
if travel_profile["passport"] and travel_profile["tickets"]:
    if (
        travel_profile["visa"]["required"] and not travel_profile["visa"]["available"]
    ):  # This line contains a bug
        print("You need to apply for a visa.")
    else:
        print("You are ready to travel.")
else:
    print(
        "General travel advice: Make sure you have your passport, visa (if required), and tickets ready for hassle-free travel."
    )
