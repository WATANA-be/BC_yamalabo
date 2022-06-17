import hashlib

IV = "0000"

data_list = ["0001","0002","0003","0004"]

def hashchain(data_list,prev_hash):
    #data_list.map(data_list)
    for i in map(hashlib.sha256(block.encode()).hexdigest(),data_list):
        block = data + ":" + prev_hash
        block

blockchain = hashchain(data_list,IV)

