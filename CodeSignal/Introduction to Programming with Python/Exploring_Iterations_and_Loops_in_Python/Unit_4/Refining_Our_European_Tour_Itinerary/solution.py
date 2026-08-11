# Initially, our list included various countries with their must-see sights.
# TODO: Change the dictionary to exclude Japan, focusing the sightseeing list only on European destinations.
country_sights = {
    "France": ["Eiffel Tower", "Louvre Museum"],
    "Italy": ["Colosseum", "Piazza San Marco"],
    "Spain": ["Park Güell", "The Alhambra"],
    "Japan": ["Mt. Fuji", "Fushimi Inari Taisha"],
}

del country_sights["Japan"]


for country, sights in country_sights.items():
    print(f"***In {country}, I want to see:")
    for sight in sights:
        print(sight)
