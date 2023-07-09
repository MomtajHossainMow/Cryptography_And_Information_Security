import numpy

# Initialize the matrix
matrix = numpy.array(
    [
        ["p", "l", "a", "y", "f"],
        ["i", "r", "e", "x", "m"],
        ["b", "c", "d", "g", "h"],
        ["k", "n", "o", "q", "s"],
        ["t", "u", "v", "w", "z"],
    ]
)

# This line is for the transpose the matrix.
result = numpy.transpose(matrix)

# Input PlainText.
plaintext = "hidethegoldinthetreestump"
# This line replace all "j" in the plaintext to "i"
plaintext = plaintext.replace("j", "i")
# This list is use for store the plaintext pair
plaintextpair = []
ciphertextpair = []

# Apply Rule 1.
# If both letter are same (or only one letter is left)
# Add on "X" after the first letter.
i = 0
while i < len(plaintext):
    a = plaintext[i]
    b = ""

    # If the letter is the last charater of the plaintext.
    if (i + 1) == len(plaintext):
        b = "x"
    else:
        b = plaintext[i + 1]
        # If the two character is not same then this makes pair.
    if a != b:
        plaintextpair.append(a + b)
        i += 2
    else:
        plaintextpair.append(a + "x")
        i += 1
ciphertext = ""
for pair in plaintextpair:
    applied_rule = True

    # Apply Rule 2.
    # If the letters appear at the same row of the table
    # Replace them with the letters to their immediate right respectively
    if applied_rule:
        for row in range(5):
            if pair[0] in matrix[row] and pair[1] in matrix[row]:
                for i in range(5):
                    if matrix[row][i] == pair[0]:
                        j0 = i

                for i in range(5):
                    if matrix[row][i] == pair[1]:
                        j1 = i

                applied_rule = False
                ciphertextpair.append(
                    (matrix[row][(j0 + 1) % 5]) + (matrix[row][(j1 + 1) % 5])
                )
                ciphertext = (
                    ciphertext
                    + (matrix[row][(j0 + 1) % 5])
                    + (matrix[row][(j1 + 1) % 5])
                )
    # Apply rule 3.
    # If the letter appear on the same column of table.
    # Replace them with the letter immediate below respectively
    if applied_rule:
        for row in range(5):
            if pair[0] in result[row] and pair[1] in result[row]:
                for i in range(5):
                    if matrix[i][row] == pair[0]:
                        j0 = i

                    for i in range(5):
                        if matrix[i][row] == pair[1]:
                            j1 = i

                    applied_rule = False
                ciphertextpair.append(
                    (matrix[(j0 + 1) % 5][row]) + (matrix[(j1 + 1) % 5][row])
                )
                ciphertext = (
                    ciphertext
                    + (matrix[(j0 + 1) % 5][row])
                    + (matrix[(j1 + 1) % 5][row])
                )
    # Apply rule 4
    # If the letters are not in the same row or same column
    # replace them with the letters on the same row respectively but at the
    # other pair of the corners of the rectangle define by the orginal pair.
    if applied_rule:
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == pair[0]:
                    x0 = row
                    y0 = col
            for row1 in range(5):
                for col1 in range(5):
                    if matrix[row1][col1] == pair[1]:
                        x1 = row1
                        y1 = col1
        ciphertextpair.append((matrix[x0][y1]) + (matrix[x1][y0]))
        ciphertext = ciphertext + (matrix[x0][y1]) + (matrix[x1][y0])

print("Given plaintext : ", plaintext)
print("Ciphertext: ", ciphertext)
