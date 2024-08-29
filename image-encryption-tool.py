from PIL import Image
import os

def encrypt_decrypt_image(input_path, output_path, key):
    # Open the image
    with Image.open(input_path) as img:
        # Convert image to RGB if it's not already
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        # Get the dimensions of the image
        width, height = img.size
        
        # Create a new image for the result
        encrypted_img = Image.new('RGB', (width, height))
        
        # Iterate through each pixel
        for x in range(width):
            for y in range(height):
                # Get the RGB values of the pixel
                r, g, b = img.getpixel((x, y))
                
                # XOR each color channel with the key
                er = r ^ key
                eg = g ^ key
                eb = b ^ key
                
                # Set the encrypted/decrypted pixel in the new image
                encrypted_img.putpixel((x, y), (er, eg, eb))
        
        # Save the result
        encrypted_img.save(output_path)

def main():
    while True:
        print("\nSimple Image Encryption Tool")
        print("1. Encrypt an image")
        print("2. Decrypt an image")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '3':
            print("Thank you for using the Image Encryption Tool. Goodbye!")
            break
        
        if choice not in ['1', '2']:
            print("Invalid choice. Please try again.")
            continue
        
        input_path = input("Enter the path to the input image: ")
        if not os.path.exists(input_path):
            print("Input file does not exist. Please check the path and try again.")
            continue
        
        output_path = input("Enter the path for the output image: ")
        
        try:
            key = int(input("Enter an encryption/decryption key (integer between 0-255): "))
            if key < 0 or key > 255:
                raise ValueError
        except ValueError:
            print("Invalid key. Please enter an integer between 0 and 255.")
            continue
        
        operation = "Encrypting" if choice == '1' else "Decrypting"
        print(f"{operation} the image...")
        
        try:
            encrypt_decrypt_image(input_path, output_path, key)
            print(f"Image successfully {operation.lower()}ed and saved to {output_path}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
