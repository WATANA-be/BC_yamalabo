import hashlib

IV = "0000"

data_list = ["0001","0002","0003","0004"]
#for i in range(len(data_list)):
#for i in range(data_list):
ans_list = []
for i in range(4):
    if i == 0:
        a = IV
        data = data_list[i] +":"+ a
        #print(data)
        ans_list.append(data)
    else:
        a = hashlib.sha256(data.encode()).hexdigest()
        data = data_list[i]+ ":" + a
        #print(data)
        ans_list.append(data)
print(ans_list)

