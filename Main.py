import secrets
import string

############### CODE BEGINS ###################

# defining inputs for password
lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation
final_combined_password = lower + upper + digits + symbols

# password generator function
def password_generator(length_of_password, difficulty):
    password = "".join(
        secrets.choice(password_difficulty(difficulty))
        for i in range(length_of_password)
    )
    return password


# function for calculating difficulty of the password
def password_difficulty(difficulty):
    if difficulty == 1:
        combined_password = lower + upper
    elif difficulty == 2:
        combined_password = lower + upper + digits
    elif difficulty == 3:
        combined_password = lower + upper + symbols
    elif difficulty == 4:
        combined_password = lower + symbols + digits
    elif difficulty == 5:
        combined_password = lower + upper + digits + symbols
    return combined_password


def main():

    try:
        # length for password
        length_of_password = int(input("Enter length of password : "))

        # difficulty for password
        difficulty = int(input("Enter password security level (1-5) : "))

        # printing password
        print("-" * 70)
        print(password_generator(length_of_password, difficulty))
        print("-" * 70)

    except ValueError:
        print("Invalid input.")


if __name__ == "__main__":
    main()


############### CODE ENDS ###################
