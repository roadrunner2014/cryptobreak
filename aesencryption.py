# ----------- aesencryptionserial.py ---------------------
from Crypto.Cipher import AES
from Crypto import Random
from mpi4py import MPI
import os
import random
import sys
import time

start = time.time()

# OpenMPI setup
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# AES encryption details
key = b'Sixteen byte key'
iv = Random.new().read(AES.block_size)
cipher = AES.new(key, AES.MODE_CFB, iv)


# File(s) to encrypt
numfiles = 1000
x = 1
myfiledata = open("shakespeare.txt", "r")
inputdata = myfiledata.read() + 'This is the end of the file'
totalsize = os.path.getsize('shakespeare.txt')

for x in range(numfiles):
    filedata = open("shakespeare.txt", "r")
    inputdata = filedata.read() + 'This is the end of the file'
    filesize = os.path.getsize('shakespeare.txt')
    totalsize += filesize
    x += 1

# Details on number and size of files
print "Number of files encrypted = ", x
print "Total Size of file(s) encypted =  ", totalsize

#inputdata = b'Attack at dawn Attack at dawn Attack at dawn Attack at dawn'
#msg = iv + cipher.encrypt(b'Attack at dawn Attack at dawn Attack at dawn Attack at dawn Attack at dawn Attack at dawn')
msg = iv + cipher.encrypt(inputdata)
#print msg

end = time.time()
print "Time to compute = ", (end-start), "for processor rank = ", rank