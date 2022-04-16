import hashlib

# Hash functions expect bytes as input: the encode() method turns strings to bytes
input_bytes = b"backpack"   # changing even one character will produce a completely new hash = avalanche property: minor changes in input yield large changes in output

output = hashlib.sha256(input_bytes)

# We use hexdigest() to convert bytes to hex because it's easier to read
print(output.hexdigest())   # output is 5f00368a6ad231c3c439c4f6bc33c27014b4d35a904ff1656d74f9528636f496




# avalanche property: minor changes in input yield large changes in output.
# Typically, hash functions are considered cryptographic if they satisfy the following properties:
# • Deterministic: The same input always yields the same hash.
# • Intractability: It’s infeasible to find the input for a given hash except by exhaustion (trying a gargantuan amount of possible inputs).
# • Collision-safety: It’s infeasible to find two different inputs which output the same hash.
# • Avalanche effect: The smallest change in input should yield a hash so different that the new hash appears uncorrelated with the old hash.
# • Speed: It’s computationally fast to generate a hash.

# Choice of Hash Function Peer-to-peer blockchains make their choice of hash function known in their protocols: Bitcoin uses double sha256, while Ethereum uses keccak256. The important thing to know is that all of these hash functions do the same thing: they provide predictable output for a given input.

# hash function : a function that identifies anything function you feed into it by outputting a gargantuan, random hexadecimal number. This number is always the same for the same input.
  # e.g.: a cryptographic hash function such as sha256, md5, blake2b, etc.
# hash/digest : The output of the hash function: a huge, random hexadecimal number.
  # e.g.: The hash of the word “dan”: ec4f...f1cb
         