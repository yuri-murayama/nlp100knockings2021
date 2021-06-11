from sklearn.metrics import accuracy_score

with open('data/analogy.txt') as f:
    lines = f.readlines()

## sep前が意味的アナロジー、sep後が文法的アナロジー
sep = lines.index(': gram1-adjective-to-adverb\n')

scores = []
for lst in [lines[:sep], lines[sep:]]:
    l_true, l_pred = [], []
    for l in lst:
        if not l.startswith(':'):
            w = l.strip().split()
            l_true.append(w[3])
            l_pred.append(w[4])
    scores.append(accuracy_score(l_true, l_pred))

print('意味的アナロジーの正解率：　', scores[0])
print('文法的アナロジーの正解率：　', scores[1])

## 実行結果
#意味的アナロジーの正解率：　 0.7308602999210734
#文法的アナロジーの正解率：　 0.7400468384074942