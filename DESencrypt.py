""" Application to encrypt data with DES """

from Crypto.Cipher import DES
from numpy  import random

#plain = str(random.randint(0,9999999999999999))
plain = b'0123abcd'

#plain = "Guido van Rossum is a space alien."

plaintextsize = len(plain)

key = b'beefbeef'
iv = b'abcdefgh'
cipher = DES.new(key, DES.MODE_OFB)


# Data padding if input data is not a multiple of 8
def padlenght(x):
    pad = ''
    if multipleof8 % 8 == False:
        for n in range(0, multipleof8):
            pad += 'X'
    else:
        pad = ''
    return pad

plaintext = plain + pad

#ciphertext = cipher.iv + cipher.encrypt(plaintext)
ciphertext = cipher.encrypt(plaintext)
print ciphertext