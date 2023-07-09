# A python code for the row column transposition Encryption.
import numpy as np

input = open("F:\Python 2023\CIS Lab\Keyless Transposition\input.txt", "r+")
output = open("F:\Python 2023\CIS Lab\Keyless Transposition\output.txt", "r+")
plaintext = input.read()
ciphertext = ""

col = 4
length = len(plaintext)
reminder = length % col
if reminder == 0:
    row = length // col
else:
    row = length // col + 1

# This is dynamic array for the plaintext.
table = np.array([["z"] * col] * row)

# This part is for the fill the tabel dynamically.
index = 0
for i in range(row):
    for j in range(col):
        if index < len(plaintext):
            table[i][j] = plaintext[index]
            index += 1

# This part is for the make the ciphertext.
table = np.transpose(table)
for i in range(col):
    for j in range(row):
        ciphertext += table[i][j]

# Write the ciphertext into the file.
output.write(ciphertext)
input.truncate(0)

# Close the previously open file.
input.close()
output.close()
