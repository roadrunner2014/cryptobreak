""" Application to encrypt data with DES """

from Crypto.Cipher import DES
obj=DES.new('abcdefgh', DES.MODE_ECB)
plain="Guido van Rossum is a space alien."

plaintextsize = len(plain)

# Data padding if input data is not a multiple of 8

def padlenght(x):
    pad = 0
if multipleof8 % 8 == True:
    for n in range(0, multipleof8):
    pad += 'X'
    return pad

plaintext = plain + pad

ciphertext = obj.encrypt(plain)

