def multi_password_strength_counter(passwords):
    special_characters = "!@#$%^&*()-+"

    # List to hold the strength for each password
    password_strengths = []

    for password in passwords:
        strength = {
            "length": False,
            "digit": False,
            "lowercase": False,
            "uppercase": False,
            "special_char": False,
        }
        if len(password) >= 8:
            strength["length"] = True
        for char in password:
            if char.isdigit():
                strength["digit"] = True
            if char.islower():
                strength["lowercase"] = True
            if char.isupper():
                strength["uppercase"] = True
            if char in special_characters:
                strength["special_char"] = True
        password_strengths.append(strength)
    return password_strengths


passwords = ["password", "Pa$$w0rd", "SuperSecurePwd!", "weakpw"]
results = multi_password_strength_counter(passwords)
for result in results:
    print(result)

# The expected output is:
# {'length': True, 'digit': False, 'lowercase': True, 'uppercase': False, 'special_char': False}
# {'length': True, 'digit': True, 'lowercase': True, 'uppercase': True, 'special_char': True}
# {'length': True, 'digit': False, 'lowercase': True, 'uppercase': True, 'special_char': True}
# {'length': False, 'digit': False, 'lowercase': True, 'uppercase': False, 'special_char': False}
