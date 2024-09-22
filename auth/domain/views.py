from cryptography.fernet import Fernet
from auth.settings import SECRET_KEY

key = Fernet.generate_key()

def encrypt_password(password):
    fernet = Fernet(SECRET_KEY)
    return fernet.encrypt(password.encode())

def decrypt_password(encrypted_password):
    fernet = Fernet(SECRET_KEY)
    return fernet.decrypt(encrypted_password.encode()).decode()




