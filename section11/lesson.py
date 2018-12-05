import string
import random

from Crypto.Cipher import AES

print(AES.block_size)
print(string.ascii_letters)

key = ''.join(random.choice(string.ascii_letters)for _ in range(AES.block_size))
print(key)
