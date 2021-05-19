count = 0
correct = 0

with open('./data/result_64.txt',mode='r') as f:
    while True:
        l = f.readline()
        words = l.split(' ')
        if len(words) > 2:
            count += 1
            if words[3] == words[4]:
                correct += 1
        elif l.startswith(': gram1-adjective-to-adverb'):
            print("semantic: ",correct/count)
            count = 0
            correct = 0
        elif not l:
            break
print("syntactic: ",correct/count)

