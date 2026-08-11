# A dictionary to handle airport codes
airport_codes = {
    "JFK": {"city": "New York", "country": "USA"},
    "LAX": {"city": "Los Angeles", "country": "USA"},
    "LHR": {"city": "London", "country": "UK"},
    "HND": {"city": "Tokyo", "country": "Japan"},
    "SYD": {"city": "Sydney", "country": "Australia"},
}

# TODO: Update 'country' of 'LHR' to 'England'
airport_codes["LHR"]["country"] = "England"
print(airport_codes)
