# Define a function which tries to modify a global variable
chosen_countries = ["France", "Italy"]


def add_country(country):
    # TODO: Modify the list of chosen_countries to include the new country
    chosen_countries.append(country)
    print("Country added successfully!")  # Feedback confirmation


add_country("Spain")
print(
    chosen_countries
)  # This should print ["France", "Italy", "Spain"] after your modification
