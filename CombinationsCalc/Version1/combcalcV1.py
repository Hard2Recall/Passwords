import string


#function that calulates number of possible combinations using only number variations
def calculate_combinations(number_of_characters):
    characters = string.digits
    combinations = pow(len(characters), number_of_characters)
    return combinations


number_of_characters = int(input("Enter the number of characters: ")) #ask the user for number of characters


combinations = calculate_combinations(number_of_characters) #does the calculation
print(f"The number of possible combinations is: {combinations:,}".replace(",", ".")) #prints the result