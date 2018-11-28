# ----------- aesencryption.py ---------------------
from Crypto.Cipher import AES
from Crypto import Random
import numpy
import sys
from mpi4py import MPI
from mpi4py.MPI import ANY_SOURCE
import os
import sys
import time

start = time.time()
totaltime = float()

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

key = b'Sixteen byte key'
iv = Random.new().read(AES.block_size)
cipher = AES.new(key, AES.MODE_CFB, iv)
#myfiledata = open("README.txt", "r")
myfiledata = open("shakespeare.txt", "r")
#print(myfiledata.read())
inputdata = myfiledata.read() + str('This is the end of the file')
#print inputdata
filesize = os.path.getsize('shakespeare.txt')
print "Size of file(s) encypted =  ", filesize
print "  "

#inputdata = b'Attack at dawn Attack at dawn Attack at dawn Attack at dawn'
#msg = iv + cipher.encrypt(b'Attack at dawn Attack at dawn Attack at dawn Attack at dawn Attack at dawn Attack at dawn')
msg = iv + cipher.encrypt(inputdata)

#print msg

end = time.time()
tt = (end-start)

print "Time to compute = ", tt, "for processor rank = ", rank

totaltime += tt
print "Total time to encrypt data = ", str(totaltime)

