import hashlib

IV = "0000"

data_list = ["0001","0002","0003","0004"]
#for i in range(len(data_list)):
#for i in range(data_list):

for i in range(4):
    if i == 0:
        a = IV
        print(data_list[i],a)
        a = a
    else:
        a = hashlib.sha256(a.encode()).hexdigest()
        print(data_list[i],a)
        a = a

#数値がおかしい,test2.pyにて検証
#解決！
#このハッシュチェーンは"番号:数値"をセットでsha256してる
