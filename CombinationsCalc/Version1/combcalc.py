# Import the required module
import string

def calculate_combinations(number_of_characters):
    """Calculate the number of possible combinations for a given number of characters."""
    characters = string.digits
    combinations = pow(len(characters), number_of_characters)
    return combinations

# Get the number of characters from the user
number_of_characters = int(input("Enter the number of characters: "))

# Calculate and display the number of possible combinations
combinations = calculate_combinations(number_of_characters)
print(f"The number of possible combinations is: {combinations}")