from PIL import Image

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    width, height = img.size
    encrypted_pixels = []

    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            encrypted_pixel = tuple((p + key) % 256 for p in pixel)
            encrypted_pixels.append(encrypted_pixel)

    encrypted_img = Image.new(img.mode, img.size)
    encrypted_img.putdata(encrypted_pixels)
    encrypted_output_path = "encrypted_image.png"
    encrypted_img.save(encrypted_output_path)
    print("Image encrypted successfully! Encrypted image saved at:", encrypted_output_path)

def decrypt_image(encrypted_image_path, key):
    encrypted_img = Image.open(encrypted_image_path)
    width, height = encrypted_img.size
    decrypted_pixels = []

    for y in range(height):
        for x in range(width):
            encrypted_pixel = encrypted_img.getpixel((x, y))
            decrypted_pixel = tuple((p - key) % 256 for p in encrypted_pixel)
            decrypted_pixels.append(decrypted_pixel)

    decrypted_img = Image.new(encrypted_img.mode, encrypted_img.size)
    decrypted_img.putdata(decrypted_pixels)
    decrypted_output_path = "decrypted_image.png"
    decrypted_img.save(decrypted_output_path)
    print("Image decrypted successfully! Decrypted image saved at:", decrypted_output_path)

# Example usage
image_path = "C:/Users/Dhilipan/Pictures/ra.jpg"
encryption_key = 50

encrypt_image(image_path, encryption_key)
decrypt_image("encrypted_image.png", encryption_key)
