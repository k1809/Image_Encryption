# Image Encryption Project

This Python script allows you to encrypt and decrypt images using AES (Advanced Encryption Standard) in CBC (Cipher Block Chaining) mode.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Ensure you have Python installed on your system. This script requires the following Python libraries, which can be installed via `pip`:

```bash
pip install -r requirements.txt
```

### Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/k1809/Image_Encryption.git
cd Image_Encryption
pip install -r requirements.txt
```

### Usage

Run the script and follow the on-screen menu:

```bash
python Image_Encryption_Project.py
```

### Menu Options

- **Encrypt Image**: Encrypts an image file specified by the user.
- **Decrypt Image**: Decrypts an encrypted image file specified by the user.
- **Exit**: Terminates the program.

### Encryption Process

- Generates a random AES key.
- Reads the specified image file.
- Encrypts the image using AES-CBC with the generated key.
- Saves the encrypted image as `[original_file_name].enc`.

### Decryption Process

- Reads an encrypted image file.
- Extracts the initialization vector (IV) and ciphertext.
- Decrypts the ciphertext using the provided AES key and IV.
- Saves the decrypted image as `[original_encrypted_file_name].decrypted.png`.

## Authors

- [Karthik Krishnan D](https://github.com/k1809)
