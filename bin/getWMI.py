__author__ = 'Oscar'

import pprint

from pattern.text.en import parse

from getESMock import getCountFromWords, getTweetsFromWords

def getWMIData(wordOne, wordTwo, lang):

    wordOneTweets = getTweetsFromWords(wordOne, lang)

    oneTexts = [tweet['text'] for tweet in wordOneTweets]

    wordTwoTweets = getTweetsFromWords(wordTwo, lang)

    twoTexts = [tweet['text'] for tweet in wordTwoTweets]

    return (oneTexts, twoTexts)

def getTokensFromTexts(texts):

    for text in texts:
        result = parse(text,
   tokenize = True,
       tags = False,
     chunks = False,         # Parse chunks? (NP, VP, PNP, ...)
  relations = False,        # Parse chunk relations? (-SBJ, -OBJ, ...)
    lemmata = False,
   encoding = 'utf-8',       # Input string encoding.
     tagset = None)



(firstTexts, secondTexts) = getWMIData("geek","hipster","es")

pprint.pprint(firstTexts)
pprint.pprint(secondTexts)