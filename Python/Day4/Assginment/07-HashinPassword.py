import hashlib
import os

def hash_password(password, salt=None):
    salt = salt or os.urandom(16)
    hashed = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return salt, hashed

def verify_password(salt, hashed, password):
    return hashed == hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)

# Example usage
if __name__ == "__main__":
    password = "my_secure_password"
    salt, hashed = hash_password(password)
    print(f"Salt: {salt.hex()}\nHashed: {hashed.hex()}")

    input_password = input("Enter password: ")
    print("Password correct!" if verify_password(salt, hashed, input_password) else "Password incorrect!")