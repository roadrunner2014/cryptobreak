# cryptobreak
# Applications to break crypto algorithms using MPI

# Problem set is to use parallel processing (OpenMPI) and OpenStack to simulate attacker attempting to crack DES encryption to perform Man-In-the-Middle attacks on simulated ciphertext.   Use OpenMPI to encrypted plaintext using DES on node or cluster and transmit ciphertext to receive node. Decrypt ciphertext without knowledge of plaintext or DES encryption key using cryptographic techniques leveraging OpenMPI parallel processing on a compute cluster.

# Tools - Python Cryptography toolkit; OpenMPI, OpenStack

# Strategy on cracking DES for key strength 2^56. Divide up processing tasks among the separate processors. Can leverage linear crypto-analysis to get to 2^46 and other techniques. 

# https://en.m.wikipedia.org/wiki/EFF_DES_cracker
