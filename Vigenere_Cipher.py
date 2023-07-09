# This function generates the key in a cyclic manner
# until it's length isn't equal to the length of original text
def generateKey(string, key):
    new_key = key
    if len(string) == len(key):
        return key
    else:
        extra_len = len(string) - len(key)
        for i in range(extra_len):
            new_key = new_key + key[i % len(key)]
    return new_key


# Encryption Function
def cipherText(string, key):
    string = string.upper()
    key = key.upper()
    cipher_text = ""
    for i in range(len(string)):
        char = string[i]
        keychar = key[i]
        new_value = chr((((ord(char) - 65) + (ord(keychar) - 65)) % 26) + 65)
        cipher_text = cipher_text + new_value
    return cipher_text


# This function decrypts the encrypted text and returns the original text
def originalText(cipher_text, key):
    cipher_text = cipher_text.lower()
    key = key.lower()
    plaintext = ""
    for i in range(len(cipher_text)):
        char = cipher_text[i]
        keychar = key[i]
        new_value = chr((((ord(char) - 97) - (ord(keychar) - 97)) % 26) + 97)
        plaintext = plaintext + new_value
    return plaintext


# Driver code
if __name__ == "__main__":
    string = input("Enter the string : ")
    keyword = input("Enter the keyword string : ")
    key = generateKey(string, keyword)
    cipher_text = cipherText(string, key)
    plaintext = originalText(cipher_text, key)
    print("Ciphertext :", cipher_text)
    print("Original/Decrypted Text :", plaintext)
