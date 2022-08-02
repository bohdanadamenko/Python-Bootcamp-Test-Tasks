import hashlib


s = "Python Bootcamp"
hash_object = hashlib.md5(s.encode())
print(hash_object.hexdigest())
