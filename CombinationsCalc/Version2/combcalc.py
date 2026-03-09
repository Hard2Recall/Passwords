# Import the required module
import string

def calculate_combinations(number_of_characters, character_set):
    """Calculate the number of possible combinations for a given number of characters and character set."""
    if character_set == 1:
        characters = string.digits
    elif character_set == 2:
        characters = string.ascii_lowercase
    elif character_set == 3:
        characters = string.digits + string.ascii_lowercase
    elif character_set == 4:
        characters = string.digits + string.ascii_lowercase + string.ascii_uppercase
    elif character_set == 5:
        characters = string.digits + string.ascii_uppercase
    elif character_set == 6:
        characters = string.ascii_lowercase + string.ascii_uppercase
    else:
        print("Invalid character set choice. Exiting.")
        return None

    combinations = pow(len(characters), number_of_characters)
    return combinations

# Get the character set choice from the user
print("Choose character set:")
print("1. Only numbers")
print("2. Only lowercase letters")
print("3. Mix of numbers and lowercase letters")
print("4. Mix of numbers, lowercase and uppercase letters")
print("5. Mix of numbers and uppercase letters")
print("6. Mix of lowercase and uppercase letters")
char_set_choice = int(input("Enter your choice (1-6): "))

# Get the number of characters from the user
number_of_characters = int(input("Enter the number of characters: "))

# Calculate and display the number of possible combinations
combinations = calculate_combinations(number_of_characters, char_set_choice)
if combinations is not None:
    print(f"The number of possible combinations is: {combinations}")