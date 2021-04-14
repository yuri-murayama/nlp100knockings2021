# 05_n-gram

# 与えられたシーケンス（文字列やリスト）からn-gramを作る関数
# Type: 文字(m)か単語(t), n:数字, Input:入力文字列/リスト
def ngram(Type, n, Input):
    
    if Type == "m":
        print("文字" + str(n) + "-gram: ", end ='')
        str1 = Input.replace(" ", "")
    elif Type == "t":
        print("単語" + str(n) + "-gram: ", end ='')
        str1 = Input.split()

    S = set()
    for i in range(len(str1) - n + 1):
        str2 = ""
        for j in range(n):
            str2 += str1[i+j]
            if Type == "t" and j != n-1:
                str2 += "-"
        S.add(str2)
        
    print(S)


s = "I am an NLPer"
ngram('t', 2, s)
ngram('m', 2, s)
