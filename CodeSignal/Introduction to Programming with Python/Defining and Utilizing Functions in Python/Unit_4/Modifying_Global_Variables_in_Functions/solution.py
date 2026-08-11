# Define a function which tries to modify a global variable
chosen_countries = ["France", "Italy"]


def add_country(country):
    chosen_countries.append(country)  # This modifies the global variable


add_country("Spain")
print(chosen_countries)  # ["France", "Italy", "Spain"]
