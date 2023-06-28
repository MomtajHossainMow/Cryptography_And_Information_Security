plaintext1 = input("Enter the plaintext: ")
plaintext1 = plaintext1.upper()
ciphertext = ""
key = int(input("Enter the key: "))
for i in range(len(plaintext1)):
    ch = plaintext1[i]
    substituted_ch = chr((ord(ch)-65+key) % 26)
    substituted_ch = chr(ord(substituted_ch) + 65)
    ciphertext = ciphertext + substituted_ch
print("Encoded text: ", ciphertext)
ciphertext = ciphertext.lower()
new_plaintext = ""
for i in range(len(ciphertext)):
    ch = ciphertext[i]
    substituted_ch = chr((ord(ch)-97-key) % 26)
    substituted_ch = chr(ord(substituted_ch) + 97)
    new_plaintext = new_plaintext + substituted_ch
print("Decoded text: ", new_plaintext)
