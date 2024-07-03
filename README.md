Image Encryption Project

This Python script allows you to encrypt and decrypt images using AES (Advanced Encryption Standard) in CBC (Cipher Block Chaining) mode. Below are the steps to use this program effectively.
Prerequisites

Ensure you have Python installed on your system. This script requires the following Python libraries, which can be installed via pip using the provided requirements.txt file:

bash

pip install -r requirements.txt

Usage Instructions

    Clone the Repository

    Clone or download the repository containing the Python script (Image_Encryption_Project.py) to your local machine.

    Install Required Libraries

    Install the necessary Python libraries by running the following command in your terminal or command prompt (ensure you're in the directory where requirements.txt is located):

    bash

pip install -r requirements.txt

Run the Script

Execute the script by running the following command:

bash

python Image_Encryption_Project.py

Menu Options

Upon running the script, you'll see a menu with the following options:

    Encrypt Image: Allows you to encrypt an image file. You'll be prompted to enter the name of the image file (including the file extension).

    Decrypt Image: Allows you to decrypt an encrypted image file. You'll be prompted to enter the name of the encrypted file (including the file extension).

    Exit: Terminates the program.

Encryption Process

When encrypting an image, the program will:

    Generate a random AES key.
    Read the image file specified.
    Encrypt the image using AES-CBC with the generated key.
    Save the encrypted image as [original_file_name].enc.

Decryption Process

When decrypting an encrypted image file, the program will:

    Read the encrypted file.
    Extract the initialization vector (IV) and ciphertext.
    Decrypt the ciphertext using the provided AES key and IV.
    Save the decrypted image as [original_encrypted_file_name].decrypted.png.

Exiting the Program

To exit the program, enter 0 when prompted for a choice in the menu.
