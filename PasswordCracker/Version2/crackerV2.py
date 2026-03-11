#
#
# THIS VERSION ONLY WORKS WITH NUMBERS!!!!
#
#


#libraries needed
import hashlib
import time
import itertools
import random


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
def crack_password(sha_hash, password_length, hash_func):

    start_time = time.time()
    attempts = 0
    digits = list(range(10))
    for _ in range(password_length):
        random.shuffle(digits)
        for attempt in itertools.product(digits, repeat=password_length):
            attempts += 1
            password = ''.join(map(str, attempt))

            #if password is guessed right, print the password, time it took and number of attempts it took
            if hash_func(password.encode()).hexdigest() == sha_hash:
                end_time = time.time()
                return password, end_time - start_time, attempts
            
            #notify user for evey 100k attempts made
            if attempts % 100000 == 0:
                print(f"Tried {attempts:,} combinations".replace(",", "."))
    return None, None, attempts



#main function that starts everything and gets informations needed from user
def main():
    sha_type = input("Enter the type of SHA hash (SHA-1, SHA-256, or SHA-512): ")
    sha_hash = input("Enter the SHA hash of the password: ")
    password_length = int(input("Enter the length of the password (max 25): "))

    hash_func = get_hash_function(sha_type)
    password, crack_time, attempts = crack_password(sha_hash, password_length, hash_func)

    if password:
        print(f"~~~~~Password successfully cracked")
        print(f"~~~~~Password was: {password}")
        print(f"~~~~~Time it took to crack: {crack_time:.10f} seconds")
        print(f"~~~~~Time it took to crack: {int(crack_time // 60)} minutes and {crack_time % 60:.2f} seconds")
        print(f"~~~~~Number of combinations tried: {attempts:,}".replace(",", "."))
    else:
        print("~~~~~Failed to crack the password")
        print(f"~~~~~Time spend trying: {crack_time:.10f} seconds")
        print(f"~~~~~Number of combinations tried: {attempts:,}".replace(",", "."))




if __name__ == "__main__":
    main()
