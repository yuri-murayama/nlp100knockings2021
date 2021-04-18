def n_gram(n,target):
    result = []
    for i in range(0, len(target) - n + 1):
        result.append(target[i:i + n])

    return result

target = 'I am an NLPer'

print(n_gram(2,target.split(' ')))
print(n_gram(2,target))