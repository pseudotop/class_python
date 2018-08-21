import Crypto.Hash.SHA256 as sha

hash = sha.new()
hash.update('hello world'.encode())
print(hash.hexdigest())
hash.update('welcome to hell'.encode())
print(hash.hexdigest())

import hashlib
print(hashlib.sha256('hello world'.encode()).hexdigest())