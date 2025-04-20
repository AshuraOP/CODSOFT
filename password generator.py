import random
import string


def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars):

    character_pool = ''
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_numbers:
        character_pool += string.digits
    if use_special_chars:
        character_pool += string.punctuation


    if not character_pool:
        raise ValueError("No character types selected. Please enable at least one character type.")


    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password


def main():
    try:

        length = int(input("Enter the desired length for the password: "))
        if length < 1:
            print("Password length must be at least 1.")
            return

        use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        use_lowercase = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
        use_special_chars = input("Include special characters? (y/n): ").strip().lower() == 'y'


        try:
            # Generate password
            password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars)
            print(f"Generated Password: {password}")
        except ValueError as e:
            print(e)

    except ValueError:
        print("Invalid input. Please enter a valid number for the password length.")


if __name__ == "__main__":
    main()