# Utlilizing Parallalization to Reduce Encryption Time
# Python applications using MPI to perform AES encryption on text files

# Parallelization is an important aspect of computing to maximize utilization of the CPU.  This GitHub investigates the power of parallelization for CPU calculations.  For an example of the power of parallelization this paper analyzes the time needed to encrypt text files.

# Problem set is to use parallel processing (OpenMPI) and the cloud to encrypt text files to simlulate large scale encryption on a single CPU, point-to-point MPI communication, and MPI Scatter communication to multiple nodes.   Use OpenMPI to encrypted plaintext using AES on node or cluster. 

# To analyze the effects of parallelization, Advanced Encryption Standard (AES) encryption of data files was evaluated using serial processing, Open Message Passing Interface (MPI) point-to-point parallel processing, and MPI collective communication parallel processing with Scatter/Gather.  For the evaluation, Python with OpenMPI [2] mpi4py tools and PyCrypto [3] tools were utilized on virtual machines (VM) and Docker containers running on a varierty of hosts and Google Cloud Platform (GCP) VMs.  

# Tools - Python Cryptography toolkit; OpenMPI, Google Cloud Platform

# Serial encryption process
python aesencryptionserial.py

# Point-to-Point MPI encryption process (no of processes = no of 5.5MB files encrypted)
mpiexec -n 2 python aesencryptionserial-p2p.py

# Point-to-Point MPI encryption process on a container as root
mpiexec --allow-run-as-root -n 4 python aesencryptionserial-p2p.py

# Scatter MPI encryption process
mpiexec -n 3 --hostfile host python scatMPI.py
