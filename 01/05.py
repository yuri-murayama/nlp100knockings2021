# 05_n-gram

def n_gram(n,str):
    result = []
    for i in range(0, len(str) - n + 1):
        result.append(str[i:i + n])

    return result


str1 = "I am an NLPer"
print(n_gram(2,str1.split(' ')))
print(n_gram(2,str1))
