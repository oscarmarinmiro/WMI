__author__ = 'Oscar'

import pprint
import re
import math

from getES import getCountFromWords, getTweetsFromWords

TOP_WORDS = 100

def getStopWords():

    FILE_IN = "../data/stopwords.txt"

    fileIn = open(FILE_IN,"rb")

    for line in fileIn:
        myWords = line.decode("utf8").split(", ")

    return myWords

def normalizeTokens(myDict):

    myList = []

    topKeys = sorted(myDict.keys(), key = lambda key: myDict[key], reverse=True)[:TOP_WORDS]

    for key in topKeys:
        myList.append({'word': key, 'count': myDict[key]})

    return myList

def getWMIData(wordOne, wordTwo, lang):

    myWords = getStopWords()

    wordOneTweets = getTweetsFromWords(wordOne, lang)

    oneTexts = [tweet['text'] for tweet in wordOneTweets]

    wordTwoTweets = getTweetsFromWords(wordTwo, lang)

    twoTexts = [tweet['text'] for tweet in wordTwoTweets]

    myTokensOne = normalizeTokens(getTokensFromTexts(oneTexts, myWords,wordOne,wordTwo))

    myTokensTwo = normalizeTokens(getTokensFromTexts(twoTexts, myWords,wordTwo,wordTwo))


    finalDict = myTokensOne + myTokensTwo

    finalTokens = {}

    for entry in finalDict:
        finalTokens[entry['word']] = {}

    for key in finalTokens:
        finalTokens[key]['first'] = getCountFromWords([key,wordOne], "en")
        finalTokens[key]['second'] = getCountFromWords([key,wordTwo], "en")
        finalTokens[key]['all'] = getCountFromWords([key], "en")
        finalTokens[key]['firstPMI'] = math.log(finalTokens[key]['first']) - math.log(finalTokens[key]['all'])
        finalTokens[key]['secondPMI'] = math.log(finalTokens[key]['second']) - math.log(finalTokens[key]['all'])

    #pprint.pprint(finalTokens)

    finalStruct = []

    for key in finalTokens:
        finalStruct.append({'word': key, 'xPMI': finalTokens[key]['firstPMI'], 'yPMI': finalTokens[key]['secondPMI']})

    pprint.pprint(finalStruct)

    return

def getTokensFromTexts(texts,myWords,origWord, origWordTwo):

    tokenCounts = {}

    for text in texts:
        tokens = re.split('[\s\.\,\;\']+',text)
        for token in tokens:
            token = token.lower()
            if token not in myWords and len(token)> 2 and token != origWord.lower() and token != origWord.lower():
                if token not in tokenCounts:
                    tokenCounts[token] = 0
                tokenCounts[token] +=1
    return tokenCounts



getWMIData("geek","hipster","en")


