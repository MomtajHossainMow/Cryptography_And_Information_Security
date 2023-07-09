# A python code for the row column transposition Encryption.
import numpy as np

input = open("F:\Python 2023\CIS Lab\Keyless Transposition\output.txt", "r+")
output = open("F:\Python 2023\CIS Lab\Keyless Transposition\input.txt", "r+")
ciphertext = input.read()
plaintext = ""

col = 4
length = len(ciphertext)
reminder = length % col
if reminder == 0:
    row = length // col
else:
    row = length // col + 1

# This is dynamic array for the plaintext.
table = np.array([["z"] * col] * row)

# This part is for the fill the tabel dynamically.
index = 0
for i in range(col):
    for j in range(row):
        if index < len(ciphertext):
            table[j][i] = ciphertext[index]
            index += 1

# This part is for the make the plaintext.
for i in range(row):
    for j in range(col):
        plaintext += table[i][j]

# Write the plaintext into the file.
output.write(plaintext)
input.truncate(0)

# Close the previously open file.
input.close()
output.close()
