import random
import string

def generate_password(length, use_uppercase=True, use_numbers=True, use_special=True):
    # Define possible character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Create a pool of characters based on user selection
    char_pool = lowercase
    if use_uppercase:
        char_pool += uppercase
    if use_numbers:
        char_pool += digits
    if use_special:
        char_pool += special_characters

    # Generate a random password
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")

    # Get the password length from the user
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length < 6:  # Common practice to recommend at least 6 characters
                print("Password length should be at least 6 characters.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    # Ask for options on what to include in the password
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    # Generate the password
    password = generate_password(length, use_uppercase, use_numbers, use_special)

    # Display the password
    print("\nGenerated Password:", password)

if __name__ == "__main__":
    main()
