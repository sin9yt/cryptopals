# python3 5.py

plaintext= """\
Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""
key = 'ICE'.encode()
i=0

ciphertext = ''
for char in plaintext.encode():
    if i == len(key):
        i=0
    ciphertext += chr(char ^ key[i])
    i+=1

print(ciphertext.encode().hex())