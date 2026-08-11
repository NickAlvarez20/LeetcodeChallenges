# Travel profile has necessary details of the traveler
travel_profile = {
    "passport": True,
    "tickets": True,
}

# Check if the basic requirement for travel are met (passport and tickets)
if travel_profile["passport"] and travel_profile["tickets"]:
    print("You are ready for the initial phase of travel preparation.")
else:
    print("Please ensure you have both your passport and tickets.")
