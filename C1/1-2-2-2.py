import hashlib

IV = "0000"

data_list = ["0001","0002","0003","0004"]

for i in range(len(data_list)):
    a = hashlib.sha256(.encode()).hexdigest()
    print(data_list[i],a)