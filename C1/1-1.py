#https://pg-chain.com/python-hash-hashlib

import hashlib


date1 = "12345"
date2 = '12346'

hsdate1 = hashlib.sha256(date1.encode()).hexdigest()
hsdate2 = hashlib.sha256(date2.encode()).hexdigest()

print(hsdate1,"\n",hsdate2)