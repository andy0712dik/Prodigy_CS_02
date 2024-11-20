# Prodigy_CS_02

# **Image Encryption and Decryption Tool**

A Python-based tool for simple image encryption and decryption using the XOR operation. This script allows you to securely encrypt an image file using a user-defined key and later decrypt it using the same key.

---

## **Features**
- Encrypt and decrypt image files using XOR operations.  
- Supports color images in **RGB** format.  
- Easy-to-use interactive command-line interface.  
- Ensures that the original image can be fully restored using the same key.  

---

## **Prerequisites**
Before running the script, ensure you have the following installed:
- **Python 3.6 or later**
- **Pillow** library (`pip install pillow`)
- **NumPy** library (`pip install numpy`)

---

## **Usage**
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/image-encryption-tool.git
   ```
2. Navigate to the project directory:
   ```bash
   cd image-encryption-tool
   ```
3. Run the script:
   ```bash
   python encrypt_decrypt_image.py
   ```
4. Follow the prompts:
   - Provide the path to the input image.
   - Specify the output path for the encrypted/decrypted image.
   - Enter an encryption key (integer between 0 and 255).

---

## **How It Works**
1. **Encryption/Decryption**:
   - The script applies the XOR operation (`^`) between the image pixel values and the encryption key.
   - The same key can be used to decrypt the encrypted image back to its original form.

2. **Key Restrictions**:
   - The encryption key must be an integer between 0 and 255 to ensure compatibility with RGB pixel values.

3. **Image Support**:
   - Supports any image format that can be opened by the `Pillow` library and converts it to **RGB**.

---

## **Example**
**Input Image**: `input_image.jpg`  
**Output (Encrypted)**: `encrypted_image.jpg`  
**Output (Decrypted)**: `decrypted_image.jpg`

Encryption key: `123`

---

## **Error Handling**
The script includes basic error handling for:
- Invalid file paths.
- Unsupported file formats.
- Out-of-range or invalid encryption keys.


## **Contributions**
Contributions are welcome! If you encounter issues or have ideas for improvement, feel free to open an issue or submit a pull request.
