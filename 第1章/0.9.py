import random

def shuffle(words):
  result = []
  for word in words.split():
    if len(word) > 4:
      word = word[:1] + ''.join(random.sample(word[1:-1], len(word) - 2)) + word[-1:]
    result.append(word)

  return ' '.join(result)

words = "If you find a path with no obstacles, it probably doesn’t lead anywhere."
ans = shuffle(words)

print(ans)