# Travel profile has necessary details of the traveller, including insurance now
travel_profile = {
    "passport": True,
    "visa": {"required": True, "available": False},
    "tickets": True,
    "insurance": True,
}

# Check if all required documents for travel are available
# TODO: Insurance check missing
if (
    travel_profile["passport"]
    and travel_profile["tickets"]
    and travel_profile["insurance"]
):
    if travel_profile["visa"]["required"] and not travel_profile["visa"]["available"]:
        print("You need to apply for a visa.")
    else:
        print("You are ready to travel.")
else:
    print(
        "General travel advice: Make sure you have your passport, tickets, and insurance ready for hassle-free travel."
    )  # Mention of insurance is missing
