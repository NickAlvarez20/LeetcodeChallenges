# Organizing a photo exhibition of iconic landmarks from around the world.
exhibition_landmarks = {
    "France": ["Louvre Museum", "Mont Saint Michel"],
    "Italy": ["Leaning Tower of Pisa", "Venice Canals"],
    "Spain": ["Sagrada Familia", "Royal Palace of Madrid"],
    "Japan": ["Tokyo Tower", "Kiyomizu-dera"],
}

# TODO: Complete the loop to iterate through the countries and their landmarks
for country, landmarks in exhibition_landmarks.items():
    print(f"Landmarks in {country} to feature:")
    for landmark in landmarks:
        print(f"- {landmark}")
