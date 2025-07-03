def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    for char in text:
        if char.isalpha():
            # Shift within alphabet range
            base = ord('A') if char.isupper() else ord('a')
            if mode == 'encrypt':
                result += chr((ord(char) - base + shift) % 26 + base)
            elif mode == 'decrypt':
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char  # Keep special characters unchanged
    return result

# User input
message = input("Enter your message: ")
shift = int(input("Enter shift value (e.g. 3): "))

# Encrypt
encrypted = caesar_cipher(message, shift, mode='encrypt')
print("Encrypted message:", encrypted)

# Decrypt
decrypted = caesar_cipher(encrypted, shift, mode='decrypt')
print("Decrypted message:", decrypted)
