# Create password encoder function - Arlen Larry Gyden
def encode():
    orig_password = input("Please enter your password to encode: ")
    encod_password = ''
    for number in orig_password:
        number = int(number) + 3
        encod_password += str(number)
    return orig_password, encod_password

# Create main function
def main():
    # Open menu while loop
    password_encoder = True
    while password_encoder:
        # Print menu
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit", end='\n\n')

        # Prompt user menu selection
        user_select = int(input("Please enter an option: "))
        if user_select == 1:
            orig_password, encod_password = encode()
            print("Your password has been encoded and stored!", end='\n\n')
        if user_select == 2:
            print(f"The encoded password is {encod_password}, and the original password is {orig_password}.", end='\n\n')
        if user_select == 3:
            exit()


if __name__ == "__main__":
    main()