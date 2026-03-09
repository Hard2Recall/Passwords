import hashlib
import time
import itertools

def get_hash_function(sha_type):

    if sha_type == "SHA-1":
        return hashlib.sha1
    elif sha_type == "SHA-256":
        return hashlib.sha256
    elif sha_type == "SHA-512":
        return hashlib.sha512
    else:
        raise ValueError("Invalid SHA type")

def crack_password(sha_hash, password_length, hash_func, char_set):

    start_time = time.time()
    attempts = 0
    for attempt in itertools.product(char_set, repeat=password_length):
        attempts += 1
        password = ''.join(attempt)
        if hash_func(password.encode()).hexdigest() == sha_hash:
            end_time = time.time()
            return password, end_time - start_time, attempts
        if attempts % 1000000 == 0:
            print_progress(attempts)
    return None, None, attempts

def print_progress(attempts):

    print(f"Tried {attempts} combinations")

def main():
    sha_type = input("Enter the type of SHA hash (SHA-1, SHA-256, or SHA-512): ")
    sha_hash = input("Enter the SHA hash of the password: ")
    password_length = int(input("Enter the length of the password (max 25): "))

    print("Choose character set:")
    print("1. Only numbers")
    print("2. Only lowercase letters")
    print("3. Mix of numbers and lowercase letters")
    print("4. Mix of numbers, lowercase and uppercase letters")
    print("5. Mix of numbers and uppercase letters")
    print("6. Mix of lowercase and uppercase letters")
    char_set_choice = int(input("Enter your choice (1-6): "))

    if char_set_choice == 1:
        char_set = '0123456789'
    elif char_set_choice == 2:
        char_set = 'abcdefghijklmnopqrstuvwxyz'
    elif char_set_choice == 3:
        char_set = '0123456789abcdefghijklmnopqrstuvwxyz'
    elif char_set_choice == 4:
        char_set = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    elif char_set_choice == 5:
        char_set = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    elif char_set_choice == 6:
        char_set = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    else:
        raise ValueError("Invalid character set choice")

    hash_func = get_hash_function(sha_type)
    password, crack_time, attempts = crack_password(sha_hash, password_length, hash_func, char_set)

    if password:
        print(f"~~~~~Password successfully cracked")
        print(f"~~~~~Password was: {password}")
        print(f"~~~~~Time it took to crack: {crack_time:.10f} seconds")
        print(f"~~~~~Time it took to crack: {int(crack_time // 60)} minutes and {crack_time % 60:.2f} seconds")
        print(f"~~~~~Number of combinations tried: {attempts}")
    else:
        print("~~~~~Failed to crack the password")
        print(f"~~~~~Time spend trying: {crack_time:.10f} seconds")
        print(f"~~~~~Number of combinations tried: {attempts}")

if __name__ == "__main__":
    main()