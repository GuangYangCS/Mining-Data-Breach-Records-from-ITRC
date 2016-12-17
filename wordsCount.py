import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
from bs4 import BeautifulSoup
import re
from collections import Counter

def stemWord():
    #words = "Alice is testing spark application. Testing spark is fun"
    file = open('transformedData.txt', 'r')
    words = file.read()
    #sentences = re.split("\.", words)
    bsObj = BeautifulSoup(words)
    words = bsObj.get_text()
    sentences = re.split("\.", words)

    filtered_words = []
    for sentence in sentences:
        if sentence == '':
            sentences.remove(sentence)
        else:
            filtered_words.append([word for word in sentence.strip().split(' ') if word not in stopwords.words('english')])
    ps = PorterStemmer()
    processedWords = []
    for sentence in filtered_words:
        for word in sentence:
            processedWords.append(ps.stem(word).lower())

    # for sentence in filtered_words:
    #     processedSentence = []
    #     for word in sentence:
    #         processedSentence.append(str(ps.stem(word)))
    #     processedSentences.append(processedSentence)
    counter = Counter(processedWords)
    print(counter)
    # bigrams = []
    # for sentence in processedSentences:
    #     for i in range(len(sentence) - 1):
    #         bigrams.append((sentence[i].lower(), sentence[i + 1].lower()))
    # for mostCommon in Counter(bigrams).most_common(2):
    #     if mostCommon[1] > 1:
    #         print(mostCommon)

if __name__ == "__main__":
    stemWord()
