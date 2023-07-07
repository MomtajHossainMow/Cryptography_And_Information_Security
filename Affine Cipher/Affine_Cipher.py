# Encryption Function
def encryption(plaintext, key1, key2):
    ciphertext = ""
    # This for loop is for the traversing the text.
    for i in range(len(plaintext)):
        char = plaintext[i]
        # This condition is for keeping the "space" same on the cipher text.
        if char == " ":
            ciphertext = ciphertext + char
        # Ascii value of upper case letters start from 65.
        elif char.isupper():
            ciphertext = ciphertext + chr(
                ((((ord(char) - 65) * key1) + key2) % 26) + 65
            )
        # Ascii value of lower case letters start from 97.
        else:
            ciphertext = ciphertext + chr(
                ((((ord(char) - 97) * key1) + key2) % 26) + 97
            )
    return ciphertext


# Decryption Function
def decryption(ciphertext, key1, key2):
    plaintext = ""
    # Finding the multiplicative inverse of key1
    mi = pow(key1, -1, 26)
    # This for loop is for the traverse the text.
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        # This condition is for keeping the "space" same on the plaintext.
        if char == " ":
            plaintext = plaintext + char
        # Ascii value of upper case letters start from 65.
        elif char.isupper():
            plaintext = plaintext + chr(((((ord(char) - 65) - key2) * mi) % 26) + 65)
        # Ascii value of lower case letters start from 97.
        else:
            plaintext = plaintext + chr(((((ord(char) - 97) - key2) * mi) % 26) + 97)
    return plaintext


input = open("F:\Python 2023\CIS Lab\Affine Cipher\input.txt", "r+")
output = open("F:\Python 2023\CIS Lab\Affine Cipher\output.txt", "w")
plaintext = input.read()
key1 = 7
key2 = 2
ciphertext = encryption(plaintext, key1, key2)
decodedtext = decryption(ciphertext, key1, key2)
output.write("Given plaintext is: " + plaintext + "\n")
output.write("Encrypted text is: " + ciphertext.upper() + "\n")
output.write("Decrypted text is: " + decodedtext.lower() + "\n")
# This line is for the truncating the file.
input.truncate(0)
# This line is for the closing the files.
input.close()
output.close()
