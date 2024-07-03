import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from PIL import Image
import io

def encrypt_image(file_name, key):
    cipher = AES.new(key, AES.MODE_CBC)
    img = Image.open(file_name)
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    ct_bytes = cipher.encrypt(pad(img_byte_arr, AES.block_size))
    with open(file_name + '.enc', 'wb') as f:
        f.write(cipher.iv)
        f.write(ct_bytes)
    print("Image encrypted and saved as " + file_name + '.enc')

def decrypt_image(file_name, key):
    with open(file_name, 'rb') as f:
        iv = f.read(16)
        ct = f.read()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    img_byte_arr = unpad(cipher.decrypt(ct), AES.block_size)
    img = Image.open(io.BytesIO(img_byte_arr))
    decrypted_file_name = file_name.rsplit('.', 1)[0] + '.decrypted.png'
    img.save(decrypted_file_name)
    print("Image decrypted and saved as " + decrypted_file_name)

def main():
    key = get_random_bytes(16)  # AES-128
    while True:
        print("\nMenu:")
        print("1. Encrypt Image")
        print("2. Decrypt Image")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            file_name = input("Enter the image file name to encrypt: ")
            encrypt_image(file_name, key)
        elif choice == '2':
            file_name = input("Enter the encrypted file name to decrypt: ")
            decrypt_image(file_name, key)
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()