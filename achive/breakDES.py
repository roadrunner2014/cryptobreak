""" Application to break DES algorithm """

import time
from Crypto.Cipher import DES

class BreakDES(object):
    def __init__(self, file, passwordLength = 8, testLength = 8):
        self.file = file
        self.passwordLength = passwordLength
        self.testLength = testLength
        self.EncryptedFile = open(file + '.des')
        self.DecryptedFile = open(file + '.txt')
        self.encryptedChunk = self.EncryptedFile.read(self.testLength)
        self.decryptedChunk = self.DecryptedFile.read(self.testLength)
        self.start = time.time()
        self.counter = 0
        self.chars = range(48, 58) + range(65, 91) + range(97, 123)
        self.key = False
        self.broken = False

        self.testPasswords(passwordLength, 0, '')

        if not self.broken:
            print "Password not found."

        duration = time.time() - self.start

        print "Brute force took %.2f" % duration
        print "Tested %.2f per second" % (self.counter / duration)

    def decrypt(self):
        des = DES.new(self.key.decode('hex'))
        if des.decrypt(self.encryptedChunk) == self.decryptedChunk:
            self.broken = True
            print "Password found: 0x%s" % self.key
        self.counter += 1

    def testPasswords(self, width, position, baseString):
            for char in self.chars:
                if(not self.broken):
                    if position < width:
                        self.testPasswords(width, position + 1, baseString + "%c" % char)
                        self.key = (baseString + "%c" % char).encode('hex').zfill(16)
                        self.decrypt()

# run it for password length 4
BreakDES("test3", 4)
