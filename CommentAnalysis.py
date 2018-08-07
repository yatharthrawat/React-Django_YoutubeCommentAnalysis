import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import twitter_samples
from nltk.tag import pos_tag_sents
from nltk.corpus import movie_reviews
import pickle

def CreateFeautureSet_movie(words):
    temp = []
    for word in words:
        if word.isalpha():
            temp.append(word)
    return({word: True for word in temp})

def CreateFeautureSet(line):
    temp=[]
    for word in nltk.tokenize.word_tokenize(line):
        if word.isalpha():
            temp.append(word)

    return({word: True for word in temp})

# Lists to store positive and negative numbers for NaiveBayesClassifier
positive = []
negative = []
#  First lets add data from twitter_samples
for line in twitter_samples.strings('positive_tweets.json'):
    positive.append([CreateFeautureSet(line), 'pos'])

for line in twitter_samples.strings('negative_tweets.json'):
    negative.append([CreateFeautureSet(line), 'neg'])

#  Now Let's add data from movie_reviews
# Accessing fileids of each movie review
fileid_pos=movie_reviews.fileids('pos')
fileid_neg=movie_reviews.fileids('neg')

for id in fileid_pos:
    positive.append([CreateFeautureSet_movie(movie_reviews.words(fileids=[id])), 'pos'])
for id in fileid_neg:
    negative.append([CreateFeautureSet_movie(movie_reviews.words(fileids=[id])), 'neg'])

train_set = positive + negative

classifier = NaiveBayesClassifier.train(train_set)
# Save model to disk
filename = 'Classifier.sav'
pickle.dump(classifier,open(filename,'wb'))

