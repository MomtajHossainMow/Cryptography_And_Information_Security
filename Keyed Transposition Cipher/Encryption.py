# A python code for encryption keyed transposition cipher.
import numpy as np

input = open("F:\Python 2023\CIS Lab\Keyed Transposition Cipher\input.txt", "r+")
output = open("F:\Python 2023\CIS Lab\Keyed Transposition Cipher\output.txt", "r+")
plaintext = input.read()
ciphertext = ""

# This block size is dynamic you can give any value.
blockSize = 4
value = len(plaintext) % blockSize

# This is used for the adding extra dummy character in the plaintext.
if value != 0:
    for i in range(blockSize - value):
        plaintext += "z"

# This line used for find how many block needed for represent the plaintext.
value = int(len(plaintext) / blockSize)
print(value)
# This is key need for transfer the plaintext block.
key = [2, 0, 3, 4, 1]

list = np.array([["z"] * value] * blockSize)
list1 = np.array([["z"] * value] * blockSize)
index = 0

# Represent the plaintext into the matrix so that we can transpose the character .
for i in range(blockSize):
    for j in range(value):
        list[i][j] = plaintext[index]
        index += 1

# Perform the transposition.
for i in range(blockSize):
    index = 0
    for j in range(value):
        list1[i][j] = list[i][key[index]]
        ciphertext += list1[i][j]
        index += 1

print("The required ciphertext is : ", ciphertext)

# Write the ciphertext into the output file.
output.write(ciphertext)

# Clear the input file.
input.truncate(0)

# Close the previously open file.
input.close()
output.close()
