# Let's imagine a traveler who has a dictionary of destinations with some essential travel info
travel_destinations = {
    "France": {"capital": "Paris", "visited": False},
    "Italy": {"capital": "Rome", "visited": True},
    "Spain": {"capital": "Madrid", "visited": False},
}

# Check if the traveler is planning to visit Spain this year
destination = "Spain"

if travel_destinations[destination]["visited"]:
    print(f"You have already visited {destination}!")
else:
    print(
        f"It seems you haven't visited {destination} yet. Get ready for an exciting adventure in {travel_destinations[destination]["capital"]}!"
    )
