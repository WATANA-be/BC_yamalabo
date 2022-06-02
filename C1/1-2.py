import hashlib

IV = "0000"
block1 = "0001"+":"+IV
block2 = "0002"+":"+hashlib.sha256(block1.encode()).hexdigest()
block3 = "0003"+":"+hashlib.sha256(block2.encode()).hexdigest()
block4 = "0004"+":"+hashlib.sha256(block3.encode()).hexdigest()

hashchain = [block1,block2,block3,block4]
lasthash = hashlib.sha256(block4.encode()).hexdigest()

print(hashchain)
print(lasthash)