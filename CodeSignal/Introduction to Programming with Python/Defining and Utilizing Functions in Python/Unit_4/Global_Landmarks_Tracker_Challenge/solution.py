# TODO: Declare a global list to keep track of visited landmarks
visited_landmarks = [
    "Colosseum in Rome",
    "Pyramids of Giza in Egypt",
    "Christ the Redeemer in Rio de Janeiro",
]


# TODO: Define a function named log_landmark that takes two parameters: landmark and city
def log_landmark(landmark, city):
    visited_landmarks.append(f"{landmark} in {city}")

    # TODO: Add the landmark and its city to the global list in the format "landmark in city"


# TODO: Call the log_landmark function with examples e.g., "Eiffel Tower" and "Paris"
log_landmark("Eiffel Tower", "Paris")

# TODO: Print the list of visited landmarks
print(visited_landmarks)
