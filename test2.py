import hashlib

IV = "0001:0000"


a = hashlib.sha256(IV.encode()).hexdigest()
print(a)