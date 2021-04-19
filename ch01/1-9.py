import random

def shuffle(str):
    ans = []
    for word in str.split():
        if len(word) > 4:
            word = word[:1] + ''.join(random.sample(word[1:-1],len(word)-2)) + word[-1:]
        ans.append(word)
    return ' '.join(ans)

sentence ="I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

ans = shuffle(sentence)
print(ans)