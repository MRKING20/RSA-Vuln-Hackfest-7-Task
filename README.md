# RSA-Vuln-Hackfest-Task-7
This is my first writeup about RSA Vuln a Cryptography task of Hackfest 7 CTF Qualification !!! Don't forget to give me feedback .

# Description of the task:

I found a broadcasted message encrypted using RSA and all i know that it uses exponent= 3 and i also find out the module used for for each message 
I kept it in ASCII for you 

'Encrypted Message ASCII '   => ' module used' : 

'411 312 216 512 419 140 77 46 216 209 77 312 380 426 77 380 525 122 126 430  449 140 209 559 426 430 1'    => module = '589'
'47 130 75 431 272 424 463 58 285 79 463 130 48 103 463 48 86 349 34 97 393 424 79 55 103 97 352' => module ='493'
'473 216 122 417 122 480 434 51 359 64 434 216 233 156 434 233 174 364 376 454 73 480 64 356 156 454 265' => module= '481'


I hope this helps you 
Good Luck !
Author: 𝕷a_3𝖋𝖚𝖋#5148

# Solution:

When I encountered the problem, I turned to ChatGPT for assistance, and it provided me with a more detailed explanation of the problem:

To decrypt the RSA-encrypted messages, you need to find the corresponding private keys for each message. In RSA, the private key consists of the modulus (module) and the private exponent (d). Since you know that the public exponent (e) used for encryption is 3, you can calculate the private exponent (d) using the Extended Euclidean Algorithm. Here's how you can decrypt the messages:

For the first encrypted message:

Encrypted Message ASCII: 411 312 216 512 419 140 77 46 216 209 77 312 380 426 77 380 525 122 126 430 449 140 209 559 426 430 1
Module (N): 589
To calculate the private exponent (d):

Find the value of φ(N) (Euler's totient function), where N is the module.
φ(N) = N - p - q + 1, where p and q are prime factors of N.
Since we don't know the prime factors directly, let's assume that N is a prime number.
Therefore, φ(N) = N - 1.

Calculate the value of d:
d = e^(-1) mod φ(N)
Here, e = 3.

Since N is a prime number (589), φ(N) = 588.
d = 3^(-1) mod 588

Using the Extended Euclidean Algorithm, we can find the modular inverse of 3 modulo 588.

Applying the algorithm:
588 = 3 × 196 + 0
3 = 0 × 3 + 3

Now, working backward:
3 = 588 - 3 × 196

Therefore, the modular inverse of 3 modulo 588 is -196 (or 392, which is the positive equivalent modulo 588 ). 

//However, to ensure a positive modular inverse, we can add the modulus (588) to the negative modular inverse (-196):

-196 + 588 = 392

Therefore, the modular inverse of 3 modulo 588 is 392.//


Now that we have the private exponent (d), we can decrypt the message using the formula: decrypted_message = encrypted_message^d mod N.

Decryption for the first message:

Convert the ASCII numbers back to integers: [411, 312, 216, 512, 419, 140, 77, 46, 216, 209, 77, 312, 380, 426, 77, 380, 525, 122, 126, 430, 449, 140, 209, 559, 426, 430, 1]
Decrypt each number using the formula: decrypted_number = encrypted_number^d mod N
For example, the first number:
decrypted_number = 411^392 mod 589

Repeat this step for each number in the encrypted message to get the decrypted message.

After reading this I ask one more time chatgpt to write a python script for me :

# Script 
```python
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
```
# Finally the flag is 

Hackfest{rsa_4s_Vu3lnerb4l}
