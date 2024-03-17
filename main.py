from PIL import Image
import os

def encrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size

    # Encrypt each pixel
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256
            pixels[x, y] = (r, g, b)

    # Save the encrypted image
    encrypted_image_path = os.path.splitext(image_path)[0] + "_encrypted" + os.path.splitext(image_path)[1]
    img.save(encrypted_image_path)
    print("Image encrypted successfully!")

def decrypt_image(image_path, key):
    # Open the encrypted image
    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size

    # Decrypt each pixel
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256
            pixels[x, y] = (r, g, b)

    # Save the decrypted image
    decrypted_image_path = os.path.splitext(image_path)[0] + "_decrypted" + os.path.splitext(image_path)[1]
    img.save(decrypted_image_path)
    print("Image decrypted successfully!")

# Example usage
image_path = "C:/Users/Dhilipan/Pictures/ra.jpg"  # Change this to your image path
key = 50

encrypt_image(image_path, key)
decrypt_image(os.path.splitext(image_path)[0] + "_encrypted.jpg", key)
