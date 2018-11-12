from Crypto.Cipher import DES
from numpy import random
import os

key = b'-8B key-'
cipher = DES.new(key,DES.MODE_OFB)
plaintext = b'sona si latine loqueris'
iv = random.bytes(8)
msg = cipher.iv + cipher.encrypt(plaintext)

print msg