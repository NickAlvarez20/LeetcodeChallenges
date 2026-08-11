# A dictionary to handle airport codes
airport_codes = {
    "JFK": {"city": "New York", "country": "USA"},
    "LAX": {"city": "Los Angeles", "country": "USA"},
    "LHR": {"city": "London", "country": "UK"},
    "HND": {"city": "Tokyo", "country": "Japan"},
    "SYD": {"city": "Sydney", "country": "Australia"},
}

# TODO: Access and print the city and country that corresponds to a particular airport code.
print(airport_codes["LHR"]["city"], "-", airport_codes["LHR"]["country"])
