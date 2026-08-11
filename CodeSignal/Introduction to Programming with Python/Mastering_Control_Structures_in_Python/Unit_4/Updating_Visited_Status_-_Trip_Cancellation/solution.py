# Let's imagine a traveler who has a dictionary of destinations with some essential travel info
# TODO: Change visited status for Italy to False
travel_destinations = {
    "France": {"capital": "Paris", "visited": False},
    "Italy": {"capital": "Rome", "visited": False},
    "Spain": {"capital": "Madrid", "visited": False},
}

# Test if the traveler had to cancel their trip to Italy
destination = "Italy"

if travel_destinations[destination]["visited"]:
    print(f"You have already visited {destination}!")
else:
    print(
        f"It seems you had to cancel your trip to {destination}. Hopefully, you can visit {travel_destinations[destination]['capital']} soon!"
    )
