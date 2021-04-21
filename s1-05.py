#https://www.tutorialspoint.com/python_text_processing/python_bigrams.htm       
import nltk
sentence = "I am an NLPer"
split=sentence.split()
print(list(nltk.bigrams(split)))
print(list(nltk.bigrams(sentence)))


remove=sentence.replace(' ', '')
print(list(nltk.bigrams(remove)))


