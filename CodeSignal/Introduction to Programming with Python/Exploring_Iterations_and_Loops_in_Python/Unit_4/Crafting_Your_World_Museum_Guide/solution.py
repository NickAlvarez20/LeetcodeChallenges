# Organizing a travel guide for museums around the world.
world_museums = {
    "France": ["Louvre Museum", "Orsay Museum"],
    "Italy": ["Uffizi Gallery", "Vatican Museums"],
    "Spain": ["Prado Museum", "Reina Sofia Museum"],
    "Japan": ["Tokyo National Museum", "Kyoto National Museum"],
}

# TODO: Write a nested loop to print each country and its must-see museums in the format:
# In [country], you should visit:
# - [museum 1]
# - [museum 2]
# (Continue for each museum in the country)

for country, museums in world_museums.items():
    print(f"Musuems in {country} to see:")
    for museum in museums:
        print(f"- {museum}")
# Organizing a travel guide for museums around the world.
world_museums = {
    "France": ["Louvre Museum", "Orsay Museum"],
    "Italy": ["Uffizi Gallery", "Vatican Museums"],
    "Spain": ["Prado Museum", "Reina Sofia Museum"],
    "Japan": ["Tokyo National Museum", "Kyoto National Museum"],
}

# TODO: Write a nested loop to print each country and its must-see museums in the format:
# In [country], you should visit:
# - [museum 1]
# - [museum 2]
# (Continue for each museum in the country)

for country, museums in world_museums.items():
    print(f"Musuems in {country} to see:")
    for museum in museums:
        print(f"- {museum}")
