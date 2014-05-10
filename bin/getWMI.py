__author__ = 'Oscar'

import pprint
import re

#from pattern.text.en import parse, parsetree

from getESMock import getCountFromWords, getTweetsFromWords

def getWMIData(wordOne, wordTwo, lang):

    wordOneTweets = getTweetsFromWords(wordOne, lang)

    oneTexts = [tweet['text'] for tweet in wordOneTweets]

    wordTwoTweets = getTweetsFromWords(wordTwo, lang)

    twoTexts = [tweet['text'] for tweet in wordTwoTweets]

    return (oneTexts, twoTexts)

def getTokensFromTexts(texts):

    for text in texts:
        tokens = re.split('[\s\.\,\;\']+',text)
        pprint.pprint(tokens)



(firstTexts, secondTexts) = getWMIData("geek","hipster","es")

# pprint.pprint(firstTexts)
# pprint.pprint(secondTexts)


getTokensFromTexts(firstTexts)
getTokensFromTexts(secondTexts)