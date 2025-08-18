#me trying to code a simple encryption & decryption program

import random, string

chars = string.ascii_letters + string.digits + string.punctuation + " "
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#Encrypt

plain_text = input("Enter a message to encrypt: ")
cypher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cypher_text += key[index]

print(f"Original Message: {plain_text}")
print(f"Encrypted Message: {cypher_text}")

#Decrypt
cypher_text = input("Enter a message to decrypt: ")
plain_text = ""

for letter in cypher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Encrypted Message: {cypher_text}")
print(f"Original Message: {plain_text}")