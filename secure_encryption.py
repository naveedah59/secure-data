from cryptography.fernet import Fernet

# Function to generate and save a key


def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("✅ Key generated and saved to secret.key")

# Function to load the key


def load_key():
    with open("secret.key", "rb") as key_file:
        return key_file.read()

# Function to encrypt a message


def encrypt_message(message):
    key = load_key()
    f = Fernet(key)
    encrypted = f.encrypt(message.encode())
    print("🔐 Encrypted message:")
    print(encrypted.decode())

# Function to decrypt a message


def decrypt_message(encrypted_message):
    key = load_key()
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_message.encode())
    print("🔓 Decrypted message:")
    print(decrypted.decode())

# Main menu


def main():
    while True:
        print("\n=== Secure Data Encryption ===")
        print("1. Generate Key")
        print("2. Encrypt Message")
        print("3. Decrypt Message")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            generate_key()
        elif choice == '2':
            message = input("Enter the message to encrypt: ")
            encrypt_message(message)
        elif choice == '3':
            encrypted_message = input("Enter the encrypted message: ")
            decrypt_message(encrypted_message)
        elif choice == '4':
            print("Goodbye! 🔐")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
