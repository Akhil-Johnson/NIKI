import string
#import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download()



#text = open("sentiment.txt", enc).read()

text = input("enter the question ")
text = text.lower()
print(text)

# Tokenise the input

tokenised_words = word_tokenize(text)
flag = 0
for w in tokenised_words:

    if w=='what':
            print('what')
            
    elif w=='when':
            print('when')
            
    elif w=='who':
            print('who')
            
    else:
        print('unknown')