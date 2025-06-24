import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def load_key():
    return open("key.key", 'rb').read()  # This returns a salt


def generate_fernet_key(master_pwd: str):
    salt = load_key()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(master_pwd.encode()))
    return Fernet(key)


# Run this once to generate the key.key file
def write_key():
    salt = os.urandom(16)
    with open("key.key", 'wb') as f:
        f.write(salt)


# Run this once manually before first run if key.key doesn't exist
if not os.path.exists("key.key"):
    write_key()


# Main Logic
master_pwd = input("What is the master password? ")
fer = generate_fernet_key(master_pwd)

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            try:
                decrypted = fer.decrypt(passw.encode()).decode()
                print("User:", user, "| Password:", decrypted)
            except:
                print("Could not decrypt for user:", user)

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    encrypted = fer.encrypt(pwd.encode()).decode()
    with open("passwords.txt", "a") as f:
        f.write(name + "|" + encrypted + "\n")


while True:
    mode = input("Would you like to add, view, or press quit? ").lower()
    if mode == "quit":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
