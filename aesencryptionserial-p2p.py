# ----------- aesencryptionserial.py ---------------------
from Crypto.Cipher import AES
from Crypto import Random
from mpi4py import MPI
import os
import random
import sys
import time
import numpy as np

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
numfiles = size
totalsize = os.path.getsize('shakespeare.txt')
count = 1

if rank == 0:
    for i in range(1, numfiles):
        filedata = open("shakespeare.txt", "r")
        inputdata = filedata.read() + 'This is the end of the file'
        comm.send(inputdata, dest=i, tag=11)
        count += 1
        totalsize += os.path.getsize('shakespeare.txt')
else:
    inputdata = comm.recv(source=0, tag=11)

# Local computation of encryption
msg = iv + cipher.encrypt(inputdata)
totalsize += os.path.getsize('shakespeare.txt')
#print "encryption done on process ", rank

# Wait until all processes are done
comm.Barrier()

if rank == 0:
    # Details on number and size of files
    print "Number of files encrypted = ", count
    print "Total Size of file(s) encypted =  ", totalsize
    end = time.time()
    print "Time to compute = ", (end-start), "using point-to-point communication"
