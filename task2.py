from PIL import Image  # type: ignore
import numpy as np  # type: ignore

def encrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    pixels = image.load()

    width, height = image.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            # Simple XOR operation with the key (you can replace this with a more secure encryption method)
            encrypted_r = r ^ key
            encrypted_g = g ^ key
            encrypted_b = b ^ key

            encrypted_pixels = (encrypted_r, encrypted_g, encrypted_b)
            pixels[i, j] = encrypted_pixels

    image.save(output_path)
    print("Image Encrypted Successfully")


def decrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    pixels = image.load()

    width, height = image.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            # Simple XOR operation with the key (you can replace this with a more secure decryption method)
            decrypted_r = r ^ key
            decrypted_g = g ^ key
            decrypted_b = b ^ key

            decrypted_pixels = (decrypted_r, decrypted_g, decrypted_b)
            pixels[i, j] = decrypted_pixels

    image.save(output_path)
    print("Image Decrypted Successfully")


input_image = r"C:/Users/preci\Desktop/Internship/img.jpg"
encrypted_image = r"C:/Users/preci\Desktop/Internship/encrypted_img.jpg"
decrypted_image = r"C:/Users/preci\Desktop/Internship/decrypted_img.jpg"

key = 123  # Replace with a secure key

encrypt_image(input_image, encrypted_image, key)
decrypt_image(encrypted_image, decrypted_image, key)