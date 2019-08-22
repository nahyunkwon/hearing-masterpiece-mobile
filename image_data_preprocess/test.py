from nltk.corpus import wordnet as wn

words = ['nucleus']

for w in words:
    tmp = wn.synsets(w)[0].pos()
    print(w, ":", tmp)
