# Fuction for generating the keystream
def generateKeyStream(plainText, key):
    result = key
    for i in range(len(plainText) - 1):
        result = result + plainText[i]
    return result


# Encryption function
def encrypt(message, key):
    ciphertext = ""
    for i in range(len(message)):
        messageChar = message[i]
        keyStreamChar = key[i]
        # Main formula: cipherText = (plainText + keyStream) mod 26
        if messageChar.isupper():
            ciphertext = ciphertext + chr(
                ((ord(messageChar) - 65) + (ord(keyStreamChar) - 65)) % 26 + 65
            )
        elif messageChar.islower():
            ciphertext = ciphertext + chr(
                ((ord(messageChar) - 97) + (ord(keyStreamChar) - 97)) % 26 + 97
            )
        else:  # If we have space as character, then just concatenate it
            ciphertext = ciphertext + messageChar
    return ciphertext


# Decryption function
def decrypt(message, key):
    plaintext = ""
    for i in range(len(message)):
        messageChar = message[i]
        keyStreamChar = key[i]
        # Main formula: plainText = (cipherText - keyStream) mod 26
        if messageChar.isupper():
            plaintext = plaintext + chr(
                ((ord(messageChar) - 65) - (ord(keyStreamChar) - 65)) % 26 + 65
            )
        elif messageChar.islower():
            plaintext = plaintext + chr(
                ((ord(messageChar) - 97) - (ord(keyStreamChar) - 97)) % 26 + 97
            )
        else:  ##If we have space as character, then just concatenate it
            plaintext = plaintext + messageChar
    return plaintext


def main():
    plainText = input("Enter the plainText: ")
    autoKey = input("Enter the autoKey: ")
    keyStream = generateKeyStream(plainText, autoKey)
    # Printing the keyStream
    print(f"Key Stream : {keyStream}")
    ciphertext = encrypt(plainText, keyStream)
    print(f"Encrypted ciphertext: {ciphertext}")
    decryptedPlainText = decrypt(ciphertext, keyStream)
    print(f"Decrypted PlainText: {decryptedPlainText}")


if __name__ == "__main__":
    main()
