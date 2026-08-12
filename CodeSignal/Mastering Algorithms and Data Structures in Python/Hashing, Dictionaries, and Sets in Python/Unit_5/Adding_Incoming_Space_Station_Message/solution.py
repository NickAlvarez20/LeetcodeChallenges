# Initialize an empty dictionary as a Hash Table
spacemail = {}

# Let's populate with incoming messages
spacemail["Station Alpha"] = "Supply request: cosmic fuel"
spacemail["Station Beta"] = "Engineering report: engines operational"
spacemail["Station Gamma"] = "Medical report: crew status healthy"


# Let's print the initial spacemail log
print("Initial Spacemail Log:")
for station, message in spacemail.items():
    print(f"Station: {station}, Message: {message}")

# TODO: Add a new message from Station Delta and verify the updated spacemail log
spacemail["Station Delta"] = "Biomedical report: crew colons clean"

print("Updated Spacemail Log:")
for station, message in spacemail.items():
    print(f"Station: {station}, Message: {message}")
