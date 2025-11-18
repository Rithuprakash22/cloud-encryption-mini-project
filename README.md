# Cloud Data Security using AES Encryption

This mini project demonstrates secure file storage using AES-based encryption.
The user encrypts a file locally, uploads it to cloud storage (Google Drive), 
and later downloads and decrypts it safely.

## Features
- AES (Fernet) symmetric key encryption
- Local file protection
- Secure cloud upload (Google Drive)
- Cloud download + decryption
- Simple Python CLI app

## How it works
1. Generate a secret key (`secret.key`)
2. Encrypt any file (e.g., PDF, image, text)
3. Upload the encrypted file (`*.enc`) to Google Drive
4. Download it back
5. Decrypt the file to restore the original

## How to run
