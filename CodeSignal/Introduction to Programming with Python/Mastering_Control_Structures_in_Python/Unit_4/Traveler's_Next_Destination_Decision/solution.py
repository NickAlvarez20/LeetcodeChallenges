travel_destinations = {
    "France": {"capital": "Paris", "visited": False},
    "Italy": {"capital": "Rome", "visited": True},
    "Spain": {"capital": "Madrid", "visited": False},
}

# TODO: Set 'destination' to "Italy".
destination = "Italy"

# TODO: Use an if statement to check if 'destination' has been visited.
# Print a message according to the visited status.

if travel_destinations[destination]["visited"]:
    print(f"You have already visited {destination}!")
else:
    print(f"You have not visited {destination}")
