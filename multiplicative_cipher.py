plaintext1 = input("Enter the plaintext: ")
plaintext1 = plaintext1.upper()
ciphertext = ""
key = int(input("Enter the key: "))
for i in range(len(plaintext1)):
    ch = plaintext1[i]
    substituted_ch = chr(((ord(ch)-65)*key) % 26)
    substituted_ch = chr(ord(substituted_ch) + 65)
    ciphertext = ciphertext + substituted_ch
print("Encoded text: ", ciphertext)

r1 = 26
r2 = key
t1 = 0
t2 = 1
while r2 > 0:
    q = r1//r2
    r = r1 - q*r2
    r1 = r2
    r2 = r
    t = t1 - q*t2
    t1 = t2
    t2 = t

if r1 == 1:
    ciphertext = ciphertext.lower()
    new_plaintext = ""
    for i in range(len(ciphertext)):
        ch = ciphertext[i]
        substituted_ch = chr(((ord(ch)-97)*t1) % 26)
        substituted_ch = chr(ord(substituted_ch) + 97)
        new_plaintext = new_plaintext + substituted_ch
    print("Decoded text: ", new_plaintext)

else:
    print("Multiplicative inverse doesn't exist")
