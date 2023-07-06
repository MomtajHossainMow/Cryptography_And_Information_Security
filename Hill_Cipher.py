"""
Implementation of Hill Cipher!
Important notation:
K = Matrix which is our 'Secret Key'
P = Vector of plaintext (that has been mapped to numbers)
C = Vector of Ciphered text (in numbers)

C = E(K,P) = K*P (mod X) -- X is length of alphabet used
P = D(K,C) = inv(K)*C (mod X)  -- X is length of alphabet used
"""
import numpy as np


# Encrption Function
def hill_encrypt(plaintext, key):
    ciphertext = ""
    i = 0
    while i < len(plaintext):
        a = ord(plaintext[i]) - 97
        b = ord(plaintext[i + 1]) - 97
        c = ord(plaintext[i + 2]) - 97
        matrix = np.array([[a], [b], [c]])
        cipher = np.dot(key, matrix) % 26  # matrix multiplication
        list = cipher.flatten().tolist()  # convert matrix into list
        for j in range(3):
            ciphertext = ciphertext + chr(list[j] + 97)
        i = i + 3
    return ciphertext


# Decryption Function
def hill_decrypt(ciphertext, key):
    """
    We find the matrix modulus inverse by
    Step 1) Find determinant
    Step 2) Find determinant value in a specific modulus (usually length of alphabet)
    Step 3) Take that det_inv times the det*inverted matrix (this will then be the adjoint) in mod 26
    """
    modulus = 26
    # Here we calculate the determinant of matrix via np.linalg.det(matrix), since this method calculate the
    # result numerically, we need to round off the result to avoid round-off error
    det = int(np.round(np.linalg.det(key)))  # Step (1)
    # Here we calculate the determinant inverse modulo 26 via extended Euclidean Algorithm
    det_inv = pow(det, -1, modulus)  # Step (2)
    # Adjoint matrix = determinant * (inverse of matrix)
    # Matrix modulo inverse(K^-1) = determinantInverse * Adjoint matrix
    matrix_modulus_inv = (
        det_inv * np.round(det * np.linalg.inv(key)).astype(int) % modulus
    )  # Step 3)

    plaintext = ""
    i = 0
    while i < len(ciphertext):
        a = ord(ciphertext[i]) - 97
        b = ord(ciphertext[i + 1]) - 97
        c = ord(ciphertext[i + 2]) - 97
        matrix = np.array([[a], [b], [c]])
        plaintext_vector = (
            np.dot(matrix_modulus_inv, matrix) % 26
        )  # matrix multiplication
        list = plaintext_vector.flatten().tolist()  # convert matrix into list
        for j in range(3):
            plaintext = plaintext + chr(list[j] + 97)
        i = i + 3

    return plaintext


# key is represented into 3*3 matrix
key = np.array([[17, 17, 5], [21, 18, 21], [2, 2, 19]])
# Input PlainText
plaintext = "paymoremoney"
cipher_text = hill_encrypt(plaintext, key)
decrypted_text = hill_decrypt(cipher_text, key)
print("plaintext is: ", plaintext)
print("Ciphertext is: ", cipher_text)
print("Decrypted text is: ", decrypted_text)
