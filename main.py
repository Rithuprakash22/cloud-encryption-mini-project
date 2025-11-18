from cryptography.fernet import Fernet

# --------- KEY MANAGEMENT ---------
def generate_key():
    """
    Generates a secret key and saves it into a file.
    """
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved as secret.key")


def load_key():
    """
    Loads the secret key from the current directory named `secret.key`.
    """
    with open("secret.key", "rb") as key_file:
        key = key_file.read()
    return key


# --------- ENCRYPTION / DECRYPTION ---------
def encrypt_file(filename):
    key = load_key()
    f = Fernet(key)

    with open(filename, "rb") as file:
        data = file.read()

    encrypted_data = f.encrypt(data)

    encrypted_filename = filename + ".enc"
    with open(encrypted_filename, "wb") as file:
        file.write(encrypted_data)

    print(f"Encrypted file saved as: {encrypted_filename}")


def decrypt_file(encrypted_filename, output_filename):
    key = load_key()
    f = Fernet(key)

    with open(encrypted_filename, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = f.decrypt(encrypted_data)

    with open(output_filename, "wb") as file:
        file.write(decrypted_data)

    print(f"Decrypted file saved as: {output_filename}")


# --------- SIMPLE MENU ---------
if __name__ == "__main__":
    print("=== Cloud Encryption Mini Project ===")
    print("1. Generate key (do this once)")
    print("2. Encrypt a file before uploading to cloud")
    print("3. Decrypt a downloaded file from cloud")

    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        generate_key()

    elif choice == "2":
        filename = input("Enter file name (with extension, example: report.pdf): ")
        encrypt_file(filename)

    elif choice == "3":
        enc_name = input("Enter encrypted file name (example: report.pdf.enc): ")
        out_name = input("Enter name for decrypted file (example: report_decrypted.pdf): ")
        decrypt_file(enc_name, out_name)

    else:
        print("Invalid choice")
