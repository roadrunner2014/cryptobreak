# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 00:52:36 2018

@author: Rabbit
"""

from Crypto.Cipher import AES
from Crypto import Random
from mpi4py import MPI
import tempfile
import os
import time

start = time.time()

# OpenMPI setup
mode = MPI.MODE_RDONLY
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
msg = ' '

unit = comm.Scatter(inputdata, msg, root=0)


for x in range(numfiles<1):
   
    msg = iv + cipher.encrypt(inputdata)
    filesize = os.path.getsize(inputdata)
    totalsize += filesize
    x += 1
    if x > numfiles:
        break
    
# ===================================
# End of node-related work
# ===================================

# gather results
result = comm.Gather(inputdata, msg, root=0)
# do something with result
if rank == 0:
    print (result)
else:
    result = None

# Details on number and size of files
print ("Number of files encrypted = ", x)
print ("Total Size of file(s) encypted =  ", totalsize)

#inputdata = b'Attack at dawn Attack at dawn Attack at dawn Attack at dawn'
#msg = iv + cipher.encrypt(b'Attack at dawn Attack at dawn Attack at dawn Attack at dawn Attack at dawn Attack at dawn')
#print msg

end = time.time()
print ("Time to compute = ", (end-start), "for processor rank = ", rank)