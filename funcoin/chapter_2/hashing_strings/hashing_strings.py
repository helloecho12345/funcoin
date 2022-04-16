import hashlib

# Hash functions expect bytes as input: the encode() method turns strings to bytes
input_bytes = b"backpack"   # changing even one character will produce a completely new hash = avalanche property: minor changes in input yield large changes in output

output = hashlib.sha256(input_bytes)

# We use hexdigest() to convert bytes to hex because it's easier to read
print(output.hexdigest())   # output is 5f00368a6ad231c3c439c4f6bc33c27014b4d35a904ff1656d74f9528636f496