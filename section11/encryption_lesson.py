import string
import random

from Crypto.Cipher import AES

# print(AES.block_size)
# print(string.ascii_letters)
key = ''.join(random.choice(string.ascii_letters)for _ in range(AES.block_size))

# initial vector
iv = ''.join(random.choice(string.ascii_letters)for _ in range(AES.block_size))
print(key,iv)

plaintext = 'HelloWorldCipher'

cipher = AES.new(key, AES.MODE_CBC,iv)
padding_length = AES.block_size - len(plaintext) % AES.block_size
plaintext += chr(padding_length) * padding_length

cipher_text = cipher.encrypt(plaintext)
print(cipher_text)

cipher2 = AES.new(key, AES.MODE_CBC,iv)
decprypt_text = cipher2.decrypt(cipher_text)
print(decprypt_text[:-decprypt_text[-1]])

with open('plaintext','r') as f, open('enc.dat','wb') as e:
    plain_file = f.read()
    cipher = AES.new(key, AES.MODE_CBC,iv)
    padding_length = AES.block_size - len(plain_file) % AES.block_size
    plain_file += chr(padding_length) * padding_length

    cipher_text = cipher.encrypt(plain_file)
    e.write(cipher_text)

with open('enc.dat','rb') as f:
    cipher2 = AES.new(key, AES.MODE_CBC,iv)
    decprypt_text = cipher2.decrypt(f.read())
    print(decprypt_text[:-decprypt_text[-1]].decode('utf-8'))
