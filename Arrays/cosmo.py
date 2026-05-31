# Space exploration crew members' data, containing their names, missions, and roles
crew_data = (
    "Neil,Armstrong,Apollo 11,C;Buzz,Aldrin,Apollo 11,P;Michael,Collins,Apollo 11,CM"
)

crew_data = crew_data.split(";")
clean_data = []

for person in crew_data:
    first, last, mission, role = person.split(",")
    clean_data.append((f"{first} {last} {mission} {role}"))

print("\n".join(clean_data))

# TODO: Split the crew_data string into a list of individual crew member information using the appropriate delimiter

# TODO: Iterate over the list of crew member data

# TODO: For each member, split their data string using commas as delimiters

# TODO: Print the crew member's details in a formatted string

# Expected output:
# Neil Armstrong Apollo 11 C
# Buzz Aldrin Apollo 11 P
# Michael Collins Apollo 11 CM
