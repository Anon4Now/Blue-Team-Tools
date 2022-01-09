import hashlib


class HashGenerator:
    hash_sha256 = hashlib.sha256()  # Create the hash object for SHA256 `.sha256()`
    hash_sha1 = hashlib.sha1()  # Create the hash object for SHA1 `.sha1()`
    hash_md5 = hashlib.md5()  # Create the hash object for MD5`.md5()'

    def __init__(self, fileName):
        self.fileName = fileName
        self.data = None

    def readFile(self):
        with open(self.fileName) as file:
            self.data = file.read()
            print(f'[File Name] - {self.data}')

    def generateHash(self):
        BLOCK_SIZE = 65536  # The size of each read from the file

        with open(self.data, 'rb') as f:  # Open the file to read its bytes
            fb = f.read(BLOCK_SIZE)  # Read from the file. Take in the amount declared above
            while len(fb) > 0:  # While there is still data being read from the file
                HashGenerator.hash_sha256.update(fb)  # Update the hash
                HashGenerator.hash_sha1.update(fb)  # Update the hash
                HashGenerator.hash_md5.update(fb)  # Update the hash
                fb = f.read(BLOCK_SIZE)  # Read the next block from the file

    @staticmethod
    def returnHashes():
        print(f'[SHA-256 Hash] - {HashGenerator.hash_sha256.hexdigest()}')  # Print the hash value to CLI
        print(f'[SHA-1 Hash] - {HashGenerator.hash_sha1.hexdigest()}')  # Print the hash value to CLI
        print(f'[MD5 Hash] - {HashGenerator.hash_md5.hexdigest()}\n')  # Print the hash value to CLI

    def startHash(self):
        self.readFile()
        self.generateHash()
        self.returnHashes()
