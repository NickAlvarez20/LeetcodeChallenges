# Create a Python dictionary that acts as a hash table
event_system = {}

# Add upcoming events
event_system[1] = "Coding Bootcamp - Monday, 8:00 AM"
event_system[2] = "Python Webinar(Data Structures) - Tuesday, 11:00 AM"
event_system[3] = "Data Science Meetup - Wednesday, 6:00 PM"

# TODO: Update the Python Webinar description
# Note: don't change previous definitions of `event_system` elements.

# Print the updated events list
print("\nUpdated upcoming events:")
for event_id, event_desc in event_system.items():
    print(f"Event ID: {event_id}, Description: {event_desc}")
