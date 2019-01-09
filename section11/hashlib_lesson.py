import hashlib
import base64
import os

print(hashlib.sha256(b'test').hexdigest())

user_name = 'user1'
user_pass = 'password'
db = {}

def get_digest(password):
    password = bytes(password, 'utf-8')
    digest = hashlib.sha256(password).hexdigest()
    return digest

db[user_name] = get_digest(user_pass)

def is_login(user_name, password):
    return get_digest(password) == db[user_name]

print(is_login(user_name, user_pass))
