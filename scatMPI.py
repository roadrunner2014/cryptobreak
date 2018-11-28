# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 00:52:36 2018

@author: Rabbit
"""

from Crypto.Cipher import AES
from Crypto import Random
from mpi4py import MPI
import os
import random
import sys
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

if rank == 0:
    # get a list of the files to scatter
    #for f in glob.glob(args.alignments):
    work = ['shakespeare.txt', 'shakespeare2.txt','shakespeare3.txt']
else:
    work = None

# File(s) to encrypt
numfiles = 3 
x = 1
myfiledata = open("shakespeare.txt", "r")
inputdata = myfiledata.read() + 'This is the end of the file'
totalsize = os.path.getsize('shakespeare.txt')

unit = comm.scatter(work, root=0)




for x in range(numfiles):
    # open the file on a node
    f = MPI.File.Open(comm, unit, mode)
    # create a buffer for the data of size f.Get_size()
    ba = bytearray(f.Get_size())
    # read the contents into a byte array
    f.Iread(ba)
    msg = iv + cipher.encrypt(f)
    filesize = os.path.getsize(work)
    totalsize += filesize
    x += 1


# Details on number and size of files
print ("Number of files encrypted = ", x)
print ("Total Size of file(s) encypted =  ", totalsize)

#inputdata = b'Attack at dawn Attack at dawn Attack at dawn Attack at dawn'
#msg = iv + cipher.encrypt(b'Attack at dawn Attack at dawn Attack at dawn Attack at dawn Attack at dawn Attack at dawn')
#print msg

end = time.time()
print ("Time to compute = ", (end-start), "for processor rank = ", rank)