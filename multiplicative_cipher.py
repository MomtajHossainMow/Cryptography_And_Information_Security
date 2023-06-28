# Input
plaintext = input("Enter the plaintext: ")
key = int(input("Enter the key: "))

# Encryption Funtion
plaintext = plaintext.upper()
ciphertext = ""
for i in range(len(plaintext)):
    ch = plaintext[i]
    if ch == " ":
        substituted_ch = ch
    else:
        substituted_ch = chr(((ord(ch) - 65) * key) % 26)
        substituted_ch = chr(ord(substituted_ch) + 65)
    ciphertext = ciphertext + substituted_ch
print("Encoded text: ", ciphertext)

# Finding the multiplicative inverse of key value
# Using Extended Euclidean Algorithm
r1 = 26
r2 = key
t1 = 0
t2 = 1
while r2 > 0:
    q = r1 // r2
    r = r1 - q * r2
    r1 = r2
    r2 = r
    t = t1 - q * t2
    t1 = t2
    t2 = t

if r1 == 1:
    ciphertext = ciphertext.lower()
    new_plaintext = ""
    for i in range(len(ciphertext)):
        ch = ciphertext[i]
        if ch == " ":
            substituted_ch = ch
        else:
            substituted_ch = chr(((ord(ch) - 97) * t1) % 26)
            substituted_ch = chr(ord(substituted_ch) + 97)
        new_plaintext = new_plaintext + substituted_ch
    print("Decoded text: ", new_plaintext)

else:
    print("Multiplicative inverse of the key doesn't exist")
