# python3 2.py

def xor(a,b):
    str = [chr(x ^ y) for x,y in zip(a,b)]
    return ''.join(str).encode().hex()

print(xor(bytes.fromhex('1c0111001f010100061a024b53535009181c'),bytes.fromhex('686974207468652062756c6c277320657965')))