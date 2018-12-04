# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 00:52:36 2018

@author: Rabbit
"""
"""
from Crypto.Cipher import AES
from Crypto import Random
from mpi4py import MPI
import numpy as np
import os
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
numfiles = 2
x = 1
myfiledata =  open("shakespeare.txt", "r")
inputdata = (myfiledata.read() + "This is the end")
inputArray = np.fromfile(inputdata)
totalsize = os.path.getsize('shakespeare.txt')
msg = np.array(np.empty)


comm.Scatterv(inputArray,msg, root=0)

for x in range(numfiles):
    
    msg = iv + cipher.encrypt(inputdata)
    filesize = os.path.getsize('shakespeare.txt')
    totalsize += filesize
    x += 1

# ===================================
# End of node-related work
# ===================================

# gather results
#comm.Gatherv(msg, inputdata, rank=0)
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
"""
from Crypto.Cipher import AES
from Crypto import Random
from mpi4py import MPI
import numpy as np
import os
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
# Assume number of files = size (i.e. number of processes)
numfiles = 100
totalsize = os.path.getsize('shakespeare.txt')
inputArray = np.fromfile(open("shakespeare.txt"))
count = 1
output = np.empty(os.path.getsize("shakespeare.txt"))
comm.Scatterv(inputArray, output, root=0)
for i in range(1, numfiles):
    filedata = open("shakespeare.txt", "r")
    inputdata = filedata.read() + 'This is the end of the file'
    count += 1
    totalsize += os.path.getsize('shakespeare.txt')

# Local computation of encryption
msg = iv + cipher.encrypt(inputdata)
totalsize += os.path.getsize('shakespeare.txt')
print ("encryption done by: ", rank)

# Wait until all processes are done
comm.Barrier()

if rank == 0:
    # Details on number and size of files
    print ("Number of files encrypted = ", count)
    print ("Total Size of file(s) encypted =  ", totalsize)
    end = time.time()
    print ("Time to compute = ", (end-start)