from PIL import Image
import numpy as np

def encrypt_decrypt_image(input_image_path, output_image_path, key=123):
    try:
        # Open the image and convert it to RGB format
        image = Image.open(input_image_path)
        image = image.convert('RGB')
        
        # Convert the image to a numpy array
        image_data = np.array(image, dtype=np.uint8)

        # Encrypt/Decrypt by applying XOR operation with the key
        encrypted_data = image_data ^ key
        
        # Convert the modified data back to an image
        encrypted_image = Image.fromarray(encrypted_data, 'RGB')

        # Save the new image
        encrypted_image.save(output_image_path)
        print(f"Image saved as {output_image_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print("Simple Image Encryption/Decryption Tool")
    
    # Get the user input for file paths and operation
    input_path = input("Enter the path to the input image: ")
    output_path = input("Enter the path to save the output image: ")
    try:
        key = int(input("Enter the encryption key (integer between 0 and 255): "))
        if not (0 <= key <= 255):
            raise ValueError("Key must be an integer between 0 and 255.")
    except ValueError as ve:
        print(f"Invalid key: {ve}")
        return
    
    # Run the encryption/decryption process
    encrypt_decrypt_image(input_path, output_path, key)
    print("Process completed!")

if __name__ == "__main__":
    main()
