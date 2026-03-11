#library needed
import hashlib


password = input("Enter your password: ")

# Generates SHA-1 hash for your password
hash_obj = hashlib.sha1()
hash_obj.update(password.encode())
sha1_hash = hash_obj.hexdigest()

# Generates SHA-256 hash for your password
hash_obj = hashlib.sha256()
hash_obj.update(password.encode())
sha256_hash = hash_obj.hexdigest()

# Generates SHA-512 hash for your password
hash_obj = hashlib.sha512()
hash_obj.update(password.encode())
sha512_hash = hash_obj.hexdigest()

# Print the corresponding SHA hashes of the password
print(f"Your SHA-1 hash is: {sha1_hash}")
print(f"Your SHA-256 hash is: {sha256_hash}")
print(f"Your SHA-512 hash is: {sha512_hash}")