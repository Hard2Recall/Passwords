#libraries needed
import hashlib
import time
import itertools
import string



#function that gets SHA hash type
def get_hash_function(sha_type):

    if sha_type == "SHA-1":
        return hashlib.sha1
    elif sha_type == "SHA-256":
        return hashlib.sha256
    elif sha_type == "SHA-512":
        return hashlib.sha512
    else:
        raise ValueError("Invalid SHA type")



#function that does bruteforcing
def crack_password(sha_hash, password_length, hash_func, char_set):

    start_time = time.time()
    attempts = 0
    for attempt in itertools.product(char_set, repeat=password_length):
        attempts += 1
        password = ''.join(attempt)

         #if password is guessed right, print the password, time it took and number of attempts it took
        if hash_func(password.encode()).hexdigest() == sha_hash:
            end_time = time.time()
            return password, end_time - start_time, attempts
        
        #notify user for evey milion attempts made
        if attempts % 1000000 == 0:
            print(f"Tried {attempts:,} combinations".replace(",", "."))
    return None, None, attempts


#main function that starts everything and gets informations needed from user
def main():
    sha_type = input("Enter the type of SHA hash (SHA-1, SHA-256, or SHA-512): ")
    sha_hash = input("Enter the SHA hash of the password: ")
    password_length = int(input("Enter the length of the password (max 25): "))

    #function that defines character combinations and pre determened sets
    def calculate_combinations(number_of_characters, character_set):
        if character_set == 1:
            characters = string.digits
        elif character_set == 2:
            characters = string.ascii_lowercase
        elif character_set == 3:
            characters = string.ascii_uppercase
        elif character_set == 4:
            characters = string.digits + string.ascii_lowercase
        elif character_set == 5:
            characters = string.digits + string.ascii_uppercase
        elif character_set == 6:
            characters = string.ascii_lowercase + string.ascii_uppercase
        elif character_set == 7:
            characters = string.digits + string.ascii_lowercase + string.ascii_uppercase
        else:
            print("Invalid character set choice. Exiting.")
            return None
        return characters
    
    #chosing the character set
    print("Choose character set:")
    print("1. Only numbers")
    print("2. Only lowercase letters")
    print("3. Only uppercase letters")
    print("4. Mix of numbers and lowercase letters")
    print("5. Mix of numbers and uppercase letters")
    print("6. Mix of lowercase and uppercase letters")
    print("7. Mix of numbers, lowercase and uppercase letters")
    character_set_choice = int(input("Enter your choice (1-7): "))

    char_set = calculate_combinations(password_length, character_set_choice)
    
    hash_func = get_hash_function(sha_type)
    password, crack_time, attempts = crack_password(sha_hash, password_length, hash_func, char_set)


    #if password is corectly guessed prints this informations
    if password:
        print(f"~~~~~Password successfully cracked")
        print(f"~~~~~Password was: {password}")
        print(f"~~~~~Time it took to crack: {crack_time:.2f} seconds")
        print(f"~~~~~Time it took to crack: {int(crack_time // 60)} minutes and {crack_time % 60:.2f} seconds")
        print(f"~~~~~Number of combinations tried: {attempts:,}".replace(",", "."))

    #if we fail to guess the password print this information
    else:
        print("~~~~~Failed to crack the password")
        print(f"~~~~~Time spend trying: {crack_time:.2f} seconds")
        print(f"~~~~~Number of combinations tried: {attempts:,}".replace(",", "."))

if __name__ == "__main__":
    main()