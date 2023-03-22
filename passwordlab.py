# Create password encoder function - Arlen Larry Gyden
def encode():
    orig_password = input("Please enter your password to encode: ")
    encod_password = ''
    for number in orig_password:
        number = int(number) + 3
        encod_password += str(number)
    return orig_password, encod_password