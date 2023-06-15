import string

def decrypt_rsa(encrypted_message, module):
    # Convert the ASCII numbers to integers
    encrypted_numbers = list(map(int, encrypted_message.split()))

    # Try all possible values for the private exponent (d)
    for d in range(1, module):
        decrypted_message = ''
        for number in encrypted_numbers:
            decrypted_number = pow(number, d, module)
            decrypted_message += chr(decrypted_number)
            
        # Check if the decrypted message contains only printable ASCII characters
        if all(char in string.printable for char in decrypted_message):
            return decrypted_message,d

    return None

# Encrypted messages and their corresponding modules
encrypted_messages = [
    ('411 312 216 512 419 140 77 46 216 209 77 312 380 426 77 380 525 122 126 430 449 140 209 559 426 430 1', 589),
    ('47 130 75 431 272 424 463 58 285 79 463 130 48 103 463 48 86 349 34 97 393 424 79 55 103 97 352', 493),
    ('473 216 122 417 122 480 434 51 359 64 434 216 233 156 434 233 174 364 376 454 73 480 64 356 156 454 265', 481)
]

# Decrypt and print each message
for encrypted_message, module in encrypted_messages:
    decrypted_message = decrypt_rsa(encrypted_message, module)
    if decrypted_message:
        print(f"Decrypted Message: {decrypted_message}")
    else:
        print("Decryption failed for the given modulus.")
