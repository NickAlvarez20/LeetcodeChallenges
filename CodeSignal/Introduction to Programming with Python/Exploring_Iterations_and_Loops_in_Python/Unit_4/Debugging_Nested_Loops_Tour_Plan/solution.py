# We might want to do some sightseeing in each country. For each country, we have a list of sights.
country_sights = {
    "France": ["Eiffel Tower", "Louvre Museum"],
    "Italy": ["Colosseum", "Piazza San Marco"],
    "Spain": ["Park Güell", "The Alhambra"],
    "Japan": ["Mt. Fuji", "Fushimi Inari Taisha"],
}

# There's a bug in the loop structure that prevents the sights from being printed correctly. Fix it.
for country, sights in country_sights.items():
    print(f"***In {country}, I want to see:")
    for sight in sights:
        print(sight)
