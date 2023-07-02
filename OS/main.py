from cryptography.fernet import Fernet
import os


def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()
        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(data)

    with open(file_path + '.encrypted', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

    os.remove(file_path)  # Delete the original file


def decrypt_file(file_path, key):
    with open(file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()

    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)

    with open(file_path[:-10], 'wb') as decrypted_file:  # Remove the '.encrypted' extension
        decrypted_file.write(decrypted_data)

    os.remove(file_path)  # Delete the encrypted file


def encrypt_directory(directory_path, key):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file != 'jeff.txt':
                file_path = os.path.join(root, file)
                encrypt_file(file_path, key)


def decrypt_directory(directory_path, key):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.encrypted'):
                file_path = os.path.join(root, file)
                decrypt_file(file_path, key)


# Load the key from the file
#CREATE A KEY FIRST
with open("jeff.txt", 'rb') as f:
    key = f.read()

# Directory path to encrypt or decrypt
directory_path = 'jeff'

# Encrypt or decrypt the directory
if input("Encrypt: ") == "y":
    encrypt_directory(directory_path, key)

if input("Decrypt: ") == "y":
    decrypt_directory(directory_path, key)
