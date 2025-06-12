from cryptography.fernet import Fernet
import os

KEY_FILE = "logs/secret.key"
LOG_FILE = "logs/command_log.json"

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)

def load_key():
    if not os.path.exists(KEY_FILE):
        generate_key()
    with open(KEY_FILE, "rb") as f:
        return f.read()

def encrypt_log():
    key = load_key()
    fernet = Fernet(key)

    with open(LOG_FILE, "rb") as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(LOG_FILE, "wb") as encrypted_file:
        encrypted_file.write(encrypted)

def decrypt_log():
    key = load_key()
    fernet = Fernet(key)

    with open(LOG_FILE, "rb") as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)

    with open(LOG_FILE, "wb") as dec_file:
        dec_file.write(decrypted)
