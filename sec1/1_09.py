import random

def shuffle(words):
  result = []
  for word in words.split():
    if len(word) > 4:
      word = word[:1] + ''.join(random.sample(word[1:-1], len(word) - 2)) + word[-1:]
    result.append(word)

  return ' '.join(result)

target = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
result = shuffle(target)

print(result)