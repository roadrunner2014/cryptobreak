from Crypto.Cipher import AES
from Crypto import Random
import os
import sys
import time


start = time.time()

key = b'Sixteen byte key'
iv = Random.new().read(AES.block_size)
cipher = AES.new(key, AES.MODE_CFB, iv)
#myfiledata = open("README.txt", "r")
myfiledata = open("shakespeare.txt", "r")
#print(myfiledata.read())
inputdata = myfiledata.read() + str('This is the end of the file')
#print inputdata
print "  "

#inputdata = b'Attack at dawn Attack at dawn Attack at dawn Attack at dawn'
#msg = iv + cipher.encrypt(b'Attack at dawn Attack at dawn Attack at dawn Attack at dawn Attack at dawn Attack at dawn')
msg = iv + cipher.encrypt(inputdata)

#print msg

end = time.time()
print "Time to compute = ", (end-start)