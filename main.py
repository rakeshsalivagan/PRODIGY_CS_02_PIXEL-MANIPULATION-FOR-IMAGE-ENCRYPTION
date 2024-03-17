from PIL import Image
import os

def encrypt_image(image_path, key, output_dir):
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
    encrypted_image_path = os.path.join(output_dir, os.path.splitext(os.path.basename(image_path))[0] + "_encrypted" + os.path.splitext(image_path)[1])
    img.save(encrypted_image_path)
    print("Image encrypted successfully!")

def decrypt_image(image_path, key, output_dir):
    # Open the encrypted image
    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size

    # Decrypt each pixel
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            r = (r - key + 256) % 256
            g = (g - key + 256) % 256
            b = (b - key + 256) % 256
            pixels[x, y] = (r, g, b)

    # Save the decrypted image
    decrypted_image_path = os.path.join(output_dir, os.path.splitext(os.path.basename(image_path))[0] + "_decrypted" + os.path.splitext(image_path)[1])
    img.save(decrypted_image_path)
    print("Image decrypted successfully!")

# Example usage
input_image_path = "C:/Users/Dhilipan/Pictures/ra.jpg"  # Change this to your input image path
output_dir = "C:/Users/Dhilipan/Documents/EncryptedImages"  # Change this to your desired output directory
key = 50

encrypt_image(input_image_path, key, output_dir)
decrypt_image(os.path.join(output_dir, os.path.basename(input_image_path) + "_encrypted.jpg"), key, output_dir)
