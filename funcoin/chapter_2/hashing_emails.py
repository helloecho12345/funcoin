from hashlib import sha256

# agreed shared secret - so both sender and recipient can decode
secret_phrase = "bolognese"

# Alice then removes the secret phrase from the message, and sends it to Bob with the hash. Bob then performs the same procedure as Alice: he appends the pre-shared secret phrase and outputs a hash. If the hash isn’t the same as the one Alice sent, he’ll know that the message has been tampered with.
def get_hash_with_secret_phrase(input_data, secret_phrase): 
  combined = input_data + secret_phrase
  return sha256(combined.encode()).hexdigest()

email_body = "Hey Bob, I think you should learn about Blockchains! " \
  "I've been investing in Bitcoin and currently have exactly 12.03 BTC in my account."
  
print(get_hash_with_secret_phrase(email_body, secret_phrase))



# Example: 
# 1. Alice and Bob both share a secret phrase S.
# 2. Alice then creates a hash H of the message M with the secret appended to the end of the message: H = hash(M + S).
# 3. Alice sends H and M to Bob (the message and the computed hash).
# 4. Bob checks the message integrity by calculating H himself to see if it’s the same as the hash Alice advertised.

# Note This general scheme describes a range of protocols called hMaC (hashed Message authentication Code) and is described by IETf rfC 2104.

# Before Alice and Bob begin communicating, they both agree on a secret password, bolognese. Alice formulates her email using the given scheme. Here’s what it looks like when Bob receives it:
# From: <Alice> alice@example.com
# Subject: Have you heard about Bitcoin?
# Hey Bob,I think you should learn about Blockchains! I've been
# investing in Bitcoin and currently have exactly 12.03 BTC in my account.
# hash: 71890dc61c21370874d2a7b74064396cb613a1924f09aa06925abc7842e6802c

# Bob notices that Alice has included the hash in the body of the email. He strips the hash then appends the secret phrase (bolognese) to the body of the email and computes the hash of it. If the hash matches the included hash in the body of the email, then he can conclude that the message hasn’t been tampered with (and Alice does in fact have 12.03 BTC).
# It’s important that Alice and Bob both know the protocol that they’ll be using for verification. This includes the hash function to be used (sha256) and where to put the secret phrase in the context of the message (they agree to append it to the end), and any other data that may further secure the scheme (such as a timestamp).