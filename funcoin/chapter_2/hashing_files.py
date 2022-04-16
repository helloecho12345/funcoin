# import sha256 hashing function from hashlib library which is included with Python and one of the most popular hashing functions (used extensively in Bitcoin)
from hashlib import sha256

# opens my_image.jpg and "rb" denotes that the files should be in read-only mode and read in bytes
file = open("my_image.jpg", "rb")
# read the opened file into our hash function and assign the hexdigest (the out of the hex string) to a variable called hash
hash = sha256(file.read()).hexdigest()
# close the opened file and print the hash to the terminal
file.close()

print(f"The hash of my file is: {hash}")